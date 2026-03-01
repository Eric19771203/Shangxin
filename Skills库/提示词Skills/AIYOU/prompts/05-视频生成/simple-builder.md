# 简单文本提示词构建器 (SimpleTextBuilder)

> **源文件**: `services/promptBuilders/simpleBuilder.ts` 第 38-58 行
> **类名**: `SimpleTextBuilder`
> **适用模型**: 不与任何模型直接关联，适用于不支持多镜头格式的模型

## 系统指令原文

```
你是一个视频描述生成工具。负责将分镜信息转换为简洁的视频描述。
```

## 用户输入格式

```
请将以下分镜信息转换为一个流畅的视频描述：

分镜信息：

镜头 {shot.shotNumber} ({shot.duration}秒)
- 景别: {shot.shotSize}
- 拍摄角度: {shot.cameraAngle}
- 运镜方式: {shot.cameraMovement}
- 场景: {shot.scene || '未指定'}
- 视觉描述: {shot.visualDescription}
- 对话: {shot.dialogue || '无'}

总时长：约 {totalDuration} 秒

输出要求：
1. 生成一个简洁流畅的视频描述文本
2. 包含所有关键视觉信息
3. 不要添加任何前缀、后缀或解释
4. 直接输出描述文本
```

## 输出格式说明

与 Sora2Builder 和 GenericPromptBuilder 不同，SimpleTextBuilder 生成的是**一段连续的描述文本**，而非结构化的多镜头格式。

### 回退方案输出

当 AI 调用失败时，回退为基础格式：

```
1. (3.0s) 视觉描述内容
2. (2.0s) 视觉描述内容
3. (4.0s) 视觉描述内容
```
