#!/usr/bin/env python3
"""Export print-oriented figure copies for Springer submission.

The manuscript keeps browser/PDF-friendly image references in Markdown and
LaTeX. This script creates an additional production-source folder with EPS
copies for SVG figures and TIFF copies for raster figures, plus a manifest that
maps every converted file back to the manuscript image path.
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
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_EN = ROOT / "docs" / "en"
DEFAULT_OUTPUT_DIR = ROOT / "output" / "springer_print_figures"
DEFAULT_CACHE_DIR = ROOT / "output" / ".cache" / "springer_print_figures"
SUPPORTED_VECTOR = {".svg"}
SUPPORTED_RASTER = {".png", ".jpg", ".jpeg"}


@dataclass
class FigureRef:
    source_markdown: str
    image_path: str


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_markdown_images(markdown_path: Path) -> list[str]:
    text = markdown_path.read_text(encoding="utf-8", errors="replace")
    urls: list[str] = []
    for match in re.finditer(r"!\[[^\]]*]\(([^)]+)\)", text):
        urls.append(match.group(1))
    for match in re.finditer(r"<img[^>]+src=[\"']([^\"']+)[\"'][^>]*>", text, flags=re.I):
        urls.append(match.group(1))
    return urls


def collect_figures() -> list[FigureRef]:
    seen: set[str] = set()
    refs: list[FigureRef] = []
    for markdown_path in sorted(DOCS_EN.rglob("*.md")):
        for raw in iter_markdown_images(markdown_path):
            url = raw.strip().split("#", 1)[0].split("?", 1)[0]
            if not url or re.match(r"^(?:https?:|data:|file:|#)", url):
                continue
            image_path = (markdown_path.parent / url).resolve()
            if not image_path.exists() or not image_path.is_file():
                continue
            if not image_path.is_relative_to(ROOT):
                continue
            rel = image_path.relative_to(ROOT).as_posix()
            if rel in seen:
                continue
            seen.add(rel)
            refs.append(
                FigureRef(
                    source_markdown=markdown_path.relative_to(DOCS_EN).as_posix(),
                    image_path=rel,
                )
            )
    return refs


def safe_output_path(rel_path: str, suffix: str, output_dir: Path) -> Path:
    src = Path(rel_path)
    return output_dir / src.with_suffix(suffix)


def cache_key(src: Path, target_suffix: str, digest: str) -> str:
    return hashlib.sha256(f"{src.relative_to(ROOT).as_posix()}|{digest}|{target_suffix}".encode("utf-8")).hexdigest()


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def convert_svg_to_eps(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    run(["inkscape", str(src), "--export-type=eps", f"--export-filename={dst}"])


def convert_raster_to_tif(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    run(["magick", str(src), "-units", "PixelsPerInch", "-density", "300", "-compress", "lzw", str(dst)])


def export_print_figures(output_dir: Path, cache_dir: Path) -> tuple[list[dict[str, str]], list[str]]:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    errors: list[str] = []
    for ref in collect_figures():
        src = ROOT / ref.image_path
        suffix = src.suffix.lower()
        digest = sha256(src)
        if suffix in SUPPORTED_VECTOR:
            target_suffix = ".eps"
            converter = convert_svg_to_eps
            conversion = "svg_to_eps"
        elif suffix in SUPPORTED_RASTER:
            target_suffix = ".tif"
            converter = convert_raster_to_tif
            conversion = "raster_to_tif"
        else:
            target_suffix = suffix
            converter = None
            conversion = "copied_original_unsupported_for_conversion"

        dst = safe_output_path(ref.image_path, target_suffix, output_dir)
        cached = cache_dir / f"{cache_key(src, target_suffix, digest)}{target_suffix}"
        status = "ok"
        message = ""
        try:
            if converter is None:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            else:
                if not cached.exists():
                    converter(src, cached)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(cached, dst)
        except Exception as exc:  # pragma: no cover - exercised by environment failures
            status = "error"
            message = str(exc)
            errors.append(f"{ref.image_path}: {message}")

        rows.append(
            {
                "source_markdown": ref.source_markdown,
                "original_image_path": ref.image_path,
                "original_sha256": digest,
                "original_format": suffix.lstrip("."),
                "print_format_path": dst.relative_to(output_dir).as_posix(),
                "print_format": target_suffix.lstrip("."),
                "conversion": conversion,
                "status": status,
                "message": message,
            }
        )

    manifest_csv = output_dir / "figures_print_format_manifest.csv"
    fieldnames = [
        "source_markdown",
        "original_image_path",
        "original_sha256",
        "original_format",
        "print_format_path",
        "print_format",
        "conversion",
        "status",
        "message",
    ]
    with manifest_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    (output_dir / "figures_print_format_manifest.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return rows, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Export EPS/TIFF figure copies for Springer production.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--cache-dir", type=Path, default=DEFAULT_CACHE_DIR)
    parser.add_argument("--check", action="store_true", help="Fail if any figure conversion fails.")
    args = parser.parse_args()

    rows, errors = export_print_figures(args.output_dir, args.cache_dir)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["print_format"]] = counts.get(row["print_format"], 0) + 1
    print(f"[ok] print figures: rows={len(rows)}, counts={counts}, errors={len(errors)}")
    print(f"[ok] output: {args.output_dir}")
    if errors:
        for error in errors[:20]:
            print(f"[error] {error}", file=sys.stderr)
        if len(errors) > 20:
            print(f"[error] ... {len(errors) - 20} more", file=sys.stderr)
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
