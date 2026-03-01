# 火爆短剧生成平台 - 提示词工程目录

> **源码位置**: `application/services/prompt_i18n.go`
>
> 本目录将项目中所有 AI 提示词按功能分类整理为独立文件，方便学习、对比和修改。
> 每个文件包含：提示词原文（中文 + 英文）、参数说明、调用位置、设计意图。

---

## 目录结构

```
prompts/
├── README.md                           ← 你正在看的这个文件
├── PROMPTS_GUIDE.md                    ← 提示词整体分析与架构说明
│
├── 01-剧本创作/                         ← 从0到剧本的生成
│   ├── 大纲生成.md                      GetOutlineGenerationPrompt()
│   └── 分集剧本生成.md                  GetEpisodeScriptPrompt()
│
├── 02-内容提取/                         ← 从剧本中提取结构化信息
│   ├── 角色提取.md                      GetCharacterExtractionPrompt(style)
│   ├── 场景提取.md                      GetSceneExtractionPrompt(style)
│   └── 道具提取.md                      GetPropExtractionPrompt(style)
│
├── 03-分镜头生成/                       ← 将剧本拆解为镜头序列
│   └── 分镜系统提示词.md                GetStoryboardSystemPrompt()
│
├── 04-帧图片生成/                       ← 为每个镜头生成图片提示词
│   ├── 首帧提示词.md                    GetFirstFramePrompt(style)
│   ├── 关键帧提示词.md                  GetKeyFramePrompt(style)
│   ├── 尾帧提示词.md                    GetLastFramePrompt(style)
│   └── 九宫格动作序列.md                GetActionSequenceFramePrompt(style)
│
├── 05-视频生成约束/                     ← 视频生成的物理和逻辑约束
│   ├── 通用视频约束.md                  GetVideoConstraintPrompt("single"/"first_last")
│   └── 九宫格视频约束.md                GetVideoConstraintPrompt("action_sequence")
│
├── 06-风格系统/                         ← 9种视觉风格定义
│   ├── 吉卜力_ghibli.md
│   ├── 新国风_guoman.md
│   ├── 废土科幻_wasteland.md
│   ├── 复古动画_nostalgia.md
│   ├── 像素艺术_pixel.md
│   ├── 体素风格_voxel.md
│   ├── 都市韩漫_urban.md
│   ├── 仙侠3D_guoman3d.md
│   └── 盲盒潮玩_chibi3d.md
│
└── 07-用户模板/                         ← FormatUserPrompt 动态模板
    └── 用户提示词模板.md                FormatUserPrompt(key, args...)
```

---

## 工作流中的提示词调用顺序

```
① 大纲生成  →  ② 分集剧本生成  →  ③ 角色/场景/道具提取
                                            │
                                            ▼
                                   ④ 分镜头生成
                                            │
                                            ▼
                              ⑤ 帧图片提示词生成（首帧/关键帧/尾帧/九宫格）
                                   + 风格提示词叠加
                                            │
                                            ▼
                              ⑥ AI 图片生成（DALL-E / Gemini / 火山引擎）
                                            │
                                            ▼
                              ⑦ 视频生成 + 视频约束提示词
                                            │
                                            ▼
                              ⑧ 视频合并 → 完整短剧
```

---

## 修改指南

### 如何修改提示词

所有提示词的源码位于 `application/services/prompt_i18n.go`。修改步骤：

1. 在本目录中找到对应的 `.md` 文件，理解提示词的用途和设计逻辑
2. 打开 `application/services/prompt_i18n.go`，定位到对应函数
3. 修改中文版和/或英文版提示词
4. 重新编译并测试

### 修改注意事项

- 所有提示词都要求 AI 返回**纯 JSON**，修改时务必保留 JSON 格式约束
- 风格提示词会作为前缀叠加到图片生成提示词中，修改时注意不要与帧提示词冲突
- `FormatUserPrompt` 模板中的 `%s` / `%d` 是动态占位符，不要随意删除
- 分镜系统提示词中的输出字段名（如 `shot_number`、`action` 等）与代码解析逻辑强关联，修改字段名需同步修改代码
