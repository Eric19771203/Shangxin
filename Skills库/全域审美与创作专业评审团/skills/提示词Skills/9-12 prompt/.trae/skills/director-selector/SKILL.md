---
name: "director-selector"
description: "Selects and matches film directors based on project genre, style, and tone. Provides director recommendations with reasoning. Invoke when genre is identified and need director style guidance."
---

# Director Selector

Match film directors to projects based on genre, style, and tone.

## When to Invoke

- Genre has been identified from requirement analysis
- Need director recommendations for style reference
- User wants specific directorial vision applied

## Input

```json
{
  "genre": "string - Project genre",
  "style": "string - Visual style preference",
  "tone": "string - Emotional tone",
  "requirement": "string - Original requirement text"
}
```

## Output

```json
{
  "primary_director": {
    "id": "string - Director identifier",
    "name": "string - Director name",
    "reason": "string - Why this director matches"
  },
  "alternative_directors": [
    {
      "id": "string",
      "name": "string",
      "reason": "string"
    }
  ],
  "style_characteristics": {
    "visual_style": "string - Visual approach",
    "narrative_approach": "string - Storytelling style",
    "camera_work": "string - Camera techniques",
    "color_palette": "string - Color usage"
  }
}
```

## Director Database

### War Genre
- **spielberg**: Steven Spielberg - Realistic war depiction, emotional depth, Saving Private Ryan style
- **nolan**: Christopher Nolan - Non-linear storytelling, epic scale, Dunkirk style
- **kurosawa**: Akira Kurosawa - Samurai/war aesthetics, composition, Seven Samurai style

### Romance Genre
- **wong_kar_wai**: Wong Kar-wai - Poetic visuals, color symbolism, In the Mood for Love style
- **linklater**: Richard Linklater - Naturalistic dialogue, intimacy, Before Sunrise style
- **allen**: Woody Allen - Urban romance, witty dialogue, Manhattan style

### Sci-Fi Genre
- **scott**: Ridley Scott - Futuristic realism, atmospheric, Blade Runner style
- **villeneuve**: Denis Villeneuve - Visual grandeur, philosophical, Dune/Arrival style
- **kubrick**: Stanley Kubrick - Precise composition, intellectual, 2001 Space Odyssey style

### Horror Genre
- **burton**: Tim Burton - Gothic fantasy, stylized horror, Sleepy Hollow style
- **hitchcock**: Alfred Hitchcock - Psychological suspense, Psycho style
- **del_toro**: Guillermo del Toro - Dark fantasy, creature design, Pan's Labyrinth style

### Action Genre
- **bay**: Michael Bay - High-energy, explosive visuals, Transformers style
- **woo**: John Woo - Stylized action, slow-motion, Hard Boiled style
- **snyder**: Zack Snyder - Graphic novel aesthetic, 300 style

### Drama Genre
- **scorsese**: Martin Scorsese - Character-driven, gritty realism, Taxi Driver style
- **anderson_pt**: Paul Thomas Anderson - Complex narratives, There Will Be Blood style
- **coppola**: Sofia Coppola - Atmospheric, intimate, Lost in Translation style

## Prompt Template

```
你是一位资深的电影导演匹配专家。基于以下项目信息，推荐最适合的导演：

项目类型：{genre}
视觉风格：{style}
情感基调：{tone}
项目描述：{requirement}

请推荐：
1. 一位主要推荐导演（最匹配）
2. 两位备选导演
3. 每位导演的匹配理由
4. 该导演的风格特征（视觉风格、叙事方式、镜头语言、色彩运用）

以JSON格式返回结果。
```

## Example

Input:
```json
{
  "genre": "scifi",
  "style": "cinematic",
  "tone": "epic",
  "requirement": "未来战争科幻短片"
}
```

Output:
```json
{
  "primary_director": {
    "id": "villeneuve",
    "name": "Denis Villeneuve",
    "reason": "擅长史诗级科幻视觉，氛围营造出色"
  },
  "alternative_directors": [
    {
      "id": "scott",
      "name": "Ridley Scott",
      "reason": "未来现实主义风格标杆"
    },
    {
      "id": "nolan",
      "name": "Christopher Nolan",
      "reason": "非线性叙事与宏大场面"
    }
  ],
  "style_characteristics": {
    "visual_style": "宏大、极简、自然光运用",
    "narrative_approach": "慢节奏、哲学性、视觉驱动",
    "camera_work": "广角镜头、缓慢移动、航拍",
    "color_palette": "沙色调、冷色调、高对比度"
  }
}
```