"""Build the Chinese USTC Press submission package.

The package is intentionally separate from the Springer submission outputs. It
contains chapter-level LaTeX source files, local images, warnings, and a compiled
Chinese PDF for preview.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

import export_en_book_latex as en_latex
import export_zh_book_latex as zh_latex


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_DIR = ROOT / "output" / "ustc_press_submission"
LATEX_DIR = PACKAGE_DIR / "01_LaTeX"
CHAPTERS_DIR = LATEX_DIR / "chapters"
IMAGES_DIR = LATEX_DIR / "images"
PDF_DIR = PACKAGE_DIR / "03_PDF"
LOG_DIR = PACKAGE_DIR / "04_Build_Logs"
MAIN_TEX = LATEX_DIR / "main.tex"
OUT_PDF = PDF_DIR / "大模型数据工程_中国科大出版社送审稿.pdf"
OUT_WARNINGS = LOG_DIR / "ustc_press_latex_warnings.txt"


def breakable_monospace(value: str) -> str:
    return (
        value.replace(r"\_", r"\_\allowbreak{}")
        .replace("/", r"/\allowbreak{}")
        .replace(".", r".\allowbreak{}")
        .replace("-", r"-\allowbreak{}")
    )


URL_PATTERN = r"https?://[A-Za-z0-9._~:/?#@!$&'()*+,;=%-]+"


def ustc_inline_to_latex(text: str) -> str:
    text = re.sub(r"<(https?://[^>\s]+)>", r"\1", text)
    text = re.sub(rf"({URL_PATTERN})", lambda match: normalize_bare_url_for_latex(match, text), text)
    rendered = en_latex.inline_to_latex(text)
    return rendered


def normalize_bare_url_for_latex(match: re.Match[str], source: str) -> str:
    url = match.group(1)
    previous = source[match.start(1) - 1] if match.start(1) > 0 else ""
    if previous in "([":
        return url
    trailing = ""
    while url and url[-1] in ".,;:。，；：、！？）】》\"'":
        trailing = url[-1] + trailing
        url = url[:-1]
    return f"[{url}]({url}){trailing}"


def ustc_render_table(lines: list[str], stats: zh_latex.ExportStats) -> str:
    stats.tables += 1
    header = zh_latex.split_table_row(lines[0])
    rows = [zh_latex.split_table_row(line) for line in lines[2:]]
    cols = max(1, len(header))
    width = max(0.075, min(0.28, 0.82 / cols))
    spec = (
        "@{}"
        + "".join([rf">{{\RaggedRight\hspace{{0pt}}\arraybackslash}}p{{{width:.3f}\textwidth}}" for _ in range(cols)])
        + "@{}"
    )

    def normalize(row: list[str]) -> list[str]:
        row = row[:cols]
        return row + [""] * (cols - len(row))

    rendered: list[str] = [
        r"\begingroup",
        r"\footnotesize",
        r"\setlength{\tabcolsep}{3pt}",
        r"\renewcommand{\arraystretch}{1.16}",
        rf"\begin{{longtable}}{{{spec}}}",
        r"\hline",
    ]
    rendered.append(
        r"\rowcolor{tablehead} "
        + " & ".join(rf"\textbf{{{ustc_inline_to_latex(cell)}}}" for cell in normalize(header))
        + r" \\ \hline"
    )
    rendered.append(r"\endfirsthead")
    rendered.append(
        r"\rowcolor{tablehead} "
        + " & ".join(rf"\textbf{{{ustc_inline_to_latex(cell)}}}" for cell in normalize(header))
        + r" \\ \hline"
    )
    rendered.append(r"\endhead")
    for row in rows:
        rendered.append(" & ".join(ustc_inline_to_latex(cell) for cell in normalize(row)) + r" \\ \hline")
    rendered.append(r"\end{longtable}")
    rendered.append(r"\endgroup")
    return "\n".join(rendered)


def ustc_render_heading(line: str) -> str:
    match = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
    if not match:
        return ustc_inline_to_latex(line)
    level = len(match.group(1))
    title = ustc_inline_to_latex(match.group(2).strip())
    toc_titles = {1: "chapter", 2: "section", 3: "subsection"}
    macros = {
        1: "ustcchapter",
        2: "ustcsection",
        3: "ustcsubsection",
        4: "ustcsubsubsection",
        5: "ustcparagraph",
        6: "ustcparagraph",
    }
    macro = macros[level]
    needed_space = "8" if level == 1 else "5" if level == 2 else "4"
    block = [rf"\Needspace{{{needed_space}\baselineskip}}"]
    if level in toc_titles:
        block.extend(
            [
                r"\phantomsection",
                rf"\{macro}{{{title}}}",
                rf"\addcontentsline{{toc}}{{{toc_titles[level]}}}{{{title}}}",
            ]
        )
        if level == 1:
            block.append(rf"\markboth{{{title}}}{{{title}}}")
    else:
        block.append(rf"\{macro}{{{title}}}")
    return "\n".join(block)


def ustc_render_source_header(item: zh_latex.NavItem) -> str:
    header = ustc_inline_to_latex(item.title)
    return r"\noindent\parbox{\textwidth}{\small\textsf{\RaggedRight " + header + r"}}\par\vspace{1.5mm}"


def polish_contributors_tex(tex: str) -> str:
    def repl(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        body = match.group(2).lstrip()
        return rf"\par\noindent{{\bfseries {name}}}\par\vspace{{0.15em}}" + "\n" + rf"\noindent {body}"

    return re.sub(
        r"\\textbf\{([^{}\n]+)\}\s*\n\s*\n([^\\\n][^\n]*)",
        repl,
        tex,
    )


def polish_reference_sections(tex: str) -> str:
    reference_headings = [
        r"\ustcsection{参考文献}",
        r"\ustcsection{References}",
        r"\ustcchapter{参考文献}",
        r"\ustcchapter{References}",
    ]
    if not any(heading in tex for heading in reference_headings):
        return tex
    lines = tex.splitlines()
    out: list[str] = []
    in_references = False
    pending_reference_setup = False
    for line in lines:
        if in_references and line.startswith(r"\Needspace{"):
            out.append(r"\endgroup")
            in_references = False
        out.append(line)
        if any(line.strip() == heading for heading in reference_headings):
            pending_reference_setup = True
            continue
        if pending_reference_setup and line.startswith(r"\addcontentsline"):
            out.extend(
                [
                    r"\begingroup",
                    r"\setlength{\parindent}{0pt}",
                    r"\setlength{\parskip}{0.45em}",
                ]
            )
            in_references = True
            pending_reference_setup = False
    if in_references:
        out.append(r"\endgroup")
    return "\n".join(out)


def polish_unit_tex(tex: str, item: zh_latex.NavItem) -> str:
    tex = polish_reference_sections(tex)
    if item.path == "contributors.md":
        tex = polish_contributors_tex(tex)
    if item.path in {
        "title_page.md",
        "author_affiliations.md",
        "online_resources.md",
        "contributors.md",
    }:
        tex = wrap_ragged_frontmatter(tex)
    return tex


def wrap_ragged_frontmatter(tex: str) -> str:
    parts = tex.split("\n\n", 2)
    if len(parts) < 3:
        return tex
    prefix = "\n\n".join(parts[:2])
    body = parts[2].strip()
    return (
        prefix
        + "\n\n"
        + r"\begingroup\RaggedRight\setlength{\parindent}{0pt}"
        + "\n"
        + body
        + "\n"
        + r"\par\endgroup"
        + "\n"
    )


def install_ustc_render_overrides() -> None:
    zh_latex.inline_to_latex = ustc_inline_to_latex
    zh_latex.render_table = ustc_render_table
    zh_latex.render_heading = ustc_render_heading


def ustc_preamble(stats: zh_latex.ExportStats) -> str:
    return rf"""
\documentclass[UTF8,openany,10pt]{{ctexbook}}
\usepackage[paperwidth=185mm,paperheight=260mm,top=22mm,bottom=21mm,left=18mm,right=18mm,headheight=14pt]{{geometry}}
\usepackage{{fontspec}}
\setmainfont{{Arial Unicode MS}}
\setCJKmainfont{{Songti SC}}
\setCJKsansfont{{PingFang SC}}
\setCJKmonofont{{PingFang SC}}
\setmonofont{{Menlo}}
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{graphicx}}
\usepackage{{float}}
\usepackage{{caption}}
\usepackage{{longtable}}
\usepackage{{booktabs}}
\usepackage{{array}}
\usepackage{{ragged2e}}
\usepackage[table]{{xcolor}}
\usepackage{{enumitem}}
\usepackage{{fvextra}}
\usepackage{{hyperref}}
\usepackage{{needspace}}
\hypersetup{{colorlinks=true,linkcolor=black,urlcolor=blue,citecolor=black}}
\definecolor{{tablehead}}{{RGB}}{{238,243,248}}
\definecolor{{codeframe}}{{RGB}}{{190,198,210}}
\DefineVerbatimEnvironment{{printcode}}{{Verbatim}}{{breaklines=true,breakanywhere=true,fontsize=\scriptsize,frame=single,framesep=2mm,rulecolor=\color{{codeframe}}}}
\setlist{{nosep,leftmargin=2em}}
\setlength{{\parindent}}{{2em}}
\setlength{{\parskip}}{{0.25em}}
\setlength{{\emergencystretch}}{{3em}}
\setlength{{\leftmargini}}{{1.5em}}
\renewenvironment{{quote}}{{\list{{}}{{\leftmargin=1.5em\rightmargin=1.5em}}\item\relax}}{{\endlist}}
\newcommand{{\ustcchapter}}[1]{{\noindent{{\LARGE\bfseries #1}}\par\vspace{{1.2em}}}}
\newcommand{{\ustcsection}}[1]{{\par\vspace{{1.0em}}\noindent{{\Large\bfseries #1}}\par\vspace{{0.55em}}}}
\newcommand{{\ustcsubsection}}[1]{{\par\vspace{{0.8em}}\noindent{{\large\bfseries #1}}\par\vspace{{0.35em}}}}
\newcommand{{\ustcsubsubsection}}[1]{{\par\vspace{{0.55em}}\noindent{{\normalsize\bfseries #1}}\par\vspace{{0.25em}}}}
\newcommand{{\ustcparagraph}}[1]{{\par\vspace{{0.35em}}\noindent{{\normalsize\bfseries #1}}\quad}}
\linespread{{1.18}}
\captionsetup{{font=small,labelformat=empty}}
\sloppy

\title{{大模型数据工程：架构、算法及项目实战}}
\author{{於俊、陈长汶、于璠、王聪、骆阳、张然、杜文卓、徐鑫、王柯、汪志立、刘中一、曹旭宏、穆冠霖、刘冠君、邹月峰、徐霖、陈新宇、陈凤欣、李轩、Gongpeng Zhao、王灿、Feng Zhao、Ye Yu、Fang Gao、Jiaen Liang、Wei Huang、Shengping Liu、Qingsong Liu、Jianqing Sun}}
\date{{中国科学技术大学出版社中文送审稿\\LaTeX 分章节源文件包\\生成文件数：{stats.files}；图片：{stats.images}；代码块：{stats.code_blocks}；表格：{stats.tables}}}
"""


class UstcAssetManager(zh_latex.AssetManager):
    def register(self, image_path: Path, source_file: Path) -> str | None:
        self.stats.images += 1
        image_path = image_path.resolve()
        suffix = image_path.suffix.lower()
        if not image_path.exists():
            self.stats.unsupported_images += 1
            self.stats.warnings.append(
                f"missing image skipped: {source_file.relative_to(ROOT)} -> {image_path}"
            )
            return None
        if suffix in {".gif", ".webp"}:
            self.stats.unsupported_images += 1
            self.stats.warnings.append(
                f"unsupported image format skipped: {source_file.relative_to(ROOT)} -> {image_path}"
            )
            return None
        if image_path in self._seen:
            return self._seen[image_path]

        self._counter += 1
        if suffix == ".svg":
            target_suffix = ".png"
            target_name = f"image_{self._counter:04d}{target_suffix}"
            target = self.asset_dir / target_name
            try:
                en_latex.convert_svg_to_png(image_path, target)
            except Exception as exc:
                self.stats.unsupported_images += 1
                self.stats.warnings.append(
                    f"svg conversion failed: {source_file.relative_to(ROOT)} -> {image_path} ({exc})"
                )
                return None
        else:
            actual_suffix = zh_latex.detect_image_suffix(image_path)
            if actual_suffix is None:
                self.stats.unsupported_images += 1
                self.stats.warnings.append(
                    f"invalid image skipped: {source_file.relative_to(ROOT)} -> {image_path}"
                )
                return None
            target_suffix = actual_suffix
            target_name = f"image_{self._counter:04d}{target_suffix}"
            target = self.asset_dir / target_name
            shutil.copy2(image_path, target)

        rel = f"{self.asset_dir.name}/{target_name}"
        self._seen[image_path] = rel
        return rel


def is_submission_unit(item: zh_latex.NavItem) -> bool:
    if item.path == "index.md":
        return False
    if re.search(r"part\d+/index\.md$", item.path):
        return False
    return True


def submission_items(items: list[zh_latex.NavItem]) -> list[zh_latex.NavItem]:
    return [item for item in items if is_submission_unit(item)]


def latex_unit_slug(item: zh_latex.NavItem, index: int) -> str:
    stem = Path(item.path).with_suffix("").as_posix()
    stem = stem.replace("/", "-").replace("_", "-")
    stem = re.sub(r"[^A-Za-z0-9-]+", "-", stem).strip("-").lower()
    return f"{index:02d}-{stem}.tex"


def input_line(path: Path) -> str:
    rel = Path(os.path.relpath(path, LATEX_DIR)).as_posix()
    return rf"\input{{{rel}}}"


def build_wrapper(input_paths: list[Path], stats: zh_latex.ExportStats) -> str:
    contributors_index = next(
        (index for index, path in enumerate(input_paths) if path.name.endswith("-contributors.tex")),
        len(input_paths),
    )
    abbreviations_index = next(
        (index for index, path in enumerate(input_paths) if path.name.endswith("-abbreviations.tex")),
        len(input_paths),
    )
    front_cutoff = min(contributors_index, abbreviations_index)
    body_start = max(contributors_index, abbreviations_index) + 1

    front_includes = [input_line(path) for path in input_paths[:front_cutoff]]
    catalog_tail_includes = [
        input_line(path)
        for path in input_paths[front_cutoff:body_start]
        if path.name.endswith("-contributors.tex") or path.name.endswith("-abbreviations.tex")
    ]
    body_includes = [input_line(path) for path in input_paths[body_start:]]

    includes = front_includes + [r"\tableofcontents"] + catalog_tail_includes
    if body_includes:
        includes.extend([r"\mainmatter", *body_includes])
    return "\n".join(
        [
            ustc_preamble(stats),
            r"\begin{document}",
            r"\frontmatter",
            r"\begin{titlepage}",
            r"\centering",
            r"\vspace*{0.30\textheight}",
            r"{\Huge\bfseries 大模型数据工程\par}",
            r"\vspace{6mm}",
            r"{\Large\bfseries 架构、算法及项目实战\par}",
            r"\vspace{22mm}",
            r"{\large\begin{minipage}{0.88\textwidth}\centering 於俊、陈长汶、于璠、王聪、骆阳、张然、杜文卓、徐鑫、王柯、汪志立、刘中一、曹旭宏、穆冠霖、刘冠君、邹月峰、徐霖、陈新宇、陈凤欣、李轩、Gongpeng Zhao、王灿、Feng Zhao、Ye Yu、Fang Gao、Jiaen Liang、Wei Huang、Shengping Liu、Qingsong Liu、Jianqing Sun\end{minipage}\par}",
            r"\vfill",
            rf"{{\large 中国科学技术大学出版社中文送审稿\par LaTeX 分章节源文件包\par 生成文件数：{stats.files}；图片：{stats.images}；代码块：{stats.code_blocks}；表格：{stats.tables}\par}}",
            r"\end{titlepage}",
            "\n\n".join(includes),
            r"\end{document}",
            "",
        ]
    )


def build_unit_tex(
    item: zh_latex.NavItem,
    assets: zh_latex.AssetManager,
    stats: zh_latex.ExportStats,
    tex_dir: Path,
) -> str:
    source_file = zh_latex.DOCS_ZH / item.path
    if not source_file.exists():
        stats.missing += 1
        stats.warnings.append(f"missing nav source: {source_file.relative_to(ROOT)}")
        return ""
    stats.files += 1
    text = source_file.read_text(encoding="utf-8")
    unit_tex = "\n\n".join(
        [
            r"\clearpage",
            ustc_render_source_header(item),
            zh_latex.markdown_to_latex(text, source_file, assets, stats, tex_dir),
        ]
    ).strip() + "\n"
    return polish_unit_tex(unit_tex, item)


def compile_with_xelatex(tex_path: Path, timeout: int) -> Path:
    xelatex = shutil.which("xelatex")
    if xelatex is None:
        raise RuntimeError("xelatex is required to compile the USTC Press preview PDF")
    for suffix in (".aux", ".toc", ".out", ".lof", ".lot", ".fls", ".fdb_latexmk", ".log"):
        stale = tex_path.with_suffix(suffix)
        if stale.exists():
            stale.unlink()
    log_file = LOG_DIR / "xelatex_build.log"
    cmd = [
        xelatex,
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        tex_path.name,
    ]
    combined_logs: list[str] = []
    previous_toc: str | None = None
    for round_no in range(1, 5):
        proc = subprocess.run(
            cmd,
            cwd=tex_path.parent,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        combined_logs.append(f"===== xelatex pass {round_no} rc={proc.returncode} =====\n")
        combined_logs.append(proc.stdout)
        combined_logs.append(proc.stderr)
        if proc.returncode != 0:
            log_file.write_text("\n".join(combined_logs), encoding="utf-8")
            raise RuntimeError(f"xelatex failed on pass {round_no}; see {log_file}")
        toc_path = tex_path.with_suffix(".toc")
        current_toc = toc_path.read_text(encoding="utf-8", errors="ignore") if toc_path.exists() else ""
        if round_no >= 2 and current_toc == previous_toc:
            combined_logs.append(f"===== table of contents stabilized after pass {round_no} =====\n")
            break
        previous_toc = current_toc
    log_file.write_text("\n".join(combined_logs), encoding="utf-8")
    built_pdf = tex_path.with_suffix(".pdf")
    if not built_pdf.exists() or built_pdf.stat().st_size < 100_000:
        raise RuntimeError("PDF was not produced or is suspiciously small")
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(built_pdf, OUT_PDF)
    return OUT_PDF


def write_readme(stats: zh_latex.ExportStats, chapter_paths: list[Path]) -> None:
    lines = [
        "# 中国科学技术大学出版社中文交付包",
        "",
        "本目录独立生成，供中文出版社送审与排版沟通使用；不复用或覆盖英文版交付目录。",
        "",
        "## 当前包含",
        "",
        "- `01_LaTeX/main.tex`：全书主 LaTeX 文件。",
        "- `01_LaTeX/chapters/`：按章节、附录、卷前卷后拆分的 LaTeX 源文件。",
        "- `01_LaTeX/images/`：编译 PDF 所需图片；Markdown 中的 SVG 已转换为 PNG。",
        "- `03_PDF/大模型数据工程_中国科大出版社送审稿.pdf`：本次导出的中文预览 PDF。",
        "- `04_Build_Logs/`：图片、LaTeX 转换和编译告警。",
        "- `00_Audit_Reports/`：中英文同步与中文出版语气检查报告。",
        "",
        "## 生成统计",
        "",
        f"- 源文件单元：{stats.files}",
        f"- 图片引用：{stats.images}",
        f"- 未能内嵌图片：{stats.unsupported_images}",
        f"- 代码块：{stats.code_blocks}",
        f"- 表格：{stats.tables}",
        f"- LaTeX 单元文件：{len(chapter_paths)}",
        "",
        "## 后续等待出版社确认的材料",
        "",
        "CIP、ISBN、版权页、作者简介、合同与授权、终校红样、封面与版式模板等，待出版社给出正式清单后再补齐。",
        "",
    ]
    (PACKAGE_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def export_package(limit: int, compile_pdf: bool, timeout: int) -> None:
    for path in (LATEX_DIR, PDF_DIR, LOG_DIR):
        path.mkdir(parents=True, exist_ok=True)
    if CHAPTERS_DIR.exists():
        shutil.rmtree(CHAPTERS_DIR)
    if IMAGES_DIR.exists():
        shutil.rmtree(IMAGES_DIR)
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    zh_latex.OUT_DIR = LATEX_DIR
    zh_latex.ASSET_DIR = IMAGES_DIR
    zh_latex.latex_preamble = ustc_preamble
    install_ustc_render_overrides()

    config = yaml.safe_load(zh_latex.MKDOCS.read_text(encoding="utf-8"))
    items = submission_items(zh_latex.flatten_nav(zh_latex.find_zh_nav(config)))
    if limit:
        items = items[:limit]

    total = zh_latex.ExportStats()
    assets = UstcAssetManager(IMAGES_DIR, total)
    assets.reset()
    chapter_paths: list[Path] = []
    manifest_lines = [
        "# LaTeX 分章节文件清单",
        "",
        "| 序号 | LaTeX 文件 | Markdown 源文件 | 标题 |",
        "| --- | --- | --- | --- |",
    ]

    for index, item in enumerate(items, 1):
        chapter_stats = zh_latex.ExportStats()
        assets.stats = chapter_stats
        tex_path = CHAPTERS_DIR / latex_unit_slug(item, index)
        unit_tex = build_unit_tex(item, assets, chapter_stats, LATEX_DIR)
        zh_latex.write_outputs(unit_tex, chapter_stats, tex_path, tex_path.with_suffix(".warnings.txt"))
        chapter_paths.append(tex_path)
        manifest_lines.append(f"| {index} | `{tex_path.name}` | `{item.path}` | {item.title} |")
        total.files += chapter_stats.files
        total.missing += chapter_stats.missing
        total.images += chapter_stats.images
        total.unsupported_images += chapter_stats.unsupported_images
        total.code_blocks += chapter_stats.code_blocks
        total.tables += chapter_stats.tables
        total.warnings.extend(chapter_stats.warnings)

    main_stats = zh_latex.ExportStats(
        files=total.files,
        missing=total.missing,
        images=total.images,
        unsupported_images=total.unsupported_images,
        code_blocks=total.code_blocks,
        tables=total.tables,
        warnings=total.warnings,
    )
    zh_latex.write_outputs(build_wrapper(chapter_paths, main_stats), main_stats, MAIN_TEX, OUT_WARNINGS)
    (CHAPTERS_DIR / "README.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    write_readme(main_stats, chapter_paths)
    if compile_pdf:
        pdf_path = compile_with_xelatex(MAIN_TEX, timeout)
        print(f"[ok] PDF written: {pdf_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export the Chinese USTC Press submission package")
    parser.add_argument("--compile", action="store_true", help="Compile the preview PDF with XeLaTeX")
    parser.add_argument("--limit", type=int, default=0, help="Only export the first N units for smoke testing")
    parser.add_argument("--timeout", type=int, default=2400, help="XeLaTeX timeout in seconds")
    args = parser.parse_args()
    export_package(args.limit, args.compile, args.timeout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
