# 角色三视图生成提示词 (Three-View Sheet)

> **源文件**: `services/promptManager.ts` 第 61-276 行
> **函数**: `buildThreeViewPrompt()`
> **目标模型**: 图像生成模型（Gemini Image）
> **支持风格**: 3D / REAL / ANIME（各有中英文双版本）

---

## 3D 动漫风格

### 中文版

```
3D动漫风格，风格化3D渲染，PBR材质渲染，高精度3D建模，3D动漫美学。

角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

角色描述：{APPEARANCE}
属性：{STATS}

构图：
- 创建垂直布局，包含3个视图：正视图、侧视图（侧面）、后视图
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

### 英文版

```
Xianxia 3D animation character, semi-realistic style, Xianxia animation aesthetics, high precision 3D modeling, PBR shading with soft translucency, subsurface scattering, ambient occlusion, delicate and smooth skin texture (not overly realistic), flowing fabric clothing, individual hair strands, neutral studio lighting, clear focused gaze, natural demeanor.

CHARACTER THREE-VIEW GENERATION TASK:
Generate a character three-view reference sheet (front, side, back views).

Character Description: {APPEARANCE}
Attributes: {STATS}

COMPOSITION:
- Create vertical layout with 3 views: Front View, Side View (profile), Back View
- Full body standing pose, neutral expression
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white, light gray, or black). NO patterns, NO gradients, NO environmental elements
- Each view should clearly show the character from the specified angle

CRITICAL REQUIREMENTS:
1. CONSISTENT CHARACTER DESIGN - All three views must show the SAME character with consistent facial features, hair style, body proportions, and clothing
2. NO TEXT, NO LABELS - Pure image only, no "Front View" or "Side View" text labels
3. PROPER ANATOMY - Ensure correct body proportions and natural stance for each view angle
4. NEUTRAL EXPRESSION - Use a calm, neutral face expression across all views
5. CLEAR ALIGNMENT - Front, side, and back views should be vertically aligned and proportionally consistent

REFERENCE IMAGE: Use the expression sheet as visual reference for face and clothing details.
```

### 3D 负面提示词

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality, writing, letters, logo, interface, ui, username, website, chinese characters, english text, patterned background, gradient background, scenery, environmental background, shadows on background, 2D illustration, hand-drawn, anime 2D, flat shading, cel shading, toon shading, cartoon 2D, paper cutout, translucent, ghostly, ethereal, glowing aura, overly photorealistic, hyper-realistic skin, photorealistic rendering
```

---

## REAL 真人风格

### 中文版

```
专业人像摄影风格，真实写实，电影级摄影质感。

角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

角色描述：{APPEARANCE}
属性：{STATS}

构图：
- 创建垂直布局，包含3个视图：正视图、侧视图（侧面）、后视图
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

### 英文版

```
Professional portrait photography, photorealistic human, cinematic photography, fashion photography style, studio lighting, realistic skin texture, natural fabric folds, detailed clothing materials.

CHARACTER THREE-VIEW GENERATION TASK:
Generate a character three-view reference sheet (front, side, back views).

Character Description: {APPEARANCE}
Attributes: {STATS}

COMPOSITION:
- Create vertical layout with 3 views: Front View, Side View (profile), Back View
- Full body standing pose, neutral expression
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white or black). NO patterns, NO gradients, NO environmental elements
- Each view should clearly show the character from the specified angle

CRITICAL REQUIREMENTS:
1. CONSISTENT CHARACTER DESIGN - All three views must show the SAME character with consistent facial features, hair style, body proportions, and clothing
2. NO TEXT, NO LABELS - Pure image only, no "Front View" or "Side View" text labels
3. PROPER ANATOMY - Ensure correct body proportions and natural stance for each view angle
4. NEUTRAL EXPRESSION - Use a calm, neutral face expression across all views
5. CLEAR ALIGNMENT - Front, side, and back views should be vertically aligned and proportionally consistent

REFERENCE IMAGE: Use the expression sheet as visual reference for face and clothing details.
```

### REAL 负面提示词

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality, writing, letters, logo, interface, ui, username, website, chinese characters, english text, patterned background, gradient background, scenery, environmental background, shadows on background, anime, cartoon, illustration, 3d render, cgi, 3d animation, painting, drawing
```

---

## ANIME 2D动漫风格

### 中文版

```
2D动漫风格，日式动漫插画，漫画艺术风格。

角色三视图生成任务：生成角色三视图参考表（正视图、侧视图、后视图）。

角色描述：{APPEARANCE}
属性：{STATS}

构图：
- 创建垂直布局，包含3个视图：正视图、侧视图（侧面）、后视图
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

### 英文版

```
Anime character, 2D anime art, manga illustration, character reference sheet, clean linework, crisp outlines, anime style.

CHARACTER THREE-VIEW GENERATION TASK:
Generate a character three-view reference sheet (front, side, back views).

Character Description: {APPEARANCE}
Attributes: {STATS}

COMPOSITION:
- Create vertical layout with 3 views: Front View, Side View (profile), Back View
- Full body standing pose, neutral expression
- SOLID FLAT BACKGROUND - Plain solid color background ONLY (white, light gray, or black). NO patterns, NO gradients, NO environmental elements
- Each view should clearly show the character from the specified angle

CRITICAL REQUIREMENTS:
1. CONSISTENT CHARACTER DESIGN - All three views must show the SAME character with consistent facial features, hair style, body proportions, and clothing
2. NO TEXT, NO LABELS - Pure image only, no "Front View" or "Side View" text labels
3. PROPER ANATOMY - Ensure correct body proportions and natural stance for each view angle
4. NEUTRAL EXPRESSION - Use a calm, neutral face expression across all views
5. CLEAR ALIGNMENT - Front, side, and back views should be vertically aligned and proportionally consistent

REFERENCE IMAGE: Use the expression sheet as visual reference for face and clothing details.
```

### ANIME 负面提示词

```
nsfw, text, watermark, label, signature, bad anatomy, deformed, low quality, writing, letters, logo, interface, ui, username, website, chinese characters, english text, patterned background, gradient background, scenery, environmental background, shadows on background, photorealistic, realistic, photo, 3d, cgi, live action, hyper-realistic, skin texture, pores
```

---

## 动态参数

| 参数 | 含义 | 来源 |
|------|------|------|
| `{APPEARANCE}` | 角色外观描述 | `profile.appearancePrompt` 或 `profile.appearance` |
| `{STATS}` | 角色属性 | `profile.profession` |
