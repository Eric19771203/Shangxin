# Seedance Skill 工作流集成指南 (Workflow Integration Guide)

本指南演示如何将 `Seedance_Unified_Master_Skill.md` 作为模块嵌入到其他自动化工作流或代码中。

## 场景一：在 AI Agent 编排中使用 (如 Coze/Dify/LangChain)

在这个场景中，Seedance Skill 被视为一个**“工具”**或**“插件”**。

### 1. 结构化定义
*   **工具名称**：`Seedance_Prompt_Generator`
*   **工具描述**：专业的 Seedance 2.0 视频提示词生成器，用于将自然语言描述转化为符合官方标准的提示词。
*   **System Prompt (核心指令)**：
    *(直接复制 `Seedance_Unified_Master_Skill.md` 的全部内容到这里)*
*   **输入变量**：`user_query` (用户的画面描述)

### 2. 工作流编排示例 (伪代码)
```python
def main_workflow(script_segment):
    # 步骤 1: 剧本分析
    scene_description = analyze_script(script_segment)
    
    # 步骤 2: 调用 Seedance Skill (核心集成点)
    # 将 Skill 文件作为 System Prompt 加载
    system_prompt = load_file("Seedance_Unified_Master_Skill.md")
    
    # 让 AI 根据 Skill 定义生成提示词
    seedance_prompt = llm.chat(
        system_prompt=system_prompt,
        user_message=f"请根据这段描述生成视频提示词：{scene_description}"
    )
    
    # 步骤 3: 后续处理 (如自动通过 API 提交生成任务)
    submit_job_to_seedance(seedance_prompt)
```

---

## 场景二：在漫剧生产流水线中嵌入

在漫剧生产中，这个 Skill 是 **"分镜脚本" -> "视频生成"** 的中间件。

### 流水线架构
1.  **编剧 Agent**：生成《分镜脚本表格》（包含画面描述、运镜、台词）。
2.  **Seedance Skill (本模块)**：读取《分镜脚本表格》的“画面描述”和“运镜”列，**批量转换**为 Seedance 提示词。
3.  **执行 Agent / 人工**：将生成的提示词复制到即梦平台。

### 批处理 Prompt 示例
您可以直接给 AI 发送这样的指令，它会自动调用 Skill 的能力：

> **用户指令**：
> "我现在有一个包含 5 个镜头的表格（见附件），请激活 `Seedance 2.0 终极全能创作大师 Skill`，按照 Skill 中的『高手分镜模板』，为这 5 个镜头分别生成对应的 Seedance 提示词。"

---

## 场景三：作为 Python 函数调用 (Function Calling)

如果您正在开发一个自动化程序，可以将 Skill 封装为函数：

```python
import openai

def generate_seedance_prompt(description, style="Cinematic"):
    # 读取 Skill 定义
    with open("Seedance_Unified_Master_Skill.md", "r", encoding="utf-8") as f:
        skill_definition = f.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": skill_definition},
            {"role": "user", "content": f"生成提示词：{description}，风格：{style}"}
        ]
    )
    return response.choices[0].message.content
```
