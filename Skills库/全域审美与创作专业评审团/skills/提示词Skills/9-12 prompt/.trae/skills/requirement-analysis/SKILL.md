---
name: "requirement-analysis"
description: "Analyzes user requirements for storyboard projects and extracts key parameters like genre, style, tone, and target audience. Invoke when user provides a project description or brief and needs structured analysis."
---

# Requirement Analysis

Analyze user requirements for storyboard projects and extract structured parameters.

## When to Invoke

- User provides a project description or creative brief
- Need to parse unstructured text into actionable parameters
- Starting a new storyboard generation workflow

## Input

```json
{
  "requirement": "string - Raw user description of the project"
}
```

## Output

```json
{
  "genre": "string - Primary genre (war, romance, scifi, horror, action, drama, comedy)",
  "style": "string - Visual style preference (cinematic, realistic, stylized, vintage)",
  "tone": "string - Emotional tone (dark, light, epic, intimate)",
  "audience": "string - Target demographic",
  "keywords": ["array of extracted keywords"],
  "scenes_count": "number - Estimated scene count",
  "technical_requirements": {
    "aspect_ratio": "string",
    "duration": "string",
    "format": "string"
  }
}
```

## Analysis Rules

### Genre Detection Keywords
- **War**: 战争, 军事, 战斗, 史诗, war, battle, military, soldier
- **Romance**: 爱情, 浪漫, 情感, romance, love, relationship
- **Sci-Fi**: 科幻, 未来, 太空, scifi, future, space, cyber
- **Horror**: 恐怖, 惊悚, 悬疑, horror, thriller, scary
- **Action**: 动作, 冒险, action, adventure, fight
- **Drama**: 剧情, 文艺, drama, story
- **Comedy**: 喜剧, 搞笑, comedy, funny, humor

### Style Keywords
- **Cinematic**: 电影感, cinematic, film-like, movie
- **Realistic**: 写实, 真实, realistic, photorealistic
- **Stylized**: 风格化, 艺术, stylized, artistic
- **Vintage**: 复古, 怀旧, vintage, retro, classic

### Tone Indicators
- **Dark**: 黑暗, 沉重, 严肃, dark, serious, grim
- **Light**: 轻松, 明亮, 欢快, light, cheerful, bright
- **Epic**: 史诗, 宏大, 壮观, epic, grand, spectacular
- **Intimate**: 私密, 细腻, 温情, intimate, personal

## Prompt Template

```
你是一位专业的影视项目分析师。请分析以下项目需求，提取关键信息：

项目描述：
{requirement}

请提取以下信息并以JSON格式返回：
1. 类型/题材 (genre): 从 [war, romance, scifi, horror, action, drama, comedy] 中选择
2. 视觉风格 (style): 从 [cinematic, realistic, stylized, vintage] 中选择
3. 情感基调 (tone): 从 [dark, light, epic, intimate] 中选择
4. 目标受众 (audience): 描述目标观众群体
5. 关键词列表 (keywords): 提取5-10个关键描述词
6. 预估场景数量 (scenes_count): 数字
7. 技术要求 (technical_requirements): 包含 aspect_ratio, duration, format

只返回JSON格式数据，不要其他解释。
```

## Example

Input:
```json
{"requirement": "一个关于未来战争的科幻短片，需要电影感强烈的视觉风格，讲述士兵在废墟中寻找希望的故事"}
```

Output:
```json
{
  "genre": "scifi",
  "style": "cinematic",
  "tone": "epic",
  "audience": "科幻电影爱好者",
  "keywords": ["未来", "战争", "士兵", "废墟", "希望", "科幻", "电影感"],
  "scenes_count": 5,
  "technical_requirements": {
    "aspect_ratio": "16:9",
    "duration": "5-10 minutes",
    "format": "digital"
  }
}
```