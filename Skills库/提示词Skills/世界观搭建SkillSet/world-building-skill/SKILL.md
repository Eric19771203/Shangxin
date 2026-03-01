# 世界观搭建 SKILL

## 1. 简介
本 SKILL 专为生成“电影级、逻辑闭环、可落地”的完整世界观而设计，融合了专业的编剧世界观构建法则、标准化的定稿模板、多类型对标范例以及自动化的一致性校验机制。旨在帮助创作者高效、系统地构建出能够支撑长篇连载（如漫剧、网文、剧本）的坚实世界观底座。

## 2. 能力定义 (Capabilities)

### 2.1 核心能力
*   **核心设定构建 (Core Concept Design)**：确立世界名称、时代、核心规则（物理/魔法/科技）、稀缺资源、禁忌与核心矛盾。
*   **社会体系搭建 (Social System Building)**：构建权力结构、阶级划分、法律暴力边界及核心势力分布。
*   **文化与生活填充 (Culture & Life Filling)**：设计语言、仪式、价值观、衣食住行等文化细节，增加世界真实感。
*   **历史背景铺设 (History & Lore)**：编织起源传说、关键历史事件与遗留创伤，为剧情提供深度。
*   **视觉化呈现 (Visual Presentation)**：生成关键场景的画面描述、分镜概念，适配漫剧/影视制作。
*   **一致性校验 (Alignment Check)**：对世界观的逻辑闭环、规则统一性、服务剧情程度进行自动检查。

### 2.2 适用场景
*   漫剧/网文/剧本的前期世界观开发。
*   游戏世界观架构设计。
*   IP 孵化与系列作品的世界观统一。

## 3. 运行逻辑 (Workflow)

本 SKILL 采用分阶段流式创作模式，建议按照以下顺序执行：

1.  **Stage 1: 核心概念 (Core Concept)**
    *   **输入**：用户的一句话灵感或题材类型（如“赛博朋克”、“修仙”）。
    *   **执行**：调用 `world-building-method.md` 中的核心法则，填充 `templates/core-concept-template.md`。
    *   **输出**：包含核心矛盾与规则的世界观雏形。

2.  **Stage 2: 体系深化 (System Deepening)**
    *   **输入**：已生成的核心概念。
    *   **执行**：扩展地理、社会、文化、历史等维度，填充 `templates/full-world-template.md`。
    *   **输出**：完整的世界观设定文档。

3.  **Stage 3: 角色绑定 (Character Integration)**
    *   **输入**：完整世界观。
    *   **执行**：将世界观规则与主角/反派的动机、困境绑定，填充 `templates/character-binding-template.md`。
    *   **输出**：角色与世界观的强绑定关系图谱。

4.  **Stage 4: 视觉化呈现 (Visual Presentation)**
    *   **输入**：关键场景列表。
    *   **执行**：依据 `visual-style.md`，生成场景概念图提示词或分镜描述。
    *   **输出**：场景概念图 Prompt / 关键场景分镜描述。

5.  **Stage 5: 质检与修正 (QA & Refine)**
    *   **输入**：完整的世界观文档。
    *   **执行**：调用 `Aligner` 进行一致性校验。
    *   **输出**：逻辑漏洞报告或通过确认。

## 4. 资源索引 (Resources)

### 4.1 方法论 (Methodology)
*   **构建法则**: `world-building-method.md` (定义冰山法则、冲突驱动、角色绑定)
*   **视觉规范**: `visual-style.md` (定义电影级质感、漫剧分镜标准)

### 4.2 模板库 (Templates)
*   **核心概念模板**: `templates/core-concept-template.md`
*   **完整世界观模板**: `templates/full-world-template.md`
*   **角色绑定模板**: `templates/character-binding-template.md`
*   **场景描述模板**: `templates/scene-template.md`

### 4.3 范例库 (Examples)
*   **都市异能范例**: `examples/urban-fantasy-example.md`
*   **东方玄幻范例**: `examples/oriental-fantasy-example.md`
*   **赛博朋克范例**: `examples/cyberpunk-example.md`

### 4.4 质检卫士 (Aligner)
*   **角色定义**: `world-aligner-subagent/description.md`
*   **检查提示词**: `world-aligner-subagent/prompt.md`

## 5. 交互指令 (Commands)

*   `/start [灵感/类型]`：启动核心概念生成阶段。
*   `/deepen`：进入体系深化阶段。
*   `/bind`：进入角色绑定阶段。
*   `/visualize [场景名]`：生成指定场景的视觉描述。
*   `/check`：触发世界观一致性校验。
*   `/help`：显示帮助信息。
