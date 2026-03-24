# 三视图 Skill

## 使用工具
- Gemini

## 核心功能
生成角色的三视图参考表（正视图、侧视图、后视图）

## 使用场景
角色设计、3D 建模参考

## 提示词模板 - 中文版

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

## 提示词模板 - 英文版

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

## 参数说明
- 输出格式：三视图参考表
- 包含视图：正视图、侧视图、后视图
- 构图：全身站立姿势
- 背景：纯色平背景
- 风格类型：三维 / 真人 / 二维动漫

## 触发词
- "三视图"
- "角色三视图"
- "3D建模参考"

---
*来源：AI-Prompts-文档.md*
*最后更新：2026-02-19*
