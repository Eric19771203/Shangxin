# 金标准 Skill 架构规范 (Golden Standard Architecture)

基于“末世重生类漫剧剧本创作 SKill”的成功实践，定义以下 Skill 架构规范。该架构旨在将复杂的创意/逻辑任务转化为可控的工程化流水线。

## 1. 核心理念
**“工厂模式” (Factory Pattern)**：将生成过程拆解为 **方法论 (Logic)**、**规范 (Style)**、**模板 (Structure)** 和 **质检 (QA)** 四个独立维度。

## 2. 目录结构标准
一个标准的、高质量的 Skill 应包含以下目录和文件：

```text
My-Skill/
├── SKILL.md                  # [核心配置] 元数据、I/O定义、指令入口
├── knowledge/                # [大脑] 存放核心逻辑与规范
│   ├── method.md             # - 方法论：底层逻辑、公式、步骤
│   └── style.md              # - 风格指南：文风、格式、符号系统
├── templates/                # [骨架] 标准化输出模板
│   ├── main-template.md      # - 主模板
│   └── sub-template.md       # - 子模块模板
├── examples/                 # [参照系] Few-Shot Learning 样例
│   ├── perfect-example.md    # - 完美对标样例
│   └── bad-example.md        # - (可选) 负面教材
└── qa/                       # [质检] 质量控制模块
    ├── aligner-prompt.md     # - 对齐检查提示词
    └── checklist.md          # - 检查清单
```

## 3. 各模块详细定义

### 3.1 核心配置 (`SKILL.md`)
- **定义**：Skill 的入口文件。
- **内容**：
    - `Description`：清晰定义 Skill 的能力边界（能做什么，不能做什么）。
    - `Workflow`：定义多阶段生成流程（如：Step 1 -> Step 2 -> QA）。
    - `Commands`：定义用户指令与 Skill 动作的映射。

### 3.2 知识库 (`knowledge/`)
- **`method.md` (逻辑)**：
    - 定义任务的“物理定律”和“公式”。
    - 例如：故事结构的公式（三幕式）、代码架构的模式（MVC）、分析报告的模型（SWOT）。
    - **作用**：确保输出内容的逻辑正确性。
- **`style.md` (风格)**：
    - 定义输出的“视听语言”或“代码风格”。
    - 例如：强制使用的符号、语气（严肃/幽默）、代码命名规范。
    - **作用**：确保输出形式的一致性和专业感。

### 3.3 执行模组 (`templates/` & `examples/`)
- **Templates**：
    - 提供“填空题”式的 Markdown/Code 结构。
    - **作用**：降低模型自由发挥带来的格式混乱风险。
- **Examples**：
    - 提供至少一个“完美样例”。
    - **作用**：利用 LLM 的上下文学习能力 (In-Context Learning)，模仿语气和细节。

### 3.4 质检模组 (`qa/`)
- **定义**：独立的检查机制，用于“Self-Correction”。
- **`aligner-prompt.md`**：
    - 一个独立的 System Prompt，扮演“审核员”角色。
    - **核心**：必须包含具体的检查维度（如：逻辑闭环、风格符合度、关键要素遗漏）。
    - **流程**：生成内容 -> 调用 Aligner -> Pass/Fail -> 修改。

## 4. 运行模式 (Operation Mode)
标准 Skill 应支持 **“流式生成 + 节点质检”**：
1.  **用户输入** -> **匹配 Stage** (如 Outline/Draft)。
2.  **加载资源** -> 读取对应的 Method + Template + Example。
3.  **生成内容** -> 输出初稿。
4.  **触发质检** -> (可选) 调用 Aligner 进行评分和建议。
5.  **最终输出**。
