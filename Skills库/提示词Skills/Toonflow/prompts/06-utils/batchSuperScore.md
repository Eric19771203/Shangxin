# 图片超分辨率 - 系统/用户提示词

| 属性 | 值 |
|------|------|
| **源文件** | `src/routes/storyboard/batchSuperScoreImage.ts` |
| **类型** | 硬编码系统 + 用户提示词（内容相同） |
| **AI配置组** | `storyboardImage` |
| **输出** | 超分后图片（1K分辨率） |
| **修改方式** | 需修改源文件中的 `systemPrompt` 和 `prompt` |

---

## 提示词原文

系统提示词和用户提示词使用相同的内容：

```
你的核心任务是将所给的图片超分到 1K ，不改变图片任何内容，仅改变分辨率
```

---

## AI 调用参数

```javascript
u.ai.image({
  aspectRatio: videoRatio,    // 项目视频比例
  size: "1K",
  resType: "b64",
  systemPrompt: "你的核心任务是将所给的图片超分到 1K ，不改变图片任何内容，仅改变分辨率",
  prompt: "你的核心任务是将所给的图片超分到 1K ，不改变图片任何内容，仅改变分辨率",
  imageBase64: [await urlToBase64(src)],  // 原始图片
})
```

---

## 使用场景

批量超分辨率处理分镜图片。在生成分镜后，将每个分镜 cell 的图片进行超分处理，提升图片分辨率到 1K，同时保持图片内容不变。处理后的图片保存到 OSS 的 `/${projectId}/chat/` 目录下。
