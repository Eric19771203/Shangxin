# AIYOU 项目提示词（Prompts）完整指南

> 本文档系统整理了 AIYOU 漫剧创作平台中所有关键环节使用的 AI 提示词，按业务流程分类，便于理解、维护和二次开发。

---

## 目录

- [一、概述](#一概述)
- [二、剧本创作类提示词](#二剧本创作类提示词)
  - [2.1 剧本大纲生成（Script Planner）](#21-剧本大纲生成script-planner)
  - [2.2 分集剧本生成（Script Episode）](#22-分集剧本生成script-episode)
- [三、角色设计类提示词](#三角色设计类提示词)
  - [3.1 角色名提取（Character Extraction）](#31-角色名提取character-extraction)
  - [3.2 主角档案生成（Character Profile）](#32-主角档案生成character-profile)
  - [3.3 配角档案生成（Supporting Character）](#33-配角档案生成supporting-character)
  - [3.4 角色表情图生成（Expression Sheet）](#34-角色表情图生成expression-sheet)
  - [3.5 角色三视图生成（Three-View Sheet）](#35-角色三视图生成three-view-sheet)
- [四、剧集分析类提示词](#四剧集分析类提示词)
  - [4.1 剧集深度分析（Drama Analyzer）](#41-剧集深度分析drama-analyzer)
  - [4.2 剧集精炼提取（Drama Refined）](#42-剧集精炼提取drama-refined)
- [五、分镜生成类提示词](#五分镜生成类提示词)
  - [5.1 电影级分镜（Cinematic Storyboard）](#51-电影级分镜cinematic-storyboard)
  - [5.2 详细分镜脚本（Detailed Storyboard）](#52-详细分镜脚本detailed-storyboard)
  - [5.3 分镜智能增强（Shot Enhancer）](#53-分镜智能增强shot-enhancer)
- [六、视频生成类提示词](#六视频生成类提示词)
  - [6.1 视频编排提示词（Video Orchestrator）](#61-视频编排提示词video-orchestrator)
  - [6.2 Sora 2 专用提示词构建器（Sora2 Builder）](#62-sora-2-专用提示词构建器sora2-builder)
  - [6.3 通用多镜头提示词构建器（Generic Builder）](#63-通用多镜头提示词构建器generic-builder)
  - [6.4 简单文本提示词构建器（Simple Builder）](#64-简单文本提示词构建器simple-builder)
  - [6.5 Sora 专业提示词生成（Sora Professional Prompt）](#65-sora-专业提示词生成sora-professional-prompt)
  - [6.6 敏感词净化（Sensitive Words Removal）](#66-敏感词净化sensitive-words-removal)
- [七、图像处理类提示词](#七图像处理类提示词)
  - [7.1 图片文字检测（Text Detection）](#71-图片文字检测text-detection)
  - [7.2 图像高保真修复（Image Restoration）](#72-图像高保真修复image-restoration)
- [八、风格预设类提示词](#八风格预设类提示词)
  - [8.1 场景风格模板生成（Scene Style）](#81-场景风格模板生成scene-style)
  - [8.2 人物风格模板生成（Character Style）](#82-人物风格模板生成character-style)
- [九、AI 助手类提示词](#九ai-助手类提示词)
  - [9.1 助手面板多模式系统指令](#91-助手面板多模式系统指令)
- [十、提示词架构总览](#十提示词架构总览)

---

## 一、概述

AIYOU 平台的 AI 提示词体系覆盖了短剧创作的全部关键环节，形成了从 **剧本构思 → 角色设计 → 分镜拆解 → 视频生成** 的完整链路。提示词主要分布在以下源文件中：

| 文件路径 | 提示词数量 | 主要职责 |
|---------|-----------|---------|
| `services/geminiService.ts` | 10+ | 核心 AI 服务，包含剧本、角色、分镜、分析等提示词 |
| `services/promptManager.ts` | 6 | 角色表情图、三视图的图像生成提示词模板 |
| `services/shotEnhancer.ts` | 1 | 分镜智能增强（景别、角度、运镜选择） |
| `services/soraPromptBuilder.ts` | 2 | Sora 专业提示词生成与敏感词净化 |
| `services/promptBuilders/genericBuilder.ts` | 1 | 通用视频模型提示词构建 |
| `services/promptBuilders/sora2Builder.ts` | 1 | Sora 2 Story Mode 格式构建 |
| `services/promptBuilders/simpleBuilder.ts` | 1 | 简单文本描述构建 |
| `services/videoStrategies.ts` | 1 | 图像高保真修复提示词 |
| `components/AssistantPanel.tsx` | 4 | AI 助手面板多模式系统指令 |

所有提示词均以 **中文** 为主要语言（部分图像/视频生成提示词使用英文），目标模型主要为 **Google Gemini**，同时兼容云雾 API 和自定义 API 供应商。

---

## 二、剧本创作类提示词

### 2.1 剧本大纲生成（Script Planner）

**源文件**: `services/geminiService.ts` (约 438-620 行)
**函数**: `generateScriptPlanner()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位专精于短剧和微电影的专业编剧 (Professional Screenwriter)。你的任务是根据用户的核心创意和约束条件，创建一个引人入胜的**中文剧本大纲**。

#### 核心原则

- 剧本大纲只在**章节层面**规划，不细化到每集
- 每个章节描述 100-150 字
- 严格遵循叙事结构：每 3-5 集设置高潮，每 10-15 集设置转折点

#### 动态参数

| 参数 | 含义 | 示例 |
|------|------|------|
| `{TotalEpisodes}` | 总集数 | 30 |
| `{ChapterCount}` | 章节数 | 6 |
| `{EpisodesPerChapter}` | 每章集数 | 5 |
| `{MinCharacters}` / `{MaxCharacters}` | 角色数量范围 | 3-6 |
| `{MinItems}` / `{MaxItems}` | 关键物品数量范围 | 2-4 |
| `{Duration}` | 单集时长（分钟） | 1 |
| `{Visual Style}` | 视觉风格 | 3D / REAL / ANIME |

#### 输出格式

Markdown 结构化大纲，包含：
- 剧名与核心设定
- 角色列表（核心角色 80-120 字，配角 20-40 字）
- 关键物品设定
- 分章节剧情概要
- 质量自检清单

#### 用户输入格式

```
核心创意: {prompt}
主题: {config.theme || 'N/A'}
类型: {config.genre || 'N/A'}
背景: {config.setting || 'N/A'}
预估集数: {config.episodes || 10}
单集时长: {config.duration || 1} 分钟
视觉风格: {config.visualStyle || 'N/A'}
```

---

### 2.2 分集剧本生成（Script Episode）

**源文件**: `services/geminiService.ts` (约 622-707 行)
**函数**: `generateScriptEpisodes()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位专业的短剧分集编剧，擅长创作连贯、一致的系列剧集。你的任务是根据提供的【剧本大纲】和【指定章节】，将该章节拆分为 N 个具体的剧集脚本。

#### 输入上下文（9 项）

1. **剧本大纲** — 所有章节的概览
2. **目标章节** — 当前要拆分的章节
3. **前序剧集摘要** — 之前已生成的剧集摘要（保持连贯性）
4. **全局角色设定** — 所有角色信息
5. **全局物品设定** — 所有关键物品信息
6. **拆分集数** — N
7. **单集时长参考**
8. **视觉风格**
9. **修改建议**（可选）

#### 连贯性要求（CRITICAL）

1. **角色一致性** — 严格遵循全局角色设定中的外貌、性格、说话方式
2. **物品命名一致性** — 严格使用标准名称，禁止混用
   - ❌ 错误：一会儿叫"脊骨"，一会儿叫"灵骨"
   - ✅ 正确：始终使用"脊骨"
3. **剧情连贯性** — 参考前序剧集摘要，确保时间线衔接
4. **场景连贯性** — 场景描述符合既定视觉风格

#### 内容要求

- 每分钟时长需 **200-250 字** 详细剧本内容
- 必须包含：场景描述、肢体动作、表情细节、精彩对白、情感描写
- 每集结尾必须有**悬念 (Cliffhanger)**

#### 细节扩写示例

```
❌ 不要只写"他走进房间"
✅ 要写"他推开沉重的红木门，脚步沉重地踏入昏暗的书房，皮鞋在大理石地板上发出清脆的回响"

❌ 不要只写"她哭了"
✅ 要写"她的眼泪如断了线的珍珠般滑落，肩膀随着压抑的抽泣微微颤抖，双手紧紧攥着衣角，指节泛白"
```

#### 输出格式

```json
[
  {
    "title": "第X集：[分集标题]",
    "content": "[详细剧本内容]",
    "characters": "[本集角色列表]",
    "keyItems": "[本集关键物品列表]",
    "visualStyleNote": "[视觉风格备注]",
    "continuityNote": "[连贯性说明]"
  }
]
```

---

## 三、角色设计类提示词

### 3.1 角色名提取（Character Extraction）

**源文件**: `services/geminiService.ts` (约 268-273 行)
**函数**: `extractCharactersFromText()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 系统指令

```
你是一位专业的选角导演。
你的任务是从剧本或大纲中提取所有出现的角色名称。
请只输出一个 JSON 字符串数组，不要包含其他内容。
例如: ["张三", "李四", "王五"]
```

#### 用户输入

```
提取以下剧本内容中的所有角色名：
{text}
```

#### 输出格式

```json
["角色A", "角色B", "角色C"]
```

---

### 3.2 主角档案生成（Character Profile）

**源文件**: `services/geminiService.ts` (约 275-334 行)
**函数**: `generateCharacterProfile()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位资深的角色设计师和小说家。你的任务是根据提供的角色名称和剧本上下文，生成极度详细的角色档案。

#### 输出格式

```json
{
  "name": "角色名",
  "alias": "称谓（同事、家人等）",
  "basicStats": "基础属性（年龄、性别、身高、身材、发型、特征、着装）",
  "profession": "职业（含隐藏身份）",
  "background": "生活环境、生理特征、地域标签",
  "personality": "性格（主性格+次性格）",
  "motivation": "核心动机",
  "values": "价值观",
  "weakness": "恐惧与弱点",
  "relationships": "核心关系及影响",
  "habits": "语言风格、行为习惯、兴趣爱好",
  "appearancePrompt": "用于AI生图的详细英文提示词"
}
```

#### 视觉风格特定要求

提示词中内嵌了三种视觉风格的详细约束，根据传入的 `Visual Style` 参数自动选用：

**3D 动画风格：**
- 核心风格：`Xianxia 3D animation character, semi-realistic style`
- 必须使用：`high precision 3D modeling, PBR shading with soft translucency`
- 皮肤质感：`delicate and smooth skin texture, subsurface scattering`
- 严格禁止：`2D illustration, flat shading, cel shading, overly photorealistic`

**REAL 真人风格：**
- 核心风格：`Photorealistic portrait, cinematic photography, professional headshot`
- 必须使用：`Professional portrait photography, DSLR quality, 85mm lens`
- 皮肤质感：`Realistic skin texture, visible pores, natural skin imperfections`
- 严格禁止：`anime, cartoon, illustration, 3d render, cgi`

**ANIME 2D 动漫风格：**
- 核心风格：`Anime character, anime style, 2D anime art, manga illustration style`
- 必须使用：`Clean linework, crisp outlines, manga art style`
- 皮肤质感：`Smooth flat skin, cel shading, clean skin rendering`
- 严格禁止：`photorealistic, realistic, photo, 3d, cgi, live action`

#### 用户输入格式

```
Role Name: {name}
Script Context: {contextText}
Visual Style Context (CRITICAL): {styleContext || "Default"}
Additional User Description: {customDesc}（如有）
```

---

### 3.3 配角档案生成（Supporting Character）

**源文件**: `services/geminiService.ts` (约 336-387 行)
**函数**: `generateSupportingCharacter()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位资深的角色设计师。你的任务是为配角生成简化的角色档案。

#### 与主角档案的区别

| 维度 | 主角档案 | 配角档案 |
|------|---------|---------|
| 字段数量 | 12 个字段 | 5 个字段 |
| 性格/动机 | 详细 | 不需要 |
| 关系/弱点 | 详细 | 不需要 |
| 外观提示词 | 详细 | 简洁 |

#### 输出格式

```json
{
  "name": "角色名",
  "basicStats": "基础属性（年龄、性别、身高、身材、发型、特征、着装）",
  "profession": "职业",
  "introduction": "简短介绍（1-2句话描述角色定位和在剧中的作用）",
  "appearancePrompt": "用于AI生图的详细英文提示词"
}
```

---

### 3.4 角色表情图生成（Expression Sheet）

**源文件**: `services/promptManager.ts` (约 27-229 行)
**函数**: `buildExpressionPrompt()`
**目标模型**: 图像生成模型（Gemini Image）

此提示词用于生成角色的 **3x3 九宫格表情参考表**，包含 9 种表情：**喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫**。

根据视觉风格分为中文版和英文版两套提示词，以下为核心结构：

#### 通用构图要求

```
构图：特写肖像，仅头部和肩部，专注于面部表情。
角色面部表情参考表，3x3网格布局，展示9种不同的面部表情。

关键约束：
- 仅特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景（白色、浅灰色或黑色），无图案、无渐变
- 所有9个表情中保持一致的角色设计
- 3x3网格构图
```

#### 3D 风格前缀

```
3D动漫风格，风格化3D渲染，PBR材质渲染，高精度3D建模，3D动漫美学。
```

英文版：
```
Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics,
high precision 3D modeling, PBR shading with soft translucency, subsurface scattering,
ambient occlusion, delicate and smooth skin texture, flowing fabric clothing,
individual hair strands, neutral studio lighting, clear focused gaze, natural demeanor.
```

#### REAL 风格前缀

```
Professional portrait photography, photorealistic human, cinematic photography,
professional headshot, DSLR quality, 85mm lens, sharp focus, realistic skin texture,
visible pores, natural skin imperfections, subsurface scattering.
```

#### ANIME 风格前缀

```
Anime character, anime style, 2D anime art, manga illustration style,
clean linework, crisp outlines, manga art style, detailed illustration.
```

#### 负面提示词（Negative Prompt）

每种风格都有对应的负面提示词列表，用于排除不期望的元素。例如 3D 风格：

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality,
writing, letters, logo, interface, ui, username, website, chinese characters,
english text, patterned background, gradient background, scenery,
2D illustration, hand-drawn, anime 2D, flat shading, cel shading, toon shading,
cartoon 2D, overly photorealistic, hyper-realistic skin, photorealistic rendering
```

---

### 3.5 角色三视图生成（Three-View Sheet）

**源文件**: `services/promptManager.ts` (约 61-276 行)
**函数**: `buildThreeViewPrompt()`
**目标模型**: 图像生成模型（Gemini Image）

此提示词用于生成角色的 **正视图、侧视图、后视图** 三视图参考表。

#### 核心结构

```
角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

角色描述：{APPEARANCE}
属性：{STATS}

构图：
- 创建垂直布局，包含3个视图：正视图、侧视图（侧面）、后视图
- 全身站立姿势，中性表情
- 纯色平背景
- 每个视图应清晰显示指定角度的角色

关键要求：
1. 一致的角色设计 - 三个视图必须显示相同的角色
2. 无文本、无标签 - 纯图像，无"正视图"或"侧视图"文字标签
3. 正确的解剖结构 - 正确身体比例和自然姿势
4. 中性表情 - 所有视图使用平静、中性的面部表情
5. 清晰对齐 - 正视图、侧视图和后视图垂直对齐且比例一致

参考图片：使用表情图作为面部和服装细节的视觉参考。
```

同样按 **3D / REAL / ANIME** 三种风格提供不同的风格前缀和负面提示词。

---

## 四、剧集分析类提示词

### 4.1 剧集深度分析（Drama Analyzer）

**源文件**: `services/geminiService.ts` (约 389-413 行)
**函数**: `analyzeDrama()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位资深的影视剧分析专家和编剧顾问。你的任务是对用户提供的剧名进行深度分析，从多个维度评估其创作价值和 IP 潜力。

#### 分析维度（8 维度）

| 字段 | 分析维度 | 参考示例 | 字数要求 |
|------|---------|---------|---------|
| `dramaIntroduction` | 剧集介绍 | — | 100-200字 |
| `worldview` | 世界观分析 | 《进击的巨人》「巨人吃人的世界」 | 约200字 |
| `logicalConsistency` | 逻辑自洽性 | 《火影忍者》后期「查克拉滥用」 | 约150字 |
| `extensibility` | 延展性 | 《宝可梦》「精灵收集」可衍生游戏 | 约150字 |
| `characterTags` | 角色标签 | 「高冷学霸+反差萌」 | 约200字 |
| `protagonistArc` | 主角弧光 | 《海贼王》路飞从「单细胞船长」到「领袖」 | 约200字 |
| `audienceResonance` | 受众共鸣 | 《夏目友人帐》「孤独但温柔」 | 约150字 |
| `artStyle` | 画风/视觉风格 | 《JOJO》「荒木线」成为IP标识 | 约200字 |

#### 输出格式

```json
{
  "dramaName": "剧名",
  "dramaIntroduction": "...",
  "worldview": "...",
  "logicalConsistency": "...",
  "extensibility": "...",
  "characterTags": "...",
  "protagonistArc": "...",
  "audienceResonance": "...",
  "artStyle": "..."
}
```

#### 未知剧集处理

如果 AI 不了解该剧，需明确说明「无法检索到该剧的详细信息」，并建议用户提供更多上下文。

---

### 4.2 剧集精炼提取（Drama Refined）

**源文件**: `services/geminiService.ts` (约 2125 行)
**函数**: `extractRefinedTags()`
**目标模型**: Gemini (通过 llmProviderManager)

此提示词用于从剧集分析结果中提取**精炼关键词和通用特征**，将其转换为可复用的创作素材（不含特定专有名词），供后续剧本创作参考。

---

## 五、分镜生成类提示词

### 5.1 电影级分镜（Cinematic Storyboard）

**源文件**: `services/geminiService.ts` (约 709-743 行)
**函数**: `generateCinematicStoryboard()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位世界级的电影导演和摄影指导 (Director of Photography)。你的任务是根据提供的【剧集脚本】，将其拆解为一系列专业的**电影分镜头 (Cinematic Shots)**。

#### 输入参数

- 剧集内容 (Episode Content)
- 拆解数量 (Shot Count)：N 个镜头
- 镜头时长 (Shot Duration)：T 秒
- 视觉风格 (Visual Style)

#### 输出格式（每个镜头 8 个字段）

```json
[
  {
    "subject": "主体：[详细描述人物外貌、动作、情绪]",
    "scene": "场景：[时间、地点、光影、氛围]",
    "camera": "镜头语言：[景别、角度、运镜方式、焦点]",
    "lighting": "光影：[光源性质、光比、色调]",
    "dynamics": "动态与特效：[环境动态、物理特效]",
    "audio": "声音：[人声、音效、BGM]",
    "style": "风格与质感：[画面风格、分辨率、胶片感]",
    "negative": "负面约束：[禁止出现的内容]"
  }
]
```

#### 创作要求

1. **视觉语言专业化** — 使用专业电影术语（侧逆光、浅景深、推镜头、荷兰角等）
2. **画面感极强** — 描述极其具体，能直接指导 AI 生成高质量画面
3. **连贯性** — 镜头之间有逻辑衔接，服务于叙事
4. **情感传递** — 通过光影和构图强化角色情绪
5. **风格一致性** — 所有镜头描述符合指定风格

---

### 5.2 详细分镜脚本（Detailed Storyboard）

**源文件**: `services/geminiService.ts` (约 745-923 行)
**函数**: `generateDetailedStoryboard()`
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位专业的影视分镜师和摄影指导 (Storyboard Artist & DoP)。你的任务是将提供的【剧集脚本内容】细化拆分为详细的**影视级分镜脚本**。

#### 时长控制（CRITICAL）

```
每个分镜时长：严格控制在 1-4 秒
平均镜头时长：2-3秒（保持快节奏）
不得出现超过4秒的长镜头
不得出现少于1秒的碎片化镜头
```

#### 分镜数量计算

| 内容时长 | 最少分镜数 | 推荐分镜数 |
|---------|-----------|-----------|
| 1 分钟（60秒） | 20 个 | 25-30 个 |
| 2 分钟（120秒） | 40 个 | 50-60 个 |
| 3 分钟（180秒） | 60 个 | 75-90 个 |

#### 内容类型节奏策略

| 内容类型 | 镜头时长 | 节奏 |
|---------|---------|------|
| 关键剧情/高潮 | 1-2秒 | 快切，制造紧张感 |
| 情感/对话 | 2-3秒 | 跟随情感 |
| 环境/过渡 | 3-4秒 | 建立空间 |
| 动作场面 | 1秒 | 快速剪辑，强化动感 |

#### 肢体状态描述要求

每个分镜的 `visualDescription` 必须以角色肢体状态开头（用括号标注）：

```
✅ "(角色俯卧在地，全身被雨水浸透) 角色的眼中充满了莫名的恨意..."
❌ "角色的眼中充满了莫名的恨意..."（缺少肢体状态）
```

#### 输出格式

```json
[
  {
    "shotNumber": 1,
    "duration": 2,
    "scene": "教室 - 白天 - 靠窗最后一排",
    "characters": ["林霄"],
    "shotSize": "特写",
    "cameraAngle": "低位仰拍",
    "cameraMovement": "固定",
    "visualDescription": "(角色肢体状态) [详细画面描述]",
    "dialogue": "对白内容 或 '无'",
    "visualEffects": "景深、色调、特效、风格",
    "audioEffects": "环境音、音效、背景音乐"
  }
]
```

---

### 5.3 分镜智能增强（Shot Enhancer）

**源文件**: `services/shotEnhancer.ts` (约 29-68 行)
**函数**: `enhanceShotWithAI()`
**目标模型**: Gemini (通过 generateTextWithProvider)

#### 角色定义

> 你是一位专业的影视导演和分镜师。根据场景描述，为这个镜头选择最合适的景别、拍摄角度和运镜方式。

#### 完整知识库

**可选景别（8种）：**

| 景别 | 画面范围 | 适用场景 |
|------|---------|---------|
| 大远景 | 人物如蚂蚁，环境主导 | 开场定场、表现孤独 |
| 远景 | 人物小但能看清动作 | 动作场面、环境展示 |
| 全景 | 顶天立地，全身可见 | 角色介绍、舞蹈、对决 |
| 中景 | 腰部以上 | 标准对话、动作与表情兼顾 |
| 中近景 | 胸部以上 | 情感交流、反应镜头 |
| 近景 | 脖子以上 | 强调情绪、重要台词 |
| 特写 | 只有脸 | 内心戏、强烈冲击力 |
| 大特写 | 局部细节 | 制造紧张感、暗示线索 |

**可选拍摄角度（6种）：**

| 角度 | 描述 | 作用 |
|------|------|------|
| 视平 | 与角色眼睛同高 | 建立共情、平等对话 |
| 高位俯拍 | 从上往下拍 | 表现无助、被压迫 |
| 低位仰拍 | 从下往上拍 | 塑造英雄、制造恐惧 |
| 斜拍 | 摄影机倾斜 | 精神错乱、悬疑氛围 |
| 越肩 | 从肩膀后方拍摄 | 对话场面、建立对抗 |
| 鸟瞰 | 垂直向下90度 | 交代地理环境、表现宿命论 |

**可选运镜方式（11种）：**

| 运镜 | 描述 | 作用 |
|------|------|------|
| 固定 | 摄影机纹丝不动 | 喜剧效果、积蓄张力 |
| 横移 | 水平移动 | 跟随行动、展示环境 |
| 俯仰 | 镜头上下转动 | 揭示高度、展现力量关系 |
| 横摇 | 镜头左右转动 | 跟随视线、建立空间关系 |
| 升降 | 垂直升降 | 史诗感开场/结尾 |
| 轨道推拉 | 物理靠近或远离 | 情绪高潮、表现孤独 |
| 变焦推拉 | 改变焦距 | 复古风、希区柯克变焦 |
| 正跟随 | 位于角色身后跟随 | 代入感、走进未知环境 |
| 倒跟随 | 在角色前方后退 | 边走边谈、恐惧与逃亡 |
| 环绕 | 围绕主体旋转 | 英雄时刻、浪漫时刻 |
| 滑轨横移 | 小型轨道平滑移动 | 静物特写、狭小空间 |

#### 输出格式

```json
{
  "shotSize": "景别名称",
  "cameraAngle": "拍摄角度",
  "cameraMovement": "运镜方式",
  "reasoning": "选择理由（50字以内）"
}
```

---

## 六、视频生成类提示词

### 6.1 视频编排提示词（Video Orchestrator）

**源文件**: `services/geminiService.ts` (约 415-436 行)
**函数**: `orchestrateVideoPrompt()`
**目标模型**: Gemini (通过 llmProviderManager)
**语言**: 英文

#### 系统指令

```
You are a video prompt engineering expert for AI video generation models.

Your task is to create a single, concise video generation prompt in English
that seamlessly transitions between the provided storyboard images.

CRITICAL REQUIREMENTS:
1. Output ONLY the video prompt in English - no explanations
2. Start directly with the prompt text (e.g., "A cinematic scene showing...")
3. Focus on visual descriptions: camera movement, transitions, lighting, mood
4. Keep it concise (under 200 words)
5. Use professional video terminology: pan, zoom, fade, transition, tracking shot
6. Describe the flow between images, not just individual images

DO NOT include:
- "Here is a prompt..." or similar introductions
- Any explanations or commentary
- Bullet points or numbered lists
- Any non-English text
```

#### 使用场景

当用户提供多张分镜图片时，将其编排为一段流畅过渡的视频生成提示词。

---

### 6.2 Sora 2 专用提示词构建器（Sora2 Builder）

**源文件**: `services/promptBuilders/sora2Builder.ts`
**类**: `Sora2PromptBuilder`
**适用模型**: Sora

#### 特点

- **不调用 AI 增强**，直接使用中文分镜信息拼接
- 支持黑色空镜作为视频开头（默认 0.5 秒）
- 保留完整分镜信息（景别、角度、运镜、场景、特效、对话、音效）

#### 输出格式

```
Shot 1:
duration: 0.5s
Scene: 纯黑空镜，无任何视觉内容

Shot 2:
duration: 3.0s
Scene: 特写，低位仰拍，固定，角色缓缓抬起头...[视觉特效]，"对白"，[音效]
```

---

### 6.3 通用多镜头提示词构建器（Generic Builder）

**源文件**: `services/promptBuilders/genericBuilder.ts`
**类**: `GenericPromptBuilder`
**适用模型**: Luma, Runway, Veo, MiniMax, 火山引擎, Grok, Qwen

#### 系统提示词

```
你是一个视频提示词格式化工具。只负责将分镜信息转换为指定格式，不添加任何额外内容。
```

#### 用户提示词

```
你是一位专业的视频提示词生成器。你的任务是将分镜信息转换为多镜头视频提示词格式。

分镜信息：[分镜列表]
总时长：约 X 秒

输出要求：
1. 第一行输出统一风格声明：Style: {visualStyle}
2. 空一行后，依次输出每个 Shot
3. 每个 Shot 包含 duration、Scene、Dialogue（如有）、SFX（如有）字段
4. Scene 只描述视觉画面，不要重复风格信息
5. 对白原样保留 / 忽略对白（可配置）
6. 不添加任何前缀、后缀、说明
```

#### 输出格式

```
Style: Cinematic, high quality, consistent style

Shot 1:
duration: 3.0s
Scene: [场景描述]，[动作描述]
Dialogue: "对白内容"
SFX: [音效描述]

Shot 2:
duration: 2.5s
Scene: [场景描述]
```

#### 清理逻辑

构建器内置了输出清理逻辑，自动移除 AI 常生成的多余前缀（如"好的，"、"以下是"、"Sure,"、"Here is"等）和 Markdown 标记。

---

### 6.4 简单文本提示词构建器（Simple Builder）

**源文件**: `services/promptBuilders/simpleBuilder.ts`
**类**: `SimpleTextBuilder`
**适用模型**: 不支持多镜头格式的模型

#### 系统提示词

```
你是一个视频描述生成工具。负责将分镜信息转换为简洁的视频描述。
```

#### 用户提示词

```
请将以下分镜信息转换为一个流畅的视频描述：

分镜信息：[每个镜头的景别、角度、运镜、场景、描述、对白]
总时长：约 X 秒

输出要求：
1. 生成一个简洁流畅的视频描述文本
2. 包含所有关键视觉信息
3. 不要添加任何前缀、后缀或解释
4. 直接输出描述文本
```

#### 回退方案

AI 调用失败时，回退为简单的编号列表格式：

```
1. (3.0s) 角色缓缓走入昏暗的房间...
2. (2.5s) 镜头推近角色面部...
```

---

### 6.5 Sora 专业提示词生成（Sora Professional Prompt）

**源文件**: `services/soraPromptBuilder.ts` (约 70-94 行)
**函数**: `buildProfessionalSoraPromptLegacy()`
**目标模型**: Sora 2 (通过 LLM 增强)

#### 系统提示词

```
你是一个 Sora 2 提示词格式化工具。只负责将分镜信息转换为指定格式，不添加任何额外内容。
```

#### 用户提示词

```
你是一位专业的 Sora 2 提示词生成器。你的任务是将分镜信息转换为 Sora 2 Story Mode 格式。

分镜信息：[每个镜头的编号、时长、景别、角度、运镜、场景、对白、特效、音效]
总时长：约 X 秒

输出要求：
1. 只输出 Sora 2 Story Mode 格式
2. 必须以 Shot 1 开始
3. 不要添加任何前缀、后缀、说明、建议或解释
4. 不要使用 "---" 分隔线
5. 不要添加"导演建议"、"色彩控制"等额外内容
6. 直接开始输出 Shot 1

输出格式：
Shot 1:
duration: X.Xs
Scene: [场景描述]

Shot 2:
duration: X.Xs
Scene: [场景描述]
```

---

### 6.6 敏感词净化（Sensitive Words Removal）

**源文件**: `services/soraPromptBuilder.ts` (约 288-320 行)
**函数**: `removeSensitiveWords()`
**目标模型**: Gemini/LLM

#### 系统提示词

```
你是一个专业的Sora提示词净化工具。你的任务是检测并优化提示词中的敏感内容，
同时保持原有的结构和格式不变。
```

#### 敏感词类型

1. **暴力内容** — 流血、死亡、残肢、酷刑、吐血、鲜血等
2. **色情内容** — 裸露、性暗示、不雅行为等
3. **版权侵权** — 商标、品牌、受版权保护的角色名（米老鼠、迪士尼等）
4. **名人信息** — 真实人物姓名、肖像描述

#### 替换示例

| 原始词 | 替换为 |
|--------|--------|
| 吐血 | 重伤 / 吐白沫 |
| 死亡 | 倒地不起 / 失去意识 |
| 鲜血直流 | 红色液体流出 |
| 赤身裸体 | 穿着单薄 |
| 米老鼠 | 某卡通老鼠角色 |
| 迪士尼 | 某动画公司 |

#### 优化原则

- 仅针对特定敏感词进行替换或删除
- 保持 Shot 结构完整（Shot X:, duration:, Scene:）
- 不添加任何额外的解释或说明
- 输出必须以 "Shot 1:" 开始

---

## 七、图像处理类提示词

### 7.1 图片文字检测（Text Detection）

**源文件**: `services/geminiService.ts` (约 226-264 行)
**函数**: `detectTextInImage()`
**目标模型**: Gemini (多模态)
**语言**: 英文

#### 提示词

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

#### 使用场景

检测角色图片中是否存在文字覆盖（标签、水印、签名等），用于判断图片质量是否适合后续处理。

#### 输出

`YES` 或 `NO`

---

### 7.2 图像高保真修复（Image Restoration）

**源文件**: `services/videoStrategies.ts` (约 164-181 行)
**目标模型**: Gemini Image
**语言**: 英文

#### 提示词

```
CRITICAL IMAGE RESTORATION TASK:
1. Input is a low-resolution crop. Your goal is to UPSCALE and RESTORE it to 4K quality.
2. STRICTLY PRESERVE the original composition, character pose, camera angle, and object placement.
3. DO NOT reframe, DO NOT zoom out, DO NOT change the perspective.
4. Fix blurriness and noise. Add skin texture and realistic details matching the description.
5. Ensure the style matches the specified visual style.
6. Output a single, high-quality image that looks exactly like the input but sharper.

NEGATIVE CONSTRAINTS:
- DO NOT add new people, characters, or subjects.
- The number of people MUST remain exactly the same as the input.
- DO NOT hallucinate extra limbs, faces, or background figures.

STRUCTURAL INTEGRITY:
- Treat the input image as the absolute ground truth for composition.
- Only enhance existing pixels, do not invent new geometry.
```

#### 使用场景

将分镜拆分后的低分辨率裁剪图修复为高质量 4K 图片，作为视频生成的参考图。

---

## 八、风格预设类提示词

### 8.1 场景风格模板生成（Scene Style）

**源文件**: `services/geminiService.ts` (约 2311-2356 行)
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位 Prompt 工程专家，专门生成可复用的**场景风格描述词模板**。

#### 核心任务

生成一段通用的风格描述词，用作后续场景图像/视频生成的**风格前缀**。不包含具体场景内容，只包含画风、渲染质量、色调、光影等抽象风格元素。

#### 必须包含的元素

| 元素 | REAL | ANIME | 3D |
|------|------|-------|-----|
| 核心风格标签 | photorealistic, cinematic | anime style, anime background art | 3d render, octane render |
| 渲染质量 | 8k uhd, professional photography | high quality, masterpiece | ray tracing, global illumination |
| 光影风格 | natural lighting, volumetric lighting | soft lighting, rim light | studio lighting, HDRI lighting |
| 色调风格 | 暖色调 / 冷色调 / 中性 | 暖色调 / 冷色调 / 中性 | 暖色调 / 冷色调 / 中性 |
| 画面质感 | sharp focus, depth of field | cel shading, flat colors | PBR materials, realistic reflections |

#### 禁止包含

- ❌ 具体场景（forest, street, room）
- ❌ 具体物体（tree, building, furniture）
- ❌ 构图角度（wide shot, close-up）
- ❌ 具体光源（sunset, candlelight, neon lights）

#### 输出格式

纯英文文本，逗号分隔关键词，30-50 个单词。

---

### 8.2 人物风格模板生成（Character Style）

**源文件**: `services/geminiService.ts` (约 2358-2407 行)
**目标模型**: Gemini (通过 llmProviderManager)

#### 角色定义

> 你是一位 Prompt 工程专家，专门生成可复用的**人物风格描述词模板**。

#### 核心任务

生成一段通用的风格描述词，用作后续人物图像/视频生成的**风格前缀**。不包含具体人物特征。

#### 必须包含的元素

| 元素 | REAL | ANIME | 3D |
|------|------|-------|-----|
| 核心风格标签 | photorealistic portrait | anime character | photorealistic 3D CG |
| 渲染质量 | 8k uhd, professional portrait | masterpiece, best quality | high poly model, 8k |
| 人物绘制质量 | detailed facial features, realistic skin | beautiful detailed eyes, clean linework | smooth realistic skin |
| 画面质感 | shallow depth of field, bokeh | vibrant colors, cel shading | toon shading, artistic rendering |
| 光照风格 | soft portrait lighting, natural light | soft shading, anime lighting | studio lighting, three-point lighting |

#### 禁止包含

- ❌ 具体外貌（long hair, blue eyes）
- ❌ 具体服装（dress, suit）
- ❌ 具体姿态（standing, sitting）
- ❌ 具体表情（smiling, serious）
- ❌ 具体年龄/性别
- ❌ 构图角度

#### 输出格式

纯英文文本，逗号分隔关键词，30-50 个单词。

---

## 九、AI 助手类提示词

### 9.1 助手面板多模式系统指令

**源文件**: `components/AssistantPanel.tsx` (约 183-190 行)
**目标模型**: Gemini (通过 getClient)

AI 助手面板根据用户选择的模式切换不同的系统指令：

| 模式 | 系统指令 | 功能 |
|------|---------|------|
| 默认模式 | `你是一个AI创意助手，擅长提供创作建议和灵感。` | 通用创作辅助 |
| 分镜模式 | `你是一个专业的分镜设计师，擅长将文字描述转化为分镜脚本。` | 文字转分镜 |
| 写作助手 | `你是一个专业的写作助手，擅长帮助用户改进和优化文本。` | 文本润色优化 |
| 深度思考 | `你是一个深思熟虑的分析助手，擅长深入分析问题。` | 深度分析 |

---

## 十、提示词架构总览

### 业务流程与提示词映射

```
用户输入创意
    │
    ▼
┌─────────────────────┐
│ 剧集分析 (可选)       │ ← Drama Analyzer + Drama Refined
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 剧本大纲生成         │ ← Script Planner
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 角色名提取            │ ← Character Extraction
│ 主角/配角档案生成      │ ← Character Profile / Supporting Character
│ 表情图 + 三视图       │ ← Expression Sheet + Three-View Sheet
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 分集剧本生成          │ ← Script Episode
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 分镜脚本生成          │ ← Cinematic / Detailed Storyboard
│ 分镜智能增强          │ ← Shot Enhancer
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 视频提示词生成         │ ← Sora2 / Generic / Simple Builder
│ 视频编排              │ ← Video Orchestrator
│ 敏感词净化            │ ← Sensitive Words Removal
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ 图像处理              │ ← Text Detection + Image Restoration
│ 风格预设              │ ← Scene Style + Character Style
└─────────────────────┘
```

### 提示词完整索引

| 编号 | 提示词名称 | 源文件 | 函数/类 | 目标模型 | 语言 |
|------|-----------|--------|---------|---------|------|
| P01 | 角色名提取 | `geminiService.ts:268` | `extractCharactersFromText` | Gemini/LLM | 中文 |
| P02 | 主角档案生成 | `geminiService.ts:275` | `generateCharacterProfile` | Gemini/LLM | 中文 |
| P03 | 配角档案生成 | `geminiService.ts:336` | `generateSupportingCharacter` | Gemini/LLM | 中文 |
| P04 | 剧集深度分析 | `geminiService.ts:389` | `analyzeDrama` | Gemini/LLM | 中文 |
| P05 | 视频编排 | `geminiService.ts:415` | `orchestrateVideoPrompt` | Gemini/LLM | 英文 |
| P06 | 剧本大纲生成 | `geminiService.ts:438` | `generateScriptPlanner` | Gemini/LLM | 中文 |
| P07 | 分集剧本生成 | `geminiService.ts:622` | `generateScriptEpisodes` | Gemini/LLM | 中文 |
| P08 | 电影级分镜 | `geminiService.ts:709` | `generateCinematicStoryboard` | Gemini/LLM | 中/英 |
| P09 | 详细分镜脚本 | `geminiService.ts:745` | `generateDetailedStoryboard` | Gemini/LLM | 中文 |
| P10 | 剧集精炼提取 | `geminiService.ts:2125` | `extractRefinedTags` | Gemini/LLM | 中文 |
| P11 | 场景风格模板 | `geminiService.ts:2311` | `generateSceneStyle` | Gemini/LLM | 中/英 |
| P12 | 人物风格模板 | `geminiService.ts:2358` | `generateCharacterStyle` | Gemini/LLM | 中/英 |
| P13 | 图片文字检测 | `geminiService.ts:226` | `detectTextInImage` | Gemini | 英文 |
| P14 | 分镜智能增强 | `shotEnhancer.ts:29` | `enhanceShotWithAI` | Gemini/LLM | 中文 |
| P15 | 表情图(3D) | `promptManager.ts:27` | `buildExpressionPrompt` | Image Gen | 中/英 |
| P16 | 表情图(REAL) | `promptManager.ts:112` | `buildExpressionPrompt` | Image Gen | 中/英 |
| P17 | 表情图(ANIME) | `promptManager.ts:197` | `buildExpressionPrompt` | Image Gen | 中/英 |
| P18 | 三视图(3D) | `promptManager.ts:61` | `buildThreeViewPrompt` | Image Gen | 中/英 |
| P19 | 三视图(REAL) | `promptManager.ts:146` | `buildThreeViewPrompt` | Image Gen | 中/英 |
| P20 | 三视图(ANIME) | `promptManager.ts:231` | `buildThreeViewPrompt` | Image Gen | 中/英 |
| P21 | Sora2 提示词构建 | `sora2Builder.ts` | `Sora2PromptBuilder.build` | Sora | 中文 |
| P22 | 通用多镜头构建 | `genericBuilder.ts:51` | `GenericPromptBuilder.build` | Luma/Runway/Veo 等 | 中文 |
| P23 | 简单文本构建 | `simpleBuilder.ts:38` | `SimpleTextBuilder.build` | 通用 | 中文 |
| P24 | Sora 专业提示词 | `soraPromptBuilder.ts:70` | `buildProfessionalSoraPromptLegacy` | Sora | 中文 |
| P25 | 敏感词净化 | `soraPromptBuilder.ts:288` | `removeSensitiveWords` | Gemini/LLM | 中文 |
| P26 | 图像高保真修复 | `videoStrategies.ts:164` | — | Gemini Image | 英文 |
| P27 | 助手-默认模式 | `AssistantPanel.tsx:183` | — | Gemini | 中文 |
| P28 | 助手-分镜模式 | `AssistantPanel.tsx:185` | — | Gemini | 中文 |
| P29 | 助手-写作模式 | `AssistantPanel.tsx:187` | — | Gemini | 中文 |
| P30 | 助手-深度思考 | `AssistantPanel.tsx:189` | — | Gemini | 中文 |

---

### 提示词设计模式总结

1. **角色扮演模式** — 几乎所有提示词都以"你是一位..."开头，赋予 AI 特定专业身份
2. **结构化输出约束** — 大量使用 JSON 格式要求，确保输出可被程序解析
3. **负面约束（Negative Prompt）** — 图像生成提示词均附带详细的排除列表
4. **多风格适配** — 角色类提示词内嵌 3D / REAL / ANIME 三套风格规范
5. **动态参数注入** — 提示词中预留 `{变量}` 占位符，运行时动态填充
6. **链式上下文传递** — 分集剧本接收大纲输出，分镜接收剧本输出，形成完整链路
7. **清理后处理** — 视频提示词构建器内置输出清理逻辑，移除 AI 常见的多余前缀

---

> 本文档基于代码库自动分析生成，如提示词有更新，请同步更新本文档。
