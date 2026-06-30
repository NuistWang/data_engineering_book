#!/usr/bin/env python3
"""Audit Chinese manuscript publication integrity.

This complements the broader publication linters with checks that are specific
to final Chinese copy editing: captions, in-text mentions, numbering order,
navigation-title consistency, and fenced-code language tags.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "docs" / "zh"
MKDOCS = ROOT / "mkdocs.yml"
OUT = ROOT / "output" / "ustc_press_submission" / "00_Audit_Reports"


CAPTION_RE = re.compile(
    r"^\*\s*(?P<kind>图|表|代码清单)\s*(?P<label>(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+)\s*[:：]",
)
IMAGE_RE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)")
CODE_FENCE_RE = re.compile(r"^\s*```(?P<lang>[A-Za-z0-9_+.-]*)\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$")

TONE_PATTERNS = {
    "chatty_or_marketing": [
        r"你会发现",
        r"不难发现",
        r"大家都知道",
        r"简单来说",
        r"说白了",
        r"换句话说",
        r"非常重要",
        r"毫无疑问",
        r"显而易见",
        r"让我们",
    ],
    "absolute_or_overclaim": [
        r"最强",
        r"最佳",
        r"唯一可靠",
        r"唯一正确",
        r"唯一标准",
        r"革命性",
        r"颠覆性",
        r"史无前例",
        r"完全解决",
        r"一劳永逸",
        r"极致",
        r"无与伦比",
    ],
}


@dataclass
class Issue:
    file: str
    line: int
    severity: str
    kind: str
    detail: str
    suggestion: str = ""


def normalize_label(label: str) -> str:
    return re.sub(r"\s+", "", label.replace("—", "-")).upper()


def source_files() -> list[Path]:
    ignored = {
        "translation-status.md",
        "translation-style-guide.md",
    }
    return [
        p
        for p in sorted(ZH.rglob("*.md"))
        if p.name not in ignored and "superpowers" not in p.parts
    ]


def strip_code_blocks(text: str) -> str:
    out: list[str] = []
    in_code = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            out.append("")
        elif in_code:
            out.append("")
        else:
            out.append(line)
    return "\n".join(out)


def expected_prefix(path: Path, first_heading: str) -> str | None:
    name = path.name
    m = re.match(r"ch(\d+)_", name)
    if m:
        return str(int(m.group(1)))
    m = re.match(r"p(\d+)_", name)
    if m:
        return f"P{int(m.group(1)):02d}"
    m = re.search(r"附录\s*([A-Z])", first_heading)
    if m:
        return m.group(1)
    return None


def infer_code_lang(body: str) -> str | None:
    sample = body.strip()
    if not sample:
        return None
    if re.search(r"^\s*(from\s+\w+|import\s+\w+|def\s+\w+\(|class\s+\w+\(|async\s+def\s+|with\s+[\w.]+\()", sample, re.M):
        return "python"
    if sample.startswith("{") or sample.startswith("["):
        return "json"
    if re.search(r"^\s*export\s+[A-Z_][A-Z0-9_]*=", sample, re.M):
        return "bash"
    if re.search(r"^\s*(const|let|var|function|import .* from |export\s+|async function)\b", sample, re.M):
        return "javascript"
    if re.search(r"^\s*(SELECT|WITH|CREATE|INSERT|UPDATE|DELETE)\b", sample, re.I | re.M):
        return "sql"
    if re.search(r"^\s*(curl|uv |python |pip |git |docker |mkdir |cp |rm |export |cd )", sample, re.M):
        return "bash"
    if re.search(r"^\s*[\w.-]+:\s+.+$", sample, re.M) and not re.search(r";\s*$", sample, re.M):
        return "yaml"
    return None


def compatible_lang(actual: str, inferred: str | None) -> bool:
    if not actual or actual in {"text", "txt"} or inferred is None:
        return True
    aliases = {
        "py": "python",
        "js": "javascript",
        "shell": "bash",
        "sh": "bash",
        "zsh": "bash",
        "yml": "yaml",
        "md": "markdown",
    }
    actual_norm = aliases.get(actual.lower(), actual.lower())
    if actual_norm == "jsonl" and inferred == "json":
        return True
    if actual_norm == "yaml" and inferred in {"python", "sql"}:
        # YAML snippets often contain GitHub Actions keys (`on`, `jobs`) or
        # schema examples with enum-like values that resemble Python/SQL to
        # simple regex heuristics.
        return True
    if actual_norm == "python" and inferred == "yaml":
        return True
    return actual_norm == inferred


def nav_titles() -> dict[str, str]:
    config = yaml.safe_load(MKDOCS.read_text(encoding="utf-8"))
    i18n = next(p["i18n"] for p in config["plugins"] if isinstance(p, dict) and "i18n" in p)
    zh_nav = next(lang["nav"] for lang in i18n["languages"] if lang["locale"] == "zh")

    def walk(items: list) -> list[tuple[str, str]]:
        out: list[tuple[str, str]] = []
        for item in items:
            if isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        out.append((value, title))
                    elif isinstance(value, list):
                        out.extend(walk(value))
        return out

    return dict(walk(zh_nav))


def norm_title(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    text = re.sub(r"[：:]+", ":", text)
    return text


def audit_file(path: Path) -> list[Issue]:
    rel = path.relative_to(ZH).as_posix()
    text = path.read_text(encoding="utf-8")
    no_code = strip_code_blocks(text)
    lines = text.splitlines()
    issues: list[Issue] = []

    first_h1 = ""
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            first_h1 = m.group(1).strip()
            break
    prefix = expected_prefix(path, first_h1)
    requires_numbered_tables = prefix is not None

    captions: list[tuple[str, str, int]] = []
    code_blocks: list[tuple[int, int, str, str]] = []
    images: list[tuple[int, str]] = []
    tables: list[int] = []
    in_code = False
    code_start = 0
    code_lang = ""
    code_body: list[str] = []

    for i, line in enumerate(lines, start=1):
        m = CODE_FENCE_RE.match(line)
        if m:
            if not in_code:
                in_code = True
                code_start = i
                code_lang = m.group("lang").strip()
                code_body = []
            else:
                code_blocks.append((code_start, i, code_lang, "\n".join(code_body)))
                in_code = False
            continue
        if in_code:
            code_body.append(line)
            continue

        cm = CAPTION_RE.match(line.strip())
        if cm:
            captions.append((cm.group("kind"), normalize_label(cm.group("label")), i))
        im = IMAGE_RE.match(line.strip())
        if im:
            images.append((i, im.group("alt")))
        if i < len(lines) and "|" in line and TABLE_SEP_RE.match(lines[i]):
            tables.append(i)

    by_caption = defaultdict(list)
    for kind, label, line in captions:
        by_caption[(kind, label)].append(line)
        if prefix and not label.startswith(prefix.upper() + "-"):
            # Appendix table/figure prefixes may be A-1. Project prefixes are Pxx-.
            issues.append(
                Issue(rel, line, "P1", "caption-prefix", f"{kind}{label} 与文件/标题前缀 {prefix} 不一致")
            )
    for (kind, label), hit_lines in by_caption.items():
        if len(hit_lines) > 1:
            issues.append(Issue(rel, hit_lines[0], "P1", "duplicate-caption", f"{kind}{label} 出现重复题注: {hit_lines}"))

    seq_by_kind = defaultdict(list)
    for kind, label, line in captions:
        if prefix and label.startswith(prefix.upper() + "-"):
            seq_by_kind[kind].append((int(label.split("-")[-1]), line, label))
    for kind, seqs in seq_by_kind.items():
        nums = [n for n, _, _ in seqs]
        if nums != sorted(nums):
            issues.append(Issue(rel, seqs[0][1], "P1", "number-order", f"{kind}编号非递增: {nums}"))
        expected = list(range(1, max(nums) + 1)) if nums else []
        if nums and nums != expected:
            issues.append(Issue(rel, seqs[0][1], "P2", "number-gap", f"{kind}编号存在缺口或重复: 实际 {nums}，期望 {expected}"))

    caption_labels = {(kind, label): line for kind, label, line in captions}
    for line, alt in images:
        alt_m = re.search(r"图\s*((?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+)", alt)
        caption_window = "\n".join(lines[line : min(len(lines), line + 5)])
        cap_m = re.search(r"\*\s*图\s*((?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+)\s*[:：]", caption_window)
        if alt_m:
            label = normalize_label(alt_m.group(1))
        elif cap_m:
            label = normalize_label(cap_m.group(1))
        else:
            issues.append(Issue(rel, line, "P2", "image-no-label", "图片 alt 或邻近图题未包含图号"))
            continue
        if ("图", label) not in caption_labels:
            issues.append(Issue(rel, line, "P1", "image-no-caption", f"图{label} 缺少独立斜体图题"))

    for table_line in tables:
        if not requires_numbered_tables:
            continue
        window = "\n".join(lines[max(0, table_line - 4) : table_line])
        if not re.search(r"\*\s*表\s*(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+\s*[:：]", window):
            issues.append(Issue(rel, table_line, "P1", "table-no-caption", "Markdown 表格前缺少独立斜体表题"))

    for start, end, lang, body in code_blocks:
        window = "\n".join(lines[max(0, start - 5) : min(len(lines), end + 6)])
        if not re.search(r"代码清单\s*(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+", window):
            issues.append(Issue(rel, start, "P1", "code-no-listing", "代码块附近缺少代码清单编号/题注"))
        inferred = infer_code_lang(body)
        if not compatible_lang(lang, inferred):
            issues.append(
                Issue(rel, start, "P2", "code-lang-mismatch", f"代码块标记为 `{lang}`，内容更像 `{inferred}`")
            )

    for kind, label, line in captions:
        mention_re = re.compile(re.escape(kind) + r"\s*" + re.escape(label).replace("\\-", r"\s*[-—]\s*"))
        mentions = [
            i
            for i, l in enumerate(no_code.splitlines(), start=1)
            if mention_re.search(l) and not CAPTION_RE.match(l.strip())
        ]
        if not mentions:
            issues.append(Issue(rel, line, "P2", "caption-not-mentioned", f"{kind}{label} 未在正文中提及"))

    for kind, patterns in TONE_PATTERNS.items():
        for i, line in enumerate(no_code.splitlines(), start=1):
            if not line.strip():
                continue
            for pat in patterns:
                if re.search(pat, line):
                    issues.append(Issue(rel, i, "P2", f"tone-{kind}", f"疑似 AI/营销化表达: {pat}", "改为克制、可验证的技术书面语"))
                    break

    return issues


def audit_nav() -> list[Issue]:
    nav = nav_titles()
    issues: list[Issue] = []
    for rel, title in nav.items():
        path = ZH / rel
        if not path.exists() or not rel.endswith(".md"):
            continue
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if not m:
            issues.append(Issue(rel, 1, "P1", "missing-h1", "目录文件缺少 H1 标题"))
            continue
        # 篇首页、卷前页可能有展示性标题，正文章/项目章/附录必须一致。
        if re.search(r"(^|/)ch\d+_|(^|/)p\d+_|appendix_", rel):
            if norm_title(title) != norm_title(m.group(1)):
                issues.append(Issue(rel, 1, "P1", "nav-title-mismatch", f"目录标题 `{title}` 与正文 H1 `{m.group(1)}` 不一致"))
    return issues


def write_outputs(issues: list[Issue]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    csv_path = OUT / "zh_publication_integrity_audit.csv"
    md_path = OUT / "zh_publication_integrity_audit.md"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(issues[0]).keys()) if issues else ["file", "line", "severity", "kind", "detail", "suggestion"])
        writer.writeheader()
        for issue in issues:
            writer.writerow(asdict(issue))

    counter = Counter((i.severity, i.kind) for i in issues)
    lines = [
        "# 中文出版完整性专项审计",
        "",
        f"- 扫描文件：{len(source_files())}",
        f"- 问题总数：{len(issues)}",
        "",
        "## 分类汇总",
        "",
        "| 严重程度 | 类型 | 数量 |",
        "| --- | --- | ---: |",
    ]
    for (severity, kind), count in sorted(counter.items()):
        lines.append(f"| {severity} | {kind} | {count} |")
    lines += ["", "## 前 200 条问题", "", "| 文件 | 行 | 严重程度 | 类型 | 说明 |", "| --- | ---: | --- | --- | --- |"]
    for issue in issues[:200]:
        lines.append(f"| `{issue.file}` | {issue.line} | {issue.severity} | {issue.kind} | {issue.detail} |")
    lines.append("")
    lines.append(f"完整 CSV：`{csv_path.name}`。")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(md_path)
    print(f"issues={len(issues)}")


def main() -> int:
    issues: list[Issue] = []
    issues.extend(audit_nav())
    for path in source_files():
        issues.extend(audit_file(path))
    write_outputs(issues)
    return 1 if any(i.severity == "P1" for i in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
