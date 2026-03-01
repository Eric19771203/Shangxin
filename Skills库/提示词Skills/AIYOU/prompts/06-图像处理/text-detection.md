# 图片文字检测提示词 (Text Detection)

> **源文件**: `services/geminiService.ts` 第 231-241 行
> **函数**: `detectTextInImage()`
> **目标模型**: Gemini (多模态，getClient 直接调用)
> **语言**: 英文

## 提示词原文

```
Analyze this image carefully.
Does it contain any of the following visual elements?
1. Text labels (e.g., "Front View", "Side", names, "Fig 1").
2. Info boxes, stats blocks, or character descriptions overlaying the image.
3. Watermarks, signatures, or large logos.
4. Chinese characters or any handwritten notes.

Answer strictly "YES" if any of these are visibly present.
Answer "NO" if the image contains ONLY the character illustration with no overlay text.
```

## 使用场景

检测角色图片中是否存在文字覆盖（标签、水印、签名等），用于判断图片质量是否适合后续处理（如三视图生成、视频参考图等）。

## 输入

- 图片的 base64 编码数据

## 输出

- `YES` — 图片中包含文字/水印/标签
- `NO` — 图片中仅有角色插画，无文字覆盖
