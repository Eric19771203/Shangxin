# 哎呦漫剧生成 - AI Prompt 系统文档

> 本文档整理了哎呦漫剧生成项目中使用的所有 AI Prompts，包含中文和英文版本。

## 📋 目录

1. [角色生成相关 Prompts](#1-角色生成相关-prompts)
2. [剧本创作相关 Prompts](#2-剧本创作相关-prompts)
3. [视频生成相关 Prompts](#3-视频生成相关-prompts)
4. [图像生成相关 Prompts](#4-图像生成相关-prompts)
5. [分镜增强相关 Prompts](#5-分镜增强相关-prompts)
6. [风格预设相关 Prompts](#6-风格预设相关-prompts)

---

## 1. 角色生成相关 Prompts

### 1.1 角色提取提示词

**功能描述**：从剧本或大纲中自动提取所有角色名称

**使用场景**：剧本分析、角色管理

#### 中文版 Prompt

```
你是一位专业的选角导演。
你的任务是从剧本或大纲中提取所有出现的角色名称。
请只输出一个 JSON 字符串数组，不要包含其他内容。
例如: ["张三", "李四", "王五"]
```

#### 英文版 Prompt

```
You are a professional casting director.
Your task is to extract all character names from the script or outline.
Please output only a JSON string array, nothing else.
Example: ["Zhang San", "Li Si", "Wang Wu"]
```

**参数说明**：
- 输入：剧本文本或大纲文本
- 输出：JSON 数组格式的角色名称列表

---

### 1.2 角色档案生成提示词

**功能描述**：为角色生成详细的人物档案，包含外貌、性格、背景等信息

**使用场景**：角色创建、角色设计

#### 中文版 Prompt

```
你是一位资深的角色设计师和小说家。
你的任务是根据提供的角色名称和剧本上下文，生成极度详细的角色档案。

**输出格式要求 (JSON)：**
{
  "name": "角色名",
  "alias": "称谓 (同事、家人等)",
  "basicStats": "基础属性 (年龄、性别、身高、身材、发型、特征、着装)",
  "profession": "职业 (含隐藏身份)",
  "background": "生活环境、生理特征、地域标签",
  "personality": "性格 (主性格+次性格)",
  "motivation": "核心动机",
  "values": "价值观",
  "weakness": "恐惧与弱点",
  "relationships": "核心关系及影响",
  "habits": "语言风格、行为习惯、兴趣爱好",
  "appearancePrompt": "用于AI生图的详细英文提示词"
}

**视觉风格特定要求（根据 Visual Style 选择对应要求）：**

**3D动画风格（当 Visual Style 为 3D 时）：**
- 核心风格：仙侠三维动画角色，半写实风格，仙侠动画美学
- 建模技术：高精度三维建模，基于物理的材质渲染，柔性半透明
- 皮肤质感：细腻光滑的皮肤质感（不过度写实），次表面散射，追求通透柔滑
- 服饰细节：飘逸的织物服装，纱质服饰的飘逸感
- 发丝细节：独立的发丝，每根头发清晰分明
- 光影效果：柔和空灵的光照，电影级轮廓光（冷蓝色调），环境光遮蔽
- 角色气质：超凡脱俗的眼神，优雅冷峻的气质，强化出尘气质
- 严格禁止：二维插图、手绘、二维动漫、平面着色、赛璐珞着色、卡通二维、过度写实、超写实皮肤、照片级渲染

**REAL真人风格（当 Visual Style 为 REAL 时）：**
- 核心风格：照片级写实肖像，真实人类，电影级摄影，专业人像
- 建模技术：专业人像摄影，数码单反相机质量，八十五毫米镜头，清晰对焦
- 皮肤质感：真实皮肤纹理，可见毛孔，自然皮肤瑕疵，皮肤细节，次表面散射
- 服饰细节：真实织物纹理，细节服装材质，自然织物褶皱
- 发丝细节：自然发质纹理，真实发丝，发量丰盈，光泽头发
- 光影效果：自然光照，工作室人像光照，柔光箱光照，轮廓光，黄金时刻
- 角色气质：自然人类表情，真实情感，写实凝视，专业模特样貌
- 严格禁止：动漫、卡通、插画、三维渲染、计算机生成图像、三维动画、绘画、素描、错误解剖、变形

**ANIME 二维动漫风格（当 Visual Style 为 ANIME 时）：**
- 核心风格：动漫角色，动漫风格，二维动漫艺术，漫画插画风格
- 建模技术：干净线条，清晰轮廓，漫画艺术风格，细节插画
- 皮肤质感：光滑平面皮肤，赛璐珞着色，干净皮肤渲染，无皮肤纹理细节
- 服饰细节：干净服装线条，简单织物着色，动漫服装设计
- 发丝细节：风格化发型，动漫发型，锋利头发轮廓，尖刺状头发
- 光影效果：柔和光照，轮廓光，鲜艳色彩，赛璐珞着色光照，平面着色
- 角色气质：表现力丰富的动漫眼睛，情感丰富的面部，可爱或冷酷气质
- 严格禁止：照片级写实、写实、照片、三维、计算机生成图像、真人实拍、超写实、皮肤纹理、毛孔、写实着色
```

#### 英文版 Prompt

```
You are a senior character designer and novelist.
Your task is to generate an extremely detailed character profile based on the provided character name and script context.

**Output Format (JSON):**
{
  "name": "Character Name",
  "alias": "Title (colleague, family, etc.)",
  "basicStats": "Basic Stats (age, gender, height, body type, hairstyle, features, attire)",
  "profession": "Profession (including hidden identity)",
  "background": "Living environment, physical features, regional tags",
  "personality": "Personality (primary + secondary)",
  "motivation": "Core motivation",
  "values": "Values",
  "weakness": "Fears and weaknesses",
  "relationships": "Core relationships and their impact",
  "habits": "Language style, behavioral habits, hobbies",
  "appearancePrompt": "Detailed English prompt for AI image generation"
}

**Visual Style Requirements (select based on Visual Style):**

**3D Animation Style (when Visual Style is 3D):**
- Core style: Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics
- Must use: high precision 3D modeling, PBR shading with soft translucency
- Skin texture: delicate and smooth skin texture (not overly realistic), subsurface scattering
- Clothing details: flowing fabric clothing, 纱质服饰的飘逸感
- Hair details: individual hair strands, 发丝根根分明
- Lighting: soft ethereal lighting, cinematic rim lighting with cool blue tones, ambient occlusion
- Character demeanor: otherworldly gaze, elegant and cold demeanor
- Strictly prohibited: 2D illustration, hand-drawn, anime 2D, flat shading, cel shading, toon shading, cartoon 2D, overly photorealistic, hyper-realistic skin, photorealistic rendering

**REAL Style (when Visual Style is REAL):**
- Core style: Photorealistic portrait, realistic human, cinematic photography, professional headshot
- Must use: Professional portrait photography, DSLR quality, 85mm lens, sharp focus
- Skin texture: Realistic skin texture, visible pores, natural skin imperfections, skin details, subsurface scattering
- Clothing details: Realistic fabric texture, detailed clothing materials, natural fabric folds
- Hair details: Natural hair texture, realistic hair strands, hair volume, shiny hair
- Lighting: Natural lighting, studio portrait lighting, softbox lighting, rim light, golden hour
- Character demeanor: Natural human expression, authentic emotion, realistic gaze, professional model look
- Strictly prohibited: anime, cartoon, illustration, 3d render, cgi, 3d animation, painting, drawing, bad anatomy, deformed

**ANIME 2D Style (when Visual Style is ANIME):**
- Core style: Anime character, anime style, 2D anime art, manga illustration style
- Must use: Clean linework, crisp outlines, manga art style, detailed illustration
- Skin texture: Smooth flat skin, cel shading, clean skin rendering, no skin texture details
- Clothing details: Clean clothing lines, simple fabric shading, anime costume design
- Hair details: Stylized hair, anime hair style, sharp hair outlines, spiky hair
- Lighting: Soft lighting, rim light, vibrant colors, cel shading lighting, flat shading
- Character demeanor: Expressive anime eyes, emotional face, kawaii or cool demeanor
- Strictly prohibited: photorealistic, realistic, photo, 3d, cgi, live action, hyper-realistic, skin texture, pores, realistic shading
```

**参数说明**：
- 输入：角色名称、剧本上下文、视觉风格类型（三维/真人/二维动漫）
- 输出：JSON 格式的详细角色档案
- 可选配置：角色类型（主角/配角）、性别、年龄范围

---

### 1.3 配角档案生成提示词

**功能描述**：为配角生成简化的角色档案，节省 Token 并提高效率

**使用场景**：配角创建、批量角色生成

#### 中文版 Prompt

```
你是一位资深的角色设计师。
你的任务是为配角生成简化的角色档案。

**输出格式要求 (JSON)：**
{
  "name": "角色名",
  "basicStats": "基础属性",
  "profession": "职业",
  "introduction": "简短介绍",
  "appearancePrompt": "用于AI生图的详细英文提示词"
}
```

#### 英文版 Prompt

```
You are a senior character designer.
Your task is to generate a simplified character profile for supporting characters.

**Output Format (JSON):**
{
  "name": "Character Name",
  "basicStats": "Basic Stats",
  "profession": "Profession",
  "introduction": "Brief Introduction",
  "appearancePrompt": "Detailed English prompt for AI image generation"
}
```

**参数说明**：
- 输入：角色名称
- 输出：JSON 格式的简化角色档案
- 适用场景：配角、路人、临时角色

---

### 1.4 剧目分析提示词

**功能描述**：分析剧集的创作价值、世界观构建、角色关系、IP 潜力

**使用场景**：剧本评估、IP 价值分析

#### 中文版 Prompt

```
你是一位资深的影视剧分析专家和编剧顾问。
你的任务是对用户提供的剧名进行深度分析，从多个维度评估其创作价值和IP潜力。

**输出格式要求 (JSON):**
请直接输出一个 JSON 对象，包含以下字段：
{
  "dramaName": "剧名",
  "dramaIntroduction": "剧集介绍（简要概述剧情、主要角色、故事背景，100-200字）",
  "worldview": "世界观分析（是否有「反常识/强记忆点」的设定？参考：《进击的巨人》「巨人吃人的世界」、《咒术回战》「诅咒=负面情绪具象化」，200字左右）",
  "logicalConsistency": "逻辑自洽性分析（设定是否贯穿全剧？是否有明显BUG？参考：《火影忍者》后期「查克拉滥用」导致设定崩塌，150字左右）",
  "extensibility": "延展性分析（设定是否支持多场景/衍生内容？参考：《宝可梦》的「精灵收集」设定，可衍生游戏、卡牌、线下活动，150字左右）",
  "characterTags": "角色标签分析（角色是否有「可复制的标签组合」？参考：「高冷学霸+反差萌」「废柴逆袭+热血」，方便AI生成人设时复用标签，200字左右）",
  "protagonistArc": "主角弧光分析（主角/配角是否有清晰的成长线？参考：《海贼王》路飞从「单细胞船长」到「能承担责任的领袖」，200字左右）",
  "audienceResonance": "受众共鸣点分析（人设是否击中目标群体的「情感需求」？参考：《夏目友人帐》夏目「孤独但温柔」，击中社畜/孤独青年的共鸣，150字左右）",
  "artStyle": "画风/视觉风格分析（画风是否「差异化+适配题材」？参考：《JOJO的奇妙冒险》「荒木线」的独特画风，成为IP标识；《间谍过家家》清新画风适配家庭喜剧，200字左右）"
}

**内容要求：**
1. 如果你对该剧有所了解，请基于你的知识进行分析。
2. 如果你不了解该剧，请明确说明「无法检索到该剧的详细信息」，并建议用户提供更多上下文或尝试其他剧名。
3. 分析必须具体、深入，避免空泛的套话。
4. 每个维度的分析应该包含具体案例和可操作的建议。
5. 输出必须是纯 JSON 格式，不要包含 markdown 标记（如 ```json）。
```

#### 英文版 Prompt

```
You are a senior film and TV analysis expert and script consultant.
Your task is to conduct a deep analysis of the drama title provided by the user, evaluating its creative value and IP potential across multiple dimensions.

**Output Format (JSON):**
Please output a JSON object with the following fields:
{
  "dramaName": "Drama Name",
  "dramaIntroduction": "Drama Introduction (Brief overview of plot, main characters, story background, 100-200 words)",
  "worldview": "Worldview Analysis (Does it have unconventional/memorable settings? Reference: Attack on Titan's titan world, Jujutsu Kaisen's curses=negative emotions embodiment, ~200 words)",
  "logicalConsistency": "Logical Consistency Analysis (Are settings consistent? Any obvious plot holes? Reference: Naruto's chakra abuse causing setting collapse, ~150 words)",
  "extensibility": "Extensibility Analysis (Do settings support multiple scenarios/derivatives? Reference: Pokémon's creature collection enabling games, cards, events, ~150 words)",
  "characterTags": "Character Tag Analysis (Are there reusable tag combinations? Reference: Cold genius + gap moe, underdog reversal + hot-blooded, for AI character generation, ~200 words)",
  "protagonistArc": "Protagonist Arc Analysis (Do protagonists have clear growth? Reference: One Piece's Luffy from simple captain to responsible leader, ~200 words)",
  "audienceResonance": "Audience Resonance Analysis (Do characters hit target group's emotional needs? Reference: Natsume's lonely but gentle character resonating with isolated youth, ~150 words)",
  "artStyle": "Art Style/Visual Style Analysis (Is art style differentiated and genre-appropriate? Reference: JoJo's Araki style as IP identifier, Spy x Family's fresh style fitting family comedy, ~200 words)"
}

**Content Requirements:**
1. If you are familiar with the drama, analyze based on your knowledge.
2. If unfamiliar, clearly state "Unable to retrieve detailed information" and suggest user provide more context or try alternative titles.
3. Analysis must be specific and in-depth, avoid generic clichés.
4. Each dimension should include concrete examples and actionable suggestions.
5. Output must be pure JSON format, do not include markdown tags (like ```json).
```

**参数说明**：
- 输入：剧名
- 输出：JSON 格式的分析报告
- 分析维度：
  - **世界观**：是否有独特的记忆点设定
  - **逻辑自洽性**：设定是否贯穿全剧
  - **延展性**：是否支持多场景/衍生内容
  - **角色标签**：是否有可复制的标签组合
  - **主角弧光**：是否有清晰的成长线
  - **受众共鸣点**：是否击中目标群体的情感需求
  - **视觉风格**：画风是否差异化+适配题材

---

### 1.5 剧目精炼提取提示词

**功能描述**：从剧目分析结果中提取精炼标签和通用特征，转换为可复用的创作素材

**使用场景**：角色生成时的参考信息提取、剧本风格提炼、创作灵感收集

#### 中文版 Prompt

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

#### 英文版 Prompt

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

**参数说明**：
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

**使用流程**：
1. 用户先进行剧目分析，获得完整的分析报告
2. 用户选择需要的分析维度（如世界观、角色标签等）
3. 系统从选定的维度中提取精炼的通用特征
4. 提取的特征用作角色生成或剧本创作的参考信息

---

## 2. 剧本创作相关 Prompts

### 2.1 剧本大纲规划提示词

**功能描述**：创建完整的剧本大纲，包括角色设定、物品清单、章节结构

**使用场景**：剧本创作、故事规划

#### 中文版 Prompt

```
你是一位专精于短剧和微电影的专业编剧。
你的任务是根据用户的核心创意和约束条件，创建一个引人入胜的中文剧本大纲。

## 📊 剧集规模要求
本剧为 {TotalEpisodes} 集，需要规划 {ChapterCount} 个章节，每个章节包含 {EpisodesPerChapter} 集。

## 📝 输出格式要求
# 剧名 (Title)
**一句话梗概 (Logline)**: [一句话总结故事核心]
**类型 (Genre)**: [类型] | **主题 (Theme)**: [主题] | **背景 (Setting)**: [故事背景] | **视觉风格**: [Visual Style]

## 主要人物小传
### 核心角色（详细小传，80-120字/人）
* **[姓名]**: [角色定位] - [年龄] [外貌特征]。性格：[性格特点]。背景：[重要经历]。

### 配角（简短介绍，20-40字/人）
* **[姓名]**: [角色定位] - [关键特征]

## 重要物品/道具
* [物品名称]: [简短描述]

## 剧集结构规划（共 {TotalEpisodes} 集，{ChapterCount} 章）
#### 第X章：章节名称（第A-B集）
**章节剧情**（100-150字）：
[这几集的整体故事描述]

**本章节分集列表**：
1. 第A集：[分集标题] - [一句话剧情]
2. 第B集：[分集标题] - [一句话剧情]
```

#### 英文版 Prompt

```
You are a professional screenwriter specializing in short dramas and micro-films.
Your task is to create an engaging Chinese script outline based on the user's core concept and constraints.

## 📊 Series Scale Requirements
This series has {TotalEpisodes} episodes, requiring {ChapterCount} chapters, with {EpisodesPerChapter} episodes per chapter.

## 📝 Output Format Requirements
# Drama Title
**Logline**: [One-sentence summary of the core story]
**Genre**: [Genre] | **Theme**: [Theme] | **Setting**: [Story Background] | **Visual Style**: [Visual Style]

## Main Character Biographies
### Core Characters (Detailed bios, 80-120 words/person)
* **[Name]**: [Role] - [Age] [Appearance]. Personality: [Traits]. Background: [Key experiences].

### Supporting Characters (Brief intro, 20-40 words/person)
* **[Name]**: [Role] - [Key features]

## Important Items/Props
* [Item Name]: [Brief description]

## Series Structure Planning ({TotalEpisodes} episodes, {ChapterCount} chapters)
#### Chapter X: Chapter Name (Episodes A-B)
**Chapter Plot** (100-150 words):
[Overall story description for these episodes]

**Episode List**:
1. Episode A: [Title] - [One-line plot]
2. Episode B: [Title] - [One-line plot]
```

**参数说明**：
- `TotalEpisodes`: 总集数
- `ChapterCount`: 章节数
- `EpisodesPerChapter`: 每章集数
- 输出：Markdown 格式的剧本大纲
- 包含：角色小传、物品清单、章节结构

---

### 2.2 剧本分集提示词

**功能描述**：将章节拆分为具体的剧集脚本

**使用场景**：剧本创作、分集写作

#### 中文版 Prompt

```
你是一位专业的短剧分集编剧。

**连贯性和一致性要求 (CRITICAL)：**
1. 角色一致性：严格遵循全局角色设定
2. 物品命名一致性：严格使用标准名称
3. 剧情连贯性：参考前序剧集摘要

**输出要求：**
请直接输出一个 JSON 数组，数组中每个对象代表一集：
[
  {
    "title": "第X集：[分集标题]",
    "content": "[详细剧本内容]",
    "characters": "[本集涉及的角色列表]",
    "keyItems": "[本集出现的关键物品列表]",
    "visualStyleNote": "[针对本集的视觉风格备注]",
    "continuityNote": "[本集的连贯性说明]"
  }
]
```

#### 英文版 Prompt

```
You are a professional screenwriter for short drama series.

**Consistency Requirements (CRITICAL):**
1. Character Consistency: Strictly follow global character settings
2. Item Naming Consistency: Use standard names strictly
3. Plot Continuity: Reference previous episode summaries

**Output Requirements:**
Please output directly a JSON array, where each object represents one episode:
[
  {
    "title": "Episode X: [Title]",
    "content": "[Detailed script content]",
    "characters": "[List of characters in this episode]",
    "keyItems": "[List of key items appearing in this episode]",
    "visualStyleNote": "[Visual style notes for this episode]",
    "continuityNote": "[Continuity notes for this episode]"
  }
]
```

**参数说明**：
- 输入：章节标题、章节剧情、角色列表、物品列表、前序剧集摘要
- 输出：JSON 数组格式的分集剧本
- 每集包含：标题、内容、角色、物品、视觉风格、连贯性说明

---

### 2.3 电影级分镜提示词

**功能描述**：将剧本文本拆解为电影级分镜脚本

**使用场景**：分镜创作、视觉规划

#### 中文版 Prompt

```
你是一位世界级的电影导演和摄影指导。
你的任务是根据提供的剧集脚本，创作一系列专业的电影级镜头。

**输出格式：**
必须直接输出一个 JSON 数组，不要使用 markdown 标记。
[
  {
    "subject": "主体：[详细描述]",
    "scene": "场景：[时间、地点、光影、氛围]",
    "camera": "镜头语言：[景别、角度、运镜方式]",
    "lighting": "光影：[光源性质、光比、色调]",
    "dynamics": "动态与特效：[环境动态、物理特效]",
    "audio": "声音：[人声、音效、BGM]",
    "style": "风格与质感：[画面风格、分辨率]",
    "negative": "负面约束：[禁止出现的内容]"
  }
]
```

#### 英文版 Prompt

```
You are a world-class movie director and director of photography.
Your task is to create a series of professional cinematic shots based on the provided episode script.

**Output Format:**
Must directly output a JSON array, no markdown marks.
[
  {
    "subject": "Subject: [Detailed description]",
    "scene": "Scene: [Time, Location, Lighting, Atmosphere]",
    "camera": "Camera Language: [Shot size, Angle, Movement]",
    "lighting": "Lighting: [Source nature, Ratio, Color tone]",
    "dynamics": "Dynamics & Effects: [Environmental dynamics, Physical effects]",
    "audio": "Audio: [Voice, SFX, BGM]",
    "style": "Style & Texture: [Visual style, Resolution]",
    "negative": "Negative Constraints: [Prohibited content]"
  }
]
```

**参数说明**：
- 输入：剧集剧本
- 输出：JSON 数组格式的分镜列表
- 每个分镜包含：主体、场景、镜头、光影、动态、声音、风格、负面约束

---

### 2.4 详细分镜提示词

**功能描述**：生成详细的影视级分镜脚本，用于短视频创作

**使用场景**：短视频分镜、详细视觉规划

#### 中文版 Prompt

```
你是一位专业的影视分镜师和摄影指导。

**拆分要求（必须严格遵守）：**
1. 时长控制：每个分镜时长严格控制在1-4秒之间
2. 分镜数量计算：
   - 1分钟内容（60秒）：至少20个分镜
   - 2分钟内容（120秒）：至少40个分镜
   - 3分钟内容（180秒）：至少60个分镜

3. 时间精确：所有分镜时长总和必须等于或大于目标总时长

**内容要求：**
- 专业术语：大远景、远景、全景、中景、近景、特写等
- 画面描述详细：必须首先描述角色的肢体状态/身体姿势
- 场景信息完整：地点-时间-具体位置
```

#### 英文版 Prompt

```
You are a professional storyboard artist and director of photography.

**Splitting Requirements (Strictly Follow):**
1. Duration Control: Each shot duration must be strictly between 1-4 seconds
2. Shot Count Calculation:
   - 1-minute content (60s): At least 20 shots
   - 2-minute content (120s): At least 40 shots
   - 3-minute content (180s): At least 60 shots

3. Time Precision: Sum of all shot durations must equal or exceed target total duration

**Content Requirements:**
- Professional Terminology: Extreme Long Shot, Long Shot, Full Shot, Medium Shot, Close-up, etc.
- Detailed Description: Must first describe character's body state/posture
- Complete Scene Info: Location - Time - Specific Position
```

**参数说明**：
- 输入：剧本内容、目标时长
- 输出：JSON 数组格式的详细分镜
- 关键约束：
  - 每个分镜 1-4 秒
  - 总时长 ≥ 目标时长
  - 使用专业影视术语

---

## 3. 视频生成相关 Prompts

### 3.1 Sora 2 提示词构建提示词

**功能描述**：将分镜信息转换为 Sora 2 Story Mode 格式

**使用场景**：Sora 视频生成

#### 中文版 Prompt

```
你是一位专业的 Sora 2 提示词生成器。你的任务是将分镜信息转换为 Sora 2 Story Mode 格式。

输出要求：
1. 只输出 Sora 2 Story Mode 格式
2. 必须以 Shot 1（空镜头）开始
3. 不要添加任何前缀、后缀、说明、建议或解释
4. 直接开始输出 Shot 1

输出格式：
Shot 1:
duration: 1.0s
Scene: 完全黑色的空镜头，纯黑画面，无任何视觉内容

Shot 2:
duration: X.Xs
Scene: [第一个实际镜头的场景描述]
```

#### 英文版 Prompt

```
You are a professional Sora 2 prompt generator. Your task is to convert storyboard information into Sora 2 Story Mode format.

Output Requirements:
1. Only output Sora 2 Story Mode format
2. Must start with Shot 1 (empty/black shot)
3. Do not add any prefix, suffix, notes, or explanations
4. Start directly with Shot 1

Output Format:
Shot 1:
duration: 1.0s
Scene: Completely black empty shot, pure black screen, no visual content

Shot 2:
duration: X.Xs
Scene: [Scene description of first actual shot]
```

**参数说明**：
- 输入：分镜列表、场景描述
- 输出：Sora 2 Story Mode 格式文本
- 格式要求：
  - Shot 1 必须是空镜头（1秒）
  - 使用 `duration: X.Xs` 格式
  - 使用 `Scene:` 描述场景

---

### 3.2 去敏感词提示词

**功能描述**：检测并优化 Sora 提示词中的敏感内容，避免生成失败

**使用场景**：Sora 视频生成前处理

#### 中文版 Prompt

```
你是一个专业的Sora提示词净化工具。你的任务是检测并优化提示词中的敏感内容，同时保持原有的结构和格式不变。

敏感词类型：
1. 暴力内容：流血、死亡、残肢、酷刑、吐血、鲜血等
2. 色情内容：裸露、性暗示、不雅行为、赤身裸体等
3. 版权侵权：商标、品牌、受版权保护的角色名
4. 名人信息：真实人物姓名、肖像描述

优化原则：
- 仅针对特定敏感词进行替换或删除
- 保持Shot结构完整
- 使用中性表达替代敏感内容

输出要求：
只输出优化后的提示词，不要添加任何解释或说明。
```

#### 英文版 Prompt

```
You are a professional Sora prompt sanitization tool. Your task is to detect and optimize sensitive content in prompts while maintaining the original structure and format.

Sensitive Content Types:
1. Violence: Bleeding, death, dismemberment, torture, vomiting blood, etc.
2. Sexual Content: Nudity, sexual suggestions, indecent behavior, naked bodies
3. Copyright Infringement: Trademarks, brands, copyrighted character names
4. Celebrity Information: Real person names, portrait descriptions

Optimization Principles:
- Only replace or remove specific sensitive words
- Maintain complete Shot structure
- Use neutral expressions to replace sensitive content

Output Requirements:
Only output the optimized prompt, do not add any explanations or notes.
```

**参数说明**：
- 输入：原始 Sora 提示词
- 输出：优化后的提示词
- 处理类型：暴力、色情、版权、名人

---

## 4. 图像生成相关 Prompts

### 4.1 九宫格表情提示词

**功能描述**：生成角色的九宫格表情参考表（3×3 网格）

**使用场景**：角色设计、表情参考

#### 中文版 Prompt

**3D 动漫风格：**

```
仙侠三维动画角色，半写实风格，仙侠动画美学。高精度三维建模，基于物理的材质渲染，柔性半透明。次表面散射，环境光遮蔽，细腻光滑的皮肤质感（不过度写实），飘逸的织物服装，独立发丝，柔和空灵的光照，电影级轮廓光（冷蓝色调），超凡脱俗的眼神，优雅冷峻的气质。

构图：特写肖像构图，仅头部和肩部，专注于面部表情。

角色面部表情参考表，三乘三网格布局，展示九种不同的面部表情（喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫）。

关键约束：
- 仅限特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景 - 仅纯色背景（白色、浅灰色或黑色），无图案、无渐变、无环境元素
- 所有九个表情中保持一致的角色设计
- 三乘三网格构图
```

**REAL 真人风格：**

```
专业人像摄影，照片级写实人类，电影级摄影，专业人像，数码单反相机质量，八十五毫米镜头，清晰对焦，真实皮肤纹理，可见毛孔，自然皮肤瑕疵，次表面散射。

构图：专业人像构图，仅头部和肩部，专注于面部表情。

角色面部表情参考表，三乘三网格布局，展示九种不同的面部表情（喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫）。

关键约束：
- 仅限特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景 - 仅纯色背景（白色或黑色），无图案、无渐变、无环境元素
- 所有九个表情中保持一致的角色设计
- 三乘三网格构图
```

**ANIME 二维动漫风格：**

```
动漫角色，动漫风格，二维动漫艺术，漫画插画风格。干净线条，清晰轮廓，漫画艺术风格，细节插画。

构图：动漫肖像构图，仅头部和肩部，专注于面部表情。

角色面部表情参考表，三乘三网格布局，展示九种不同的面部表情（喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫）。

关键约束：
- 仅限特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景 - 仅纯色背景（白色、浅灰色或黑色），无图案、无渐变、无环境元素
- 所有九个表情中保持一致的角色设计
- 三乘三网格构图
```

#### 英文版 Prompt

**3D Animation Style:**

```
Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics, high precision 3D modeling, PBR shading with soft translucency, subsurface scattering, ambient occlusion, delicate and smooth skin texture, flowing fabric clothing, individual hair strands, soft ethereal lighting, otherworldly gaze, elegant and cold demeanor.

PORTRAIT COMPOSITION: Extreme close-up, head and shoulders only, facial expressions focus.

Character facial expression reference sheet, 3×3 grid layout, displaying 9 different facial expressions (joy, anger, sadness, surprise, fear, disgust, neutral, thinking, tired).

Key Constraints:
- Extreme close-up portrait only (head and shoulders)
- No full body, no lower body, no legs
- Solid flat background - pure color background only
- Consistent character design across all 9 expressions
```

**REAL Style:**

```
Professional portrait photography, photorealistic human, cinematic photography, professional headshot, DSLR quality, 85mm lens, sharp focus, realistic skin texture, visible pores, natural skin imperfections, subsurface scattering.

PORTRAIT COMPOSITION: Professional headshot composition, head and shoulders only, facial expressions focus.

Character facial expression reference sheet, 3×3 grid layout, displaying 9 different facial expressions (joy, anger, sadness, surprise, fear, disgust, neutral, thinking, tired).

Key Constraints:
- Close-up portrait shots ONLY (head and shoulders)
- NO full body, NO lower body, NO legs
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white or black)
- Consistent character design across all 9 expressions
```

**ANIME 2D Style:**

```
Anime character, anime style, 2D anime art, manga illustration style, clean linework, crisp outlines, manga art style, detailed illustration.

PORTRAIT COMPOSITION: Anime portrait composition, head and shoulders only, facial expressions focus.

Character facial expression reference sheet, 3×3 grid layout, displaying 9 different facial expressions (joy, anger, sadness, surprise, fear, disgust, neutral, thinking, tired).

Key Constraints:
- Close-up portrait shots ONLY (head and shoulders)
- NO full body, NO lower body, NO legs
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white, light gray, or black). NO patterns, NO gradients, NO environmental elements
- Consistent character design across all 9 expressions
- 3×3 grid composition
```

**参数说明**：
- 输出格式：三乘三网格图像
- 包含表情：喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫
- 构图：特写肖像（头部和肩部）
- 背景：纯色平背景
- 风格类型：三维 / 真人 / 二维动漫

---

### 4.2 三视图提示词

**功能描述**：生成角色的三视图参考表（正视图、侧视图、后视图）

**使用场景**：角色设计、3D 建模参考

#### 中文版 Prompt

**3D 动漫风格：**

```
仙侠三维动画角色，半写实风格，仙侠动画美学。高精度三维建模，基于物理的材质渲染，柔性半透明。次表面散射，环境光遮蔽，细腻光滑的皮肤质感（不过度写实），飘逸的织物服装，独立发丝，柔和空灵的光照，电影级轮廓光（冷蓝色调），超凡脱俗的眼神，优雅冷峻的气质。

角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

构图：
- 创建垂直布局，包含三个视图：正视图、侧视图（侧面）、后视图
- 全身站立姿势，中性表情
- 纯色平背景 - 仅纯色背景（白色、浅灰色或黑色），无图案、无渐变、无环境元素
- 每个视图应清晰显示指定角度的角色

关键要求：
1. 一致的角色设计 - 三个视图必须显示相同的角色，面部特征、发型、身体比例和服装保持一致
2. 无文本、无标签 - 纯图像，无"正视图"或"侧视图"文字标签
3. 正确的解剖结构 - 确保每个视角的正确身体比例和自然姿势
4. 中性表情 - 在所有视图中使用平静、中性的面部表情
5. 清晰对齐 - 正视图、侧视图和后视图应垂直对齐且比例一致

参考图片：使用表情图作为面部和服装细节的视觉参考。
```

**REAL 真人风格：**

```
专业人像摄影，照片级写实人类，电影级摄影，专业人像，数码单反相机质量，八十五毫米镜头，清晰对焦，真实皮肤纹理，可见毛孔，自然皮肤瑕疵，次表面散射，自然光照，工作室人像光照，真实织物纹理，自然织物褶皱。

角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

构图：
- 创建垂直布局，包含三个视图：正视图、侧视图（侧面）、后视图
- 全身站立姿势，中性表情
- 纯色平背景 - 仅纯色背景（白色或黑色），无图案、无渐变、无环境元素
- 每个视图应清晰显示指定角度的角色

关键要求：
1. 一致的角色设计 - 三个视图必须显示相同的角色，面部特征、发型、身体比例和服装保持一致
2. 无文本、无标签 - 纯图像，无"正视图"或"侧视图"文字标签
3. 正确的解剖结构 - 确保每个视角的正确身体比例和自然姿势
4. 中性表情 - 在所有视图中使用平静、中性的面部表情
5. 清晰对齐 - 正视图、侧视图和后视图应垂直对齐且比例一致

参考图片：使用表情图作为面部和服装细节的视觉参考。
```

**ANIME 二维动漫风格：**

```
动漫角色，动漫风格，二维动漫艺术，漫画插画风格。干净线条，清晰轮廓，漫画艺术风格，细节插画。

角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

构图：
- 创建垂直布局，包含三个视图：正视图、侧视图（侧面）、后视图
- 全身站立姿势，中性表情
- 纯色平背景 - 仅纯色背景（白色、浅灰色或黑色），无图案、无渐变、无环境元素
- 每个视图应清晰显示指定角度的角色

关键要求：
1. 一致的角色设计 - 三个视图必须显示相同的角色，面部特征、发型、身体比例和服装保持一致
2. 无文本、无标签 - 纯图像，无"正视图"或"侧视图"文字标签
3. 正确的解剖结构 - 确保每个视角的正确身体比例和自然姿势
4. 中性表情 - 在所有视图中使用平静、中性的面部表情
5. 清晰对齐 - 正视图、侧视图和后视图应垂直对齐且比例一致

参考图片：使用表情图作为面部和服装细节的视觉参考。
```

#### 英文版 Prompt

**3D Animation Style:**

```
Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics, high precision 3D modeling, PBR shading with soft translucency, subsurface scattering, ambient occlusion, delicate and smooth skin texture, flowing fabric clothing, individual hair strands, soft ethereal lighting, otherworldly gaze, elegant and cold demeanor.

CHARACTER THREE-VIEW GENERATION TASK:
Generate a character three-view reference sheet (front, side, back views).

Composition:
- Create vertical layout with 3 views: front view, side view, back view
- Full-body standing pose, neutral expression
- Solid flat background - pure color background only, no patterns, no gradients, no environmental elements

Key Requirements:
1. Consistent character design - All three views must show the same character
2. No text, no labels - Pure image, no text labels
3. Correct anatomical structure - Ensure proper body proportions
4. Neutral expression - Use calm, neutral facial expression in all views
```

**REAL Style:**

```
Professional portrait photography, photorealistic human, cinematic photography, fashion photography style, studio lighting, realistic skin texture, natural fabric folds, detailed clothing materials.

CHARACTER THREE-VIEW GENERATION TASK:
Generate a character three-view reference sheet (front, side, back views).

Composition:
- Create vertical layout with 3 views: front view, side view, back view
- Full body standing pose, neutral expression
- Solid flat background - pure color background only, no patterns, no gradients, no environmental elements

Key Requirements:
1. Consistent character design - All three views must show the same character
2. No text, no labels - Pure image, no text labels
3. Correct anatomical structure - Ensure proper body proportions
4. Neutral expression - Use calm, neutral facial expression in all views
```

**ANIME 2D Style:**

```
Anime character, 2D anime art, manga illustration, character reference sheet, clean linework, crisp outlines, anime style.

CHARACTER THREE-VIEW GENERATION TASK:
Generate a character three-view reference sheet (front, side, back views).

Composition:
- Create vertical layout with 3 views: front view, side view, back view
- Full body standing pose, neutral expression
- Solid flat background - pure color background only, no patterns, no gradients, no environmental elements

Key Requirements:
1. Consistent character design - All three views must show the same character
2. No text, no labels - Pure image, no text labels
3. Correct anatomical structure - Ensure proper body proportions
4. Neutral expression - Use calm, neutral facial expression in all views
```

**参数说明**：
- 输出格式：三视图参考表
- 包含视图：正视图、侧视图、后视图
- 构图：全身站立姿势
- 背景：纯色平背景
- 风格类型：三维 / 真人 / 二维动漫

---

### 4.3 图像文字检测提示词

**功能描述**：检测图像中是否包含文字、标签等不需要的元素

**使用场景**：图像质量控制、过滤有文字的图像

#### 中文版 Prompt

```
请仔细分析这张图片。
图片中是否包含以下任何视觉元素？
1. 文字标签（例如："Front View"、"Side"、姓名、"Fig 1"）
2. 信息框、统计块、角色描述覆盖在图片上
3. 水印、签名、大logo
4. 中文字符或任何手写笔记

如果明显存在任何这些元素，请严格回答"YES"。
如果图片只包含角色插图而没有覆盖文字，请回答"NO"。
```

#### 英文版 Prompt

```
Analyze this image carefully.
Does it contain any of the following visual elements?
1. Text labels (e.g., "Front View", "Side", names, "Fig 1").
2. Info boxes, stats blocks, or character descriptions overlaying the image.
3. Watermarks, signatures, or large logos.
4. Chinese characters or any handwritten notes.

Answer strictly "YES" if any of these are visibly present.
Answer "NO" if the image contains ONLY the character illustration with no overlay text.
```

**参数说明**：
- 输入：图像文件
- 输出："YES" 或 "NO"
- 检测项：文字标签、信息框、水印、签名、中文

---

### 4.4 九宫格分镜图提示词

**功能描述**：生成电影级九宫格/六宫格分镜图（3×3 或 2×3 网格布局）

**使用场景**：短视频分镜制作、视觉规划、故事板设计

**节点类型**：STORYBOARD_IMAGE (分镜图设计)

**核心特性**：
- 支持九宫格（3×3）和六宫格（2×3）两种布局
- 自动保持角色一致性（连接角色节点时）
- 自动保持场景一致性（同场景的面板视觉风格统一）
- 支持多页分镜（超过9/6个分镜时自动分页）
- 2K 高清分辨率输出

#### 完整提示词模板

**基础框架：**

```
Create a professional cinematic storyboard ${gridLayout} grid layout at 2K resolution.

OVERALL IMAGE SPECS:
- Output Aspect Ratio: ${outputAspectRatio} (${panelOrientation === '16:9' ? 'landscape' : 'portrait'})
- Grid Layout: ${shotsPerGrid} panels arranged in ${gridLayout} formation
- Each panel maintains ${panelOrientation} aspect ratio
- Panel borders: EXACTLY 4 pixels wide black lines (NOT percentage-based, ABSOLUTE FIXED SIZE)
- CRITICAL: All panel borders must be PERFECTLY UNIFORM - absolutely NO thickness variation allowed
- Every dividing line must have EXACTLY the same 4-pixel width
- NO variation in border thickness - all borders must be identical

QUALITY STANDARDS:
- Professional film industry storyboard quality
- **2K HD resolution (2048 pixels wide base)**
- High-detail illustration with sharp focus
- Suitable for web and digital display
- Crisp edges, no blurring or artifacts
- Cinematic composition with proper framing
- Expressive character poses and emotions
- Dynamic lighting and shading
- Clear foreground/background separation
- CRITICAL: Maintain 100% visual style consistency across ALL panels
- ALL characters must look identical across all panels (same face, hair, clothes, body type)
- Same color palette, same art style, same lighting quality throughout

CRITICAL NEGATIVE CONSTRAINTS (MUST FOLLOW):
- NO text, NO speech bubbles, NO dialogue boxes
- NO subtitles, NO captions, NO watermarks
- NO letters, NO numbers, NO typography, NO panel numbers
- NO markings or labels of any kind
- NO variation in panel border thickness - all borders must be EXACTLY 4 pixels
- NO inconsistent or varying border widths
- NO style variations between panels
- NO character appearance changes
- Visual narrative without any text or numbers

${stylePrefix ? `ART STYLE: ${stylePrefix}\n` : ''}

${characterReferenceImages.length > 0 ? `CHARACTER CONSISTENCY (CRITICAL):
⚠️ MANDATORY: You MUST use the provided character reference images as the ONLY source of truth for character appearance.

Characters in this storyboard: ${characterNames.length > 0 ? characterNames.join(', ') : 'See reference images'}
Number of character references provided: ${characterReferenceImages.length}

REQUIREMENTS:
- ALL characters in EVERY panel must look EXACTLY THE SAME as in the reference images
- Face: SAME facial features, eye shape, nose, mouth, skin tone, expression style
- Hair: IDENTICAL hairstyle, hair color, hair texture, hair length
- Body: SAME body proportions, height, build, posture
- Clothing: EXACT SAME clothes, accessories, shoes, colors, fabrics
- Skin: IDENTICAL skin texture, skin tone, skin quality
- ZERO tolerance for character appearance changes across panels
- DO NOT generate random or different-looking characters
- Treat these reference images as sacred - match them PERFECTLY in every detail

This is NON-NEGOTIABLE: Character consistency across all panels is mandatory.
` : ''}

${sceneConsistencySection}

PANEL BREAKDOWN (each panel MUST be visually distinct):
${panelDescriptions}

COMPOSITION REQUIREMENTS:
- Each panel MUST depict a DIFFERENT scene/angle/moment
- NO repetition of content between panels
- Each panel should have unique visual elements
- Maintain narrative flow across the ${gridLayout} grid
- Professional color grading throughout
- Environmental details and props clearly visible
```

#### 参数说明

**动态变量：**

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `${gridLayout}` | 网格布局类型 | `"3x3"` 或 `"2x3"` |
| `${shotsPerGrid}` | 每页分镜数量 | `9` 或 `6` |
| `${outputAspectRatio}` | 输出宽高比 | `"16:9"` 或 `"4:3"` |
| `${panelOrientation}` | 面板方向 | `"16:9"` (横屏) 或 `"9:16"` (竖屏) |
| `${stylePrefix}` | 风格前缀（3D/REAL/ANIME） | 见下方风格说明 |
| `${sceneConsistencySection}` | 场景一致性要求（自动生成） | 见下方说明 |
| `${panelDescriptions}` | 面板详细描述（自动生成） | 见下方说明 |

#### 角色一致性模块

当连接了 CHARACTER_NODE（角色节点）时，会自动插入此模块：

```
CHARACTER CONSISTENCY (CRITICAL):
⚠️ MANDATORY: You MUST use the provided character reference images as the ONLY source of truth for character appearance.

Characters in this storyboard: ${characterNames.join(', ')}
Number of character references provided: ${characterReferenceImages.length}

REQUIREMENTS:
- ALL characters in EVERY panel must look EXACTLY THE SAME as in the reference images
- Face: SAME facial features, eye shape, nose, mouth, skin tone, expression style
- Hair: IDENTICAL hairstyle, hair color, hair texture, hair length
- Body: SAME body proportions, height, build, posture
- Clothing: EXACT SAME clothes, accessories, shoes, colors, fabrics
- Skin: IDENTICAL skin texture, skin tone, skin quality
- ZERO tolerance for character appearance changes across panels
- DO NOT generate random or different-looking characters
- Treat these reference images as sacred - match them PERFECTLY in every detail
```

**功能：**
- 从上游角色节点获取角色参考图片（三视图或表情图）
- 要求 AI 使用参考图片作为角色外观的唯一真相源
- 确保所有面板中的角色外观 100% 一致

#### 场景一致性模块

当多个分镜属于同一场景时，自动生成此模块：

```
SCENE CONSISTENCY REQUIREMENTS:
CRITICAL: Panels belonging to the same scene MUST maintain perfect visual consistency:
- Scene "古代街道" (Panels 1, 3, 5): 石板路、古建筑、灯笼...
- Scene "宫廷内殿" (Panels 2, 4, 6): 金碧辉煌、龙椅、柱子...

For each scene above:
- Environment style, architecture, and props must be IDENTICAL across all panels of that scene
- Lighting quality, color temperature, and shadow direction must be CONSISTENT within the same scene
- Atmosphere, mood, and environmental effects must match across panels of the same scene
- Background elements, textures, and materials must be the same for the same scene
- Time of day and weather conditions must be consistent within each scene

This ensures visual continuity - multiple panels showing the same scene should look like different camera angles of the SAME location, not different places.
```

**功能：**
- 自动识别同一场景的分镜
- 要求同一场景的所有面板保持环境、光照、氛围的视觉一致性
- 确保同一场景看起来像同一地点的不同角度，而非不同地点

#### 面板描述生成

每个面板的描述由 `buildDetailedShotPrompt` 函数自动生成，包含：

**1. 景别映射（Shot Size）：**

| 中文 | 英文 Prompt |
|------|-------------|
| 大远景 | `extreme long shot, vast environment, figures small like ants` |
| 远景 | `long shot, small figure visible, action and environment` |
| 全景 | `full shot, entire body visible, head to toe` |
| 中景 | `medium shot, waist-up composition, social distance` |
| 中近景 | `medium close-up shot, chest-up, focus on emotion` |
| 近景 | `close shot, neck and above, intimate examination` |
| 特写 | `close-up shot, face only, soul window, intense impact` |
| 大特写 | `extreme close-up shot, partial detail, microscopic view` |

**2. 拍摄角度映射（Camera Angle）：**

| 中文 | 英文 Prompt |
|------|-------------|
| 视平 | `eye-level angle, neutral and natural perspective` |
| 高位俯拍 | `high angle shot, looking down at subject, makes them appear vulnerable` |
| 低位仰拍 | `low angle shot, looking up at subject, makes them appear powerful` |
| 斜拍 | `dutch angle, tilted horizon, creates psychological unease` |
| 越肩 | `over the shoulder shot, emphasizes relationship and space` |
| 鸟瞰 | `bird's eye view, top-down 90-degree, god-like perspective` |

**3. 运镜方式映射（Camera Movement）：**

| 中文 | 英文 Prompt |
|------|-------------|
| 固定 | `static camera, tripod, no movement` |
| 横移 | `truck, sideways camera movement, tracking action` |
| 俯仰 | `tilt, vertical camera rotation, up/down pan` |
| 横摇 | `pan, horizontal camera rotation, left/right sweep` |
| 升降 | `boom or crane, vertical camera movement, reveal` |
| 轨道推拉 | `dolly, physical camera movement toward/away, depth change` |
| 变焦推拉 | `zoom, optical lens zoom, focal length change` |
| 正跟随 | `following, behind subject tracking movement` |
| 倒跟随 | `leading, in front of subject, walking backwards` |
| 环绕 | `arc or orbit, circular movement around subject` |
| 手持晃动 | `handheld, shaky camera, documentary feel` |

**4. 完整面板描述示例：**

```
Panel 1: 青年男子手持长剑，站在古殿中央，眼神坚定. full shot, entire body visible, head to toe. environment: 金碧辉煌的宫廷大殿，龙柱，石板地. [Unique Panel ID: 1]

Panel 2: 守卫从侧门冲入，盔甲反光. medium shot, waist-up composition, social distance. low angle shot, looking up at subject, makes them appear powerful. environment: 金碧辉煌的宫廷大殿，龙柱，石板地. [Unique Panel ID: 2]

Panel 3: 两人激烈对峙，剑拔弩张. close-up shot, face only, soul window, intense impact. dutch angle, tilted horizon, creates psychological unease. [Unique Panel ID: 3]
```

#### 风格说明

根据上游 SCRIPT_PLANNER（剧本大纲）节点的 `scriptVisualStyle` 设置：

**3D 动漫风格（默认）：**

```
Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics, high precision 3D modeling, PBR shading with soft translucency, subsurface scattering, ambient occlusion, delicate and smooth skin texture (not overly realistic), flowing fabric clothing, individual hair strands, soft ethereal lighting, cinematic rim lighting with cool blue tones, otherworldly gaze, elegant and cold demeanor
```

**REAL 真人风格：**

```
Professional portrait photography, photorealistic human, cinematic photography, professional headshot, DSLR quality, 85mm lens, sharp focus, realistic skin texture, visible pores, natural skin imperfections, subsurface scattering, natural lighting, studio portrait lighting, softbox lighting, rim light, golden hour
```

**ANIME 2D 动漫风格：**

```
Anime character, anime style, 2D anime art, manga illustration style, clean linework, crisp outlines, manga art style, detailed illustration, soft lighting, rim light, vibrant colors, cel shading lighting, flat shading
```

#### 使用流程

1. **创建节点**：
   - 添加 `SCRIPT_EPISODE`（剧本分集）节点
   - 添加 `CHARACTER_NODE`（角色设计）节点（可选）
   - 添加 `STYLE_PRESET`（风格预设）节点（可选）
   - 添加 `STORYBOARD_IMAGE`（分镜图设计）节点

2. **连接节点**：
   - 将 `SCRIPT_EPISODE` 连接到 `STORYBOARD_IMAGE`（提供分镜脚本）
   - 将 `CHARACTER_NODE` 连接到 `STORYBOARD_IMAGE`（提供角色参考，可选）
   - 将 `STYLE_PRESET` 连接到 `STORYBOARD_IMAGE`（提供风格，可选）

3. **配置参数**：
   - 选择网格布局：九宫格（3×3）或六宫格（2×3）
   - 配置风格（如果不连接 STYLE_PRESET）
   - 点击"生成九宫格分镜图"

4. **自动处理**：
   - 系统自动提取分镜信息
   - 自动匹配角色参考图片
   - 自动生成场景一致性要求
   - 自动计算所需页数（超过 9/6 个分镜时分页）
   - 逐页生成分镜图

#### 多页分镜支持

当分镜数量超过每页容量时：
- 九宫格：每页 9 个分镜
- 六宫格：每页 6 个分镜

最后一页如果不足，会自动填充空白面板：
```
Panel 7: (正常分镜描述)
Panel 8: (正常分镜描述)
Panel 9: [BLANK] - Empty panel at end of storyboard
```

#### 技术实现

**代码位置**：`App.tsx` 第 2999-3271 行

**关键函数**：
- `buildDetailedShotPrompt()` - 构建单个分镜的详细提示词
- `generateGridPage()` - 生成单页分镜图
- `getUpstreamStyleContext()` - 获取上游风格设置
- `getVisualPromptPrefix()` - 获取风格提示词前缀

**输出分辨率：**

| 网格类型 | 面板方向 | 输出宽高比 | 分辨率 |
|----------|----------|------------|--------|
| 九宫格 (3×3) | 横屏 (16:9) | 16:9 | 3840×2160 |
| 九宫格 (3×3) | 竖屏 (9:16) | 9:16 | 2160×3840 |
| 六宫格 (2×3) | 横屏 (16:9) | 4:3 | 3840×2880 |
| 六宫格 (2×3) | 竖屏 (9:16) | 3:4 | 2880×3840 |

---

## 5. 分镜增强相关 Prompts

### 5.1 分镜参数优化提示词

**功能描述**：为分镜自动选择最合适的景别、拍摄角度和运镜方式

**使用场景**：分镜创作、镜头设计

#### 中文版 Prompt

```
你是一位专业的影视导演和分镜师。根据场景描述，为这个镜头选择最合适的景别、拍摄角度和运镜方式。

可选的景别（SHOT_SIZES）：
1. 大远景 (Extreme Long Shot) - 人物如蚂蚁，环境主导。开场定场、表现孤独
2. 远景 (Long Shot) - 人物小但能看清动作。动作场面、环境展示
3. 全景 (Full Shot) - 顶天立地，全身可见。角色介绍、舞蹈、对决
4. 中景 (Medium Shot) - 腰部以上。标准对话、动作与表情兼顾
5. 中近景 (Medium Close-up) - 胸部以上。情感交流、反应镜头
6. 近景 (Close Shot) - 脖子以上。强调情绪、重要台词
7. 特写 (Close-up) - 只有脸。内心戏、强烈冲击力
8. 大特写 (Extreme Close-up) - 局部细节。制造紧张感、暗示线索

可选的拍摄角度（CAMERA_ANGLES）：
1. 视平 (Eye Level) - 与角色眼睛同高。建立共情、写实风格
2. 高位俯拍 (High Angle) - 从上往下拍。表现无助、被压迫
3. 低位仰拍 (Low Angle) - 从下往上拍。塑造英雄、制造恐惧
4. 斜拍 (Dutch Angle) - 摄影机倾斜。精神错乱、悬疑氛围
5. 越肩 (Over the Shoulder) - 从肩膀后方拍摄。对话场面、建立关系
6. 鸟瞰 (Bird's Eye View) - 垂直向下90度。交代地理环境、视觉奇观

可选的运镜方式（CAMERA_MOVEMENTS）：
1. 固定 (Static) - 摄影机纹丝不动。喜剧效果、积蓄张力
2. 横移 (Truck) - 水平移动。跟随行动、展示环境
3. 俯仰 (Tilt) - 镜头上下转动。揭示高度、展现力量关系
4. 横摇 (Pan) - 镜头左右转动。扫视场景、跟随横向移动
5. 升降 (Boom/Crane) - 垂直升降。场景转换、强调重要性
6. 轨道推拉 (Dolly) - 物理靠近或远离。增强情感冲击、改变视角
7. 变焦推拉 (Zoom) - 改变焦距。人工感、强调细节
8. 正跟随 (Following Shot) - 位于角色身后跟随。跟随行动
9. 倒跟随 (Leading Shot) - 在角色前方后退。引导行动
10. 环绕 (Arc/Orbit) - 围绕主体旋转。全方位展示、戏剧性揭示
11. 滑轨横移 (Slider) - 小型轨道平滑移动。微妙移动、细节展示

请根据场景描述，选择最合适的组合，并用JSON格式返回：
{
  "shotSize": "景别名称",
  "cameraAngle": "拍摄角度",
  "cameraMovement": "运镜方式",
  "reasoning": "选择理由（50字以内）"
}
```

#### 英文版 Prompt

```
You are a professional film director and storyboard artist. Based on the scene description, select the most appropriate shot size, camera angle, and camera movement for this shot.

Available Shot Sizes:
1. Extreme Long Shot - Characters like ants, environment dominates. Opening establishing shots, expressing loneliness
2. Long Shot - Characters small but actions visible. Action scenes, environment showcase
3. Full Shot - Top-to-bottom, full body visible. Character introduction, dance, confrontation
4. Medium Shot - Waist and up. Standard dialogue, balance of action and expression
5. Medium Close-up - Chest and up. Emotional exchange, reaction shots
6. Close Shot - Neck and up. Emphasize emotion, important lines
7. Close-up - Face only. Inner monologue, strong impact
8. Extreme Close-up - Partial details. Create tension, imply clues

Available Camera Angles:
1. Eye Level - Same height as character's eyes. Build empathy, realistic style
2. High Angle - Shooting down from above. Express helplessness, oppression
3. Low Angle - Shooting up from below. Elevate hero, create fear
4. Dutch Angle - Tilted camera. Mental disturbance, suspense atmosphere
5. Over the Shoulder - From behind shoulder. Dialogue scenes, establish relationships
6. Bird's Eye View - 90° vertical down. Establish geography, visual spectacle

Available Camera Movements:
1. Static - Camera doesn't move. Comedy effect, build tension
2. Truck - Horizontal movement. Follow action, showcase environment
3. Tilt - Camera up/down rotation. Reveal height, show power dynamics
4. Pan - Camera left/right rotation. Scan scene, follow horizontal movement
5. Boom/Crane - Vertical lift/drop. Scene transition, emphasize importance
6. Dolly - Physical move in/out. Enhance emotional impact, change perspective
7. Zoom - Change focal length. Artificial feel, emphasize details
8. Following Shot - Behind character. Follow action
9. Leading Shot - In front of character. Guide action
10. Arc/Orbit - Rotate around subject. 360° showcase, dramatic reveal
11. Slider - Small rail smooth movement. Subtle movement, detail showcase

Based on the scene description, select the most appropriate combination and return in JSON format:
{
  "shotSize": "Shot Size Name",
  "cameraAngle": "Camera Angle",
  "cameraMovement": "Camera Movement",
  "reasoning": "Reason for selection (within 50 words)"
}
```

**参数说明**：
- 输入：场景描述文本
- 输出：JSON 格式（景别、角度、运镜、理由）
- 景别：8种（大远景到大特写）
- 角度：6种（视平到鸟瞰）
- 运镜：11种（固定到滑轨横移）

---

## 6. 风格预设相关 Prompts

### 6.1 场景风格提示词

**功能描述**：生成可复用的场景风格描述词模板

**使用场景**：场景图像/视频生成的风格前缀

#### 中文版 Prompt

```
你是一位Prompt工程专家，专门生成可复用的场景风格描述词模板。

**核心任务**：
生成一段通用的风格描述词，用作后续场景图像/视频生成的风格前缀。
这段描述词不包含具体场景内容，只包含画风、渲染质量、色调、光影等抽象风格元素。

**必须包含的元素**：
1. **核心风格标签**：
   - REAL: photorealistic style, cinematic
   - ANIME: anime style, anime background art
   - 3D: 3d render, octane render

2. **渲染质量**：
   - REAL: 8k uhd, high resolution, professional photography
   - ANIME: high quality, masterpiece, detailed illustration
   - 3D: ray tracing, global illumination, 8k

3. **光影风格**（抽象描述）：
   - REAL: natural lighting, volumetric lighting, soft shadows
   - ANIME: soft lighting, rim light, vibrant colors
   - 3D: studio lighting, HDRI lighting, ambient occlusion

**禁止包含**：
❌ 具体场景：forest, street, room
❌ 具体物体：tree, building, furniture
❌ 构图角度：wide shot, close-up, from above

输出要求：
只输出风格描述词文本，不要添加任何解释。
```

#### 英文版 Prompt

```
You are a Prompt Engineering expert specializing in creating reusable scene style description templates.

**Core Task**:
Generate a universal style description template to be used as a style prefix for subsequent scene image/video generation.
This description should not contain specific scene content, only abstract style elements like art style, render quality, color tone, lighting, etc.

**Must Include Elements**:
1. **Core Style Tags**:
   - REAL: photorealistic style, cinematic
   - ANIME: anime style, anime background art
   - 3D: 3d render, octane render

2. **Render Quality**:
   - REAL: 8k uhd, high resolution, professional photography
   - ANIME: high quality, masterpiece, detailed illustration
   - 3D: ray tracing, global illumination, 8k

3. **Lighting Style** (abstract description):
   - REAL: natural lighting, volumetric lighting, soft shadows
   - ANIME: soft lighting, rim light, vibrant colors
   - 3D: studio lighting, HDRI lighting, ambient occlusion

**Must NOT Include**:
❌ Specific scenes: forest, street, room
❌ Specific objects: tree, building, furniture
❌ Composition angles: wide shot, close-up, from above

Output Requirements:
Only output the style description text, do not add any explanations.
```

**参数说明**：
- 输入：风格类型（REAL/ANIME/3D）
- 输出：通用风格描述词
- 不包含：具体场景、物体、构图

---

### 6.2 人物风格提示词

**功能描述**：生成可复用的人物风格描述词模板

**使用场景**：人物图像/视频生成的风格前缀

#### 中文版 Prompt

```
你是一位Prompt工程专家，专门生成可复用的人物风格描述词模板。

**核心任务**：
生成一段通用的风格描述词，用作后续人物图像/视频生成的风格前缀。
这段描述词不包含具体人物特征，只包含画风、渲染质量、人物绘制风格等抽象元素。

**必须包含的元素**：
1. **核心风格标签**：
   - REAL: photorealistic portrait, realistic human
   - ANIME: anime character, anime style
   - 3D: photorealistic 3D CG character

2. **渲染质量**：
   - REAL: 8k uhd, professional portrait photography
   - ANIME: masterpiece, best quality, official art
   - 3D: high poly model, 8k, clean 3d render

**禁止包含**：
❌ 具体外貌：long hair, blue eyes, fair skin
❌ 具体服装：dress, suit, uniform
❌ 具体姿态：standing, sitting, running
❌ 具体表情：smiling, serious, sad

输出要求：
只输出风格描述词文本，不要添加任何解释。
```

#### 英文版 Prompt

```
You are a Prompt Engineering expert specializing in creating reusable character style description templates.

**Core Task**:
Generate a universal style description template to be used as a style prefix for subsequent character image/video generation.
This description should not contain specific character features, only abstract elements like art style, render quality, character drawing style, etc.

**Must Include Elements**:
1. **Core Style Tags**:
   - REAL: photorealistic portrait, realistic human
   - ANIME: anime character, anime style
   - 3D: photorealistic 3D CG character

2. **Render Quality**:
   - REAL: 8k uhd, professional portrait photography
   - ANIME: masterpiece, best quality, official art
   - 3D: high poly model, 8k, clean 3d render

**Must NOT Include**:
❌ Specific appearance: long hair, blue eyes, fair skin
❌ Specific clothing: dress, suit, uniform
❌ Specific pose: standing, sitting, running
❌ Specific expression: smiling, serious, sad

Output Requirements:
Only output the style description text, do not add any explanations.
```

**参数说明**：
- 输入：风格类型（REAL/ANIME/3D）
- 输出：通用人物风格描述词
- 不包含：具体外貌、服装、姿态、表情

---

## 7. 视频生成策略 Prompts

### 7.1 视频提示词编排提示词

**功能描述**：创建无缝的视频生成提示词，连接图像序列

**使用场景**：视频连续性生成、图像序列转视频

#### 中文版 Prompt

```
你是一位视频提示词工程专家。
你的任务是创建一个无缝的视频生成提示词，用于连接图像序列。

分析提供的图像和用户意图，创建一个描述动作和过渡的提示词。

提示词应该：
1. 描述主体动作
2. 描述镜头运动
3. 描述场景过渡
4. 保持视觉一致性
5. 确保流畅的叙事流

输出要求：
只输出优化后的视频生成提示词，不要添加解释。
```

#### 英文版 Prompt

```
You are a video prompt engineering expert.
Your task is to create a seamless video generation prompt that bridges a sequence of images.

Analyze the provided images and the user's intent to create a prompt that describes the motion and transition.

The prompt should:
1. Describe subject movement
2. Describe camera movement
3. Describe scene transitions
4. Maintain visual consistency
5. Ensure smooth narrative flow

Output Requirements:
Only output the optimized video generation prompt, do not add explanations.
```

**参数说明**：
- 输入：图像序列、用户意图
- 输出：视频生成提示词
- 关键要素：主体动作、镜头运动、场景过渡、视觉一致性、叙事流

---

### 7.2 图像恢复提示词

**功能描述**：将低分辨率裁剪图像恢复并放大到 4K 高清质量

**使用场景**：SceneDirector 视频生成模式、局部分镜高清化

**节点类型**：VIDEO_GENERATOR (视频生成节点 - SceneDirector 模式)

**核心功能：**
- 严格保持原始构图和相机角度
- 修复模糊和噪点
- 添加皮肤纹理和真实细节
- 防止 AI 产生幻觉和额外内容

#### 完整提示词

```
CRITICAL IMAGE RESTORATION TASK:
1. Input is a low-resolution crop. Your goal is to UPSCALE and RESTORE it to 4K quality.
2. STRICTLY PRESERVE the original composition, character pose, camera angle, and object placement.
3. DO NOT reframe, DO NOT zoom out, DO NOT change the perspective.
4. Fix blurriness and noise. Add skin texture and realistic details matching the description: "${prompt}".
5. Ensure the style matches: "${upstreamContextStyle || 'Cinematic, High Fidelity'}".
6. Output a single, high-quality image that looks exactly like the input but sharper.

NEGATIVE CONSTRAINTS:
- DO NOT add new people, characters, or subjects.
- The number of people MUST remain exactly the same as the input.
- DO NOT hallucinate extra limbs, faces, or background figures.

STRUCTURAL INTEGRITY:
- Treat the input image as the absolute ground truth for composition.
- Only enhance existing pixels, do not invent new geometry.
```

#### 中文版说明

```
关键图像恢复任务：
1. 输入是低分辨率裁剪图像。你的目标是将它放大并恢复到 4K 质量。
2. 严格保持原始构图、角色姿势、相机角度和物体位置。
3. 不要重新构图，不要拉远镜头，不要改变视角。
4. 修复模糊和噪点。添加皮肤纹理和真实细节，匹配描述："${prompt}"。
5. 确保风格匹配："${upstreamContextStyle || '电影级，高保真'}"。
6. 输出单张高质量图像，看起来与输入完全一致但更清晰。

负面约束：
- 不要添加新的人物、角色或主体。
- 人物数量必须与输入完全一致。
- 不要产生幻觉，添加额外的肢体、脸部或背景人物。

结构完整性：
- 将输入图像视为构图的绝对真相。
- 只增强现有像素，不要发明新的几何结构。
```

#### 参数说明

**动态变量：**

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `${prompt}` | 用户提供的场景描述 | "青年男子手持长剑，眼神坚定" |
| `${upstreamContextStyle}` | 上游视频的视觉风格分析 | "Cinematic, High Fidelity" 或 "电影级，高保真" |

#### 使用场景

**1. SceneDirector 模式（局部分镜）：**

当用户在视频中框选局部区域生成新视频时：
- 用户框选区域 → 生成低分辨率裁剪图像
- 使用本提示词恢复到 4K 高清
- 使用高清图像作为 Veo 视频生成的输入
- 确保生成的视频质量高、细节丰富

**2. 工作流程：**

```
原视频 (1080p)
    ↓
用户框选局部区域
    ↓
低分辨率裁剪 (如 270p)
    ↓
图像恢复提示词 (本 Prompt)
    ↓
4K 高清恢复图像 (3840x2160)
    ↓
Veo 视频生成
    ↓
高质量局部视频
```

#### 关键约束

**构图保持（最重要）：**
- ❌ 不允许重新构图
- ❌ 不允许拉远镜头
- ❌ 不允许改变透视
- ✅ 必须保持原始构图
- ✅ 必须保持原始相机角度
- ✅ 必须保持物体位置

**防止幻觉：**
- ❌ 不能添加新人物
- ❌ 不能添加额外肢体
- ❌ 不能添加背景人物
- ✅ 人物数量必须与输入一致

**增强策略：**
- ✅ 增强现有像素质量
- ✅ 添加皮肤纹理细节
- ✅ 修复模糊和噪点
- ✅ 匹配用户描述的场景
- ✅ 匹配上游视频风格

#### 技术实现

**代码位置**：`services/videoStrategies.ts` 第 163-180 行

**使用示例：**

```typescript
const restorationPrompt = `
CRITICAL IMAGE RESTORATION TASK:
1. Input is a low-resolution crop. Your goal is to UPSCALE and RESTORE it to 4K quality.
2. STRICTLY PRESERVE the original composition, character pose, camera angle, and object placement.
3. DO NOT reframe, DO NOT zoom out, DO NOT change the perspective.
4. Fix blurriness and noise. Add skin texture and realistic details matching the description: "${prompt}".
5. Ensure the style matches: "${upstreamContextStyle || 'Cinematic, High Fidelity'}".
6. Output a single, high-quality image that looks exactly like the input but sharper.

NEGATIVE CONSTRAINTS:
- DO NOT add new people, characters, or subjects.
- The number of people MUST remain exactly the same as the input.
- DO NOT hallucinate extra limbs, faces, or background figures.

STRUCTURAL INTEGRITY:
- Treat the input image as the absolute ground truth for composition.
- Only enhance existing pixels, do not invent new geometry.
`;

const restoredImages = await generateImageFromText(
    restorationPrompt,
    getUserDefaultModel('image'),
    [inputImageForGeneration],
    { aspectRatio: node.data.aspectRatio || '16:9', count: 1 }
);
```

#### 输入输出规格

| 项目 | 规格 |
|------|------|
| 输入分辨率 | 任意（通常为 270p - 720p 的裁剪图像） |
| 输出分辨率 | 4K (3840×2160 或 2880×3840) |
| 输出数量 | 1 张 |
| 宽高比 | 保持输入宽高比 |
| 处理时间 | 通常 5-15 秒（取决于模型） |

#### 与其他提示词的区别

| 提示词 | 用途 | 构图要求 | 输出数量 |
|--------|------|----------|----------|
| 九宫格分镜图 | 从文本生成多面板分镜 | 自由创建 | 1 张（包含多个面板） |
| 九宫格表情 | 从角色档案生成表情图 | 3×3 网格 | 1 张（包含9个表情） |
| 三视图 | 从角色档案生成三视图 | 正/侧/后视图 | 1 张（包含3个角度） |
| **图像恢复** | **放大低分辨率裁剪** | **严格保持原图** | **1 张（单张高清）** |

#### 常见问题

**Q: 为什么要严格保持构图？**
A: 在 SceneDirector 模式中，用户框选的局部区域代表了他们想要的精确构图。如果 AI 改变构图，生成的视频将与用户期望不符。

**Q: 如何防止 AI 添加额外人物？**
A: 通过明确的负面约束（NEGATIVE CONSTRAINTS）和结构完整性（STRUCTURAL INTEGRITY）要求，强调人物数量必须一致。

**Q: 可以用于人物以外的主体吗？**
A: 可以，提示词适用于任何需要高清恢复的主体（风景、物体、建筑等），只需调整 `${prompt}` 描述即可。

---

## 📚 总结

本文档整理了哎呦漫剧生成项目中使用的所有 AI Prompts，涵盖 **7 大类、25+ 个核心 Prompt**：

### 核心类别
1. **角色生成**（5个）：角色提取、档案生成、配角档案、九宫格表情、三视图
2. **剧本创作**（4个）：大纲规划、分集创作、电影级分镜、详细分镜
3. **视频生成**（2个）：Sora 提示词构建、敏感词过滤
4. **图像生成**（4个）：九宫格表情、三视图、文本检测、九宫格分镜图
5. **分镜增强**（1个）：智能参数选择
6. **风格预设**（2个）：场景风格、人物风格
7. **视频策略**（2个）：提示词编排、图像恢复

### 关键特性
- ✅ **中英文双语**：所有提示词都提供中文和英文版本，完全语言分离
- ✅ **三种视觉风格支持**：三维动漫、真人、二维动漫
- ✅ **参数说明**：每个提示词都有详细的参数说明
- ✅ **使用场景**：明确标注每个提示词的适用场景
- ✅ **输出格式**：定义清晰的输入输出格式
- ✅ **专业性**：使用行业标准和术语

### 视觉风格对比

| 风格类型 | 核心特征 | 适用场景 | 关键词 |
|---------|---------|---------|--------|
| **三维动漫** | 半写实三维风格，基于物理的材质渲染，飘逸感 | 仙侠、古风、奇幻题材 | 高精度三维建模，基于物理的材质渲染，次表面散射，环境光遮蔽 |
| **真人** | 真实摄影，自然皮肤纹理，专业摄影质感 | 现代、都市、现实主义题材 | 专业人像摄影，数码单反相机质量，八十五毫米镜头，真实皮肤纹理 |
| **二维动漫** | 二维绘画，赛璐珞上色，干净线条 | 青春、校园、二次元题材 | 动漫角色，二维动漫艺术，干净线条，清晰轮廓，赛璐珞着色 |

### 风格自动识别

系统会自动从上游节点（Script Planner）读取视觉风格配置，并应用对应的提示词模板：

```
Script Planner (选择风格) → Character Node (继承风格) →
生成档案/九宫格/三视图 (使用对应风格提示词)
```

### 版本信息
- **文档版本**：v2.1
- **最后更新**：2025-01-24
- **项目名称**：哎呦漫剧生成（AIYOU）
- **更新内容**：中英文提示词完全语言分离，中文版全部使用中文术语，英文版全部使用英文术语

---

**注意**：本文档中的所有 Prompt 都是为本项目定制的，使用时请根据实际需求调整参数和配置。
