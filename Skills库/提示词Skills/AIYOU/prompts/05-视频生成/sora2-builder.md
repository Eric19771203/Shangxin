# Sora 2 提示词构建器 (Sora2PromptBuilder)

> **源文件**: `services/promptBuilders/sora2Builder.ts`
> **类名**: `Sora2PromptBuilder`
> **适用模型**: Sora

## 构建逻辑说明

Sora2PromptBuilder 是一个**直接构建器**，不调用 AI 增强，而是直接将中文分镜信息拼接为 Sora 2 Story Mode 格式。

## 输出格式

```
Shot 1:
duration: 0.5s
Scene: 纯黑空镜，无任何视觉内容

Shot 2:
duration: 3.0s
Scene: {shotSize}，{cameraAngle}，{cameraMovement}，{visualDescription}，[{visualEffects}]，"{dialogue}"，[{audioEffects}]
```

## 格式详解

### Shot 1 - 黑色空镜（可选）

当 `includeBlackScreen = true`（默认）时，会在开头插入一个黑色空镜：

```
Shot 1:
duration: {blackScreenDuration}s
Scene: 纯黑空镜，无任何视觉内容
```

- `blackScreenDuration` 默认值为 `0.5` 秒

### 后续 Shot - 实际分镜

每个实际分镜的 Scene 字段由以下部分用中文逗号连接组成：

1. **景别** (`shot.shotSize`) - 如：特写、中景、全景等
2. **拍摄角度** (`shot.cameraAngle`) - 如：视平、高位俯拍等
3. **运镜方式** (`shot.cameraMovement`) - 如：固定、横移等
4. **视觉描述** (`shot.visualDescription`) - 画面描述
5. **视觉特效** (`shot.visualEffects`) - 用方括号包裹，非"无"时添加
6. **对话** (`shot.dialogue`) - 用引号包裹，非"无"时添加
7. **音效** (`shot.audioEffects`) - 用方括号包裹，非"无"时添加

## 配置选项

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `includeBlackScreen` | boolean | true | 是否在开头添加黑色空镜 |
| `blackScreenDuration` | number | 0.5 | 黑色空镜时长（秒） |
