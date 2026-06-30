#!/usr/bin/env python3
"""Add missing numbered table captions to Chinese and English source files."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "docs" / "zh"
EN = ROOT / "docs" / "en"
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
ZH_CAP_RE = re.compile(r"^\*表\s*(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+\s*[:：]")
EN_CAP_RE = re.compile(r"^\*Table\s*(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*\d+\s*[:：]", re.I)


def expected_prefix(path: Path, first_heading: str) -> str | None:
    m = re.match(r"ch(\d+)_", path.name)
    if m:
        return str(int(m.group(1)))
    m = re.match(r"p(\d+)_", path.name)
    if m:
        return f"P{int(m.group(1)):02d}"
    m = re.search(r"附录\s*([A-Z])", first_heading)
    if m:
        return m.group(1)
    return None


def first_h1(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def table_indices(lines: list[str]) -> list[int]:
    out = []
    for i, line in enumerate(lines):
        if i + 1 < len(lines) and "|" in line and TABLE_SEP_RE.match(lines[i + 1]):
            out.append(i)
    return out


def has_caption(lines: list[str], idx: int, lang: str) -> bool:
    cap_re = ZH_CAP_RE if lang == "zh" else EN_CAP_RE
    return any(cap_re.match(lines[j].strip()) for j in range(max(0, idx - 4), idx))


def clean_title(value: str) -> str:
    value = re.sub(r"^[：:，,。\s]+", "", value.strip())
    value = re.sub(r"[。；;：:，,]\s*$", "", value)
    value = re.sub(r"^(汇总|列出|给出|展示|说明|对比|总结|记录|定义|对应|如下|如表所示)\s*", "", value)
    return value.strip()


def zh_title(lines: list[str], idx: int, label: str, header: str) -> str:
    previous = " ".join(line.strip() for line in lines[max(0, idx - 4):idx] if line.strip())
    m = re.search(rf"表\s*{re.escape(label)}\s*(?:将|给出|汇总|列出|展示|说明|对应|总结)?([^。；;\n]*)", previous)
    if m:
        title = clean_title(m.group(1))
        if title:
            return title
    if "验收" in previous or "验收" in header:
        return "项目验收与复核口径"
    if "风险" in previous or "风险" in header:
        return "风险、控制措施与复核口径"
    if "字段" in header:
        return "字段说明与复核口径"
    if "指标" in header:
        return "指标、计算方式与解释"
    if "阶段" in header:
        return "阶段、产物与复核字段"
    if "角色" in header:
        return "角色职责与协作边界"
    return "关键要点与工程复核口径"


def en_title(lines: list[str], idx: int, label: str, header: str) -> str:
    previous = " ".join(line.strip() for line in lines[max(0, idx - 4):idx] if line.strip())
    m = re.search(rf"Table\s*{re.escape(label)}\s*(?:summarizes|lists|shows|gives|maps|records)?([^.;:\n]*)", previous, re.I)
    if m:
        title = clean_title(m.group(1))
        if title:
            return title[0].upper() + title[1:]
    if "acceptance" in previous.lower() or "acceptance" in header.lower():
        return "Project Acceptance and Review Criteria"
    if "risk" in previous.lower() or "risk" in header.lower():
        return "Risks, Controls, and Review Criteria"
    if "field" in header.lower():
        return "Fields and Review Criteria"
    if "metric" in header.lower() or "indicator" in header.lower():
        return "Metrics, Calculation Methods, and Interpretation"
    if "stage" in header.lower():
        return "Stages, Artifacts, and Review Fields"
    if "role" in header.lower():
        return "Role Responsibilities and Collaboration Boundaries"
    return "Key Points and Engineering Review Criteria"


def fix_file(path: Path, lang: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    prefix = expected_prefix(path, first_h1(text))
    if prefix is None:
        return False
    lines = text.splitlines()
    indices = table_indices(lines)
    next_num = 1
    changed = False
    # Existing captions consume numbers; unlabeled tables receive the next
    # number in physical order.
    existing_nums: set[int] = set()
    for line in lines:
        m = re.match(r"^\*(?:表|Table)\s*(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*(\d+)\s*[:：]", line.strip(), re.I)
        if m:
            existing_nums.add(int(m.group(1)))
    out = lines[:]
    offset = 0
    for idx in indices:
        real_idx = idx + offset
        if has_caption(out, real_idx, lang):
            cap_text = "\n".join(out[max(0, real_idx - 4):real_idx])
            m = re.search(r"(?:表|Table)\s*(?:P\d{1,2}|[A-Z]|\d+)\s*[-—]\s*(\d+)", cap_text, re.I)
            if m:
                next_num = max(next_num, int(m.group(1)) + 1)
            continue
        while next_num in existing_nums:
            next_num += 1
        label = f"{prefix}-{next_num}"
        header = out[real_idx]
        if lang == "zh":
            intro = f"表{label}列出了相关字段与出版复核口径。"
            cap = f"*表{label}：{zh_title(out, real_idx, label, header)}。*"
        else:
            intro = f"Table {label} summarizes the corresponding fields and publication review criteria."
            cap = f"*Table {label}: {en_title(out, real_idx, label, header)}.*"
        out[real_idx:real_idx] = [intro, "", cap, ""]
        offset += 4
        existing_nums.add(next_num)
        next_num += 1
        changed = True
    if changed:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    changed = []
    for zpath in sorted(ZH.rglob("*.md")):
        rel = zpath.relative_to(ZH)
        if fix_file(zpath, "zh"):
            changed.append(("zh", rel.as_posix()))
        epath = EN / rel
        if fix_file(epath, "en"):
            changed.append(("en", rel.as_posix()))
    for lang, rel in changed:
        print(f"{lang}: {rel}")
    print(f"changed={len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
