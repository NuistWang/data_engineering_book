"""Audit USTC Press LaTeX/PDF outputs for pre-submission layout blockers."""

from __future__ import annotations

import csv
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "output" / "ustc_press_submission"
LATEX = PACKAGE / "01_LaTeX"
CHAPTERS = LATEX / "chapters"
PDF = PACKAGE / "03_PDF" / "大模型数据工程_中国科大出版社送审稿.pdf"
LOG = PACKAGE / "04_Build_Logs" / "xelatex_build.log"
REPORT_DIR = PACKAGE / "00_Audit_Reports"
CSV_OUT = REPORT_DIR / "ustc_layout_blockers.csv"
MD_OUT = REPORT_DIR / "ustc_layout_blockers.md"


@dataclass
class Finding:
    issue_type: str
    severity: str
    location: str
    evidence: str
    suggestion: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def line_no(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit_tex_sources() -> list[Finding]:
    findings: list[Finding] = []
    for tex in sorted(CHAPTERS.glob("*.tex")):
        text = read_text(tex)
        for match in re.finditer(r"\\begin\{longtable\}\{([^}]*)\}", text):
            spec = match.group(1)
            cols = spec.count(r"\textwidth")
            widths = [float(value) for value in re.findall(r"p\{([0-9.]+)\\textwidth\}", spec)]
            if cols >= 6 or sum(widths) > 0.92:
                findings.append(
                    Finding(
                        "宽表风险",
                        "P1",
                        f"{tex.name}:{line_no(text, match.start())}",
                        f"columns={cols}, width_sum={sum(widths):.3f}",
                        "改为更窄列宽、横向表、拆表，或移入附录/配套文件。",
                    )
                )
        in_code = False
        code_start = 0
        code_lines: list[str] = []
        for idx, line in enumerate(text.splitlines(), 1):
            if r"\begin{printcode}" in line:
                in_code = True
                code_start = idx
                code_lines = []
                continue
            if r"\end{printcode}" in line and in_code:
                long_lines = [len(x) for x in code_lines if len(x) > 110]
                if len(code_lines) > 55 or long_lines:
                    findings.append(
                        Finding(
                            "长代码块/长代码行",
                            "P1" if len(code_lines) > 80 or any(x > 160 for x in long_lines) else "P2",
                            f"{tex.name}:{code_start}",
                            f"lines={len(code_lines)}, long_lines={len(long_lines)}, max_len={max([0, *map(len, code_lines)])}",
                            "正文保留关键片段，长脚本移入附录/仓库；必要时缩小字号或拆分代码块。",
                        )
                    )
                in_code = False
                continue
            if in_code:
                code_lines.append(line)
        for match in re.finditer(r"\\includegraphics\[([^\]]+)\]\{([^}]+)\}", text):
            options, image = match.groups()
            if "height=0.55\\textheight" in options:
                findings.append(
                    Finding(
                        "图片高度固定风险",
                        "P2",
                        f"{tex.name}:{line_no(text, match.start())}",
                        image,
                        "重点人工复核高图、宽图和图题分离；必要时改为 0.48\\textheight 或单独浮动页。",
                    )
                )
        if re.search(r"\\(?:chapter|section|subsection)\{", text):
            findings.append(
                Finding(
                    "自动章节编号残留",
                    "P0",
                    tex.name,
                    "found numbered heading command",
                    "提交版应使用无编号标题并手动写入目录，避免出现 61.21 10. 这类双重编号。",
                )
            )
    return findings


def audit_log() -> list[Finding]:
    findings: list[Finding] = []
    text = read_text(LOG)
    for match in re.finditer(r"Overfull \\hbox \(([0-9.]+)pt too wide\).*", text):
        width = float(match.group(1))
        if width <= 5:
            continue
        severity = "P1" if width > 10 else "P2"
        findings.append(
            Finding(
                "Overfull hbox",
                severity,
                "xelatex_build.log",
                match.group(0)[:220],
                "定位对应章节源文件并修正表格、代码、图片或路径；5pt 以下仅作为日志噪声处理。",
            )
        )
    for pattern, issue, severity in [
        (r"Overfull \\vbox.*", "Overfull vbox", "P1"),
        (r"Unable to load picture.*", "图片加载失败", "P0"),
        (r"LaTeX Warning: File `[^']+' not found.*", "文件缺失", "P0"),
    ]:
        for match in re.finditer(pattern, text):
            findings.append(
                Finding(
                    issue,
                    severity,
                    "xelatex_build.log",
                    match.group(0)[:220],
                    "定位对应章节源文件并修正表格、代码、图片或路径。",
                )
            )
    return findings


def pdf_pages() -> int:
    if not PDF.exists():
        return 0
    proc = subprocess.run(["pdfinfo", str(PDF)], capture_output=True, text=True, check=False)
    match = re.search(r"^Pages:\s+(\d+)", proc.stdout, re.M)
    return int(match.group(1)) if match else 0


def page_text(page: int) -> str:
    proc = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(PDF), "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    return proc.stdout


def audit_pdf_pages() -> list[Finding]:
    findings: list[Finding] = []
    pages = pdf_pages()
    if not pages:
        return [
            Finding("PDF 缺失", "P0", str(PDF), "pdfinfo failed or file missing", "先完成 PDF 编译。")
        ]
    blank_like: list[int] = []
    suspicious_heading_pages: list[int] = []
    for page in range(1, pages + 1):
        text = page_text(page)
        compact = re.sub(r"\s+", "", text)
        if len(compact) < 20 and page > 1:
            blank_like.append(page)
        if re.search(r"\b\d+\.\d+\s+\d+[.、]", text):
            suspicious_heading_pages.append(page)
    for page in blank_like[:80]:
        findings.append(
            Finding(
                "疑似异常空白页",
                "P1",
                f"PDF page {page}",
                "text_chars<20",
                "确认是否为篇章/章节故意空白；若不是，检查前一页浮动体、长表或标题分页。",
            )
        )
    for page in suspicious_heading_pages[:120]:
        findings.append(
            Finding(
                "疑似双重标题编号",
                "P0",
                f"PDF page {page}",
                "matched pattern like '61.21 10.'",
                "改用无编号标题或清理 Markdown 标题中的内嵌编号。",
            )
        )
    return findings


def write_reports(findings: list[Finding]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["问题类型", "严重程度", "位置", "证据", "建议修改"])
        writer.writeheader()
        for item in findings:
            writer.writerow(
                {
                    "问题类型": item.issue_type,
                    "严重程度": item.severity,
                    "位置": item.location,
                    "证据": item.evidence,
                    "建议修改": item.suggestion,
                }
            )
    counts: dict[tuple[str, str], int] = {}
    for item in findings:
        counts[(item.severity, item.issue_type)] = counts.get((item.severity, item.issue_type), 0) + 1
    lines = [
        "# USTC Press LaTeX 提交前版面阻断项检查",
        "",
        f"- PDF: `{PDF}`",
        f"- Findings: {len(findings)}",
        "",
        "## Summary",
        "",
        "| 严重程度 | 问题类型 | 数量 |",
        "| --- | --- | ---: |",
    ]
    for (severity, issue_type), count in sorted(counts.items()):
        lines.append(f"| {severity} | {issue_type} | {count} |")
    lines.extend(["", "## Top Findings", ""])
    for item in findings[:120]:
        lines.append(f"- **{item.severity} {item.issue_type}** `{item.location}`：{item.evidence}；建议：{item.suggestion}")
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    findings = audit_tex_sources()
    findings.extend(audit_log())
    findings.extend(audit_pdf_pages())
    severity_order = {"P0": 0, "P1": 1, "P2": 2}
    findings.sort(key=lambda x: (severity_order.get(x.severity, 9), x.issue_type, x.location))
    write_reports(findings)
    print(MD_OUT)
    print(f"findings={len(findings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
