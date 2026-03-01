# 图像高保真修复提示词 (Image Restoration)

> **源文件**: `services/videoStrategies.ts` 第 164-181 行
> **目标模型**: Gemini Image (generateImageWithProvider)
> **语言**: 英文

## 提示词原文

```
CRITICAL IMAGE RESTORATION TASK:
1. Input is a low-resolution crop. Your goal is to UPSCALE and RESTORE it to 4K quality.
2. STRICTLY PRESERVE the original composition, character pose, camera angle, and object placement.
3. DO NOT reframe, DO NOT zoom out, DO NOT change the perspective.
4. Fix blurriness and noise. Add skin texture and realistic details matching the description: "${prompt}".
5. Ensure the style matches: "${upstreamContextStyle || 'Cinematic, High Fidelity'}".
6. Output a single, high-quality image that looks exactly like the input but sharper.

NEGATIVE CONSTRAINTS:
- DO NOT add new people, characters, or subjects.
- The number of people MUST remain exactly the same as the input.
- DO NOT hallucinate extra limbs, faces, or background figures.

STRUCTURAL INTEGRITY:
- Treat the input image as the absolute ground truth for composition.
- Only enhance existing pixels, do not invent new geometry.
```

## 使用场景

将分镜拆分后的低分辨率裁剪图修复为高质量 4K 图片，作为视频生成（如 Veo）的参考输入图。

## 动态参数

| 参数 | 含义 |
|------|------|
| `${prompt}` | 当前分镜的视觉描述文本 |
| `${upstreamContextStyle}` | 上游节点的视觉风格设定，默认 `'Cinematic, High Fidelity'` |

## 输入

- 低分辨率裁剪图片（base64）

## 输出

- 高质量 4K 修复图片
