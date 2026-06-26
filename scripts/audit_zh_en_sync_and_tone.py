from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "docs" / "zh"
EN = ROOT / "docs" / "en"
OUT = ROOT / "output" / "ustc_press_submission" / "00_Audit_Reports"

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
CODE_RE = re.compile(r"^(```|~~~)")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")
EN_WORD_RE = re.compile(r"[A-Za-z]+(?:[-'][A-Za-z]+)?")

AI_TONE_PATTERNS = {
    "absolute_or_overclaim": [
        "最强",
        "最佳",
        "唯一",
        "革命性",
        "颠覆性",
        "史无前例",
        "完全解决",
        "一劳永逸",
        "极致",
        "无与伦比",
        "显著提升",
        "大幅提升",
    ],
    "chatty_or_marketing": [
        "你会发现",
        "不难发现",
        "大家都知道",
        "简单来说",
        "说白了",
        "换句话说",
        "非常重要",
        "值得注意的是",
        "毫无疑问",
        "显而易见",
        "让我们",
    ],
    "aiish_rhetoric": [
        "不是.*而是",
        "不仅.*而且",
        "真正",
        "核心价值",
        "闭环",
        "赋能",
        "落地",
        "生态",
        "抓手",
        "护城河",
    ],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def rel_files() -> list[Path]:
    zh_files = {p.relative_to(ZH) for p in ZH.rglob("*.md")}
    en_files = {p.relative_to(EN) for p in EN.rglob("*.md")}
    ignored = {Path("translation-status.md"), Path("translation-style-guide.md")}
    return sorted((zh_files | en_files) - ignored)


def headings(text: str) -> list[str]:
    out = []
    in_code = False
    for line in text.splitlines():
        if CODE_RE.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(line)
        if m:
            out.append(f"{m.group(1)} {m.group(2).strip()}")
    return out


def count_tables(text: str) -> int:
    return sum(1 for line in text.splitlines() if TABLE_SEP_RE.match(line))


def count_code(text: str) -> int:
    return sum(1 for line in text.splitlines() if CODE_RE.match(line)) // 2


def count_images(text: str) -> int:
    return len(IMAGE_RE.findall(text))


def count_refs(text: str) -> int:
    return len(re.findall(r"\n#{2,4}\s+(参考文献|References)\s*\n", text, flags=re.I))


def first_heading(text: str) -> str:
    hs = headings(text)
    return hs[0] if hs else ""


def sync_rows() -> list[dict[str, str]]:
    rows = []
    for rel in rel_files():
        zpath, epath = ZH / rel, EN / rel
        ztxt, etxt = read(zpath), read(epath)
        z_cjk = len(CJK_RE.findall(ztxt))
        e_words = len(EN_WORD_RE.findall(etxt))
        z_heads, e_heads = headings(ztxt), headings(etxt)
        z_hset = {h.split(" ", 1)[-1].strip() for h in z_heads}
        e_hset = {h.split(" ", 1)[-1].strip() for h in e_heads}
        flags = []
        if not zpath.exists():
            flags.append("missing-zh")
        if not epath.exists():
            flags.append("missing-en")
        if zpath.exists() and epath.exists():
            ratio = e_words / max(z_cjk, 1)
            if ratio < 0.32:
                flags.append("en-much-shorter")
            if ratio > 0.85:
                flags.append("en-much-longer-or-zh-short")
            if abs(len(z_heads) - len(e_heads)) >= 5:
                flags.append("heading-count-diff")
            if count_images(ztxt) != count_images(etxt):
                flags.append("image-count-diff")
            if abs(count_tables(ztxt) - count_tables(etxt)) >= 3:
                flags.append("table-count-diff")
            if abs(count_code(ztxt) - count_code(etxt)) >= 3:
                flags.append("code-block-count-diff")
        else:
            ratio = 0.0

        rows.append(
            {
                "file": rel.as_posix(),
                "zh_exists": str(zpath.exists()),
                "en_exists": str(epath.exists()),
                "zh_cjk_chars": str(z_cjk),
                "en_words": str(e_words),
                "en_words_per_zh_cjk": f"{ratio:.3f}",
                "zh_headings": str(len(z_heads)),
                "en_headings": str(len(e_heads)),
                "zh_images": str(count_images(ztxt)),
                "en_images": str(count_images(etxt)),
                "zh_tables": str(count_tables(ztxt)),
                "en_tables": str(count_tables(etxt)),
                "zh_code_blocks": str(count_code(ztxt)),
                "en_code_blocks": str(count_code(etxt)),
                "zh_first_heading": first_heading(ztxt),
                "en_first_heading": first_heading(etxt),
                "flags": "; ".join(flags),
            }
        )
    return rows


def tone_rows() -> list[dict[str, str]]:
    rows = []
    for path in sorted(ZH.rglob("*.md")):
        rel = path.relative_to(ZH).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        in_code = False
        for i, line in enumerate(lines, start=1):
            if CODE_RE.match(line):
                in_code = not in_code
                continue
            if in_code or not line.strip():
                continue
            for kind, patterns in AI_TONE_PATTERNS.items():
                for pat in patterns:
                    if re.search(pat, line):
                        rows.append(
                            {
                                "file": rel,
                                "line": str(i),
                                "issue_type": kind,
                                "pattern": pat,
                                "severity": "medium" if kind == "absolute_or_overclaim" else "low",
                                "suggestion": suggestion(kind),
                                "text": line.strip()[:500],
                            }
                        )
                        break
    return rows


def suggestion(kind: str) -> str:
    if kind == "absolute_or_overclaim":
        return "改为可验证、有限定条件的技术表述；避免绝对化或营销化判断。"
    if kind == "chatty_or_marketing":
        return "改为书面技术说明；删除对读者的口语化召唤或泛泛强调。"
    return "检查是否为 AI 式排比/套话；保留必要逻辑关系，压缩重复修辞。"


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_md(sync: list[dict[str, str]], tone: list[dict[str, str]]) -> None:
    flagged = [r for r in sync if r["flags"]]
    tone_counter = Counter(r["issue_type"] for r in tone)
    lines = [
        "# 中英文同步与中文出版语气审计报告",
        "",
        "## 一、范围",
        "",
        "- 中文目录：`docs/zh`",
        "- 英文目录：`docs/en`",
        "- 本报告用于中国科学技术大学出版社中文出版前检查。",
        "",
        "## 二、中英文同步概览",
        "",
        f"- 扫描文件：{len(sync)}",
        f"- 有同步差异标记的文件：{len(flagged)}",
        "",
        "### 重点关注文件",
        "",
        "| 文件 | 标记 | 中文字符 | 英文词数 | 标题数 zh/en | 图 zh/en | 表 zh/en | 代码 zh/en |",
        "| --- | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    for r in flagged[:120]:
        lines.append(
            f"| `{r['file']}` | {r['flags']} | {r['zh_cjk_chars']} | {r['en_words']} | {r['zh_headings']}/{r['en_headings']} | {r['zh_images']}/{r['en_images']} | {r['zh_tables']}/{r['en_tables']} | {r['zh_code_blocks']}/{r['en_code_blocks']} |"
        )
    lines += [
        "",
        "完整明细见 `zh_en_sync_audit.csv`。",
        "",
        "## 三、中文语气与 AI 痕迹审计概览",
        "",
        f"- 候选问题总数：{len(tone)}",
    ]
    for k, v in tone_counter.most_common():
        lines.append(f"- {k}: {v}")
    lines += [
        "",
        "### 高优先级处理建议",
        "",
        "1. 优先处理 `absolute_or_overclaim`：例如“最强、唯一、完全解决、革命性”等。",
        "2. 将口语提示改为技术书面语：例如“你会发现、说白了、让我们”等。",
        "3. 对“不是……而是……”“真正”“核心价值”等重复修辞做压缩，保留必要逻辑，删除套话。",
        "",
        "完整明细见 `zh_tone_ai_trace_audit.csv`。",
    ]
    (OUT / "zh_en_sync_and_tone_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    sync = sync_rows()
    tone = tone_rows()
    write_csv(OUT / "zh_en_sync_audit.csv", sync)
    write_csv(OUT / "zh_tone_ai_trace_audit.csv", tone)
    write_md(sync, tone)
    print(OUT / "zh_en_sync_and_tone_audit.md")
    print(f"sync_rows={len(sync)} flagged={sum(1 for r in sync if r['flags'])}")
    print(f"tone_rows={len(tone)}")


if __name__ == "__main__":
    main()
