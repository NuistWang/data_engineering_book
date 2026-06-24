# Appendix G: DataGallery Open-source Ecosystem and Reproduction Notes

## G.1 Purpose of This Appendix

This appendix explains where DataGallery sits in Project 15 and in the agentic data engineering practices discussed in this book. The public open-source entry for DataGallery is hosted on GitCode at [https://gitcode.com/datagallery](https://gitcode.com/datagallery). This appendix is not an installation manual for DataGallery or DataAgent, nor does it replace the README, example configurations, dependency notes, or release records in the corresponding repositories. When reproducing an experiment or integrating the project into an engineering system, readers should treat the public repository, a specific tag or commit, and the project documentation as the source of truth.

In this book, DataGallery is best understood as a set of open-source engineering entry points around Data + AI practice, rather than as the name of one isolated tool. Project 15 uses DataAgent to build an enterprise semantic BI assistant. Its core question is not "how to call a model to generate SQL," but how to organize business questions, the semantic layer, an NL2SQL sub-agent, tool calls, workspace assets, runtime traces, and service interfaces into a reviewable data engineering system. DataGallery provides the public organization and project entry, while DataAgent is the engineering project most directly referenced in this book.

This appendix therefore focuses on the relationship between DataGallery and the book's data engineering methods: how the chapters on agents, tool use, semantic layers, DataOps, reproduction, and governance can be connected to runnable, auditable, and iterative open-source projects. For concrete APIs, startup commands, configuration fields, and dependency versions, this appendix gives usage principles rather than a step-by-step tutorial.

## G.2 Relationship to Project 15

Project 15 uses DataAgent as the practical object for an enterprise semantic BI assistant because it places agent orchestration, semantic-layer enhancement, NL2SQL, tool use, workspace assets, and service interfaces in one engineering chain. DataGallery provides the higher-level open-source organization entry, so DataAgent can be understood not as an isolated repository, but as part of an ecosystem for data agents, data applications, and reproducible data engineering.

This boundary should remain explicit. DataAgent is the concrete project: reproduction requires checking its YAML configuration, Semantic Service, NL2SQL sub-agent, execution tools, workspace, and A2A interface. DataGallery is the ecosystem entry: readers can use it to confirm project ownership, public repositories, license status, maintenance state, related projects, and future migration clues. For a book chapter, the main text should explain the project chain; an appendix is the right place to explain the open-source ecosystem and reproduction boundary.

As a reading path, Project 15 and this appendix should be read together. Project 15 answers "how can DataAgent be used to build an enterprise semantic BI assistant?" This appendix answers "how is that project positioned, reproduced, and governed inside the DataGallery open-source ecosystem?" Together they connect the case to the ecosystem.

## G.3 DataGallery's Role in Data Engineering

From a data engineering perspective, DataGallery's value is not to hide a complex system behind a black box. Its value is to give reproducible projects a public organizational boundary. A mature data engineering case usually needs to answer seven questions: where to obtain the project, whether the code is open source, what license applies, whether example data and configuration are reproducible, whether outputs are persisted, whether failure samples and logs can be reviewed, and how later version changes are tracked. As a public entry, DataGallery helps readers check these questions in one place.

This also means that the key assets of an open-source data-agent project are not only model-calling code. For a system such as DataAgent, the long-lived assets include semantic-layer schemas, tool configurations, database connections, execution permissions, workspace directories, runtime traces, test cases, evaluation scripts, and pre-launch gates. Only when these assets are organized can an agent move from demo capability to engineering capability.

In team collaboration, DataGallery can also serve as a cross-role communication entry. Algorithm engineers care about models, prompts, and tool choices. Data engineers care about schemas, samples, sources, quality gates, and result assets. Platform engineers care about environments, permissions, service interfaces, and runtime audit. Business users care about metric definitions, query boundaries, and result interpretation. An open repository and organization entry let these roles collaborate around the same versions, documents, and issue records instead of scattered temporary notes.

## G.4 Technical Map of the DataGallery Ecosystem

From the public organization page and project documentation, DataGallery can be read as a Data + AI open-source practice that organizes data engineering through an agentic paradigm. In engineering terms, it can be read as a layered system rather than a single executable package. Its technical map contains four pillars.

The first pillar is **DataAgent**, which is the currently open-source execution engine. It carries NL2SQL, data analysis, feature engineering, tool calling, workspace asset persistence, and service exposure. This is the part most directly used by Project 15.

The second pillar is a **unified semantic layer**, including ontology modeling and enriched metadata. Its role is to make tables, columns, metrics, business concepts, and relationships machine-understandable before an agent generates SQL or calls tools. In DataAgent's current public materials, this direction appears through Semantic Service, MetaVisor-style metadata enhancement, vector retrieval, schema recall, and metric matching.

The third pillar is **agent and semantic self-evolution**. The basic idea is that execution traces, failure cases, schema-matching errors, query corrections, and business feedback should not remain transient logs. They should flow back into semantic assets, prompts, tools, evaluation cases, and data-governance rules. This is the bridge from a runnable agent to a continuously improving data system.

The fourth pillar is an **evaluation framework** for data-intelligence tasks. For enterprise BI and data-agent scenarios, evaluation should not only measure final-answer fluency. It should measure schema hit rate, execution accuracy, validation pass rate, reflection success rate, artifact persistence, trace completeness, permission interception, latency, and regression stability.

These four pillars correspond closely to the structure of this book. The semantic layer connects to the chapters on metadata, data catalogs, RAG, and data products. DataAgent connects to the chapters on tool use, multi-turn interaction, agent architecture, and project delivery. Self-evolution connects to DataOps and feedback loops. Evaluation connects to data quality, benchmark construction, acceptance gates, and reproducibility.

## G.5 DataAgent as the Current Primary Open-source Entry

DataAgent is currently a suitable open-source project for reproducing DataGallery's engineering ideas. The public project documentation presents it as an enterprise Data + AI agent platform with Python 3.11+, Apache License 2.0, LangGraph integration, openJiuwen integration, GaussVector-oriented semantic retrieval support, and a versioned open-source package entry.

From the repository structure and documentation, DataAgent can be understood through five engineering layers.

The first layer is the **interface layer**. DataAgent provides a CLI, a Python SDK, REST service components, and A2A server mode. This allows the same capability to be used in local experiments, tests, internal applications, or multi-agent platforms.

The second layer is the **configuration and runtime layer**. The "YAML as Agent" design lets teams declare models, tools, memory, workflow, workspace paths, environment-variable references, and scenario prompts in configuration files. This is important for book reproduction because a configuration file is easier to review, diff, pin, and share than a hidden notebook state.

The third layer is the **agent orchestration layer**. The project contains flexible agent runtime components, planning and execution nodes, hooks, context management, history persistence, trajectory tools, and workspace organization. For readers, these components explain why an enterprise data assistant is not just an LLM prompt. It is a runtime that must decide, call, observe, revise, and preserve evidence.

The fourth layer is the **data-action layer**. The repository exposes local tools, MCP tools, A2A tools, semantic tools, SQL readers, sandbox tools, document recall, and NL2SQL-specific nodes such as perceptor, generator, validator, reflector, executor, and selector. These modules are the practical bridge between natural-language intent and controlled data operations.

The fifth layer is the **scenario and documentation layer**. Example configurations cover quickstart, NL2SQL sub-agent execution, data analysis, e-commerce, manufacturing, finance-like scenarios, and ontology-oriented cases. The documentation covers installation, quick start, database setup, Semantic Service, architecture, APIs, application cases, and milestones. This makes DataAgent useful not only as code, but also as a teachable and auditable project artifact.

For this book, the safest wording is to treat DataAgent as an actively evolving open-source implementation of DataGallery's first pillar, not as a fixed specification for the entire DataGallery roadmap. The public repository is the source of truth for install commands, exact module names, dependency versions, and currently supported databases or services.

## G.6 Reproduction Principles for DataGallery Projects

When reproducing a project under DataGallery, first pin the version and then run examples. Minimal reproduction material should include the repository URL, commit or tag, dependency installation method, environment variables, example configuration, example data or mock data, run command, output directory, and expected artifacts. For Project 15, this information should cover the DataAgent main-agent configuration, database connection, Semantic Service, NL2SQL sub-agent, workspace path, and result files.

Second, distinguish "can start" from "can be reviewed." A DataAgent example that starts successfully only shows that dependencies and entry points are temporarily usable. Engineering reproduction also requires persisted SQL, saved CSV files, inspectable runtime traces, evidence for schema retrieval, error logs, and fixed evaluation samples. A published project case should preserve this evidence chain first.

Third, distinguish public examples from enterprise deployment. DataGallery's public projects are suitable for learning, teaching, prototyping, and engineering migration. Enterprise deployment still requires permission systems, sensitive-field governance, SQL allowlists, query quotas, audit integration, secret management, and rollback mechanisms. The public repository is an engineering starting point, not a production-ready deployment by itself.

Fourth, keep migration records. Open-source projects evolve over time, and configuration fields, dependency versions, service interfaces, and example paths may change. When reproducing experiments, readers should record the repository URL, commit, key dependency versions, and local modifications in the report. If a chapter example differs from the latest repository, the repository documentation should be treated as authoritative and the difference should be written into the reproduction notes.

## G.7 Connections to Other Chapters

DataGallery naturally connects to several parts of this book. Part 6 discusses reasoning and agent data engineering, which provides the conceptual basis for DataAgent's tool calls, memory, traces, and multi-turn interaction. Part 7 discusses RAG and application-level data engineering, which provides method background for semantic retrieval, context construction, and application loops. Part 8 discusses DataOps, which provides the governance framework for versions, observability, experiment tracking, and team collaboration. Part 9 discusses data assets and data products, allowing DataAgent's SQL, CSV, reports, and runtime records to be understood as manageable assets. Project 15 in Part 14 then brings these threads together in an enterprise semantic BI scenario.

This appendix is therefore not a tool introduction detached from Project 15. It adds open-source ecosystem context to that project. Readers who only want to run the case should start with Project 15. Readers who need to migrate the case into team projects, course labs, open-source reproduction, or internal enterprise validation should continue with this appendix to confirm version, permission, asset, evaluation, and maintenance boundaries.

## G.8 Common Misuses and Boundaries

The first misuse is treating DataAgent as an "automatic SQL generator." Project 15 already emphasizes that enterprise BI should not rely on direct schema guessing. It should build an auditable chain through the semantic layer, sub-agents, validation, execution, and artifact persistence. DataGallery provides the open-source entry, but it does not change this engineering principle.

The second misuse is treating example data in an open-source repository as equivalent to real enterprise data. Example data explains a chain; real data carries permissions, sensitive fields, business definitions, deletion requests, audit responsibilities, and cost controls. Data boundaries must be reassessed when moving into enterprise scenarios.

The third misuse is ignoring version changes. Agent frameworks, semantic services, vector databases, database drivers, and model services can all change. Without version records, later results become difficult to explain. DataGallery projects should be used with a pinned commit or release version whenever possible.

The fourth misuse is keeping only the natural-language answer and discarding intermediate assets. For projects such as DataAgent, SQL, CSV files, logs, tool-call parameters, schema-retrieval results, and failure samples are equally important. Together they determine whether a project can be reviewed, regressed, and iterated.

## G.9 Reading and Usage Suggestions

DataGallery-related projects can be used in four steps.

First, confirm the open-source entry and project boundary. Use [https://gitcode.com/datagallery](https://gitcode.com/datagallery) to inspect the organization and project entries, and use the concrete project repository to confirm the README, license, dependencies, and maintenance status.

Second, establish a minimal reproduction chain. For the DataAgent semantic BI case, first pin the configuration, database, semantic-layer index, and workspace output, then confirm that one query can produce reviewable SQL, CSV, and runtime traces.

Third, turn the reproduction chain into an engineering checklist. Record the version, environment, data source, permission status, evaluation samples, failure cases, and pre-launch gates so the example does not remain a one-off run.

Fourth, continuously synchronize with repository changes. After an open-source project changes, compare configuration fields, service interfaces, dependency versions, and example paths, then update the companion reproduction notes or teaching materials.

## Open-source Entries

- DataGallery organization entry: [https://gitcode.com/datagallery](https://gitcode.com/datagallery).

- DataAgent project repository: [https://gitcode.com/datagallery/dataagent](https://gitcode.com/datagallery/dataagent).
