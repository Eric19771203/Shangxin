# 九宫格分镜图 Skill

## 使用工具
- Gemini

## 核心功能
生成电影级九宫格/六宫格分镜图（3×3 或 2×3 网格布局）

## 使用场景
短视频分镜制作、视觉规划、故事板设计

## 完整提示词模板

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

## 参数说明

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

## 风格说明

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

## 触发词
- "九宫格分镜图"
- "分镜图设计"
- "故事板生成"

---
*来源：AI-Prompts-文档.md*
*最后更新：2026-02-19*
