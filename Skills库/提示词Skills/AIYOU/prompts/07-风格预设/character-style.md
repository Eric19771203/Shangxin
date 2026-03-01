# 人物风格预设提示词 (Character Style Preset)

> **源文件**: `services/geminiService.ts` 第 2358-2407 行
> **常量名**: `CHARACTER_STYLE_INSTRUCTION`
> **函数**: `generateStylePreset()`（第 2412-2494 行）
> **目标模型**: LLM (通过 llmProviderManager.generateContent)
> **语言**: 中文

---

## 系统指令原文

```
你是一位Prompt工程专家，专门生成可复用的**人物风格描述词模板**。

**核心任务**：
生成一段通用的风格描述词，用作后续人物图像/视频生成的**风格前缀**。
这段描述词不包含具体人物特征，只包含画风、渲染质量、人物绘制风格等抽象元素。

**输出要求**：
1. 纯风格描述，不包含具体外貌、服装、姿态
2. 可以直接作为prompt前缀使用
3. 长度：30-50个英文单词
4. 使用逗号分隔关键词

**必须包含的元素**：
1. **核心风格标签**：
   - REAL: photorealistic portrait, realistic human
   - ANIME: anime character, anime style
   - 3D: photorealistic 3D CG character

2. **渲染质量**：
   - REAL: 8k uhd, professional portrait photography, high resolution
   - ANIME: masterpiece, best quality, official art, detailed illustration
   - 3D: high poly model, 8k, clean 3d render, stylized rendering

3. **人物绘制质量**（抽象）：
   - REAL: detailed facial features, realistic skin texture, professional lighting
   - ANIME: beautiful detailed eyes, detailed character design, clean linework
   - 3D: smooth realistic skin, clean character design, realistic features

4. **画面质感**：
   - REAL: shallow depth of field, bokeh background, natural colors
   - ANIME: vibrant colors, cel shading, clean rendering
   - 3D: toon shading, vibrant colors, clean surfaces, artistic rendering, non-photorealistic

5. **光照风格**（适用于人物）：
   - REAL: soft portrait lighting, natural light, rim light
   - ANIME: soft shading, anime lighting, gentle highlights
   - 3D: studio lighting, soft shadows, ambient occlusion, three-point lighting

**禁止包含**：
❌ 具体外貌：long hair, blue eyes, fair skin
❌ 具体服装：dress, suit, uniform
❌ 具体姿态：standing, sitting, running
❌ 具体表情：smiling, serious, sad
❌ 具体年龄/性别：teenage girl, old man
❌ 构图角度：portrait, full body, close-up
❌ 真人皮肤纹理：skin texture, pores, wrinkles, skin details
❌ 照片质感：photorealistic, hyperrealistic, photo, photography

**输出格式**：
纯文本，逗号分隔，无换行，无markdown格式
```

---

## 用户提示词模板

```
请生成一段人物风格描述词模板。

【上游视觉风格信息】
画风分析：${upstreamStyleInfo.artStyle || '未提供'}
类型：${upstreamStyleInfo.genre || '未提供'}
设定：${upstreamStyleInfo.setting || '未提供'}

【视觉风格类型】
${visualStyle}

【用户补充】
${userInput || '无'}

【要求】
生成纯粹的风格描述词，不包含任何具体人物特征（外貌、服装、姿态、表情）。
只包含：画风、人物绘制质量、光影风格、渲染质感等抽象元素。
这段描述词将作为前缀，用于后续所有人物图像生成。
```

---

## 负面提示词 (Negative Prompts)

根据视觉风格类型，函数会自动附加对应的负面提示词：

| 视觉风格 | 负面提示词 Key | 负面提示词内容 |
|----------|---------------|---------------|
| **REAL** | `CHARACTER_REAL` | `anime, cartoon, illustration, 3d, cgi, bad anatomy, deformed, low quality, blurry, watermark` |
| **ANIME** | `CHARACTER_ANIME` | `realistic, photo, 3d, bad anatomy, bad hands, extra limbs, low quality, blurry, nsfw` |
| **3D** | `CHARACTER_3D` | `2d, flat, anime, photo, painting, low poly, bad topology, low quality, blurry` |

默认负面提示词（未匹配时）：`low quality, blurry, watermark`

---

## 使用场景

在节点工作流中，当用户设定了视觉风格后，系统会调用 `generateStylePreset('CHARACTER', visualStyle, ...)` 生成一段**可复用的人物风格前缀**。这段前缀会被附加到后续所有人物图像/视频生成的 prompt 前面，确保整部作品的角色绘制风格一致。

## 动态参数

| 参数 | 含义 |
|------|------|
| `presetType` | 固定为 `'CHARACTER'` |
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
