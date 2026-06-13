# Springer 提交包整理规范

本文件用于把当前 Markdown 工作稿整理为 Springer 可生产、可审查、可冻结的提交包。除非出版社编辑另有模板要求，提交前按本规范建立目录、命名文件并保留校验记录。

## 一、提交包目录

建议在最终交付目录中使用以下结构：

```text
output/springer_submission/Data_Engineering_for_Large_Foundation_Models_A_Handbook/
  Metadata/
  Source_Files/
    Markdown/
    LaTeX/
  Full_PDF/
  Chapter_PDFs/
  Figures/
  Accessibility/
  Permissions/
  Declarations/
  Audit_Reports/
  Checksums/
  README.md
```

- `Metadata/`：提交包规范、最终交付清单、书名/作者/元数据准备说明。
- `Source_Files/Markdown/`：中文正文源文件和英文参考源文件。
- `Source_Files/LaTeX/`：LaTeX 主文件、分部源文件和 LaTeX 资源文件。Springer 若要求 editable source，以此目录为主。
- `Full_PDF/`：整书分页 review PDF。
- `Chapter_PDFs/`：Springer reference PDF set，包含 `00_front_matter.pdf`、逐章/项目章/附录 PDF，以及适用时的 `99_back_matter.pdf`。
- `Figures/`：英文最终稿引用的图件文件与 `figures_manifest.csv`。每张图的权属、AI 使用情况和高清源确认应与 `publishing/final_review/figure_rights_signoff.md` 一致。
- `Accessibility/`：Springer 要求随最终稿提交的 alt text Excel，当前主文件为 `springer_alt_text_inventory.xlsx`，并保留 CSV/JSON 侧车文件便于脚本校验和人工复核。
- `Permissions/`：作者/编辑提供的第三方授权证明、改绘依据、AI 图像审查记录或人工签核说明。脚本只复制已有材料，不代造法律证明。
- `Declarations/`：AI 使用声明、竞争利益声明、伦理/知情同意/敏感数据说明、数据和代码可用性声明、作者贡献与授权材料模板。
- `Audit_Reports/`：最终审计报告、人工签核、例外说明。
- `Checksums/`：最终文件清单和 SHA-256 校验和。

## 二、文件命名

- 章节源文件：`ch01_title.ext` 至 `ch51_title.ext`，项目章使用 `p01_title.ext` 至 `p15_title.ext`，附录使用 `appendix_a_title.ext` 至 `appendix_h_title.ext`。
- PDF reference set：`00_front_matter.pdf`、`01-...pdf` 至逐章/逐项目/逐附录 PDF、`99_back_matter.pdf`。
- 图件文件：`fig_ch01_01_short-title.ext`，表格文件：`tab_ch01_01_short-title.ext`。
- 声明文件：`declaration_ai_use.ext`、`declaration_competing_interests.ext`、`declaration_ethics_consent_data.ext`、`declaration_data_code_availability.ext`。
- 元数据文件：`book_metadata.ext`、`author_metadata.ext`、`license_to_publish_preparation.ext`。

文件名只使用小写英文字母、数字、连字符和下划线，避免空格、中文标点和临时版本后缀。历史版本进入归档目录，不进入最终提交包。

## 三、冻结规则

- 提交包冻结前，必须通过 `uv run python -m unittest ...`、`uv run mkdocs build --strict --clean`、`uv run python scripts/reference_integrity_audit.py --skip-external`、`uv run python scripts/final_publication_audit.py --report-dir publishing/final_review --fail-on-blocker`。
- 冻结后只接受出版社编辑或主编确认的更改。任何更改必须重新运行导出脚本并更新 `Checksums/manifest.json` 与 `Checksums/manifest.csv`。
- 正文、图件、图表台账、参考文献审计报告、声明文件之间必须保持同一版本号。
- 任何无法确认权属、引用真实性、伦理边界或作者授权的信息，不得用默认结论代填，必须保留人工签核状态。

## 四、提交前校验

- [ ] 章节源文件数量与目录一致。
- [ ] `Chapter_PDFs/` 包含 front matter PDF、逐章/项目章/附录 PDF，以及 back matter PDF。
- [ ] 每章源文件均含参考文献、图注和表格。
- [ ] 所有图件在 `02_figures/` 中存在对应文件，并能在 PDF/HTML 中正确渲染。
- [ ] `Accessibility/springer_alt_text_inventory.xlsx` 覆盖英文最终稿全部图片，且每条都有英文 alt text。
- [ ] 第三方材料权限和 AI 图像审查记录齐备。
- [ ] 作者、ORCID、单位、通讯作者、署名顺序和 License to Publish 准备材料已冻结。
- [ ] 伦理、知情同意、隐私、敏感数据、数据可用性和代码可用性声明已由负责人确认。
- [ ] 最终 PDF 样稿与生产源文件一致。
- [ ] 文件清单、校验和、冻结日期和责任人齐备。
