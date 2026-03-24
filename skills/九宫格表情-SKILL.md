# 九宫格表情 Skill

## 使用工具
- Gemini

## 核心功能
生成角色的九宫格表情参考表（3×3 网格）

## 使用场景
角色设计、表情参考

## 提示词模板 - 中文版

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

## 提示词模板 - 英文版

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

## 参数说明
- 输出格式：三乘三网格图像
- 包含表情：喜悦、愤怒、悲伤、惊讶、恐惧、厌恶、中性、思考、疲惫
- 构图：特写肖像（头部和肩部）
- 背景：纯色平背景
- 风格类型：三维 / 真人 / 二维动漫

## 触发词
- "九宫格表情"
- "角色表情"
- "表情参考表"

---
*来源：AI-Prompts-文档.md*
*最后更新：2026-02-19*
