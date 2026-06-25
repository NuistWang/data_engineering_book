#!/usr/bin/env python3
"""Export a deterministic Springer submission package.

The script organizes the current manuscript, PDFs, figures, permissions,
declarations, audit reports, and checksums into a publisher-facing folder.
It does not fabricate legal proof files; it copies `publishing/permissions`
as provided by the author/editor.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_SLUG = "Data_Engineering_for_Large_Foundation_Models_A_Handbook_Jun_Yu"
DEFAULT_OUTPUT_ROOT = ROOT / "output" / "springer_submission"
PDF_DIR = ROOT / "output" / "pdf"
SUBMISSION_PDF_DIR = PDF_DIR / "data_engineering_book_en_16k_compact_submission_pdfs"
LATEX_PARTS_DIR = PDF_DIR / "data_engineering_book_en_16k_latex_parts"
LATEX_CHAPTERS_DIR = PDF_DIR / "data_engineering_book_en_16k_latex_chapters"
LATEX_ASSETS_DIR = PDF_DIR / "latex_assets_en"
ACCESSIBILITY_DIR = ROOT / "publishing" / "accessibility"
LATEX_EXPORT_SCRIPT = ROOT / "scripts" / "export_en_book_latex.py"
PRINT_FIGURES_SCRIPT = ROOT / "scripts" / "export_print_figures.py"
PRINT_FIGURES_DIR = ROOT / "output" / "springer_print_figures"

SOURCE_DIR_NAME = "01_Source_Files"
PDF_DIR_NAME = "02_PDF_Files"
THIRD_PARTY_DIR_NAME = "03_Third_Party_Permissions"

AUTHOR_PREFIXES = {
    "part1/ch01_": "Jun Yu; Changwen Chen; Ke Wang",
    "part1/ch02_": "Jun Yu; Changwen Chen; Ke Wang",
    "part1/ch03_": "Jun Yu; Ke Wang; Changwen Chen",
    "part2/ch04_": "Jun Yu; Ke Wang; Changwen Chen",
    "part2/ch05_": "Jun Yu; Ke Wang; Changwen Chen",
    "part2/ch06_": "Ke Wang; Fan Yu; Jun Yu",
    "part2/ch07_": "Ke Wang; Fan Yu; Jun Yu",
    "part3/ch08_": "Jun Yu; Ke Wang; Cong Wang",
    "part3/ch09_": "Jun Yu; Ke Wang; Cong Wang",
    "part3/ch10_": "Ke Wang; Cong Wang; Jun Yu",
    "part3/ch11_": "Ke Wang; Cong Wang; Jun Yu",
    "part4/ch12_": "Jun Yu; Ran Zhang; Yang Luo",
    "part4/ch13_": "Jun Yu; Ran Zhang; Yang Luo",
    "part4/ch14_": "Ran Zhang; Yang Luo; Jun Yu",
    "part5/ch15_": "Cong Wang; Ran Zhang; Jun Yu",
    "part5/ch16_": "Cong Wang; Ran Zhang; Jun Yu",
    "part5/ch17_": "Ran Zhang; Yang Luo; Jun Yu",
    "part6/ch18_": "Jun Yu; Ran Zhang; Zhongyi Liu",
    "part6/ch19_": "Jun Yu; Ran Zhang; Zhongyi Liu",
    "part6/ch20_": "Ran Zhang; Zhongyi Liu; Jun Yu",
    "part7/ch21_": "Wenzhuo Du; Gongpeng Zhao; Jun Yu",
    "part7/ch22_": "Wenzhuo Du; Gongpeng Zhao; Jun Yu",
    "part7/ch23_": "Jun Yu; Wenzhuo Du; Gongpeng Zhao",
    "part8/ch24_": "Jun Yu; Wenzhuo Du; Can Wang",
    "part8/ch25_": "Wenzhuo Du; Can Wang; Jun Yu",
    "part8/ch26_": "Wenzhuo Du; Can Wang; Jun Yu",
    "part9/ch27_": "Ran Zhang; Feng Zhao; Wenzhuo Du",
    "part9/ch28_": "Zhongyi Liu; Ye Yu; Wenzhuo Du",
    "part9/ch29_": "Zhongyi Liu; Wenzhuo Du; Jun Yu",
    "part9/ch30_": "Yang Luo; Fang Gao; Wenzhuo Du",
    "part10/ch31_": "Jun Yu; Zhili Wang; Zhongyi Liu",
    "part10/ch32_": "Jun Yu; Zhili Wang; Zhongyi Liu",
    "part10/ch33_": "Zhili Wang; Zhongyi Liu; Jun Yu",
    "part10/ch34_": "Yang Luo; Zhili Wang; Jun Yu",
    "part10/ch35_": "Yang Luo; Zhili Wang; Jun Yu",
    "part11/ch36_": "Zhili Wang; Xin Xu; Jun Yu",
    "part11/ch37_": "Zhili Wang; Xin Xu; Jun Yu",
    "part12/ch38_": "Guanlin Mu; Xuhong Cao",
    "part12/ch39_": "Guanlin Mu; Xuhong Cao",
    "part12/ch40_": "Guanjun Liu; Yuefeng Zou",
    "part12/ch41_": "Lin Xu; Xinyu Chen",
    "part12/ch42_": "Fengxin Chen; Xuan Li",
    "part12/ch43_": "Xuan Li; Fengxin Chen",
    "part13/ch44_": "Ke Wang; Jiaen Liang; Jun Yu",
    "part13/ch45_": "Cong Wang; Xin Xu; Wei Huang",
    "part13/ch46_": "Xin Xu; Shengping Liu; Fan Yu",
    "part13/ch47_": "Xuhong Cao; Ke Wang; Qingsong Liu",
    "part13/ch48_": "Ran Zhang; Jianqing Sun; Fan Yu",
    "part14/p01_": "Xin Xu; Ran Zhang; Jun Yu",
    "part14/p02_": "Xin Xu; Ran Zhang; Jun Yu",
    "part14/p03_": "Jun Yu; Xin Xu; Wenzhuo Du",
    "part14/p04_": "Xin Xu; Wenzhuo Du; Jun Yu",
    "part14/p05_": "Xuhong Cao; Ke Wang; Jun Yu",
    "part14/p06_": "Cong Wang; Xin Xu; Ke Wang",
    "part14/p07_": "Jun Yu; Xin Xu; Zhili Wang",
    "part14/p08_": "Jun Yu; Xin Xu; Zhili Wang",
    "part14/p09_": "Zhongyi Liu; Xin Xu; Guanlin Mu",
    "part14/p10_": "Ke Wang; Xin Xu; Guanlin Mu",
    "part14/p11_": "Jun Yu; Ke Wang; Yang Luo",
    "part14/p12_": "Cong Wang; Xin Xu; Yang Luo",
    "part14/p13_": "Jun Yu; Ke Wang; Wenzhuo Du",
    "part14/p14_": "Yang Luo; Ran Zhang; Wenzhuo Du",
    "part14/p15_": "Xuhong Cao; Zhongyi Liu; Jun Yu",
}


@dataclass
class ManifestRow:
    relative_path: str
    size_bytes: int
    sha256: str
    source_path: str


@dataclass
class SubmissionItem:
    no: str
    title: str
    source: str
    pdf: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    if should_skip_path(src):
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def should_skip_path(path: Path) -> bool:
    return any(part in {".DS_Store", "__MACOSX"} or part.startswith("._") for part in path.parts)


def ignore_system_files(_dir: str, names: list[str]) -> set[str]:
    return {name for name in names if name == ".DS_Store" or name == "__MACOSX" or name.startswith("._")}


def copy_tree(src: Path, dst: Path, ignore=None) -> None:
    if not src.exists():
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=ignore or ignore_system_files)


def latex_root_tex() -> Path:
    return PDF_DIR / "data_engineering_book_en_16k_latex.tex"


def has_tex_files(path: Path) -> bool:
    return path.exists() and any(item.is_file() for item in path.glob("*.tex"))


def latex_sources_complete() -> bool:
    return (
        latex_root_tex().exists()
        and has_tex_files(LATEX_CHAPTERS_DIR)
        and has_tex_files(LATEX_PARTS_DIR)
        and LATEX_ASSETS_DIR.exists()
    )


def run_latex_export(args: list[str]) -> None:
    subprocess.run([sys.executable, str(LATEX_EXPORT_SCRIPT), *args], cwd=ROOT, check=True)


def ensure_latex_sources() -> None:
    if not has_tex_files(LATEX_CHAPTERS_DIR) or not has_tex_files(LATEX_PARTS_DIR) or not LATEX_ASSETS_DIR.exists():
        run_latex_export(["--split"])
    if not latex_root_tex().exists():
        run_latex_export([])
    if not latex_sources_complete():
        missing: list[str] = []
        if not latex_root_tex().exists():
            missing.append(str(latex_root_tex()))
        if not has_tex_files(LATEX_CHAPTERS_DIR):
            missing.append(str(LATEX_CHAPTERS_DIR))
        if not has_tex_files(LATEX_PARTS_DIR):
            missing.append(str(LATEX_PARTS_DIR))
        if not LATEX_ASSETS_DIR.exists():
            missing.append(str(LATEX_ASSETS_DIR))
        raise RuntimeError("LaTeX source export incomplete; missing or empty: " + ", ".join(missing))


def safe_slug(value: str, *, max_len: int = 80) -> str:
    value = value.replace("&", " and ")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-{2,}", "-", value)
    return value[:max_len].strip("-") or "untitled"


def authors_for_source(source: str) -> str:
    normalized = source.replace("\\", "/").strip("`")
    for prefix, authors in AUTHOR_PREFIXES.items():
        if normalized.startswith(prefix) or f"/{prefix}" in normalized:
            return authors
    return "Jun Yu"


def first_author_surname(authors: str) -> str:
    first = re.split(r";|,", authors, maxsplit=1)[0].strip()
    return safe_slug(first.split()[-1], max_len=24) if first else "Yu"


def submission_items() -> list[SubmissionItem]:
    readme = SUBMISSION_PDF_DIR / "README.md"
    if not readme.exists():
        return []
    row_re = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`?([^|`]+?\.pdf)`?\s*\|")
    items: list[SubmissionItem] = []
    for line in readme.read_text(encoding="utf-8", errors="replace").splitlines():
        match = row_re.match(line)
        if not match:
            continue
        no, title, source, pdf = [part.strip().strip("`") for part in match.groups()]
        if no == "---" or title == "Title":
            continue
        items.append(SubmissionItem(no=no, title=title, source=source, pdf=pdf))
    return items


def unit_label(item: SubmissionItem) -> str:
    if item.no.isdigit():
        if item.title.startswith("Project "):
            match = re.match(r"Project\s+(\d+)", item.title)
            return f"Project{int(match.group(1)):02d}" if match else f"Item{int(item.no):02d}"
        if item.title.startswith("Appendix "):
            match = re.match(r"Appendix\s+([A-Z])", item.title)
            return f"Appendix{match.group(1)}" if match else f"Appendix{int(item.no):02d}"
        if item.title.startswith("Chapter "):
            match = re.match(r"Chapter\s+(\d+)", item.title)
            return f"Chap{int(match.group(1)):02d}" if match else f"Chap{int(item.no):02d}"
        return f"Item{int(item.no):02d}"
    if item.no.lower() == "front":
        return "FrontMatter"
    if item.no.lower() == "back":
        return "BackMatter"
    return safe_slug(item.no, max_len=32)


def item_title_for_name(item: SubmissionItem) -> str:
    title = item.title
    title = re.sub(r"^(Chapter|Project)\s+\d+\s*:\s*", "", title)
    title = re.sub(r"^Appendix\s+[A-Z]\s*:\s*", "", title)
    return title


def named_item_filename(item: SubmissionItem, suffix: str) -> str:
    authors = authors_for_source(item.source)
    return f"{first_author_surname(authors)}-{unit_label(item)}-{safe_slug(item_title_for_name(item), max_len=90)}{suffix}"


def tex_for_item(item: SubmissionItem) -> Path | None:
    exact = LATEX_CHAPTERS_DIR / item.pdf.replace(".pdf", ".tex")
    if exact.exists():
        return exact
    if item.no.isdigit():
        prefix = f"{int(item.no):02d}-"
        matches = sorted(LATEX_CHAPTERS_DIR.glob(f"{prefix}*.tex"))
        if matches:
            return matches[0]
    if item.title == "Afterword":
        candidate = LATEX_CHAPTERS_DIR / "72-afterword.tex"
        if candidate.exists():
            return candidate
    return None


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = sorted({key for row in rows for key in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as handle:
        if not fieldnames:
            return
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def rewrite_latex_package_paths(package_dir: Path) -> None:
    latex_root = package_dir / SOURCE_DIR_NAME / "LaTeX"
    replacements = {
        "../latex_assets_en/": "../assets/",
        "latex_assets_en/": "assets/",
        "../data_engineering_book_en_16k_latex_chapters/": "../chapters/",
        "data_engineering_book_en_16k_latex_chapters/": "chapters/",
    }
    for tex_file in sorted(latex_root.rglob("*.tex")):
        text = tex_file.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        tex_file.write_text(text, encoding="utf-8")


def copy_markdown_sources(package_dir: Path) -> None:
    source_root = package_dir / SOURCE_DIR_NAME
    copy_tree(ROOT / "docs" / "en", source_root / "Markdown" / "docs_en")
    copy_tree(LATEX_PARTS_DIR, source_root / "LaTeX" / "parts")
    copy_tree(LATEX_CHAPTERS_DIR, source_root / "LaTeX" / "chapters")
    copy_tree(LATEX_ASSETS_DIR, source_root / "LaTeX" / "assets")
    copy_file(latex_root_tex(), source_root / "LaTeX" / "data_engineering_book_en_16k_latex.tex")
    rewrite_latex_package_paths(package_dir)

    named_dir = source_root / "LaTeX" / "chapters_named_for_submission"
    manifest_rows: list[dict[str, str]] = []
    for item in submission_items():
        tex = tex_for_item(item)
        if tex is None:
            continue
        named = named_item_filename(item, ".tex")
        copy_file(tex, named_dir / named)
        manifest_rows.append(
            {
                "submission_tex_file": named,
                "original_tex_file": tex.name,
                "source_markdown": item.source,
                "title": item.title,
                "authors": authors_for_source(item.source),
            }
        )
    write_csv(source_root / "LaTeX" / "chapter_tex_manifest.csv", manifest_rows)


def copy_supporting_internal_files(package_dir: Path) -> None:
    internal = package_dir / "_Internal_Not_For_Submission"
    copy_file(ROOT / "publishing" / "18_springer_submission_package.md", internal / "Metadata" / "18_springer_submission_package.md")
    copy_file(ROOT / "publishing" / "15_final_delivery_checklist.md", internal / "Metadata" / "15_final_delivery_checklist.md")
    copy_file(ROOT / "publishing" / "19_declarations_and_metadata_templates.md", internal / "Declarations" / "19_declarations_and_metadata_templates.md")
    copy_tree(ROOT / "publishing" / "final_review", internal / "Audit_Reports")


def copy_permissions(package_dir: Path) -> None:
    def ignore_non_submission_permissions(_dir: str, names: list[str]) -> set[str]:
        skipped = ignore_system_files(_dir, names)
        skipped.update(name for name in names if name.endswith("_zh.md"))
        return skipped

    copy_tree(ROOT / "publishing" / "permissions", package_dir / THIRD_PARTY_DIR_NAME, ignore=ignore_non_submission_permissions)


def copy_accessibility(package_dir: Path) -> None:
    dst = package_dir / SOURCE_DIR_NAME / "Accessibility"
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True, exist_ok=True)
    for src in sorted(ACCESSIBILITY_DIR.glob("springer_alt_text_inventory.*")):
        if src.suffix.lower() != ".xlsx":
            continue
        copy_file(src, dst / src.name)


def copy_pdfs(package_dir: Path) -> None:
    pdf_root = package_dir / PDF_DIR_NAME
    full_dir = pdf_root / "Full_Manuscript_PDF"
    chapter_dir = pdf_root / "Individual_Chapter_PDFs"
    full_dir.mkdir(parents=True, exist_ok=True)
    chapter_dir.mkdir(parents=True, exist_ok=True)
    if not SUBMISSION_PDF_DIR.exists():
        return
    copy_file(SUBMISSION_PDF_DIR / "00_full_book_pagenumbered.pdf", full_dir / f"{BOOK_SLUG}-Full-Manuscript.pdf")
    rows: list[dict[str, str]] = []
    used: set[str] = set()
    for item in submission_items():
        src = SUBMISSION_PDF_DIR / item.pdf
        if not src.exists() or src.name == "00_full_book_pagenumbered.pdf":
            continue
        named = named_item_filename(item, ".pdf")
        if named in used:
            named = f"{Path(named).stem}-{safe_slug(item.pdf, max_len=24)}.pdf"
        used.add(named)
        copy_file(src, chapter_dir / named)
        authors = authors_for_source(item.source)
        rows.append(
            {
                "submission_pdf_file": named,
                "original_pdf_file": item.pdf,
                "source_markdown": item.source,
                "title": item.title,
                "authors": authors,
                "first_author_surname": first_author_surname(authors),
            }
        )
    write_csv(pdf_root / "pdf_file_manifest.csv", rows)
    copy_file(SUBMISSION_PDF_DIR / "README.md", pdf_root / "pdf_export_readme.md")


def count_files(path: Path, pattern: str) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.glob(pattern) if item.is_file())


def write_package_readme(package_dir: Path) -> None:
    chapter_pdf_count = count_files(package_dir / PDF_DIR_NAME / "Individual_Chapter_PDFs", "*.pdf")
    full_pdf_count = count_files(package_dir / PDF_DIR_NAME / "Full_Manuscript_PDF", "*.pdf")
    latex_source = f"{SOURCE_DIR_NAME}/LaTeX/data_engineering_book_en_16k_latex.tex"
    readme = f"""# Data Engineering for Large Foundation Models: A Handbook

This folder is the publisher-facing Springer submission package generated from the current repository state.

## Package Contents

| Folder | Purpose |
| --- | --- |
| `{SOURCE_DIR_NAME}` | English manuscript source files: LaTeX, Markdown backup, renamed figure files, and the alt-text Excel workbook. |
| `{PDF_DIR_NAME}` | Complete book PDF and individual PDFs. Current full PDF count: {full_pdf_count}; individual PDF count: {chapter_pdf_count}. |
| `{THIRD_PARTY_DIR_NAME}` | Author/editor-provided permissions and originality/rights confirmation copied as-is. |

## ZIP Scope

When `--zip` is used, the ZIP archive is intentionally limited to the three publisher-facing folders requested by Springer Nature's manuscript submission instructions: `{SOURCE_DIR_NAME}`, `{PDF_DIR_NAME}`, and `{THIRD_PARTY_DIR_NAME}`. Internal audit files, checksums, and local working notes are left in `_Internal_Not_For_Submission` in the unpacked package only.

## Submission Notes

- `{latex_source}` is the root LaTeX export.
- `{SOURCE_DIR_NAME}/LaTeX/chapters` keeps the original split TeX files needed by the root TeX file.
- `{SOURCE_DIR_NAME}/LaTeX/chapters_named_for_submission` provides duplicate chapter source filenames using first-author surname and chapter/project/appendix label.
- `{SOURCE_DIR_NAME}/Figures` contains the renamed figure files referenced by the English manuscript.
- `{SOURCE_DIR_NAME}/Figures_Print_Formats` contains EPS copies for SVG figures and TIFF copies for raster figures, with `figures_print_format_manifest.csv` mapping each production copy back to the manuscript image path.
- `{SOURCE_DIR_NAME}/Accessibility/springer_alt_text_inventory.xlsx` is the reviewed alt-text Excel workbook to submit with the final manuscript.
- `{THIRD_PARTY_DIR_NAME}` contains the rights/originality confirmation; signed external publisher forms, if any, should be added there before upload.

## Human-Only Items

The following human-only items cannot be generated by this repository and must be supplied or confirmed by the author/editor or Springer production workflow when requested:

- signed License to Publish forms;
- publisher-approved copyright page and imprint metadata;
- original third-party permission correspondence beyond the signoff notes already present;
- final author/editor approval of any proof-stage changes.

## Verification Pointers

- PDF manifest: `{PDF_DIR_NAME}/pdf_file_manifest.csv`.
- Alt-text coverage report: `_Internal_Not_For_Submission/alt_text_coverage_report.csv`.
"""
    (package_dir / "README.md").write_text(readme, encoding="utf-8")


def markdown_image_records(markdown_path: Path) -> list[dict[str, str]]:
    text = markdown_path.read_text(encoding="utf-8", errors="replace")
    urls: list[tuple[str, str]] = []
    for match in re.finditer(r"!\[([^\]]*)]\(([^)]+)\)", text):
        urls.append((match.group(2), match.group(1)))
    for match in re.finditer(r"<img[^>]+src=[\"']([^\"']+)[\"'][^>]*>", text, flags=re.I):
        urls.append((match.group(1), ""))
    records: list[dict[str, str]] = []
    for raw, alt in urls:
        url = raw.strip().split("#", 1)[0].split("?", 1)[0]
        if not url or re.match(r"^(?:https?:|data:|file:|#)", url):
            continue
        path = (markdown_path.parent / url).resolve()
        if path.exists() and path.is_file() and path.is_relative_to(ROOT):
            records.append(
                {
                    "source_markdown": markdown_path.relative_to(ROOT / "docs" / "en").as_posix(),
                    "image_path": path.relative_to(ROOT).as_posix(),
                    "markdown_alt": alt,
                }
            )
    return records


def read_alt_text_paths() -> set[str]:
    csv_path = ACCESSIBILITY_DIR / "springer_alt_text_inventory.csv"
    if not csv_path.exists():
        return set()
    paths: set[str] = set()
    with csv_path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.reader(handle):
            if len(row) < 11:
                continue
            value = row[10].strip()
            if value and value.lower() not in {"image file", "图片位置"}:
                paths.add(value)
                paths.add(value.removeprefix("./"))
                if value.startswith("docs/"):
                    paths.add(value)
                else:
                    paths.add(f"docs/{value}")
    return paths


def copy_figures(package_dir: Path) -> None:
    source_root = package_dir / SOURCE_DIR_NAME
    figure_root = source_root / "Figures"
    records: list[dict[str, str]] = []
    for markdown_path in sorted((ROOT / "docs" / "en").rglob("*.md")):
        records.extend(markdown_image_records(markdown_path))
    alt_paths = read_alt_text_paths()
    coverage_rows: list[dict[str, str]] = []
    for record in sorted(records, key=lambda item: (item["source_markdown"], item["image_path"])):
        src = ROOT / record["image_path"]
        copy_file(src, figure_root / record["image_path"])
        alt_match = record["image_path"] in alt_paths or f"docs/{record['image_path'].removeprefix('docs/')}" in alt_paths
        coverage_rows.append(
            {
                "image_path": record["image_path"],
                "source_markdown": record["source_markdown"],
                "alt_text_inventory_match": "yes" if alt_match else "no",
            }
        )
    write_csv(package_dir / "_Internal_Not_For_Submission" / "alt_text_coverage_report.csv", coverage_rows)


def copy_print_figures(package_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(PRINT_FIGURES_SCRIPT), "--output-dir", str(PRINT_FIGURES_DIR), "--check"],
        cwd=ROOT,
        check=True,
    )
    copy_tree(PRINT_FIGURES_DIR, package_dir / SOURCE_DIR_NAME / "Figures_Print_Formats")


def collect_manifest(package_dir: Path) -> list[ManifestRow]:
    rows: list[ManifestRow] = []
    for path in sorted(package_dir.rglob("*")):
        if not path.is_file():
            continue
        if should_skip_path(path):
            continue
        if path.relative_to(package_dir).as_posix().startswith("_Internal_Not_For_Submission/Checksums/"):
            continue
        rel = path.relative_to(package_dir).as_posix()
        rows.append(
            ManifestRow(
                relative_path=rel,
                size_bytes=path.stat().st_size,
                sha256=sha256(path),
                source_path="",
            )
        )
    return rows


def write_manifest(package_dir: Path) -> None:
    rows = collect_manifest(package_dir)
    checksums = package_dir / "_Internal_Not_For_Submission" / "Checksums"
    checksums.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).isoformat()
    payload = {
        "book": "Data Engineering for Large Foundation Models: A Handbook",
        "generated_at_utc": generated_at,
        "files": [asdict(row) for row in rows],
    }
    (checksums / "manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (checksums / "manifest.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "size_bytes", "sha256", "source_path"])
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)


def create_zip_archive(package_dir: Path) -> Path:
    zip_path = package_dir.with_suffix(".zip")
    if zip_path.exists():
        zip_path.unlink()
    submission_dirs = {SOURCE_DIR_NAME, PDF_DIR_NAME, THIRD_PARTY_DIR_NAME}
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(package_dir.rglob("*")):
            if not path.is_file():
                continue
            if should_skip_path(path):
                continue
            rel_to_package = path.relative_to(package_dir)
            if not rel_to_package.parts or rel_to_package.parts[0] not in submission_dirs:
                continue
            if path.name.endswith(".inspect.ndjson"):
                continue
            archive.write(path, path.relative_to(package_dir.parent).as_posix())
    return zip_path


def export_package(output_root: Path = DEFAULT_OUTPUT_ROOT, *, include_pdfs: bool = True, include_figures: bool = True) -> Path:
    package_dir = output_root / BOOK_SLUG
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir(parents=True, exist_ok=True)
    for name in [SOURCE_DIR_NAME, PDF_DIR_NAME, THIRD_PARTY_DIR_NAME, "_Internal_Not_For_Submission"]:
        (package_dir / name).mkdir(parents=True, exist_ok=True)
    ensure_latex_sources()
    copy_markdown_sources(package_dir)
    copy_supporting_internal_files(package_dir)
    copy_permissions(package_dir)
    copy_accessibility(package_dir)
    if include_pdfs:
        copy_pdfs(package_dir)
    if include_figures:
        copy_figures(package_dir)
        copy_print_figures(package_dir)
    write_package_readme(package_dir)
    write_manifest(package_dir)
    return package_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Export the Springer submission package.")
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--no-pdfs", action="store_true", help="Skip copying generated PDF outputs.")
    parser.add_argument("--no-figures", action="store_true", help="Skip copying referenced figure files.")
    parser.add_argument("--zip", action="store_true", help="Also create a ZIP archive next to the package folder.")
    args = parser.parse_args()
    package_dir = export_package(args.output_root, include_pdfs=not args.no_pdfs, include_figures=not args.no_figures)
    print(f"[ok] Springer submission package written: {package_dir}")
    print(f"[ok] Manifest: {package_dir / '_Internal_Not_For_Submission' / 'Checksums' / 'manifest.json'}")
    if args.zip:
        zip_path = create_zip_archive(package_dir)
        print(f"[ok] ZIP archive written: {zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
