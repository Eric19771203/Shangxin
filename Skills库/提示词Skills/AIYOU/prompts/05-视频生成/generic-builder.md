# 通用多镜头提示词构建器 (GenericPromptBuilder)

> **源文件**: `services/promptBuilders/genericBuilder.ts` 第 51-82 行
> **类名**: `GenericPromptBuilder`
> **适用模型**: luma, runway, veo, minimax, volcengine, grok, qwen

## 系统指令原文

```
你是一个视频提示词格式化工具。只负责将分镜信息转换为指定格式，不添加任何额外内容。
```

## 用户输入格式

```
你是一位专业的视频提示词生成器。你的任务是将分镜信息转换为多镜头视频提示词格式。

分镜信息：

镜头 {shot.shotNumber} ({shot.duration}秒)
- 景别: {shot.shotSize}
- 拍摄角度: {shot.cameraAngle}
- 运镜方式: {shot.cameraMovement}
- 场景: {shot.scene || '未指定'}
- 视觉描述: {shot.visualDescription}
- 对白: {shot.dialogue || '无'}
- 视觉特效: {shot.visualEffects || '无'}
- 音效: {shot.audioEffects || '无'}

总时长：约 {totalDuration} 秒

输出要求：
1. 第一行输出统一风格声明：Style: {visualStyle}
2. 空一行后，依次输出每个 Shot
3. 每个 Shot 包含 duration、Scene、Dialogue（如有）、SFX（如有）字段
4. Scene 只描述视觉画面，不要重复风格信息
5. {preserveDialogue ? '对白原样保留，用 Dialogue 字段输出' : '忽略对白'}
6. 只输出多镜头格式，不要添加任何前缀、后缀、说明、建议或解释
7. 不要使用 "---" 分隔线
8. 不要添加"导演建议"、"色彩控制"等额外内容

输出格式示例：
Style: {visualStyle}

Shot 1:
duration: X.Xs
Scene: [场景描述]，[动作描述]
Dialogue: "对白内容"
SFX: [音效描述]

Shot 2:
duration: X.Xs
Scene: [场景描述]，[动作描述]
SFX: [音效描述]
```

## 输出格式说明

与 Sora2Builder 不同，GenericPromptBuilder 的输出格式包含：

1. **Style 声明** - 首行统一风格声明
2. **Shot 结构** - 每个 Shot 包含以下字段：
   - `duration` - 时长
   - `Scene` - 场景视觉描述
   - `Dialogue` - 对白（可选，当 preserveDialogue 为 true 且有对白时）
   - `SFX` - 音效（可选，当有音效时）

## 配置选项

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `visualStyle` | string | 'Cinematic, high quality, consistent style' | 视觉风格声明 |
| `preserveDialogue` | boolean | true | 是否保留对白 |
