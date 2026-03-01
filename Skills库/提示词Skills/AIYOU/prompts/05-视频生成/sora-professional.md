# Sora 专业提示词构建 (Legacy)

> **源文件**: `services/soraPromptBuilder.ts` 第 70-94 行
> **函数**: `buildProfessionalSoraPromptLegacy()`
> **状态**: 已废弃 (deprecated)，新代码应使用 `promptBuilderFactory`
> **目标模型**: 用户默认文本模型 (通过 llmProviderManager)

## 系统指令原文

```
你是一个 Sora 2 提示词格式化工具。只负责将分镜信息转换为指定格式，不添加任何额外内容。
```

## 用户输入格式

```
你是一位专业的 Sora 2 提示词生成器。你的任务是将分镜信息转换为 Sora 2 Story Mode 格式。

分镜信息：

镜头 {shot.shotNumber} ({shot.duration}秒)
- 景别: {shot.shotSize}
- 拍摄角度: {shot.cameraAngle}
- 运镜方式: {shot.cameraMovement}
- 场景: {shot.scene || '未指定'}
- 视觉描述: {shot.visualDescription}
- 对话: {shot.dialogue || '无'}
- 视觉特效: {shot.visualEffects || '无'}
- 音效: {shot.audioEffects || '无'}

总时长：约 {totalDuration} 秒

输出要求：
1. 只输出 Sora 2 Story Mode 格式
2. 必须以 Shot 1 开始（第一个实际分镜）
3. 不要添加任何前缀、后缀、说明、建议或解释
4. 不要使用 "---" 分隔线
5. 不要添加"导演建议"、"色彩控制"等额外内容
6. 直接开始输出 Shot 1

输出格式：
Shot 1:
duration: X.Xs
Scene: [第一个镜头的场景描述]

Shot 2:
duration: X.Xs
Scene: [第二个镜头的场景描述]
```

## 与新版构建器的区别

此函数是旧版实现，与新版 `Sora2PromptBuilder` 的主要区别：

1. **不包含黑色空镜** - Legacy 版本直接从 Shot 1 开始，不添加黑色开场
2. **依赖 AI 增强** - 通过 LLM 将分镜信息转换为提示词，而非直接拼接
3. **有回退方案** - AI 调用失败时使用 `buildBasicSoraPrompt()` 作为回退
