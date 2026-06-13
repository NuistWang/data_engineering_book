# 图表与 Alt Text 出版台账

本文件为当前 Springer 交付版图表控制台，口径以中文主线 `48 章 + 15 个项目 + 3 个附录` 为准。`docs/superpowers/`、`outputs/`、PPT 产物和历史任务书不纳入本台账。

## 一、编号与交付规则

- 正文章采用 `图 章节号-序号`、`表 章节号-序号`。项目章在台账中采用 `Pxx-序号` 追踪，正文终稿可按出版社样式统一排版。
- 每张图必须登记标题、文件路径、来源、权限状态、alt text 和高清源文件需求。
- AI 生成或 AI 辅助图片在终稿阶段必须进入 AI 使用声明；无法确认可出版性的外部图默认改绘。
- 仅靠颜色区分的图形，终稿需增加标签、线型、纹理或形状区分。

## 二、覆盖概览

- 当前扫描：48 个正文章、15 个项目、3 个附录。
- 图片条目：275；表格编号/表题条目：200。
- Part 10、Part 12、Part 14 标记为高优先级，终稿前优先复核高清源、alt text 和图源权限。

| 单元 | 标题 | 图片数 | 表格条目数 | 优先级 |
| --- | --- | ---: | ---: | --- |
| Ch01 | 第1章 大模型时代的数据变革 | 2 | 6 | 常规 |
| Ch02 | 第2章：LLM数据生命周期与质量评估框架 | 3 | 1 | 常规 |
| Ch03 | 第3章 AI原生数据栈与成本治理 | 2 | 3 | 常规 |
| Ch04 | 第4章 数据源、采集与版权 | 2 | 2 | 常规 |
| Ch05 | 第5章 清洗、去重与去污染 | 2 | 2 | 常规 |
| Ch06 | 第6章 分词、序列化与高效加载 | 2 | 2 | 常规 |
| Ch07 | 第7章 数据评估、质量闭环与运营迭代 | 2 | 2 | 常规 |
| Ch08 | 第8章 图文对数据工程 | 3 | 2 | 常规 |
| Ch09 | 第9章 重标注与文档理解 | 2 | 2 | 常规 |
| Ch10 | 第10章 视频与音频数据工程 | 4 | 2 | 常规 |
| Ch11 | 第11章 跨模态对齐与融合 | 2 | 3 | 常规 |
| Ch12 | 第12章 SFT数据设计与指令体系 | 2 | 2 | 常规 |
| Ch13 | 第13章 偏好数据与奖励信号 | 2 | 2 | 常规 |
| Ch14 | 第14章 标注平台、QA体系与数据运营 | 2 | 2 | 常规 |
| Ch15 | 第15章 合成数据工厂：从种子到验证 | 2 | 0 | 常规 |
| Ch16 | 第16章 知识蒸馏与模型协作 | 2 | 0 | 常规 |
| Ch17 | 第17章 合成数据质量控制与模型坍缩 | 2 | 0 | 常规 |
| Ch18 | 第18章 思维链与推理数据工程 | 2 | 0 | 常规 |
| Ch19 | 第19章 Tool-Use 与函数调用数据 | 2 | 0 | 常规 |
| Ch20 | 第20章 Agent记忆与多轮交互数据 | 2 | 0 | 常规 |
| Ch21 | 第21章：RAG 数据流水线 | 9 | 8 | 常规 |
| Ch22 | 第22章：多模态 RAG 与视觉检索 | 5 | 8 | 常规 |
| Ch23 | 第23章：在线反馈闭环与知识更新 | 4 | 12 | 常规 |
| Ch24 | 第24章：DataOps 飞轮与团队组织 | 3 | 30 | 常规 |
| Ch25 | 第25章：数据版本管理与实验追踪 | 2 | 8 | 常规 |
| Ch26 | 第26章：数据平台可观测性 | 2 | 8 | 常规 |
| Ch27 | 第27章：数据资产目录与元数据治理 | 4 | 5 | 常规 |
| Ch28 | 第28章：数据产品化与数据契约 | 4 | 4 | 常规 |
| Ch29 | 第29章：数据资产价值评估与复用机制 | 3 | 9 | 常规 |
| Ch30 | 第30章：企业内部数据市场与共享治理 | 2 | 3 | 常规 |
| Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 0 | 9 | 高 |
| Ch32 | 第32章：自动化采集、解析与清洗 Agent | 3 | 5 | 高 |
| Ch33 | 第33章：标注、合成与评测 Agent | 2 | 8 | 高 |
| Ch34 | 第34章：DataOps Agent 与平台自治 | 3 | 5 | 高 |
| Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 3 | 6 | 高 |
| Ch36 | 第36章：数据合规框架与治理 | 8 | 0 | 常规 |
| Ch37 | 第37章：联邦学习与隐私保护技术 | 12 | 0 | 常规 |
| Ch38 | 第38章：文本语料数据工程：开放 Web、过滤去重与透明账本 | 4 | 表格随正文保留 | 高 |
| Ch39 | 第39章：图文数据工程：候选池构建、多模态筛选与 DataComp 评估 | 2 | 表格随正文保留 | 高 |
| Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 6 | 3 | 高 |
| Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 9 | 表格随正文保留 | 高 |
| Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 3 | 4 | 高 |
| Ch43 | 第43章：推理轨迹数据工程：长链压缩、隐式计算与监督掩码 | 5 | 表格随正文保留 | 高 |
| Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 5 | 5 | 常规 |
| Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 3 | 3 | 常规 |
| Ch46 | 第46章：推理模型与 RL 数据工程：R1 / QwQ 范式 | 3 | 2 | 常规 |
| Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 4 | 3 | 常规 |
| Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 3 | 3 | 常规 |
| P01 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 11 | 0 | 高 |
| P02 | 项目二：垂直领域专家 SFT（法律） | 20 | 0 | 高 |
| P03 | 项目三：LLaVA 多模态指令数据工厂 | 8 | 0 | 高 |
| P04 | 项目四：合成数学与代码教材工厂 | 11 | 1 | 高 |
| P05 | 项目五：多模态 RAG 企业财报助手 | 9 | 1 | 高 |
| P06 | 项目六：CoT 推理数据集构建与 PRM 训练 | 10 | 1 | 高 |
| P07 | 项目七：Agent Tool-Use 数据工厂 | 14 | 1 | 高 |
| P08 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 11 | 1 | 高 |
| P09 | 项目九：隐私保护数据流水线 | 12 | 1 | 高 |
| P10 | 项目十：端到端 LLM 数据飞轮 | 10 | 1 | 高 |
| P11 | 项目十一：Mini-DeepSeek 预训练复现 | 1 | 1 | 高 |
| P12 | 项目十二：R1 推理飞轮 | 1 | 1 | 高 |
| P13 | 项目十三：多模态指令工厂 | 1 | 1 | 高 |
| P14 | 项目十四：视频生成数据集：从视频源到可用于 T2V 训练的数据流水线 | 2 | 0 | 高 |
| P15 | 项目十五：基于 DataAgent 构建企业级语义问数助手 | 2 | 0 | 高 |
| appendix_a_tools_and_frameworks_quick_reference | 附录A：工具与框架速查表 | 0 | 1 | 常规 |
| appendix_b_compliance_and_release_checklist | 附录B：合规与上线检查清单 | 0 | 2 | 常规 |
| appendix_c_cost_estimation_and_resource_templates | 附录C：成本估算与资源模板 | 0 | 3 | 常规 |

## 三、图片台账

| 编号 | 类型 | 标题 / Alt 来源 | 单元 | 章节 / 项目 | 文件路径 / 来源 | 权限状态 | Alt text | 需高清源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 图1-1 | 图 | 图1-1：大模型时代数据工程职责重构图，展示平台、数据、算法、标注、产品与合规角色之间的闭环接口 | Ch1 | 第1章 大模型时代的数据变革 | 本书资源：`docs/images/part1/data_engineering_roles_1775830393574.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图1-1：大模型时代数据工程职责重构图，展示平台、数据、算法、标注、产品与合规角色之间的闭环接口 | 是 |
| 图1-2 | 图 | 图1-2：全书十四篇制生命周期地图，展示从总论、预训练、多模态、对齐、应用、平台、合规到项目实战的知识结构 | Ch1 | 第1章 大模型时代的数据变革 | 本书资源：`docs/images/part1/data_lifecycle_map_1775830407042.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图1-2：全书十四篇制生命周期地图，展示从总论、预训练、多模态、对齐、应用、平台、合规到项目实战的知识结构 | 是 |
| 图2-1 | 图 | 图2-1：生命周期视角下的多维度质量分层架构，展示不同阶段质量指标权重从规模、多样性转向真实性、帮助性 | Ch2 | 第2章：LLM数据生命周期与质量评估框架 | 本书资源：`docs/images/part1/data_quality_hierarchy_1775835516841.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图2-1：生命周期视角下的多维度质量分层架构，展示不同阶段质量指标权重从规模、多样性转向真实性、帮助性 | 是 |
| 图2-2 | 图 | 图2-2：大模型数据缺陷与质量指标交叉映射图，展示六类缺陷与准确度、一致性、多样性、覆盖度和可追溯性之间的关系 | Ch2 | 第2章：LLM数据生命周期与质量评估框架 | 本书资源：`docs/images/part1/defect_metric_radar_1775835533937.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图2-2：大模型数据缺陷与质量指标交叉映射图，展示六类缺陷与准确度、一致性、多样性、覆盖度和可追溯性之间的关系 | 是 |
| 图2-3 | 图 | 图2-3：数据评分卡驱动的自动截断与治理流，展示硬闸门、软闸门、人工复核和回滚动作 | Ch2 | 第2章：LLM数据生命周期与质量评估框架 | 本书资源：`docs/images/part1/data_quality_gates_1775835548587.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图2-3：数据评分卡驱动的自动截断与治理流，展示硬闸门、软闸门、人工复核和回滚动作 | 是 |
| 图3-1 | 图 | 图3-1：AI原生数据栈五层架构，展示采集接入、处理编排、存储索引、评测运营和治理安全层之间的数据流 | Ch3 | 第3章 AI原生数据栈与成本治理 | 本书资源：`docs/images/part1/ai_data_stack_architecture.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图3-1：AI原生数据栈五层架构，展示采集接入、处理编排、存储索引、评测运营和治理安全层之间的数据流 | 是 |
| 图3-2 | 图 | 图3-2：训练数据成本治理闭环图，展示预算规划、成本监控、ROI评估、优化决策和预算复盘的循环 | Ch3 | 第3章 AI原生数据栈与成本治理 | 本书资源：`docs/images/part1/cost_governance_loop.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图3-2：训练数据成本治理闭环图，展示预算规划、成本监控、ROI评估、优化决策和预算复盘的循环 | 是 |
| 图 8 | 图 | 数据工程 Agent 六层架构图 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch31_01.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据工程 Agent 六层架构图 | 是 |
| 图 9 | 图 | 人机协同流程图——按风险等级分流 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch31_02.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 人机协同流程图——按风险等级分流 | 是 |
| 图 10 | 图 | 四源采集 Agent 统一架构 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch32_01.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 四源采集 Agent 统一架构 | 是 |
| 图 11 | 图 | 解析异常处理决策流程 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch32_02.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 解析异常处理决策流程 | 是 |
| 图 12 | 图 | 质量过滤分级流水线 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch32_03.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 质量过滤分级流水线 | 是 |
| 图 13 | 图 | 标注辅助 Agent 的四个维度 | Ch33 | 第33章：标注、合成与评测 Agent | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch33_01.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 标注辅助 Agent 的四个维度 | 是 |
| 图 14 | 图 | 合成数据 Agent 闭环流水线 | Ch33 | 第33章：标注、合成与评测 Agent | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch33_02.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 合成数据 Agent 闭环流水线 | 是 |
| 图 15 | 图 | 告警到根因定位 Agent 流程 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch34_01.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 告警到根因定位 Agent 流程 | 是 |
| 图 16 | 图 | 回滚审批流程 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch34_02.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 回滚审批流程 | 是 |
| 图 17 | 图 | 流水线自愈决策流程 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch34_03.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 流水线自愈决策流程 | 是 |
| 图 18 | 图 | Agent 权限分层审批流程 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch35_01.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | Agent 权限分层审批流程 | 是 |
| 图 19 | 图 | 提示注入分层防御流程 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch35_02.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 提示注入分层防御流程 | 是 |
| 图 20 | 图 | Agent 安全事件应急响应流程 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书资源：`docs/images/part10/ai_agent_decision_workflow_ch35_03.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | Agent 安全事件应急响应流程 | 是 |
| 图36-1 | 图 | 图36-1：合规左移与治理协同架构图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_1_合规左移与治理协同架构图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-1：合规左移与治理协同架构图 | 是 |
| 图36-4 | 图 | 图36-4：数据分级、用途和处理动作构成的风险矩阵图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_4_数据分级用途和处理动作构成的风险矩阵图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-4：数据分级、用途和处理动作构成的风险矩阵图 | 是 |
| 图36-5 | 图 | 图36-5：从数据接入到模型训练的合规门禁流程图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_5_从数据接入到模型训练的合规门禁流程图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-5：从数据接入到模型训练的合规门禁流程图 | 是 |
| 图36-3 | 图 | 图36-3：隐私规格与策略生成流程图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_3_P09隐私规格与策略生成流程图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-3：隐私规格与策略生成流程图 | 是 |
| 图36-2 | 图 | 图36-2：DPIA与RoPA工程化审批流 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_2_DPIA与RoPA工程化审批流.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-2：DPIA与RoPA工程化审批流 | 是 |
| 图36-6 | 图 | 图36-6：审计日志、告警、事件响应与复盘闭环图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_6_审计日志告警事件响应与复盘闭环图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-6：审计日志、告警、事件响应与复盘闭环图 | 是 |
| 图36-7 | 图 | 图36-7：第三方 API / 大模型调用边界网关图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_7_第三方API与大模型调用边界网关图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-7：第三方 API / 大模型调用边界网关图 | 是 |
| 图36-8 | 图 | 图36-8：用户删除请求的全链路传播与清理示意图 | Ch36 | 第36章：数据合规框架与治理 | 本书资源：`docs/images/part11/图36_8_用户删除请求的全链路传播与清理示意图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图36-8：用户删除请求的全链路传播与清理示意图 | 是 |
| 图37-1 | 图 | 图37-1：跨机构医疗数据协作中的隐私与合规冲突示意图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_1_跨机构医疗数据协作中的隐私与合规冲突示意图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-1：跨机构医疗数据协作中的隐私与合规冲突示意图 | 是 |
| 图37-2 | 图 | 图37-2：数据可用性与隐私保护的结构性矛盾示意图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_2_数据可用性与隐私保护的结构性矛盾示意图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-2：数据可用性与隐私保护的结构性矛盾示意图 | 是 |
| 图37-3 | 图 | 图37-3：从数据安全到训练安全的治理重心迁移图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_3_从数据安全到训练安全的治理重心迁移图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-3：从数据安全到训练安全的治理重心迁移图 | 是 |
| 图37-4 | 图 | 图37-4：隐私增强技术全景矩阵图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_4_隐私增强技术全景矩阵图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-4：隐私增强技术全景矩阵图 | 是 |
| 图37-5 | 图 | 图37-5：联邦学习基本训练闭环 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_5_联邦学习基本训练闭环.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-5：联邦学习基本训练闭环 | 是 |
| 图37-6 | 图 | 图37-6：DP-SGD 训练流程示意图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_6_DPSGD训练流程示意图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-6：DP-SGD 训练流程示意图 | 是 |
| 图37-7 | 图 | 图37-7：联邦训练中的通信成本分解图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_7_联邦训练中的通信成本分解图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-7：联邦训练中的通信成本分解图 | 是 |
| 图37-8 | 图 | 图37-8：横向联邦与纵向联邦对比示意图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_8_横向联邦与纵向联邦对比示意图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-8：横向联邦与纵向联邦对比示意图 | 是 |
| 图37-9 | 图 | 图37-9：梯度反演攻击示意图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_9_梯度反演攻击示意图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-9：梯度反演攻击示意图 | 是 |
| 图37-10 | 图 | 图37-10：联邦系统整体架构图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_10_联邦系统整体架构图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-10：联邦系统整体架构图 | 是 |
| 图37-11 | 图 | 图37-11：合规治理、隐私流水线、联邦训练与应用能力闭环图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_11_合规治理隐私流水线联邦训练与应用能力闭环图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-11：合规治理、隐私流水线、联邦训练与应用能力闭环图 | 是 |
| 图37-12 | 图 | 图37-12：医疗与金融场景的隐私技术路线对比图 | Ch37 | 第37章：联邦学习与隐私保护技术 | 本书资源：`docs/images/part11/图37_12_医疗与金融场景的隐私技术路线对比图.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图37-12：医疗与金融场景的隐私技术路线对比图 | 是 |
| 图38-1 | 图 | 图38-1 FineWeb MinHash 去重和 PII 处理流程 | Ch38 | 第38章：文本语料数据工程：开放 Web、过滤去重与透明账本 | 本书资源：`docs/images/part12/ch41_01_fineweb_minhash_pii_flow.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图38-1 FineWeb MinHash 去重和 PII 处理流程 | 是 |
| 图38-2 | 图 | 图38-2 FineWeb 数据处理选择的消融评估回路 | Ch38 | 第38章：文本语料数据工程：开放 Web、过滤去重与透明账本 | 本书资源：`docs/images/part12/ch41_02_fineweb_ablation_loop.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图38-2 FineWeb 数据处理选择的消融评估回路 | 是 |
| 图38-3 | 图 | 图38-3 Dolma 透明语料证据链 | Ch38 | 第38章：文本语料数据工程：开放 Web、过滤去重与透明账本 | 本书资源：`docs/images/part12/ch42_01_dolma_evidence_chain.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图38-3 Dolma 透明语料证据链 | 是 |
| 图38-4 | 图 | 图38-4 Dolma source mix 与训练诊断回路 | Ch38 | 第38章：文本语料数据工程：开放 Web、过滤去重与透明账本 | 本书资源：`docs/images/part12/ch42_02_dolma_source_mix_diagnosis.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图38-4 Dolma source mix 与训练诊断回路 | 是 |
| 图39-1 | 图 | 图39-1 LAION-5B 图文候选记录的多通道 schema | Ch39 | 第39章：图文数据工程：候选池构建、多模态筛选与 DataComp 评估 | 本书资源：`docs/images/part12/ch43_01_laion_multichannel_schema.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图39-1 LAION-5B 图文候选记录的多通道 schema | 是 |
| 图39-2 | 图 | 图39-2 图文候选池质量评估与闭环修复 | Ch39 | 第39章：图文数据工程：候选池构建、多模态筛选与 DataComp 评估 | 本书资源：`docs/images/part12/ch43_02_laion_quality_datacomp_loop.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图39-2 图文候选池质量评估与闭环修复 | 是 |
| 图40-1 | 图 | 图40-1：Schema 到 JSON 的结构化映射 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书资源：`docs/images/part12/ch38_01_schema_decomposition.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图40-1：Schema 到 JSON 的结构化映射 | 是 |
| 图40-2 | 图 | 图40-2：StructBill-CN 数据集构建流水线 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书资源：`docs/images/part12/ch38_02_dataset_construction_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图40-2：StructBill-CN 数据集构建流水线 | 是 |
| 图40-3 | 图 | 图40-3：结构一致性校验门禁 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书资源：`docs/images/part12/ch38_03_structural_consistency_validation.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图40-3：结构一致性校验门禁 | 是 |
| 图40-4 | 图 | 图40-4：表格样本三类监督信号结构图 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书资源：`docs/images/part12/ch38_04_supervision_schema.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图40-4：表格样本三类监督信号结构图 | 是 |
| 图40-5 | 图 | 图40-5：SparseTable-Bench 四阶段构建流水线图 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书资源：`docs/images/part12/ch38_05_stb_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图40-5：SparseTable-Bench 四阶段构建流水线图 | 是 |
| 图40-6 | 图 | 图40-6：STB-Mask-Stress 遮挡生成与评测流程图 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书资源：`docs/images/part12/ch38_06_mask_stress_flow.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图40-6：STB-Mask-Stress 遮挡生成与评测流程图 | 是 |
| 图41-1 | 图 | 图41-1：多图表信息图推理数据集领域覆盖分布 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch39_01_domain_distribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-1：多图表信息图推理数据集领域覆盖分布 | 是 |
| 图41-2 | 图 | 图41-2：多图表信息图推理数据集子图表类型分布 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch39_02_chart_type_distribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-2：多图表信息图推理数据集子图表类型分布 | 是 |
| 图41-3 | 图 | 图41-3：多图表信息图推理数据集子问题类型分布 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch39_03_question_type_distribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-3：多图表信息图推理数据集子问题类型分布 | 是 |
| 图41-4 | 图 | 图41-4：多图表信息图样本（鲨鱼袭击） | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch39_04_shark_attack_infographic.jpg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-4：多图表信息图样本（鲨鱼袭击） | 是 |
| 图41-5 | 图 | 图41-5：多图标信息图推理数据集四阶段构建流水线图 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch39_05_multichart_dataset_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-5：多图标信息图推理数据集四阶段构建流水线图 | 是 |
| 图41-6 | 图 | 图41-6：MedImage-ToolVQA 数据构建概念流程 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch41_02_medimage_tool_vqa_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-6：MedImage-ToolVQA 数据构建概念流程 | 是 |
| 图41-7 | 图 | 图41-7：工具调用多轮轨迹结构 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch41_03_tool_trajectory_structure.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-7：工具调用多轮轨迹结构 | 是 |
| 图41-8 | 图 | 图41-8：SFT schema 中的真实图像与 bbox 证据 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch41_05_sft_schema_real_bbox_example.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-8：SFT schema 中的真实图像与 bbox 证据 | 是 |
| 图41-9 | 图 | 图41-9：质量控制与人工复核门禁 | Ch41 | 第41章：视觉推理数据工程：图表证据、医学图像与工具调用轨迹 | 本书资源：`docs/images/part12/ch41_04_quality_review_gate.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图41-9：质量控制与人工复核门禁 | 是 |
| 图42-1 | 图 | 图42-1：语义响应与风格控制双通道 schema | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书资源：`docs/images/part12/ch42_fig02_dual_channel_schema.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图42-1：语义响应与风格控制双通道 schema | 是 |
| 图42-2 | 图 | 图42-2：VoiceStyleControl 数据构建流水线 | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书资源：`docs/images/part12/ch42_fig01_data_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图42-2：VoiceStyleControl 数据构建流水线 | 是 |
| 图42-3 | 图 | 图42-3：质量评估与数据飞轮闭环 | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书资源：`docs/images/part12/ch42_fig03_quality_loop.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图42-3：质量评估与数据飞轮闭环 | 是 |
| 图43-1 | 图 | 图43-1：Latent-Switch-69K 构建流水线图 | Ch43 | 第43章：推理轨迹数据工程：长链压缩、隐式计算与监督掩码 | 本书资源：`docs/images/part12/ch43_latent_switch_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图43-1：Latent-Switch-69K 构建流水线图 | 是 |
| 图43-2 | 图 | 图43-2：Latent-Switch-69K 数据来源与领域组成 | Ch43 | 第43章：推理轨迹数据工程：长链压缩、隐式计算与监督掩码 | 本书资源：`docs/images/part12/ch40_05_dataset_composition.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图43-2：Latent-Switch-69K 数据来源与领域组成 | 是 |
| 图43-3 | 图 | 图43-3：原始 CoT、压缩 CoT 与 latent placeholder 对比 | Ch43 | 第43章：推理轨迹数据工程：长链压缩、隐式计算与监督掩码 | 本书资源：`docs/images/part12/ch43_cot_latent_comparison.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图43-3：原始 CoT、压缩 CoT 与 latent placeholder 对比 | 是 |
| 图43-4 | 图 | 图43-4：原始与蒸馏后推理长度及压缩率统计 | Ch43 | 第43章：推理轨迹数据工程：长链压缩、隐式计算与监督掩码 | 本书资源：`docs/images/part12/ch40_07_token_compression_distribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图43-4：原始与蒸馏后推理长度及压缩率统计 | 是 |
| 图43-5 | 图 | 图43-5：Supervision mask 示意图 | Ch43 | 第43章：推理轨迹数据工程：长链压缩、隐式计算与监督掩码 | 本书资源：`docs/images/part12/ch43_supervision_mask.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图43-5：Supervision mask 示意图 | 是 |
| 图44-1 | 图 | 图44-1：数据配方漏斗 (Data Recipe Funnel) | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书资源：`docs/images/part13/ch44_01_data_recipe_funnel_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图44-1：数据配方漏斗 (Data Recipe Funnel) | 是 |
| 图44-2 | 图 | 图44-2：大模型数据透明度光谱 (Data Transparency Spectrum) | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书资源：`docs/images/part13/ch44_02_data_transparency_spectrum_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图44-2：大模型数据透明度光谱 (Data Transparency Spectrum) | 是 |
| 图44-3 | 图 | 图44-3：预训练数据源分层地图 | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书资源：`docs/images/part13/ch44_03_pretrain_data_source_map.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图44-3：预训练数据源分层地图 | 是 |
| 图44-4 | 图 | 图44-4：三模型数据组成饼图对比 (Estimated Data Mixture Ratios) | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书资源：`docs/images/part13/ch44_04_models_pie_chart_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图44-4：三模型数据组成饼图对比 (Estimated Data Mixture Ratios) | 是 |
| 图44-5 | 图 | 图44-5：Llama-3 退火期数据组成时间轴 (Curriculum Learning Schedule) | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书资源：`docs/images/part13/ch44_05_llama3_annealing_schedule_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图44-5：Llama-3 退火期数据组成时间轴 (Curriculum Learning Schedule) | 是 |
| 图45-1 | 图 | 图45-1：LLM 后训练三阶段流水线示意图 | Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 本书资源：`docs/images/part13/ch45_01_posttrain_three_stage_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图45-1：LLM 后训练三阶段流水线示意图 | 是 |
| 图45-2 | 图 | 图45-2：Self-Instruct、Evol-Instruct 与 Magpie 三流派 pipeline 对比 | Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 本书资源：`docs/images/part13/ch45_02_sft_synthesis_pipelines.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图45-2：Self-Instruct、Evol-Instruct 与 Magpie 三流派 pipeline 对比 | 是 |
| 图45-3 | 图 | 图45-3：Tülu-3 三阶段数据流与规模示意 | Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 本书资源：`docs/images/part13/ch45_03_tulu3_posttrain_flow.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图45-3：Tülu-3 三阶段数据流与规模示意 | 是 |
| 图46-1 | 图 | 图46-1：R1 风格推理数据飞轮四阶段 | Ch46 | 第46章：推理模型与 RL 数据工程：R1 / QwQ 范式 | 本书资源：`docs/images/part13/ch46_01_r1_reasoning_flywheel.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图46-1：R1 风格推理数据飞轮四阶段 | 是 |
| 图46-2 | 图 | 图46-2：推理数据奖励信号与验证器结构 | Ch46 | 第46章：推理模型与 RL 数据工程：R1 / QwQ 范式 | 本书资源：`docs/images/part13/ch46_02_reward_verifier_architecture.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图46-2：推理数据奖励信号与验证器结构 | 是 |
| 图46-3 | 图 | 图46-3：Long-CoT 数据样例剖面 | Ch46 | 第46章：推理模型与 RL 数据工程：R1 / QwQ 范式 | 本书资源：`docs/images/part13/ch46_03_long_cot_trace_patterns.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图46-3：Long-CoT 数据样例剖面 | 是 |
| 图47-1 | 图 | 图47-1：多模态数据工程全景图 | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书资源：`docs/images/part13/ch47_01_multimodal_data_panorama.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图47-1：多模态数据工程全景图 | 是 |
| 图47-2 | 图 | 图47-2：VLM 数据三阶段流水线 (3-Stage VLM Data Engineering Pipeline) | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书资源：`docs/images/part13/ch47_02_vlm_three_stages_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图47-2：VLM 数据三阶段流水线 (3-Stage VLM Data Engineering Pipeline) | 是 |
| 图47-3 | 图 | 图47-3：Native vs Dynamic Resolution 数据 pipeline 对比 (Resolution Handling) | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书资源：`docs/images/part13/ch47_03_resolution_handling_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图47-3：Native vs Dynamic Resolution 数据 pipeline 对比 (Resolution Handling) | 是 |
| 图47-4 | 图 | 图47-4：多模态指令合成 pipeline (Multi-modal Instruction Synthesis) | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书资源：`docs/images/part13/ch47_04_instruction_synthesis_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图47-4：多模态指令合成 pipeline (Multi-modal Instruction Synthesis) | 是 |
| 图48-1 | 图 | 图48-1：T2I 数据流水线 | Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 本书资源：`docs/images/part13/ch48_01_t2i_data_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图48-1：T2I 数据流水线 | 是 |
| 图48-2 | 图 | 图48-2：T2V 数据流水线 | Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 本书资源：`docs/images/part13/ch48_02_t2v_data_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图48-2：T2V 数据流水线 | 是 |
| 图48-3 | 图 | 图48-3：美学/版权/安全多级过滤架构 | Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 本书资源：`docs/images/part13/ch48_03_multistage_filtering_architecture.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图48-3：美学/版权/安全多级过滤架构 | 是 |
| 图 P01-1 | 图 | 图 P01-1 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_01_mini_c4_pipeline_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-1 | 是 |
| 图 P01-2 | 图 | 图 P01-2 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_02_warc_to_text.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-2 | 是 |
| 图 P01-3 | 图 | 图 P01-3 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_03_cleaning_rules.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-3 | 是 |
| 图 P01-4 | 图 | 图 P01-4 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_04_dedup_minhash_lsh.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-4 | 是 |
| 图 P01-5 | 图 | 图 P01-5 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_05_language_split.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-5 | 是 |
| 图 P01-6 | 图 | 图 P01-6 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_06_quality_filter.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-6 | 是 |
| 图 P01-7 | 图 | 图 P01-7 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_07_three_iterations.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-7 | 是 |
| 图 P01-8 | 图 | 图 P01-8 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_08_funnel.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-8 | 是 |
| 图 P01-9 | 图 | 图 P01-9 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_09_cost_breakdown.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-9 | 是 |
| 图 P01-10 | 图 | 图 P01-10 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_10_validation_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-10 | 是 |
| 图 P01-11 | 图 | 图 P01-11 | P1 | 项目一：基于 Ray 构建分布式 Mini-C4 数据流水线 | 本书资源：`docs/images/part14/p01_11_methodology_summary.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P01-11 | 是 |
| 图 P02-1 | 图 | 图 P02-1 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_01_legal_sft_factory_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-1 | 是 |
| 图 P02-2 | 图 | 图 P02-2 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_02_roles_and_responsibilities.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-2 | 是 |
| 图 P02-3 | 图 | 图 P02-3 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_03_pdf_cleaning_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-3 | 是 |
| 图 P02-4 | 图 | 图 P02-4 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_04_cleaning_examples.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-4 | 是 |
| 图 P02-5 | 图 | 图 P02-5 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_05_seed_schema.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-5 | 是 |
| 图 P02-6 | 图 | 图 P02-6 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_06_task_taxonomy.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-6 | 是 |
| 图 P02-7 | 图 | 图 P02-7 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_07_task_vs_domain_distribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-7 | 是 |
| 图 P02-8 | 图 | 图 P02-8 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_08_weighted_task_sampling.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-8 | 是 |
| 图 P02-9 | 图 | 图 P02-9 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_09_cot_structure.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-9 | 是 |
| 图 P02-10 | 图 | 图 P02-10 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_10_preference_and_review.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-10 | 是 |
| 图 P02-11 | 图 | 图 P02-11 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_11_risk_refusal_flow.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-11 | 是 |
| 图 P02-12 | 图 | 图 P02-12 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_12_qa_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-12 | 是 |
| 图 P02-13 | 图 | 图 P02-13 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_13_qa_decision_table.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-13 | 是 |
| 图 P02-14 | 图 | 图 P02-14 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_14_human_in_the_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-14 | 是 |
| 图 P02-15 | 图 | 图 P02-15 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_15_training_artifacts.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-15 | 是 |
| 图 P02-16 | 图 | 图 P02-16 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_16_metrics_dashboard.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-16 | 是 |
| 图 P02-17 | 图 | 图 P02-17 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_17_eval_sampling_protocol.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-17 | 是 |
| 图 P02-18 | 图 | 图 P02-18 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_18_version_timeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-18 | 是 |
| 图 P02-19 | 图 | 图 P02-19 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_19_validation_chain.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-19 | 是 |
| 图 P02-20 | 图 | 图 P02-20 | P2 | 项目二：垂直领域专家 SFT（法律） | 本书资源：`docs/images/part14/p02_20_cross_domain_transfer.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P02-20 | 是 |
| 图 P03-1 | 图 | 图 P03-1 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_01_llava_factory_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-1 | 是 |
| 图 P03-2 | 图 | 图 P03-2 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_02_roles_and_responsibilities.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-2 | 是 |
| 图 P03-3 | 图 | 图 P03-3 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_03_asset_layers.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-3 | 是 |
| 图 P03-4 | 图 | 图 P03-4 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_04_document_tasks.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-4 | 是 |
| 图 P03-5 | 图 | 图 P03-5 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_05_bbox_alignment.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-5 | 是 |
| 图 P03-6 | 图 | 图 P03-6 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_06_quality_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-6 | 是 |
| 图 P03-7 | 图 | 图 P03-7 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_07_failure_attribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-7 | 是 |
| 图 P03-8 | 图 | 图 P03-8 | P3 | 项目三：LLaVA 多模态指令数据工厂 | 本书资源：`docs/images/part14/p03_08_validation_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P03-8 | 是 |
| 图 P04-1 | 图 | 图 P04-1 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_01_project_positioning.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-1 | 是 |
| 图 P04-2 | 图 | 图 P04-2 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_02_goals_and_scope.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-2 | 是 |
| 图 P04-3 | 图 | 图 P04-3 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_03_pipeline_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-3 | 是 |
| 图 P04-4 | 图 | 图 P04-4 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_04_roles_and_responsibilities.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-4 | 是 |
| 图 P04-5 | 图 | 图 P04-5 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_05_seed_to_plan.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-5 | 是 |
| 图 P04-6 | 图 | 图 P04-6 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_06_evol_path.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-6 | 是 |
| 图 P04-7 | 图 | 图 P04-7 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_07_cot_vs_pot.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-7 | 是 |
| 图 P04-8 | 图 | 图 P04-8 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_08_generation_chain.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-8 | 是 |
| 图 P04-9 | 图 | 图 P04-9 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_09_sandbox_validation.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-9 | 是 |
| 图 P04-10 | 图 | 图 P04-10 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_10_packaging_outputs.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-10 | 是 |
| 图 P04-11 | 图 | 图 P04-11 | P4 | 项目四：合成数学与代码教材工厂 | 本书资源：`docs/images/part14/p04_11_training_interface.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P04-11 | 是 |
| 图 P05-1 | 图 | 图 P05-1 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_01_overall_architecture.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-1 | 是 |
| 图 P05-2 | 图 | 图 P05-2 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_02_vision_vs_ocr.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-2 | 是 |
| 图 P05-3 | 图 | 图 P05-3 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_03_page_assets.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-3 | 是 |
| 图 P05-4 | 图 | 图 P05-4 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_04_indexing_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-4 | 是 |
| 图 P05-5 | 图 | 图 P05-5 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_05_topk_filtering.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-5 | 是 |
| 图 P05-6 | 图 | 图 P05-6 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_06_multi_image_prompting.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-6 | 是 |
| 图 P05-7 | 图 | 图 P05-7 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_07_eval_framework.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-7 | 是 |
| 图 P05-8 | 图 | 图 P05-8 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_08_optimization_roadmap.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-8 | 是 |
| 图 P05-9 | 图 | 图 P05-9 | P5 | 项目五：多模态 RAG 企业财报助手 | 本书资源：`docs/images/part14/p05_09_hybrid_rag.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P05-9 | 是 |
| 图 P06-1 | 图 | 图 P06-1 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_01_prm_factory_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-1 | 是 |
| 图 P06-2 | 图 | 图 P06-2 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_02_step_validation_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-2 | 是 |
| 图 P06-3 | 图 | 图 P06-3 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_03_task_sampling.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-3 | 是 |
| 图 P06-4 | 图 | 图 P06-4 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_04_trace_types.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-4 | 是 |
| 图 P06-5 | 图 | 图 P06-5 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_05_step_schema.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-5 | 是 |
| 图 P06-6 | 图 | 图 P06-6 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_06_validation_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-6 | 是 |
| 图 P06-7 | 图 | 图 P06-7 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_07_step_labels.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-7 | 是 |
| 图 P06-8 | 图 | 图 P06-8 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_08_training_interface.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-8 | 是 |
| 图 P06-9 | 图 | 图 P06-9 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_09_validation_metrics.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-9 | 是 |
| 图 P06-10 | 图 | 图 P06-10 | P6 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书资源：`docs/images/part14/p06_10_noise_sources.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P06-10 | 是 |
| 图 P07-1 | 图 | 图 P07-1 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_01_agent_tooluse_factory_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-1 | 是 |
| 图 P07-2 | 图 | 图 P07-2 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_02_three_layer_architecture.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-2 | 是 |
| 图 P07-3 | 图 | 图 P07-3 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_03_roles_and_responsibilities.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-3 | 是 |
| 图 P07-4 | 图 | 图 P07-4 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_04_tool_schema_structure.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-4 | 是 |
| 图 P07-5 | 图 | 图 P07-5 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_05_task_specs_and_templates.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-5 | 是 |
| 图 P07-6 | 图 | 图 P07-6 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_06_trajectory_taxonomy.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-6 | 是 |
| 图 P07-7 | 图 | 图 P07-7 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_07_simulated_env_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-7 | 是 |
| 图 P07-8 | 图 | 图 P07-8 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_08_pipeline_steps.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-8 | 是 |
| 图 P07-9 | 图 | 图 P07-9 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_09_recovery_flow.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-9 | 是 |
| 图 P07-10 | 图 | 图 P07-10 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_10_memory_trajectory.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-10 | 是 |
| 图 P07-11 | 图 | 图 P07-11 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_11_unsafe_block.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-11 | 是 |
| 图 P07-12 | 图 | 图 P07-12 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_12_dataset_repacking.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-12 | 是 |
| 图 P07-13 | 图 | 图 P07-13 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_13_eval_and_checks.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-13 | 是 |
| 图 P07-14 | 图 | 图 P07-14 | P7 | 项目七：Agent Tool-Use 数据工厂 | 本书资源：`docs/images/part14/p07_14_roadmap.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P07-14 | 是 |
| 图 P08-1 | 图 | 图 P08-1 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_01_dataops_platform_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-1 | 是 |
| 图 P08-2 | 图 | 图 P08-2 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_02_four_layer_architecture.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-2 | 是 |
| 图 P08-3 | 图 | 图 P08-3 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_03_specs_to_ops_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-3 | 是 |
| 图 P08-4 | 图 | 图 P08-4 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_04_object_model.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-4 | 是 |
| 图 P08-5 | 图 | 图 P08-5 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_05_version_lifecycle.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-5 | 是 |
| 图 P08-6 | 图 | 图 P08-6 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_06_experiment_tracking.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-6 | 是 |
| 图 P08-7 | 图 | 图 P08-7 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_07_lineage_graph.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-7 | 是 |
| 图 P08-8 | 图 | 图 P08-8 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_08_rollback_flow.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-8 | 是 |
| 图 P08-9 | 图 | 图 P08-9 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_09_observability_loop.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-9 | 是 |
| 图 P08-10 | 图 | 图 P08-10 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_10_audit_and_incident_review.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-10 | 是 |
| 图 P08-11 | 图 | 图 P08-11 | P8 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书资源：`docs/images/part14/p08_11_validation_pipeline.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P08-11 | 是 |
| 图 P09-1 | 图 | 图 P09-1 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_01_privacy_pipeline_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-1 | 是 |
| 图 P09-2 | 图 | 图 P09-2 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_02_roles_and_responsibilities.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-2 | 是 |
| 图 P09-3 | 图 | 图 P09-3 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_03_specs_layer.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-3 | 是 |
| 图 P09-4 | 图 | 图 P09-4 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_04_raw_records_coverage.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-4 | 是 |
| 图 P09-5 | 图 | 图 P09-5 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_05_pii_detection_distribution.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-5 | 是 |
| 图 P09-6 | 图 | 图 P09-6 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_06_classification_and_quarantine.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-6 | 是 |
| 图 P09-7 | 图 | 图 P09-7 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_07_redaction_strategies.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-7 | 是 |
| 图 P09-8 | 图 | 图 P09-8 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_08_storage_zones.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-8 | 是 |
| 图 P09-9 | 图 | 图 P09-9 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_09_alerts_and_audit.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-9 | 是 |
| 图 P09-10 | 图 | 图 P09-10 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_10_preflight_checks.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-10 | 是 |
| 图 P09-11 | 图 | 图 P09-11 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_11_incident_postmortem.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-11 | 是 |
| 图 P09-12 | 图 | 图 P09-12 | P9 | 项目九：隐私保护数据流水线 | 本书资源：`docs/images/part14/p09_12_execution_sequence.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P09-12 | 是 |
| 图 P10-1 | 图 | 图 P10-1 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_01_flywheel_overview.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-1 | 是 |
| 图 P10-2 | 图 | 图 P10-2 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_02_registry_and_interfaces.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-2 | 是 |
| 图 P10-3 | 图 | 图 P10-3 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_03_project_specs.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-3 | 是 |
| 图 P10-4 | 图 | 图 P10-4 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_04_stage_plan.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-4 | 是 |
| 图 P10-5 | 图 | 图 P10-5 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_05_architecture_code_mapping.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-5 | 是 |
| 图 P10-6 | 图 | 图 P10-6 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_06_boundaries_and_control_points.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-6 | 是 |
| 图 P10-7 | 图 | 图 P10-7 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_07_runs_and_milestones.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-7 | 是 |
| 图 P10-8 | 图 | 图 P10-8 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_08_bottleneck_map.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-8 | 是 |
| 图 P10-9 | 图 | 图 P10-9 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_09_metrics_codegen.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-9 | 是 |
| 图 P10-10 | 图 | 图 P10-10 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书资源：`docs/images/part14/p10_10_check_contracts.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P10-10 | 是 |
| 图 204 | 图 | Mini-DeepSeek Data Pipeline | P11 | 项目十一：Mini-DeepSeek 预训练复现 | 本书资源：`docs/images/part14/p11_mini_deepseek_arch_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | Mini-DeepSeek Data Pipeline | 是 |
| 图 P12-1 | 图 | 图 P12-1 | P12 | 项目十二：教学化 R1 推理数据飞轮 | 本书资源：`docs/images/part14/p12_r1_reasoning_flywheel_architecture.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图 P12-1 | 是 |
| 图 206 | 图 | Multimodal Instruction Factory | P13 | 项目十三：Qwen-VL 多模态指令工厂 | 本书资源：`docs/images/part14/p13_mm_instruction_factory_arch_en.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | Multimodal Instruction Factory | 是 |
| 图 207 | 图 | P14 Video Generation Data Pipeline | P14 | 项目十四：视频生成数据集：从视频源到可用于 T2V 训练的数据流水线 | 本书资源：`docs/images/part14/p14_video_generation_pipeline_en.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | P14 Video Generation Data Pipeline | 是 |
| 图 208 | 图 | frame1 | P14 | 项目十四：视频生成数据集：从视频源到可用于 T2V 训练的数据流水线 | 本书资源：`docs/images/part14/p14_video_frame_0.jpg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | frame1 | 是 |
| 图 209 | 图 | frame2 | P14 | 项目十四：视频生成数据集：从视频源到可用于 T2V 训练的数据流水线 | 本书资源：`docs/images/part14/p14_video_frame_1.jpg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | frame2 | 是 |
| 图 210 | 图 | DataAgent 企业语义问数助手分层架构 | P15 | 项目十五：基于 DataAgent 构建企业级语义问数助手 | 本书资源：`docs/images/part14/p15_dataagent_semantic_bi_layered_architecture.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | DataAgent 企业语义问数助手分层架构 | 是 |
| 图 211 | 图 | DataAgent 整体架构图 | P15 | 项目十五：基于 DataAgent 构建企业级语义问数助手 | 本书资源：`docs/images/part14/p15_dataagent_agent_excalidraw.png` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | DataAgent 整体架构图 | 是 |
| 图 212 | 图 | DataAgent 企业语义问数助手运行流程 | P15 | 项目十五：基于 DataAgent 构建企业级语义问数助手 | 本书资源：`docs/images/part14/p15_dataagent_semantic_bi_sequence.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | DataAgent 企业语义问数助手运行流程 | 是 |
| 图4-1 | 图 | 图4-1：预训练数据源分层地图 | Ch4 | 第4章 数据源、采集与版权 | 本书资源：`docs/images/part2/pretrain_data_source_map.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图4-1：预训练数据源分层地图 | 是 |
| 图4-2 | 图 | 图4-2：数据采集与权属存证流程图 | Ch4 | 第4章 数据源、采集与版权 | 本书资源：`docs/images/part2/data_ingestion_provenance_chain.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图4-2：数据采集与权属存证流程图 | 是 |
| 图5-1 | 图 | 图5-1：清洗与去污染全景流程图 | Ch5 | 第5章 清洗、去重与去污染 | 本书资源：`docs/images/part2/cleaning_pipeline_overview.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图5-1：清洗与去污染全景流程图 | 是 |
| 图5-2 | 图 | 图5-2：质量过滤漏斗与抽检闭环图 | Ch5 | 第5章 清洗、去重与去污染 | 本书资源：`docs/images/part2/quality_filter_funnel_loop.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图5-2：质量过滤漏斗与抽检闭环图 | 是 |
| 图6-1 | 图 | 图6-1：吞吐瓶颈诊断流程图 | Ch6 | 第6章 分词、序列化与高效加载 | 本书资源：`docs/images/part2/io_bottleneck_diagnosis_flow.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图6-1：吞吐瓶颈诊断流程图 | 是 |
| 图6-2 | 图 | 图6-2：训练输入管道分层图 | Ch6 | 第6章 分词、序列化与高效加载 | 本书资源：`docs/images/part2/training_input_pipeline_layers.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图6-2：训练输入管道分层图 | 是 |
| 图7-1 | 图 | 图7-1：数据运营飞轮图 | Ch7 | 第7章 数据评估、质量闭环与运营迭代 | 本书资源：`docs/images/part2/data_operations_flywheel.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图7-1：数据运营飞轮图 | 是 |
| 图7-2 | 图 | 图7-2：数据评估闭环图 | Ch7 | 第7章 数据评估、质量闭环与运营迭代 | 本书资源：`docs/images/part2/data_evaluation_loop.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图7-2：数据评估闭环图 | 是 |
| 图8-1 | 图 | 图8-1：图文数据工程全景图 | Ch8 | 第8章 图文对数据工程 | 本书资源：`docs/images/part3/multimodal_data_panorama.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图8-1：图文数据工程全景图 | 是 |
| 图8-2 | 图 | 图8-2：图像语义对齐与过滤流程图 | Ch8 | 第8章 图文对数据工程 | 本书资源：`docs/images/part3/image_semantic_alignment_flow.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图8-2：图像语义对齐与过滤流程图 | 是 |
| 图8-3 | 图 | 图8-3：AnyRes 动态多分辨率切割算法原理图 | Ch8 | 第8章 图文对数据工程 | 本书资源：`docs/images/part3/anyres_dynamic_patching.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图8-3：AnyRes 动态多分辨率切割算法原理图 | 是 |
| 图9-1 | 图 | 图9-1：重标注与 OCR 双流线增强图 | Ch9 | 第9章 重标注与文档理解 | 本书资源：`docs/images/part3/recaptioning_ocr_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图9-1：重标注与 OCR 双流线增强图 | 是 |
| 图9-2 | 图 | 图9-2：文档结构 Layout-to-Token 映射图 | Ch9 | 第9章 重标注与文档理解 | 本书资源：`docs/images/part3/document_structure_sample.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图9-2：文档结构 Layout-to-Token 映射图 | 是 |
| 图10-1 | 图 | 图10-1：音视频对齐分布式管线图 | Ch10 | 第10章 视频与音频数据工程 | 本书资源：`docs/images/part3/av_sample_pipeline.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图10-1：音视频对齐分布式管线图 | 是 |
| 图10-2 | 图 | 图10-2：自适应镜头边界检测与语义防泄漏架构图 | Ch10 | 第10章 视频与音频数据工程 | 本书资源：`docs/images/part3/av_shot_boundary_hsv.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图10-2：自适应镜头边界检测与语义防泄漏架构图 | 是 |
| 图10-3 | 图 | 图10-3：大规模 ASR 提取与时间轴动态校准对比图 | Ch10 | 第10章 视频与音频数据工程 | 本书资源：`docs/images/part3/asr_whisperx_comparison.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图10-3：大规模 ASR 提取与时间轴动态校准对比图 | 是 |
| 图10-4 | 图 | 图10-4：跨模态时序校准与几何对齐架构图 | Ch10 | 第10章 视频与音频数据工程 | 本书资源：`docs/images/part3/av_alignment_diagram.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图10-4：跨模态时序校准与几何对齐架构图 | 是 |
| 图11-1 | 图 | 图11-1：跨模态对齐的三级金字塔架构 | Ch11 | 第11章 跨模态对齐与融合 | 本书资源：`docs/images/part3/cross_modal_alignment_hierarchy.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图11-1：跨模态对齐的三级金字塔架构 | 是 |
| 图11-2 | 图 | 图11-2：多模态融合与负样本挖掘管线 | Ch11 | 第11章 跨模态对齐与融合 | 本书资源：`docs/images/part3/fusion_training_sample_design.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图11-2：多模态融合与负样本挖掘管线 | 是 |
| 图12-1 | 图 | 图12-1：SFT指令体系的架构示意图 | Ch12 | 第12章：SFT数据设计与指令体系 | 本书资源：`docs/images/part4/图12_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图12-1：SFT指令体系的架构示意图 | 是 |
| 图12-2 | 图 | 图12-2：样本生成与验收的闭环示意图 | Ch12 | 第12章：SFT数据设计与指令体系 | 本书资源：`docs/images/part4/图12_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图12-2：样本生成与验收的闭环示意图 | 是 |
| 图13-1 | 图 | 图13-1：偏好数据到奖励信号流程图 | Ch13 | 第13章：偏好数据与奖励信号 | 本书资源：`docs/images/part4/图13_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图13-1：偏好数据到奖励信号流程图 | 是 |
| 图13-2 | 图 | 图13-2：多目标偏好权衡示意图 | Ch13 | 第13章：偏好数据与奖励信号 | 本书资源：`docs/images/part4/图13_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图13-2：多目标偏好权衡示意图 | 是 |
| 图14-1 | 图 | 图14-1：大模型标注平台工作流图 | Ch14 | 第14章 标注平台、质量保障体系与数据运营 | 本书资源：`docs/images/part4/图14_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图14-1：大模型标注平台工作流图 | 是 |
| 图14-2 | 图 | 图14-2：人机协同 QA 闭环图 | Ch14 | 第14章 标注平台、质量保障体系与数据运营 | 本书资源：`docs/images/part4/图14_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图14-2：人机协同 QA 闭环图 | 是 |
| 图15-1 | 图 | 图15-1：合成数据工厂流程图 | Ch15 | 第15章：合成数据工厂：从种子到验证 | 本书资源：`docs/images/part5/图15_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图15-1：合成数据工厂流程图 | 是 |
| 图15-2 | 图 | 图15-2：质量闸门与回流闭环图 | Ch15 | 第15章：合成数据工厂：从种子到验证 | 本书资源：`docs/images/part5/图15_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图15-2：质量闸门与回流闭环图 | 是 |
| 图16-1 | 图 | 图16-1：模型协作生成时序图 | Ch16 | 第16章：知识蒸馏与模型协作 | 本书资源：`docs/images/part5/图16_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图16-1：模型协作生成时序图 | 是 |
| 图16-2 | 图 | 图16-2：蒸馏样本验证流程图 | Ch16 | 第16章：知识蒸馏与模型协作 | 本书资源：`docs/images/part5/图16_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图16-2：蒸馏样本验证流程图 | 是 |
| 图17-1 | 图 | 图17-1：合成数据风险传播机制图 | Ch17 | 第17章：合成数据质量控制与模型坍缩 | 本书资源：`docs/images/part5/图17_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图17-1：合成数据风险传播机制图 | 是 |
| 图17-2 | 图 | 图17-2：合成数据质量闸门与回退策略流程图 | Ch17 | 第17章：合成数据质量控制与模型坍缩 | 本书资源：`docs/images/part5/图17_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图17-2：合成数据质量闸门与回退策略流程图 | 是 |
| 图18-1 | 图 | 图18-1：推理数据构造与验证流程图 | Ch18 | 第18章：思维链与推理数据工程 | 本书资源：`docs/images/part6/图18_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图18-1：推理数据构造与验证流程图 | 是 |
| 图18-2 | 图 | 图18-2：过程监督标签示意图 | Ch18 | 第18章：思维链与推理数据工程 | 本书资源：`docs/images/part6/图18_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图18-2：过程监督标签示意图 | 是 |
| 图19-1 | 图 | 图19-1：Tool-Use 数据构造状态机图 | Ch19 | 第19章：Tool-Use 与函数调用数据 | 本书资源：`docs/images/part6/图19_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图19-1：Tool-Use 数据构造状态机图 | 是 |
| 图19-2 | 图 | 图19-2：调用失败恢复流程图 | Ch19 | 第19章：Tool-Use 与函数调用数据 | 本书资源：`docs/images/part6/图19_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图19-2：调用失败恢复流程图 | 是 |
| 图20-1 | 图 | 图20-1：多轮 Agent 状态转移图 | Ch20 | 第20章：Agent记忆与多轮交互数据 | 本书资源：`docs/images/part6/图20_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图20-1：多轮 Agent 状态转移图 | 是 |
| 图20-2 | 图 | 图20-2：任务型 Agent 的记忆分层与更新流程图 | Ch20 | 第20章：Agent记忆与多轮交互数据 | 本书资源：`docs/images/part6/图20_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图20-2：任务型 Agent 的记忆分层与更新流程图 | 是 |
| 图21-1 | 图 | 图21-1：RAG 系统中的数据变换链路 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-1：RAG 系统中的数据变换链路 | 是 |
| 图21-2 | 图 | 图21-2：文档从原始形态到 RAG 可用知识单元的结构变化 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-2：文档从原始形态到 RAG 可用知识单元的结构变化 | 是 |
| 图21-3 | 图 | 图21-3：RAG 错误如何沿数据链路累积 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-3：RAG 错误如何沿数据链路累积 | 是 |
| 图21-4 | 图 | 图21-4：RAG 系统性能的短板效应 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_4.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-4：RAG 系统性能的短板效应 | 是 |
| 图21-5 | 图 | 图21-5：复杂文档的版面解析与结构还原 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_5.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-5：复杂文档的版面解析与结构还原 | 是 |
| 图21-6 | 图 | 图21-6：不同切分策略对语义完整性的影响 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_6.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-6：不同切分策略对语义完整性的影响 | 是 |
| 图21-7 | 图 | 图21-7：父子索引与多粒度检索结构 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_7.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-7：父子索引与多粒度检索结构 | 是 |
| 图21-8 | 图 | 图21-8：混合检索与 Rerank 的两阶段检索流程 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_8.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-8：混合检索与 Rerank 的两阶段检索流程 | 是 |
| 图21-9 | 图 | 图21-9：RAG 系统的评测、反馈与优化闭环 | Ch21 | 第21章：RAG 数据流水线 | 本书资源：`docs/images/part7/图21_9.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图21-9：RAG 系统的评测、反馈与优化闭环 | 是 |
| 图22-1 | 图 | 图22-1：OCR 与视觉理解的能力边界 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书资源：`docs/images/part7/图22_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图22-1：OCR 与视觉理解的能力边界 | 是 |
| 图22-2 | 图 | 图22-2：文本与视觉元素的联合表示与对齐 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书资源：`docs/images/part7/图22_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图22-2：文本与视觉元素的联合表示与对齐 | 是 |
| 图22-3 | 图 | 图22-3：跨模态检索与重排序流程 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书资源：`docs/images/part7/图22_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图22-3：跨模态检索与重排序流程 | 是 |
| 图22-4 | 图 | 图22-4：多模态 RAG 评测漏斗 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书资源：`docs/images/part7/图22_4.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图22-4：多模态 RAG 评测漏斗 | 是 |
| 图22-5 | 图 | 图22-5：错误归因到修复动作的闭环 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书资源：`docs/images/part7/图22_5.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图22-5：错误归因到修复动作的闭环 | 是 |
| 图23-1 | 图 | 图23-1：从离线评测到线上真实问题分布 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书资源：`docs/images/part7/图23_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图23-1：从离线评测到线上真实问题分布 | 是 |
| 图23-2 | 图 | 图23-2：大模型应用的在线反馈数据飞轮 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书资源：`docs/images/part7/图23_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图23-2：大模型应用的在线反馈数据飞轮 | 是 |
| 图23-3 | 图 | 图23-3：在线反馈事件采集与分流链路 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书资源：`docs/images/part7/图23_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图23-3：在线反馈事件采集与分流链路 | 是 |
| 图23-4 | 图 | 图23-4：知识更新、灰度发布与回滚治理流程 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书资源：`docs/images/part7/图23_4.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图23-4：知识更新、灰度发布与回滚治理流程 | 是 |
| 图24-1 | 图 | 图24-1：LLM数据团队组织演进路径 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书资源：`docs/images/part8/图24_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图24-1：LLM数据团队组织演进路径 | 是 |
| 图24-2 | 图 | 图24-2：DataOps团队组织全景图 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书资源：`docs/images/part8/图24_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图24-2：DataOps团队组织全景图 | 是 |
| 图24-3 | 图 | 图24-3：DataOps飞轮四池协同示意图 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书资源：`docs/images/part8/图24_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图24-3：DataOps飞轮四池协同示意图 | 是 |
| 图25-1 | 图 | 图25-1：版本管理体系全景图 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书资源：`docs/images/part8/图25_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图25-1：版本管理体系全景图 | 是 |
| 图25-2 | 图 | 图25-2：数据谱系与实验追踪图 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书资源：`docs/images/part8/图25_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图25-2：数据谱系与实验追踪图 | 是 |
| 图26-1 | 图 | 图26-1：异常归因决策树 | Ch26 | 第26章：数据平台可观测性 | 本书资源：`docs/images/part8/图26_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图26-1：异常归因决策树 | 是 |
| 图26-2 | 图 | 图26-2：平台可观测性全景图 | Ch26 | 第26章：数据平台可观测性 | 本书资源：`docs/images/part8/图26_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 图26-2：平台可观测性全景图 | 是 |
| 图 275 | 图 | 数据资产从创建到使用的完整流程 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书资源：`docs/images/part9/图27_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据资产从创建到使用的完整流程 | 是 |
| 图 276 | 图 | 数据血缘关系图 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书资源：`docs/images/part9/图27_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据血缘关系图 | 是 |
| 图 277 | 图 | 数据资产生命周期状态转移图 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书资源：`docs/images/part9/图27_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据资产生命周期状态转移图 | 是 |
| 图 278 | 图 | 基于角色和用途的权限管理矩阵 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书资源：`docs/images/part9/图27_4.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 基于角色和用途的权限管理矩阵 | 是 |
| 图 279 | 图 | 数据产品画布 | Ch28 | 第28章：数据产品化与数据契约 | 本书资源：`docs/images/part9/图28_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据产品画布 | 是 |
| 图 280 | 图 | Data Contract 模板：五类条款的结构 | Ch28 | 第28章：数据产品化与数据契约 | 本书资源：`docs/images/part9/图28_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | Data Contract 模板：五类条款的结构 | 是 |
| 图 281 | 图 | 变更兼容性决策树 | Ch28 | 第28章：数据产品化与数据契约 | 本书资源：`docs/images/part9/图28_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 变更兼容性决策树 | 是 |
| 图 282 | 图 | 消费者影响分析 | Ch28 | 第28章：数据产品化与数据契约 | 本书资源：`docs/images/part9/图28_4.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 消费者影响分析 | 是 |
| 图 283 | 图 | 数据资产的多场景复用路径 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书资源：`docs/images/part9/图29_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据资产的多场景复用路径 | 是 |
| 图 284 | 图 | 数据资产成本—收益矩阵 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书资源：`docs/images/part9/图29_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据资产成本—收益矩阵 | 是 |
| 图 285 | 图 | 数据资产复盘卡 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书资源：`docs/images/part9/图29_3.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 数据资产复盘卡 | 是 |
| 图 286 | 图 | 内部数据市场架构图 | Ch30 | 第30章：企业内部数据市场与共享治理 | 本书资源：`docs/images/part9/图30_1.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 内部数据市场架构图 | 是 |
| 图 287 | 图 | 授权审批流程 | Ch30 | 第30章：企业内部数据市场与共享治理 | 本书资源：`docs/images/part9/图30_2.svg` | 内部自绘/改绘资源；终稿复核高清源与 AI 使用声明 | 授权审批流程 | 是 |


## 四、表格台账

| 编号 | 类型 | 标题 | 单元 | 章节 / 项目 | 来源 | 权限状态 | Alt / 说明 | 需高清源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 表 1-1 | 表 | 正文表格或清单 | Ch01 | 第1章 大模型时代的数据变革 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 1-2 | 表 | 正文表格或清单 | Ch01 | 第1章 大模型时代的数据变革 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 1-3 | 表 | 正文表格或清单 | Ch01 | 第1章 大模型时代的数据变革 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 1-4 | 表 | 正文表格或清单 | Ch01 | 第1章 大模型时代的数据变革 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 1-5 | 表 | 正文表格或清单 | Ch01 | 第1章 大模型时代的数据变革 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 1-6 | 表 | 正文表格或清单 | Ch01 | 第1章 大模型时代的数据变革 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 2-1 | 表 | 正文表格或清单 | Ch02 | 第2章：LLM数据生命周期与质量评估框架 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 3-1 | 表 | 正文表格或清单 | Ch03 | 第3章 AI原生数据栈与成本治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 3-2 | 表 | 正文表格或清单 | Ch03 | 第3章 AI原生数据栈与成本治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 3-3 | 表 | 正文表格或清单 | Ch03 | 第3章 AI原生数据栈与成本治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 4-1 | 表 | 正文表格或清单 | Ch04 | 第4章 数据源、采集与版权 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 4-2 | 表 | 正文表格或清单 | Ch04 | 第4章 数据源、采集与版权 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 5-1 | 表 | 正文表格或清单 | Ch05 | 第5章 清洗、去重与去污染 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 5-2 | 表 | 正文表格或清单 | Ch05 | 第5章 清洗、去重与去污染 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 6-1 | 表 | 正文表格或清单 | Ch06 | 第6章 分词、序列化与高效加载 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 6-2 | 表 | 正文表格或清单 | Ch06 | 第6章 分词、序列化与高效加载 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 7-1 | 表 | 正文表格或清单 | Ch07 | 第7章 数据评估、质量闭环与运营迭代 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 7-2 | 表 | 正文表格或清单 | Ch07 | 第7章 数据评估、质量闭环与运营迭代 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 8-1 | 表 | 正文表格或清单 | Ch08 | 第8章 图文对数据工程 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 8-2 | 表 | 正文表格或清单 | Ch08 | 第8章 图文对数据工程 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 9-1 | 表 | 正文表格或清单 | Ch09 | 第9章 重标注与文档理解 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 9-2 | 表 | 正文表格或清单 | Ch09 | 第9章 重标注与文档理解 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 10-1 | 表 | 正文表格或清单 | Ch10 | 第10章 视频与音频数据工程 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 10-2 | 表 | 正文表格或清单 | Ch10 | 第10章 视频与音频数据工程 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 11-1 | 表 | 正文表格或清单 | Ch11 | 第11章 跨模态对齐与融合 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 11-2 | 表 | 正文表格或清单 | Ch11 | 第11章 跨模态对齐与融合 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 11-3 | 表 | 正文表格或清单 | Ch11 | 第11章 跨模态对齐与融合 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 12-1 | 表 | 正文表格或清单 | Ch12 | 第12章 SFT数据设计与指令体系 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 12-2 | 表 | 正文表格或清单 | Ch12 | 第12章 SFT数据设计与指令体系 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 13-1 | 表 | 正文表格或清单 | Ch13 | 第13章 偏好数据与奖励信号 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 13-2 | 表 | 正文表格或清单 | Ch13 | 第13章 偏好数据与奖励信号 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 14-1 | 表 | 正文表格或清单 | Ch14 | 第14章 标注平台、QA体系与数据运营 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 14-2 | 表 | 正文表格或清单 | Ch14 | 第14章 标注平台、QA体系与数据运营 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-1 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-2 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-3 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-4 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-5 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-6 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-7 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 21-8 | 表 | 正文表格或清单 | Ch21 | 第21章：RAG 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-1 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-2 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-3 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-4 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-5 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-6 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-7 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 22-8 | 表 | 正文表格或清单 | Ch22 | 第22章：多模态 RAG 与视觉检索 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-1 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-2 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-3 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-4 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-5 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-6 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-7 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-8 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-9 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-10 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-11 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 23-12 | 表 | 正文表格或清单 | Ch23 | 第23章：在线反馈闭环与知识更新 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-1 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-2 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-3 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-4 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-5 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-6 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-7 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-8 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-9 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-10 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-11 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-12 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-13 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-14 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-15 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-16 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-17 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-18 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-19 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-20 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-21 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-22 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-23 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-24 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-25 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-26 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-27 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-28 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-29 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 24-30 | 表 | 正文表格或清单 | Ch24 | 第24章：DataOps 飞轮与团队组织 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-1 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-2 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-3 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-4 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-5 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-6 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-7 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 25-8 | 表 | 正文表格或清单 | Ch25 | 第25章：数据版本管理与实验追踪 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-1 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-2 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-3 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-4 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-5 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-6 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-7 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 26-8 | 表 | 正文表格或清单 | Ch26 | 第26章：数据平台可观测性 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 27-1 | 表 | 正文表格或清单 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 27-2 | 表 | 正文表格或清单 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 27-3 | 表 | 正文表格或清单 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 27-4 | 表 | 正文表格或清单 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 27-5 | 表 | 正文表格或清单 | Ch27 | 第27章：数据资产目录与元数据治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 28-1 | 表 | 正文表格或清单 | Ch28 | 第28章：数据产品化与数据契约 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 28-2 | 表 | 正文表格或清单 | Ch28 | 第28章：数据产品化与数据契约 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 28-3 | 表 | 正文表格或清单 | Ch28 | 第28章：数据产品化与数据契约 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 28-4 | 表 | 正文表格或清单 | Ch28 | 第28章：数据产品化与数据契约 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-1 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-2 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-3 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-4 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-5 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-6 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-7 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-8 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 29-9 | 表 | 正文表格或清单 | Ch29 | 第29章：数据资产价值评估与复用机制 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 30-1 | 表 | 正文表格或清单 | Ch30 | 第30章：企业内部数据市场与共享治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 30-2 | 表 | 正文表格或清单 | Ch30 | 第30章：企业内部数据市场与共享治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 30-3 | 表 | 正文表格或清单 | Ch30 | 第30章：企业内部数据市场与共享治理 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-1 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-2 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-3 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-4 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-5 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-6 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-7 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-8 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 31-9 | 表 | 正文表格或清单 | Ch31 | 第31章：数据工程 Agent 的架构与任务边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 32-1 | 表 | 正文表格或清单 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 32-2 | 表 | 正文表格或清单 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 32-3 | 表 | 正文表格或清单 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 32-4 | 表 | 正文表格或清单 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 32-5 | 表 | 正文表格或清单 | Ch32 | 第32章：自动化采集、解析与清洗 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-1 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-2 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-3 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-4 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-5 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-6 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-7 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 33-8 | 表 | 正文表格或清单 | Ch33 | 第33章：标注、合成与评测 Agent | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 34-1 | 表 | 正文表格或清单 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 34-2 | 表 | 正文表格或清单 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 34-3 | 表 | 正文表格或清单 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 34-4 | 表 | 正文表格或清单 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 34-5 | 表 | 正文表格或清单 | Ch34 | 第34章：DataOps Agent 与平台自治 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 35-1 | 表 | 正文表格或清单 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 35-2 | 表 | 正文表格或清单 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 35-3 | 表 | 正文表格或清单 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 35-4 | 表 | 正文表格或清单 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 35-5 | 表 | 正文表格或清单 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 35-6 | 表 | 正文表格或清单 | Ch35 | 第35章：数据工程 Agent 的安全、权限与人机协同 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 40-1 | 表 | 正文表格或清单 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 40-2 | 表 | 正文表格或清单 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 40-3 | 表 | 正文表格或清单 | Ch40 | 第40章：视觉文档与表格数据工程：结构化抽取、稀疏表格与 Schema 约束 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 42-1 | 表 | 正文表格或清单 | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 42-2 | 表 | 正文表格或清单 | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 42-3 | 表 | 正文表格或清单 | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 42-4 | 表 | 正文表格或清单 | Ch42 | 第42章：语音与音频数据工程：交互控制、风格标签与安全边界 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 4-1 | 表 | 正文表格或清单 | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 44-1 | 表 | 正文表格或清单 | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 44-2 | 表 | 正文表格或清单 | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 44-3 | 表 | 正文表格或清单 | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 44-4 | 表 | 正文表格或清单 | Ch44 | 第44章：LLM 预训练数据工程实战：从配方到落地 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 45-1 | 表 | 正文表格或清单 | Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 45-2 | 表 | 正文表格或清单 | Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 45-3 | 表 | 正文表格或清单 | Ch45 | 第45章：LLM 后训练数据工程实战：SFT 与偏好对齐 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 46-1 | 表 | 正文表格或清单 | Ch46 | 第46章：推理模型与 RL 数据工程：R1 / QwQ 范式 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 46-2 | 表 | 正文表格或清单 | Ch46 | 第46章：推理模型与 RL 数据工程：R1 / QwQ 范式 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 47-1 | 表 | 正文表格或清单 | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 47-2 | 表 | 正文表格或清单 | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 47-3 | 表 | 正文表格或清单 | Ch47 | 第47章：多模态大模型（VLM）数据配方：从预训练到视觉对齐 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 48-1 | 表 | 正文表格或清单 | Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 48-2 | 表 | 正文表格或清单 | Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 48-3 | 表 | 正文表格或清单 | Ch48 | 第48章：多模态生成模型数据工程：T2I 与 T2V 数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 P04-1 | 表 | 合成教材工厂出版验收表 | P04 | 项目四：合成数学与代码教材工厂 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P05-1 | 表 | 多模态 RAG 出版验收表 | P05 | 项目五：多模态 RAG 企业财报助手 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P06-1 | 表 | 过程监督数据出版验收表 | P06 | 项目六：CoT 推理数据集构建与 PRM 训练 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P07-1 | 表 | Agent Tool-Use 出版验收表 | P07 | 项目七：Agent Tool-Use 数据工厂 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P08-1 | 表 | DataOps 平台出版验收表 | P08 | 项目八：企业级 DataOps 平台搭建：从数据项目到组织级治理能力 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P09-1 | 表 | 隐私流水线出版验收表 | P09 | 项目九：隐私保护数据流水线 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P10-1 | 表 | LLM 数据飞轮出版验收表 | P10 | 项目十：端到端 LLM 数据飞轮 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P11-1 | 表 | Mini-DeepSeek 预训练复现出版验收表 | P11 | 项目十一：Mini-DeepSeek 预训练复现 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P12-1 | 表 | R1 推理飞轮出版验收表 | P12 | 项目十二：R1 推理飞轮 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 P13-1 | 表 | 多模态指令工厂出版验收表 | P13 | 项目十三：多模态指令工厂 | 本书整理 | 内部整理；终稿复核数据口径 | 验收维度、指标证据和出版复核口径 | 否 |
| 表 A-1 | 表 | 正文表格或清单 | appendix_a_tools_and_frameworks_quick_reference | 附录A：工具与框架速查表 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 B-1 | 表 | 正文表格或清单 | appendix_b_compliance_and_release_checklist | 附录B：合规与上线检查清单 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 B-2 | 表 | 正文表格或清单 | appendix_b_compliance_and_release_checklist | 附录B：合规与上线检查清单 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 C-1 | 表 | 正文表格或清单 | appendix_c_cost_estimation_and_resource_templates | 附录C：成本估算与资源模板 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 C-2 | 表 | 正文表格或清单 | appendix_c_cost_estimation_and_resource_templates | 附录C：成本估算与资源模板 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |
| 表 C-3 | 表 | 正文表格或清单 | appendix_c_cost_estimation_and_resource_templates | 附录C：成本估算与资源模板 | 本书整理 | 内部整理；终稿复核数据口径 | 表题和字段说明随正文保留 | 否 |

## 五、维护规则

- 修改正文图号、文件名或图片来源后，必须同步更新本台账。
- 交出版社前，资料编辑需抽检所有高优先级条目的清晰度、授权、AI 使用声明和 alt text。
