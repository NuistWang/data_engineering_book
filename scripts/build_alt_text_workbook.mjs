import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = process.cwd();
const dataPath = path.join(root, "publishing", "accessibility", "springer_alt_text_inventory.json");
const outDir = path.join(root, "publishing", "accessibility");
const outFile = path.join(outDir, "springer_alt_text_inventory.xlsx");

const payload = JSON.parse(await fs.readFile(dataPath, "utf8"));
const rows = payload.rows || [];

const labels = {
  row_id: "ID",
  language: "Language",
  part: "Part / Section",
  unit: "Unit",
  unit_title: "Chapter / Contribution Title",
  source_markdown: "Source Markdown",
  line: "Line",
  figure_number: "Figure No.",
  caption: "Caption / Figure Title",
  image_alt_in_markdown: "Markdown Alt",
  image_file: "Image File",
  image_exists: "Image Exists",
  image_dimensions: "Dimensions",
  image_format: "Format",
  alt_text: "Alt Text for Submission",
  long_description: "Long Description / Review Note",
  decorative: "Decorative?",
  review_status: "Review Status",
  reviewer: "Reviewer",
  notes: "Validation Notes",
  zh_reference_caption: "Chinese Reference Caption",
  zh_reference_alt_text: "Chinese Reference Alt",
};

const columns = Object.keys(labels);

function columnName(n) {
  let name = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    name = String.fromCharCode(65 + rem) + name;
    n = Math.floor((n - 1) / 26);
  }
  return name;
}

function writeSheet(sheet, matrix, widths = []) {
  if (!matrix.length) return;
  const endCol = columnName(matrix[0].length);
  const used = sheet.getRange(`A1:${endCol}${matrix.length}`);
  used.values = matrix;
  used.format = {
    font: { name: "Arial", size: 10, color: "#111827" },
    borders: { preset: "all", style: "thin", color: "#D1D5DB" },
    verticalAlignment: "top",
    wrapText: true,
  };
  sheet.getRange(`A1:${endCol}1`).format = {
    fill: "#D9EAF7",
    font: { name: "Arial", size: 10, bold: true, color: "#111827" },
    borders: { preset: "all", style: "thin", color: "#9CA3AF" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
  };
  for (let i = 0; i < widths.length; i += 1) {
    if (widths[i]) {
      sheet.getRange(`${columnName(i + 1)}:${columnName(i + 1)}`).format.columnWidth = widths[i];
    }
  }
}

const byUnit = new Map();
for (const row of rows) byUnit.set(row.unit, (byUnit.get(row.unit) || 0) + 1);
const missingImages = rows.filter((row) => row.image_exists !== "yes").length;
const blankAlt = rows.filter((row) => !String(row.alt_text || "").trim()).length;
const needsHumanReview = rows.filter((row) => String(row.review_status || "").toLowerCase().includes("needs human review")).length;

const workbook = Workbook.create();
const summary = workbook.worksheets.add("Summary");
const altText = workbook.worksheets.add("Alt Text");
const guidance = workbook.worksheets.add("Guidance");

writeSheet(summary, [
  ["Metric", "Value"],
  ["Generated at UTC", payload.generated_at_utc || ""],
  ["Scope", payload.scope || "English manuscript local image references"],
  ["Total image rows", rows.length],
  ["Missing image files", missingImages],
  ["Blank alt-text rows", blankAlt],
  ["Rows flagged for targeted human review", needsHumanReview],
  ["Submission note", "Springer Nature requested an Excel file containing alt text for all figures, illustrations, and images."],
  [],
  ["Unit", "Image rows"],
  ...[...byUnit.entries()].sort(([a], [b]) => a.localeCompare(b)).map(([unit, count]) => [unit, count]),
], [32, 90]);

writeSheet(
  altText,
  [
    columns.map((key) => labels[key]),
    ...rows.map((row) => columns.map((key) => row[key] ?? "")),
  ],
  [12, 10, 28, 12, 38, 42, 8, 14, 50, 32, 54, 12, 14, 10, 72, 56, 12, 24, 18, 28, 46, 36],
);

writeSheet(guidance, [
  ["Field", "Meaning"],
  ["Alt Text for Submission", "Draft English alt text to submit after human review. Keep it concise but informative; describe the information conveyed by the image, not merely the file name."],
  ["Long Description / Review Note", "Use this when a complex workflow, chart, table image, or dense diagram may need more explanation than short alt text can carry."],
  ["Decorative?", "Most manuscript figures are informative and marked no. Change only if the image is purely decorative."],
  ["Review Status", "Draft means generated from caption/context. Change to Reviewed when the responsible editor has checked the image."],
  ["Chinese Reference Caption", "Reference only, for editors comparing with the Chinese manuscript."],
], [32, 110]);

await fs.mkdir(outDir, { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outFile);
console.log(outFile);
