#!/usr/bin/env python3
"""Generate Springer alt-text inventory data for manuscript figures.

Springer Nature requests alt text for all figures, illustrations, and images as
an Excel file submitted with the final manuscript. This script scans the English
manuscript in mkdocs navigation order, extracts every local image reference, and
builds reviewable CSV/JSON data. The companion Node script
`build_alt_text_workbook.mjs` turns the JSON into the submission workbook.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "mkdocs.yml"
DOCS_EN = ROOT / "docs" / "en"
DOCS_ZH = ROOT / "docs" / "zh"
DEFAULT_OUT_DIR = ROOT / "publishing" / "accessibility"
DEFAULT_CSV = DEFAULT_OUT_DIR / "springer_alt_text_inventory.csv"
DEFAULT_JSON = DEFAULT_OUT_DIR / "springer_alt_text_inventory.json"

IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HTML_IMG_RE = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"'][^>]*>", re.I)
ATTR_RE = re.compile(r"([A-Za-z_:][-A-Za-z0-9_:.]*)=[\"']([^\"']*)[\"']")
FIGURE_NO_RE = re.compile(r"\b(?:Figure|Fig\.?|图)\s*([A-Z]?\d+|P\d+|[A-Z])[-‑–—]([A-Za-z0-9]+)\b", re.I)
PROJECT_RE = re.compile(r"part14/p(\d{2})_", re.I)
CHAPTER_RE = re.compile(r"part\d+/ch(\d{2})_", re.I)
APPENDIX_RE = re.compile(r"appendix_([a-z])_", re.I)


@dataclass
class NavItem:
    title: str
    path: str
    level: int
    group: str
    group_slug: str


@dataclass
class AltTextRow:
    row_id: str
    language: str
    part: str
    unit: str
    unit_title: str
    source_markdown: str
    line: int
    figure_number: str
    caption: str
    image_alt_in_markdown: str
    image_file: str
    image_exists: str
    image_dimensions: str
    image_format: str
    alt_text: str
    long_description: str
    decorative: str
    review_status: str
    reviewer: str
    notes: str
    zh_reference_caption: str
    zh_reference_alt_text: str


def slugify(value: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", value).strip("-")
    return slug[:48] or "section"


def find_en_nav(config: dict[str, Any]) -> list[Any]:
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "i18n" in plugin:
            for lang in plugin["i18n"].get("languages", []):
                if lang.get("locale") == "en":
                    nav = lang.get("nav")
                    if isinstance(nav, list):
                        return nav
    raise ValueError("Cannot find en navigation in mkdocs.yml")


def flatten_nav(nodes: list[Any], level: int = 1, group: str = "Front Matter", group_slug: str = "front") -> list[NavItem]:
    items: list[NavItem] = []
    for node in nodes:
        if not isinstance(node, dict):
            continue
        for title, value in node.items():
            if isinstance(value, str) and value.endswith(".md"):
                if value == "afterword.md":
                    item_group = "Back Matter"
                    item_group_slug = "back-matter"
                elif level == 1 and not re.search(r"part\d+/", value) and not value.startswith("appendix_"):
                    item_group = "Front Matter"
                    item_group_slug = "front-matter"
                else:
                    item_group = group
                    item_group_slug = group_slug
                items.append(NavItem(str(title), value, level, item_group, item_group_slug))
            elif isinstance(value, list):
                child_group = str(title) if level == 1 else group
                child_slug = slugify(child_group) if level == 1 else group_slug
                items.extend(flatten_nav(value, level + 1, child_group, child_slug))
    return items


def prepare_items(items: list[NavItem]) -> list[NavItem]:
    excluded = {"title_page.md", "index.md", "translation-status.md", "front_matter_guide.md"}
    front_order = {
        "preface.md": 1,
        "acknowledgments.md": 2,
        "contributors.md": 3,
        "abbreviations.md": 4,
    }
    kept = [item for item in items if item.path not in excluded and not re.search(r"part\d+/index\.md$", item.path)]
    front = [item for item in kept if item.path in front_order]
    rest = [item for item in kept if item.path not in front_order]
    front.sort(key=lambda item: (front_order.get(item.path, 99), item.path))
    return front + rest


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_#>|]+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_caption(text: str) -> str:
    text = html.unescape(strip_markdown(text))
    text = re.sub(r"^\s*(?:Figure|Fig\.?|图)\s+", "Figure ", text, flags=re.I)
    text = text.strip(" -*_。.")
    return text


def extract_declared_alt_text(text: str) -> str:
    text = html.unescape(strip_markdown(text))
    match = re.search(r"\bAlt text\s*[:：]\s*(.+)$", text, flags=re.I)
    if not match:
        return ""
    alt = match.group(1).strip()
    alt = re.split(r"\b(?:Source|来源)\s*[:：]", alt, maxsplit=1)[0].strip()
    alt = alt.strip(" -*_。.")
    if alt and not re.search(r"[.!?。]$", alt):
        alt += "."
    return re.sub(r"\s+", " ", alt)


def caption_without_declared_alt(text: str) -> str:
    text = clean_caption(text)
    text = re.split(r"\bAlt text\s*[:：]", text, maxsplit=1, flags=re.I)[0]
    return text.strip(" -*_。.")


def find_caption(lines: list[str], image_line_index: int) -> str:
    candidates: list[str] = []
    for idx in range(image_line_index + 1, min(len(lines), image_line_index + 6)):
        line = lines[idx].strip()
        if not line:
            continue
        if line.startswith(("![", "```", "|", "#")):
            break
        candidates.append(line)
        if re.search(r"(?:Figure|Fig\.?|图)\s*[A-Z]?\d+", line, flags=re.I):
            break
    if not candidates:
        alt_line = lines[image_line_index].strip()
        return clean_caption(alt_line)
    return clean_caption(" ".join(candidates))


def figure_number(caption: str, source: str, index_in_file: int, unit: str) -> str:
    match = FIGURE_NO_RE.search(caption)
    if match:
        return f"{match.group(1)}-{match.group(2)}"
    basename = Path(source).stem
    p_match = re.search(r"p(\d{2})[_-](\d{2})", basename, re.I)
    if p_match:
        return f"P{p_match.group(1)}-{int(p_match.group(2))}"
    ch_match = re.search(r"ch(\d{2})[_-](\d{2})", basename, re.I)
    if ch_match:
        return f"{int(ch_match.group(1))}-{int(ch_match.group(2))}"
    return f"{unit}-{index_in_file}"


def unit_from_path(path: str) -> str:
    if match := CHAPTER_RE.search(path):
        return f"Ch{int(match.group(1)):02d}"
    if match := PROJECT_RE.search(path):
        return f"P{int(match.group(1)):02d}"
    if match := APPENDIX_RE.search(path):
        return f"Appendix {match.group(1).upper()}"
    if path == "afterword.md":
        return "Afterword"
    return Path(path).stem


def local_image_path(source_file: Path, raw_src: str) -> Path | None:
    src = raw_src.strip().split("#", 1)[0].split("?", 1)[0]
    if not src or re.match(r"^(?:https?:|data:|file:|#)", src):
        return None
    return (source_file.parent / src).resolve()


def image_dimensions(path: Path | None) -> str:
    if path is None or not path.exists():
        return ""
    if path.suffix.lower() == ".svg":
        try:
            from xml.etree import ElementTree as ET

            root = ET.parse(path).getroot()

            def parse(value: str | None) -> str:
                if not value:
                    return ""
                match = re.match(r"\s*([0-9]+(?:\.[0-9]+)?)", value)
                return match.group(1) if match else ""

            width = parse(root.get("width"))
            height = parse(root.get("height"))
            if (not width or not height) and root.get("viewBox"):
                parts = [part for part in re.split(r"[\s,]+", root.get("viewBox", "").strip()) if part]
                if len(parts) == 4:
                    width = width or parts[2]
                    height = height or parts[3]
            return f"{width}x{height}" if width and height else ""
        except Exception:
            return ""
    try:
        from PIL import Image

        with Image.open(path) as image:
            return f"{image.width}x{image.height}"
    except Exception:
        return ""


def summarize_context(lines: list[str], image_line_index: int) -> str:
    context: list[str] = []
    start = max(0, image_line_index - 4)
    end = min(len(lines), image_line_index + 8)
    for idx in range(start, end):
        if idx == image_line_index:
            continue
        line = lines[idx].strip()
        if not line or line.startswith(("```", "|", "!", "#")):
            continue
        context.append(strip_markdown(line))
    return " ".join(context)[:900]


def make_alt_text(caption: str, markdown_alt: str, unit_title: str, context: str) -> tuple[str, str, str]:
    declared = extract_declared_alt_text(caption) or extract_declared_alt_text(markdown_alt)
    if declared:
        alt = declared
        long_description = ""
        if any(word in alt.lower() for word in ["pipeline", "workflow", "architecture", "matrix", "distribution", "comparison", "schema"]):
            long_description = (
                f"Review against the figure and surrounding text in {unit_title}; expand if Springer requests "
                "a longer description for the visual relationships, axes, or sequence."
            )
        return alt[:477].rstrip() + "..." if len(alt) > 480 else alt, long_description, ""

    base = caption_without_declared_alt(caption or markdown_alt)
    if not base:
        base = caption_without_declared_alt(markdown_alt)
    normalized = re.sub(r"^Figure\s+[A-Z]?\d+[-‑–—][A-Za-z0-9]+[:：]?\s*", "", base, flags=re.I).strip()
    if not normalized:
        normalized = base or "Manuscript figure"
    if len(normalized) < 25 and context:
        sentence = re.split(r"(?<=[.!?。])\s+", context.strip())[0]
        if sentence:
            normalized = f"{normalized}. {sentence}"
    alt = normalized
    if not re.search(r"[.!?。]$", alt):
        alt += "."
    alt = re.sub(r"\s+", " ", alt).strip()
    if len(alt) > 480:
        alt = alt[:477].rstrip() + "..."
    needs = []
    if len(alt) < 20:
        needs.append("short-alt-text")
    if re.fullmatch(r"(?:Figure\s*)?[A-Z]?\d+[-‑–—]?[A-Za-z0-9]*\.?", alt, flags=re.I):
        needs.append("number-only-alt-text")
    if re.search(r"\b(image|figure|chart|diagram)\s+(of|showing)\b", alt, flags=re.I):
        pass
    long_description = ""
    if any(word in alt.lower() for word in ["pipeline", "workflow", "architecture", "matrix", "distribution", "comparison", "schema"]):
        long_description = (
            f"Review against the figure and surrounding text in {unit_title}; expand if Springer requests "
            "a longer description for the visual relationships, axes, or sequence."
        )
    status = "Draft - needs human review" if needs else "Draft"
    return alt, long_description, "; ".join(needs)


def zh_reference_for(en_path: str, image_index: int) -> tuple[str, str]:
    zh_path = DOCS_ZH / en_path
    if not zh_path.exists():
        return "", ""
    lines = zh_path.read_text(encoding="utf-8", errors="replace").splitlines()
    count = 0
    for idx, line in enumerate(lines):
        match = IMAGE_RE.search(line)
        if not match:
            continue
        count += 1
        if count == image_index:
            return find_caption(lines, idx), match.group(1).strip()
    return "", ""


def iter_markdown_images(text: str) -> list[tuple[int, str, str]]:
    rows: list[tuple[int, str, str]] = []
    lines = text.splitlines()
    for line_no, line in enumerate(lines, 1):
        for match in IMAGE_RE.finditer(line):
            rows.append((line_no, match.group(1).strip(), match.group(2).strip()))
        for match in HTML_IMG_RE.finditer(line):
            attrs = dict(ATTR_RE.findall(match.group(0)))
            rows.append((line_no, attrs.get("alt", "").strip(), match.group(1).strip()))
    return rows


def collect_rows() -> list[AltTextRow]:
    config = yaml.safe_load(MKDOCS.read_text(encoding="utf-8"))
    items = prepare_items(flatten_nav(find_en_nav(config)))
    rows: list[AltTextRow] = []
    seen: set[tuple[str, int, str]] = set()
    for item in items:
        source_file = DOCS_EN / item.path
        if not source_file.exists():
            continue
        text = source_file.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        image_index = 0
        for line_no, markdown_alt, raw_src in iter_markdown_images(text):
            local = local_image_path(source_file, raw_src)
            if local is None:
                continue
            image_index += 1
            key = (item.path, line_no, raw_src)
            if key in seen:
                continue
            seen.add(key)
            line_index = line_no - 1
            caption = find_caption(lines, line_index)
            unit = unit_from_path(item.path)
            fig_no = figure_number(caption, raw_src, image_index, unit)
            context = summarize_context(lines, line_index)
            alt_text, long_description, notes = make_alt_text(caption, markdown_alt, item.title, context)
            exists = local.exists()
            image_file = rel(local) if exists and local.is_relative_to(ROOT) else str(local)
            zh_caption, zh_alt = zh_reference_for(item.path, image_index)
            row_id = f"ALT-{len(rows) + 1:04d}"
            rows.append(
                AltTextRow(
                    row_id=row_id,
                    language="en",
                    part=item.group,
                    unit=unit,
                    unit_title=item.title,
                    source_markdown=f"docs/en/{item.path}",
                    line=line_no,
                    figure_number=fig_no,
                    caption=caption,
                    image_alt_in_markdown=markdown_alt,
                    image_file=image_file,
                    image_exists="yes" if exists else "no",
                    image_dimensions=image_dimensions(local),
                    image_format=local.suffix.lower().lstrip(".") if local else "",
                    alt_text=alt_text,
                    long_description=long_description,
                    decorative="no",
                    review_status="Draft - needs human review" if notes else "Draft",
                    reviewer="",
                    notes=notes,
                    zh_reference_caption=zh_caption,
                    zh_reference_alt_text=zh_alt,
                )
            )
    return rows


def write_csv(rows: list[AltTextRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()) if rows else list(AltTextRow.__dataclass_fields__.keys()))
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)


def write_json(rows: list[AltTextRow], path: Path) -> None:
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "English Springer manuscript local image references in mkdocs navigation order",
        "row_count": len(rows),
        "rows": [asdict(row) for row in rows],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate(rows: list[AltTextRow]) -> list[str]:
    issues: list[str] = []
    seen_ids: set[str] = set()
    for row in rows:
        if row.row_id in seen_ids:
            issues.append(f"duplicate row_id: {row.row_id}")
        seen_ids.add(row.row_id)
        if row.image_exists != "yes":
            issues.append(f"missing image: {row.row_id} {row.image_file}")
        if not row.alt_text.strip():
            issues.append(f"missing alt text: {row.row_id} {row.image_file}")
        if len(row.alt_text.strip()) < 12:
            issues.append(f"too short alt text: {row.row_id} {row.alt_text!r}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Springer alt-text workbook for manuscript images.")
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="Output CSV sidecar path.")
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON, help="Output JSON sidecar path.")
    parser.add_argument("--check", action="store_true", help="Fail if any image lacks a usable alt text or file.")
    args = parser.parse_args()

    rows = collect_rows()
    if not rows:
        print("[error] no image rows found", file=sys.stderr)
        return 2

    write_csv(rows, args.csv)
    write_json(rows, args.json)

    issues = validate(rows)
    print(f"[ok] CSV sidecar written: {args.csv}")
    print(f"[ok] JSON sidecar written: {args.json}")
    print(f"[stats] rows={len(rows)}, missing_images={sum(1 for row in rows if row.image_exists != 'yes')}, validation_issues={len(issues)}")
    if issues:
        for issue in issues[:50]:
            print(f"[issue] {issue}", file=sys.stderr)
    if args.check and issues:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
