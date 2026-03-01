---
name: "color-style-advisor"
description: "Provides color palettes and visual style recommendations for storyboard projects. Includes 10+ predefined styles like Song Dynasty, Shaw Brothers, UE5 Fantasy, etc. Invoke when need color palette or visual style guidance."
---

# Color Style Advisor

Provides color palettes and visual style recommendations for storyboard projects.

## When to Invoke

- Need color palette recommendations
- Genre or director has been selected
- Preparing for image generation
- User wants specific visual aesthetic

## Input

```json
{
  "genre": "string - Project genre",
  "director": "string - Selected director (optional)",
  "tone": "string - Emotional tone",
  "style_preference": "string - Specific style name (optional)"
}
```

## Output

```json
{
  "recommended_style": {
    "name": "string - Style name",
    "description": "string - Style description",
    "reason": "string - Why this style matches"
  },
  "color_palette": {
    "primary": ["hex colors"],
    "secondary": ["hex colors"],
    "accent": ["hex colors"],
    "background": ["hex colors"]
  },
  "technical_params": {
    "saturation": "number - 0-100",
    "contrast": "number - 0-100",
    "brightness": "number - 0-100",
    "color_temperature": "string - warm/neutral/cool"
  },
  "description": "string - Visual description for prompts",
  "alternative_styles": ["array of alternative style names"]
}
```

## Available Styles

### 1. 宋代古风 (Song Dynasty)
- **Colors**: 墨黑 #1a1a1a, 朱砂 #e74c3c, 石青 #3498db, 藤黄 #f1c40f, 宣纸白 #f5f5dc
- **Tone**: Muted, elegant, scholarly, ink-wash aesthetic
- **Best for**: Historical dramas, period pieces, wuxia

### 2. 邵氏电影 (Shaw Brothers)
- **Colors**: 饱和红 #ff0000, 金色 #ffd700, 墨绿 #006400, 深棕 #8b4513
- **Tone**: Vibrant, theatrical, dramatic, saturated
- **Best for**: Martial arts, wuxia, classic Hong Kong cinema

### 3. 虚幻5幻想 (UE5 Fantasy)
- **Colors**: 霓虹蓝 #00ffff, 魔法紫 #9b59b6, 发光白 #ffffff, 能量橙 #ff6600
- **Tone**: Hyper-realistic, magical, luminous, ray-traced
- **Best for**: Fantasy, sci-fi, game cinematics

### 4. 赛博朋克 (Cyberpunk)
- **Colors**: 霓虹粉 #ff0080, 电光蓝 #00ffff, 深紫 #4b0082, 黑色 #000000, 荧光绿 #39ff14
- **Tone**: High contrast, neon-lit, dystopian, futuristic
- **Best for**: Sci-fi, futuristic, noir, tech

### 5. 韦斯·安德森 (Wes Anderson)
- **Colors**: 薄荷绿 #98fb98, 粉彩黄 #fffacd, 珊瑚橙 #ff7f50, 淡粉 #ffb6c1, 天蓝 #87ceeb
- **Tone**: Pastel, symmetrical, whimsical, quirky
- **Best for**: Comedy, drama, quirky stories

### 6. 莫兰迪色系 (Morandi)
- **Colors**: 灰粉 #d4a5a5, 灰蓝 #9fb4cc, 灰绿 #a8c0a8, 灰褐 #c4b7a6, 灰紫 #b8a9c9
- **Tone**: Muted, sophisticated, calm, understated
- **Best for**: Contemporary drama, fashion, lifestyle

### 7. 新海诚风格 (Makoto Shinkai)
- **Colors**: 天空蓝 #87ceeb, 樱花粉 #ffb7c5, 阳光金 #ffd700, 云朵白 #fffafa, 夕阳橙 #ff6347
- **Tone**: Vibrant, luminous, emotional, detailed
- **Best for**: Anime, romance, youth stories, nature

### 8. 蒂姆·波顿 (Tim Burton)
- **Colors**: 哥特黑 #1a1a1a, 深紫 #4b0082, 苍白 #f5f5dc, 暗红 #8b0000, 灰蓝 #4682b4
- **Tone**: Dark, whimsical, gothic, surreal
- **Best for**: Fantasy, horror, dark comedy, fairy tales

### 9. 王家卫 (Wong Kar-wai)
- **Colors**: 霓虹红 #ff1744, 忧郁绿 #2e7d32, 午夜蓝 #1a237e, 金黄 #ffc107, 深红 #b71c1c
- **Tone**: Moody, atmospheric, urban, nostalgic
- **Best for**: Romance, urban drama, noir, 60s-90s Hong Kong

### 10. 黑泽明 (Kurosawa)
- **Colors**: 水墨黑 #000000, 宣纸白 #f5f5dc, 朱砂红 #dc143c, 土黄 #d2b48c, 深灰 #696969
- **Tone**: High contrast, minimalist, dramatic, painterly
- **Best for**: Samurai, drama, action, rain scenes

## Genre-Style Mapping

| Genre | Recommended Styles |
|-------|-------------------|
| war | kurosawa, song_dynasty, shaw_brothers, spielberg |
| romance | wong_kar_wai, shinkai, morandi, linklater |
| scifi | cyberpunk, ue5_fantasy, villeneuve, scott |
| horror | tim_burton, cyberpunk, hitchcock |
| action | shaw_brothers, kurosawa, woo, bay |
| drama | wes_anderson, morandi, wong_kar_wai, scorsese |
| comedy | wes_anderson, allen, burton |

## Prompt Template

```
你是一位专业的色彩顾问。请为以下项目推荐色彩风格：

项目类型：{genre}
参考导演：{director}
情感基调：{tone}
风格偏好：{style_preference}

请从以下10种风格中选择推荐：
1. song_dynasty - 宋代古风
2. shaw_brothers - 邵氏电影
3. ue5_fantasy - 虚幻5幻想
4. cyberpunk - 赛博朋克
5. wes_anderson - 韦斯·安德森
6. morandi - 莫兰迪色系
7. shinkai - 新海诚风格
8. tim_burton - 蒂姆·波顿
9. wong_kar_wai - 王家卫
10. kurosawa - 黑泽明

请返回：
1. 推荐的主要风格（含名称、描述、推荐理由）
2. 完整色板（主色、辅色、强调色、背景色，提供HEX值）
3. 技术参数（饱和度、对比度、亮度、色温）
4. 用于AI生图的英文视觉描述
5. 备选风格列表

以JSON格式返回结果。
```

## Example

Input:
```json
{
  "genre": "war",
  "director": "kurosawa",
  "tone": "epic"
}
```

Output:
```json
{
  "recommended_style": {
    "name": "kurosawa",
    "description": "黑泽明风格 - 高对比度水墨美学",
    "reason": "与战争题材和史诗基调完美匹配，强调构图和光影对比"
  },
  "color_palette": {
    "primary": ["#000000", "#f5f5dc"],
    "secondary": ["#dc143c", "#d2b48c"],
    "accent": ["#696969"],
    "background": ["#f5f5dc", "#000000"]
  },
  "technical_params": {
    "saturation": 30,
    "contrast": 85,
    "brightness": 50,
    "color_temperature": "neutral"
  },
  "description": "High contrast black and white cinematography with selective red accents, inspired by Kurosawa's Ran and Seven Samurai, dramatic shadows, painterly composition",
  "alternative_styles": ["shaw_brothers", "song_dynasty"]
}
```