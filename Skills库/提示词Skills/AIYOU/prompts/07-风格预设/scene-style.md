# 场景风格预设提示词 (Scene Style Preset)

> **源文件**: `services/geminiService.ts` 第 2311-2356 行
> **常量名**: `SCENE_STYLE_INSTRUCTION`
> **函数**: `generateStylePreset()`（第 2412-2494 行）
> **目标模型**: LLM (通过 llmProviderManager.generateContent)
> **语言**: 中文

---

## 系统指令原文

```
你是一位Prompt工程专家，专门生成可复用的**场景风格描述词模板**。

**核心任务**：
生成一段通用的风格描述词，用作后续场景图像/视频生成的**风格前缀**。
这段描述词不包含具体场景内容，只包含画风、渲染质量、色调、光影等抽象风格元素。

**输出要求**：
1. 纯风格描述，不包含具体物体、场景、构图
2. 可以直接作为prompt前缀使用
3. 长度：30-50个英文单词
4. 使用逗号分隔关键词

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

4. **色调风格**：
   - 暖色调：warm tone, golden palette
   - 冷色调：cool tone, blue palette
   - 中性：natural colors, balanced colors

5. **画面质感**：
   - REAL: sharp focus, depth of field, bokeh effect
   - ANIME: cel shading, flat colors, clean lines
   - 3D: PBR materials, realistic reflections

**禁止包含**：
❌ 具体场景：forest, street, room
❌ 具体物体：tree, building, furniture
❌ 构图角度：wide shot, close-up, from above
❌ 具体光源：sunset, candlelight, neon lights

**输出格式**：
纯文本，逗号分隔，无换行，无markdown格式
```

---

## 用户提示词模板

```
请生成一段场景风格描述词模板。

【上游视觉风格信息】
画风分析：${upstreamStyleInfo.artStyle || '未提供'}
类型：${upstreamStyleInfo.genre || '未提供'}
设定：${upstreamStyleInfo.setting || '未提供'}

【视觉风格类型】
${visualStyle}

【用户补充】
${userInput || '无'}

【要求】
生成纯粹的风格描述词，不包含任何具体场景、物体或构图。
只包含：画风、渲染质量、光影风格、质感等抽象元素。
这段描述词将作为前缀，用于后续所有场景图像生成。
```

---

## 负面提示词 (Negative Prompts)

根据视觉风格类型，函数会自动附加对应的负面提示词：

| 视觉风格 | 负面提示词 Key | 负面提示词内容 |
|----------|---------------|---------------|
| **REAL** | `SCENE_REAL` | `people, characters, humans, anime, cartoon, painting, illustration, 3d render, low quality, blurry, watermark, signature` |
| **ANIME** | `SCENE_ANIME` | `realistic, photo, 3d, low quality, blurry, monochrome, watermark` |
| **3D** | `SCENE_3D` | `2d, flat, anime, photo, painting, low poly, low quality, blurry` |

默认负面提示词（未匹配时）：`low quality, blurry, watermark`

---

## 使用场景

在节点工作流中，当用户设定了视觉风格后，系统会调用 `generateStylePreset('SCENE', visualStyle, ...)` 生成一段**可复用的场景风格前缀**。这段前缀会被附加到后续所有场景图像/视频生成的 prompt 前面，确保整部作品的场景风格一致。

## 动态参数

| 参数 | 含义 |
|------|------|
| `presetType` | 固定为 `'SCENE'` |
| `visualStyle` | 视觉风格类型：`'REAL'` / `'ANIME'` / `'3D'` |
| `upstreamStyleInfo.artStyle` | 上游节点分析得到的画风描述 |
| `upstreamStyleInfo.genre` | 作品类型（如仙侠、都市等） |
| `upstreamStyleInfo.setting` | 故事设定 |
| `userInput` | 用户额外输入的风格补充 |

## 输入

- 上游视觉风格信息（画风、类型、设定）
- 视觉风格类型（REAL / ANIME / 3D）
- 可选的用户补充输入

## 输出

返回对象包含：
- `stylePrompt`: 30-50 个英文单词的风格描述词，逗号分隔
- `negativePrompt`: 对应风格类型的负面提示词
