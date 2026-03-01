# 角色表情图生成提示词 (Expression Sheet)

> **源文件**: `services/promptManager.ts` 第 27-229 行
> **函数**: `buildExpressionPrompt()`
> **目标模型**: 图像生成模型（Gemini Image）
> **支持风格**: 3D / REAL / ANIME（各有中英文双版本）

---

## 3D 动漫风格

### 中文版

```
3D动漫风格，风格化3D渲染，PBR材质渲染，高精度3D建模，3D动漫美学。

构图：特写肖像，仅头部和肩部，专注于面部表情。

角色面部表情参考表，3×3网格布局，展示9种不同的面部表情（喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫）。

角色面部描述：{APPEARANCE}

关键约束：
- 仅特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景 - 仅纯色背景（白色、浅灰色或黑色），无图案、无渐变、无环境元素
- 所有9个表情中保持一致的角色设计
- 3×3网格构图
```

### 英文版

```
Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics, high precision 3D modeling, PBR shading with soft translucency, subsurface scattering, ambient occlusion, delicate and smooth skin texture (not overly realistic), flowing fabric clothing, individual hair strands, neutral studio lighting, clear focused gaze, natural demeanor.

PORTRAIT COMPOSITION: Extreme close-up, head and shoulders only, facial expressions focus.

Character facial expressions reference sheet, 3x3 grid layout showing 9 different facial expressions (joy, anger, sorrow, surprise, fear, disgust, neutral, thinking, tired).

Character Face Description: {APPEARANCE}

CRITICAL CONSTRAINTS:
- Close-up portrait shots ONLY (head and shoulders)
- NO full body, NO lower body, NO legs
- Focus on facial features, expressions, and head
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white, light gray, or black). NO patterns, NO gradients, NO environmental elements
- Consistent character design across all 9 expressions
- 3x3 grid composition
```

### 3D 负面提示词 (Negative Prompt)

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality, writing, letters, logo, interface, ui, username, website, chinese characters, chinese text, english text, korean text, japanese text, any text, any characters, any letters, numbers, symbols, subtitles, captions, title, full body, standing, legs, feet, full-length portrait, wide shot, environmental background, patterned background, gradient background, 2D illustration, hand-drawn, anime 2D, flat shading, cel shading, toon shading, cartoon 2D, paper cutout, translucent, ghostly, ethereal, glowing aura, overly photorealistic, hyper-realistic skin, photorealistic rendering
```

---

## REAL 真人风格

### 中文版

```
专业人像摄影风格，真实写实，电影级摄影质感。

构图：专业人像构图，仅头部和肩部，专注于面部表情。

角色面部表情参考表，3×3网格布局，展示9种不同的面部表情（喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫）。

角色面部描述：{APPEARANCE}

关键约束：
- 仅特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景 - 仅纯色背景（白色或黑色），无图案、无渐变、无环境元素
- 所有9个表情中保持一致的角色设计
- 3×3网格构图
```

### 英文版

```
Professional portrait photography, photorealistic human, cinematic photography, professional headshot, DSLR quality, 85mm lens, sharp focus, realistic skin texture, visible pores, natural skin imperfections, subsurface scattering.

PORTRAIT COMPOSITION: Professional headshot composition, head and shoulders only, facial expressions focus.

Character facial expressions reference sheet, 3x3 grid layout showing 9 different facial expressions (joy, anger, sadness, surprise, fear, disgust, neutral, thinking, tired).

Character Face Description: {APPEARANCE}

CRITICAL CONSTRAINTS:
- Close-up portrait shots ONLY (head and shoulders)
- NO full body, NO lower body, NO legs
- Focus on facial features, expressions, and head
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white or black). NO patterns, NO gradients, NO environmental elements
- Consistent character design across all 9 expressions
- 3x3 grid composition
```

### REAL 负面提示词

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality, writing, letters, logo, interface, ui, username, website, chinese characters, chinese text, english text, korean text, japanese text, any text, any characters, any letters, numbers, symbols, subtitles, captions, title, full body, standing, legs, feet, full-length portrait, wide shot, environmental background, patterned background, gradient background, anime, cartoon, illustration, 3d render, cgi, 3d animation, painting, drawing
```

---

## ANIME 2D动漫风格

### 中文版

```
2D动漫风格，日式动漫插画，漫画艺术风格。

构图：动漫肖像构图，仅头部和肩部，专注于面部表情。

角色面部表情参考表，3×3网格布局，展示9种不同的面部表情（喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫）。

角色面部描述：{APPEARANCE}

关键约束：
- 仅特写肖像镜头（头部和肩部）
- 无全身、无下半身、无腿部
- 专注于面部特征、表情和头部
- 纯色平背景 - 仅纯色背景（白色、浅灰色或黑色），无图案、无渐变、无环境元素
- 所有9个表情中保持一致的角色设计
- 3×3网格构图
```

### 英文版

```
Anime character, anime style, 2D anime art, manga illustration style, clean linework, crisp outlines, manga art style, detailed illustration.

PORTRAIT COMPOSITION: Anime portrait composition, head and shoulders only, facial expressions focus.

Character facial expressions reference sheet, 3x3 grid layout showing 9 different facial expressions (joy, anger, sadness, surprise, fear, disgust, neutral, thinking, tired).

Character Face Description: {APPEARANCE}

CRITICAL CONSTRAINTS:
- Close-up portrait shots ONLY (head and shoulders)
- NO full body, NO lower body, NO legs
- Focus on facial features, expressions, and head
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white, light gray, or black). NO patterns, NO gradients, NO environmental elements
- Consistent character design across all 9 expressions
- 3x3 grid composition
```

### ANIME 负面提示词

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality, writing, letters, logo, interface, ui, username, website, chinese characters, chinese text, english text, korean text, japanese text, any text, any characters, any letters, numbers, symbols, subtitles, captions, title, full body, standing, legs, feet, full-length portrait, wide shot, environmental background, patterned background, gradient background, photorealistic, realistic, photo, 3d, cgi, live action, hyper-realistic, skin texture, pores
```

---

## 动态参数

| 参数 | 含义 | 来源 |
|------|------|------|
| `{APPEARANCE}` | 角色外观描述 | `profile.appearance` 或 `profile.basicStats` |
