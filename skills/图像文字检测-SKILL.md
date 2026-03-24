# 图像文字检测 Skill

## 使用工具
- Gemini

## 核心功能
检测图像中是否包含文字、标签等不需要的元素

## 使用场景
图像质量控制、过滤有文字的图像

## 提示词模板 - 中文版

```
请仔细分析这张图片。
图片中是否包含以下任何视觉元素？
1. 文字标签（例如："Front View"、"Side"、姓名、"Fig 1"）
2. 信息框、统计块、角色描述覆盖在图片上
3. 水印、签名、大logo
4. 中文字符或任何手写笔记

如果明显存在任何这些元素，请严格回答"YES"。
如果图片只包含角色插图而没有覆盖文字，请回答"NO"。
```

## 提示词模板 - 英文版

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

## 参数说明
- 输入：图像文件
- 输出："YES" 或 "NO"
- 检测项：文字标签、信息框、水印、签名、中文

## 触发词
- "检测文字"
- "图像文字检测"
- "过滤有文字的图像"

---
*来源：AI-Prompts-文档.md*
*最后更新：2026-02-19*
