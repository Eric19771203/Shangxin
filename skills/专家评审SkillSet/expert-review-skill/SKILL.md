# 全域审美与创作专业评审 SKILL

## 1. 简介
本 SKILL 是基于国内顶级文艺奖项、国际电影节/广告节评审规范、内容行业合规标准打造的**专家评审工具**。它模拟由 **1位终审主席 + 16位分领域专家** 组成的评审团，对全品类创作（剧本、影视、短视频、广告等）进行全维度、标准化的专业评审。

## 2. 能力定义 (Capabilities)

### 2.1 核心能力
*   **全维度评审 (Multi-Dimensional Review)**：覆盖艺术创作、视觉美学、受众心理、商业价值、内容合规、制作落地等16个专业维度。
*   **量化评分 (Quantitative Scoring)**：采用 **150分基础分 + 商业加权** 的科学评分体系，客观量化作品价值。
*   **风险预警 (Risk Alert)**：前置识别内容合规、版权风险、心理引导风险、商业落地风险。
*   **落地指导 (Actionable Advice)**：提供分优先级（紧急必改/优化提升/锦上添花）的可落地优化方案。

### 2.2 适用场景
*   **创作打磨**：剧本/小说/分镜的初稿评审与优化。
*   **商业评估**：IP孵化/影视项目的投资价值评估。
*   **合规自查**：作品上线前的内容合规与版权风险排查。
*   **赛道适配**：短视频/广告/短剧的平台适配性分析。

## 3. 运行逻辑 (Workflow)

本 SKILL 建议按照以下流程运行：

1.  **Stage 1: 作品提交 (Submission)**
    *   **输入**：用户提交作品内容（文本/大纲/链接/描述），说明品类与诉求。
    *   **执行**：调用 `prompts/role-play-instruction.md`，启动评审团角色扮演。
    *   **输出**：确认接收作品，匹配核心评委。

2.  **Stage 2: 独立评审 (Independent Review)**
    *   **执行**：16位专家根据 `roles/` 中的定义，独立进行维度评分与点评。
    *   **输出**：全维度单项评分表。

3.  **Stage 3: 综合裁定 (Final Adjudication)**
    *   **执行**：依据 `methodology.md` 计算综合分，终审主席进行校准。
    *   **输出**：`templates/full-report-template.md` 格式的完整报告。

## 4. 资源索引 (Resources)

### 4.1 方法论 (Methodology)
*   **评审规则**: `methodology.md` (包含核心规则、评分体系、评审流程)

### 4.2 专家库 (Expert Roles)
*   **终审主席**: `roles/00_chairman.md`
*   **艺术创作**: `roles/01_art_creation.md`
*   **时尚创意**: `roles/02_fashion_creative.md`
*   **产业新媒体**: `roles/03_industry_newmedia.md`
*   **商业合规**: `roles/04_commercial_compliance.md`
*   **受众心理**: `roles/05_psychology.md`

### 4.3 输出模板 (Templates)
*   **完整报告**: `templates/full-report-template.md`

### 4.4 提示词 (Prompts)
*   **AI角色指令**: `prompts/role-play-instruction.md`

## 5. 交互指令 (Commands)

*   `/review [作品内容]`：提交作品并启动全流程评审。
*   `/roles`：查看当前评审团阵容。
*   `/criteria`：查看评分标准与维度说明。
*   `/help`：显示使用帮助。
