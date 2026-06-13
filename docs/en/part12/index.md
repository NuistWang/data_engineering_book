# Part XII: Specialized Datasets and Multimodal Data Engineering Practice

## Positioning of This Part

Part XII serves as the method validation layer of the book. The first eleven parts establish frameworks for data lifecycle management, text pre-training, multimodal processing, alignment data, reasoning data, RAG, DataOps, data assetization, agent automation, and compliance governance. This part applies those methods to concrete data objects through a modality-explicit path: text corpora, image-text candidate pools, visual documents and tables, visual reasoning, speech and audio interaction, and reasoning traces.

The goal of this part is not to list dataset names. Its main thread is how specialized datasets and industry data-engineering datasets become reviewable assets under different modalities and data forms. Chapter 38 and Chapter 39 begin with open Web text corpora and image-text candidate pools, connecting back to text pre-training data engineering and image-text multimodal data engineering. Chapter 40 and Chapter 41 move into visual documents, tables, charts, medical images, and tool-call trajectories. Chapter 42 treats speech and audio interaction data as its own data-engineering object. Chapter 43 closes with reasoning-trace compression, connecting to reasoning data, reasoning models, RL data engineering, and project practice.

Looking backward, this part connects to Part II on text corpora, Part III on multimodal data, Part V on synthetic data, Part VI on tool-use and reasoning data, Part VIII on data operations, and Part XI on compliance governance. Looking forward, it provides engineering evidence for the open-source model data recipes in Part XIII and the project case studies in Part XIV.

## Terminology Conventions

Throughout this part, "specialized dataset" consistently refers to data assets constructed around a specific task, scenario, or evaluation protocol; "sample schema" refers to the structural convention covering fields, inputs, outputs, supervision signals, and quality labels; and "evaluation protocol" refers to metrics, splits, baselines, error attribution, and reproduction conditions. Each case study should make explicit the engineering problem the dataset addresses, rather than merely introducing its name, scale, or model task.

## Table of Contents for This Part

- [Chapter 38: Text Corpus Data Engineering: Open Web, Filtering, Deduplication, and Transparent Ledgers](ch38_text_corpora_transparent_ledger.md)
- [Chapter 39: Image-Text Data Engineering: Candidate Pool Construction, Multimodal Filtering, and DataComp Evaluation](ch39_image_text_candidate_pool_data_engineering.md)
- [Chapter 40: Visual Document and Table Data Engineering: Structured Extraction, Sparse Tables, and Schema Constraints](ch40_visual_document_table_data_engineering.md)
- [Chapter 41: Visual Reasoning Data Engineering: Chart Evidence, Medical Images, and Tool-Call Trajectories](ch41_visual_reasoning_tool_data_engineering.md)
- [Chapter 42: Speech and Audio Data Engineering: Interaction Control, Style Labels, and Safety Boundaries](ch42_speech_audio_interaction_data_engineering.md)
- [Chapter 43: Reasoning Trace Data Engineering: Long-Chain Compression, Implicit Computation, and Supervision Masks](ch43_reasoning_trace_compression_data_engineering.md)

## Reading Order

Chapter 38 combines FineWeb and Dolma, focusing on open Web text extraction, filtering and deduplication, privacy processing, source ledgers, and attributable evaluation. It is best read together with Part II on text pre-training data engineering and Part XIII on pre-training recipes.

Chapter 39 focuses on LAION-5B and DataComp, covering image-text candidate pools, multimodal filtering channels, quality evaluation, and governance boundaries. It extends the open Web source discussion from Chapter 38 and transitions toward image-text multimodal data engineering in Part III.

Chapter 40 combines StructBill-CN and SparseTable-Bench, focusing on visual documents, bill fields, table structures, and robustness to empty cells. It is best read together with Part III on OCR, multimodal images, and cross-modal alignment.

Chapter 41 combines multi-chart infographics and MedImage-ToolVQA, focusing on visual evidence, cross-chart reasoning, medical image ROI, and tool-call trajectories. It connects naturally to Part VI on agent data, Part X on Data Engineering Agents, and Part XI on privacy and compliance.

Chapter 42 treats VoiceStyleControl as a focused speech and audio interaction case, covering S2S, TTS, style labels, authorization status, and misuse-risk governance. It echoes Part III's discussion of video and audio data engineering.

Chapter 43 treats Latent-Switch-69K as a focused reasoning-trace case, covering Long-CoT compression, latent budgets, student sequences, and supervision masks. It connects forward to Part XIII on post-training, reasoning models, RL data engineering, and the R1 reasoning flywheel case in Part XIV.
