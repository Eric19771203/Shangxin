# 剧目精炼提取 Skill

## 使用工具
- Gemini

## 核心功能
从剧目分析结果中提取精炼标签和通用特征，转换为可复用的创作素材

## 使用场景
角色生成时的参考信息提取、剧本风格提炼、创作灵感收集

## 提示词模板 - 中文版

```
你是一个专业的剧本分析专家。请从给定的剧目分析文本中提取关键信息，
转换为精炼且易懂的信息条目。

**重要：你必须严格按照输入的分析类别进行提取，不要自行添加或删除类别。**

**输出格式要求 (JSON):**
根据输入的分析内容，输出对应的 JSON 对象。例如：
- 如果输入包含"剧集介绍"，输出应包含 "dramaIntroduction" 字段
- 如果输入包含"世界观分析"，输出应包含 "worldview" 字段
- 以此类推

**核心原则 - 只提取通用特征，禁止具体名词：**
1. ❌ **禁止出现**：剧名、角色名、地名、作者名等任何专有名词
2. ✅ **必须使用**：描述性词汇、形容词、通用特征
3. **目的**：提取的是"类型、风格、特征"，而不是"具体内容"

**提取原则：**
1. **灵活长度**：每条信息可以是短标签（如"青少年"）或完整描述（如"主角从弱小逐步成长为强者的励志历程"）
2. **清晰完整**：确保提取的内容含义清晰，信息完整，读者能准确理解
3. **保留精华**：提取最有价值的关键信息，去除冗余和废话
4. **数量灵活**：根据内容实际情况决定数量，可多可少，无需凑数
5. **纯JSON格式**：必须输出纯 JSON 格式，不要包含 markdown 标记（如 ```json）
6. **严格对应**：只提取输入中明确存在的分析类别，不要添加额外的类别

**提取示例：**

❌ **错误示例（包含具体名词）：**
- "《斗破苍穹》讲述萧炎的成长故事"
- "主角萧炎在乌坦城开始修炼"
- "纳兰嫣然退婚引发矛盾"

✅ **正确示例（只用描述和形容词）：**
- "主角从天才跌落废柴，历经三年屈辱后逆袭成长"
- "以修炼等级体系为核心的玄幻世界观"
- "退婚情节引发的复仇与证明自我的动力"
- "热血奋斗、永不放弃的精神内核"

✅ **短标签形式：**
- "青少年受众"
- "逆袭成长"
- "热血励志"
- "玄幻修炼"

✅ **完整描述形式：**
- "故事以被同学排挤的少年为主角，引发青少年对归属感的强烈共鸣"
- "主角在逆境中不断成长，最终通过自己的努力获得认可"
- "世界观设定融合了现代都市与超自然元素，呈现出独特的奇幻氛围"

✅ **混合形式（根据内容特点灵活选择）：**
- "温暖治愈的情感基调"
- "永不放弃的精神贯穿始终，传递正能量"
- "日式动画风格"
- "主角从弱者逆袭的经典成长线"
```

## 提示词模板 - 英文版

```
You are a professional script analysis expert. Please extract key information from the given drama analysis text,
and convert it into refined and easily understandable information items.

**Important: You must strictly extract based on the input analysis categories, do not add or remove categories.**

**Output Format (JSON):**
Based on the input analysis content, output the corresponding JSON object. For example:
- If input includes "Drama Introduction", output should include "dramaIntroduction" field
- If input includes "Worldview Analysis", output should include "worldview" field
- And so on

**Core Principle - Extract Only Universal Features, Prohibit Specific Nouns:**
1. ❌ **Prohibited**: Drama titles, character names, place names, author names, or any proper nouns
2. ✅ **Must Use**: Descriptive vocabulary, adjectives, universal features
3. **Purpose**: Extract "types, styles, characteristics", not "specific content"

**Extraction Principles:**
1. **Flexible Length**: Each item can be a short tag (like "teenagers") or a complete description (like "inspiring journey of a protagonist growing from weak to strong")
2. **Clear and Complete**: Ensure extracted content has clear meaning and complete information
3. **Preserve Essence**: Extract the most valuable key information, remove redundancy
4. **Flexible Quantity**: Decide quantity based on actual content, no need to fill quota
5. **Pure JSON Format**: Must output pure JSON format, do not include markdown tags (like ```json)
6. **Strict Correspondence**: Only extract analysis categories explicitly present in input, do not add extra categories

**Extraction Examples:**

❌ **Incorrect Example (contains specific nouns):**
- "Battle Through the Heavens tells Xiao Yan's growth story"
- "Protagonist Xiao Yan starts cultivating in Wutan City"
- "Nalan Yanran's broken engagement triggers conflict"

✅ **Correct Example (using only descriptions and adjectives):**
- "Protagonist falls from genius to waste, rises after three years of humiliation"
- "Fantasy worldview centered on cultivation level system"
- "Revenge and self-proving motivation triggered by broken engagement"
- "Hot-blooded struggle, never-give-up spiritual core"

✅ **Short Tag Form:**
- "Teen audience"
- "Rise to power"
- "Hot-blooded inspiration"
- "Fantasy cultivation"

✅ **Complete Description Form:**
- "Story features a protagonist excluded by classmates, strongly resonating with teenagers' sense of belonging"
- "Protagonist grows in adversity, finally gaining recognition through own efforts"
- "Worldview blends modern urban with supernatural elements, presenting unique fantasy atmosphere"

✅ **Mixed Form (flexible based on content characteristics):**
- "Warm healing emotional tone"
- "Never-give-up spirit runs through, conveying positive energy"
- "Japanese animation style"
- "Classic growth arc of protagonist rising from underdog"
```

## 参数说明
- 输入：剧目分析的JSON结果 + 用户选择的字段
- 输出：JSON格式的精炼标签数组
- 支持的字段：
  - `dramaIntroduction` - 剧集介绍
  - `worldview` - 世界观分析
  - `logicalConsistency` - 逻辑自洽性
  - `extensibility` - 延展性分析
  - `characterTags` - 角色标签
  - `protagonistArc` - 主角弧光
  - `audienceResonance` - 受众共鸣点
  - `artStyle` - 画风分析

## 使用流程
1. 用户先进行剧目分析，获得完整的分析报告
2. 用户选择需要的分析维度（如世界观、角色标签等）
3. 系统从选定的维度中提取精炼的通用特征
4. 提取的特征用作角色生成或剧本创作的参考信息

## 触发词
- "提取剧目特征"
- "精炼分析结果"
- "提取通用标签"

---
*来源：AI-Prompts-文档.md*
*最后更新：2026-02-19*
