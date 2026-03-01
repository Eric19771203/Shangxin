# Toonflow 提示词目录

本目录包含 Toonflow 项目中所有 AI 提示词的完整原文和使用说明，方便学习和修改。

---

## 目录结构

```
prompts/
├── README.md                    ← 本文件（目录索引）
├── PROMPTS.md                   ← 提示词总览文档
│
├── 01-outline/                  ← 大纲生成阶段
│   ├── outlineScript-main.md    ← 大纲主 Agent（协调者）
│   ├── outlineScript-a1.md      ← 大纲子 Agent AI1（故事家）
│   ├── outlineScript-a2.md      ← 大纲子 Agent AI2（编剧）
│   └── outlineScript-director.md ← 大纲子 Agent 导演
│
├── 02-script/                   ← 剧本生成阶段
│   ├── script.md                ← 剧本生成系统提示词（数据库）
│   └── script-user-template.md  ← 剧本生成用户消息模板（代码）
│
├── 03-storyboard/               ← 分镜生成阶段
│   ├── storyboard-main.md       ← 分镜主 Agent
│   ├── storyboard-segment.md    ← 分镜分段 Agent
│   ├── storyboard-shot.md       ← 分镜逐镜 Agent
│   └── generateImagePrompts.md  ← 图片提示词优化器
│
├── 04-assets/                   ← 资产生成阶段
│   ├── role-polish.md           ← 角色提示词润色（数据库）
│   ├── role-generateImage.md    ← 角色图片生成（数据库）
│   ├── scene-polish.md          ← 场景提示词润色（数据库）
│   ├── scene-generateImage.md   ← 场景图片生成（数据库）
│   ├── storyboard-polish.md     ← 分镜提示词润色（数据库）
│   ├── storyboard-generateImage.md ← 分镜图片生成（数据库）
│   ├── tool-polish.md           ← 道具提示词润色（数据库）
│   ├── tool-generateImage.md    ← 道具图片生成（数据库）
│   ├── assets-generate-templates.md ← 资产生成用户消息模板（代码）
│   └── assets-polish-templates.md   ← 资产润色用户消息模板（代码）
│
├── 05-video/                    ← 视频生成阶段
│   ├── video-main.md            ← 视频主提示词（数据库）
│   ├── video-startEnd.md        ← 首尾帧模式（数据库）
│   ├── video-multi.md           ← 宫格模式（数据库）
│   ├── video-single.md          ← 单图模式（数据库）
│   ├── video-text.md            ← 文本模式（数据库）
│   ├── motion-prompt.md         ← Motion Prompt 生成器（代码）
│   └── video-generate-user-template.md ← 视频生成用户消息模板（代码）
│
└── 06-utils/                    ← 工具类提示词
    ├── editImage.md             ← 图片编辑（代码）
    ├── batchSuperScore.md       ← 图片超分辨率（代码）
    ├── assets-filter.md         ← 资产筛选与映射（代码）
    └── generateImagePrompts-user-template.md ← 分镜提示词优化用户模板（代码）
```

---

## 提示词分类

### 数据库提示词（22个）

存储在 `t_prompts` 表中，通过 `customValue` 字段可覆盖默认值，**无需修改源码**。

| 阶段 | code | 名称 | 类型 |
|------|------|------|------|
| 大纲 | `outlineScript-main` | 大纲主Agent | mainAgent |
| 大纲 | `outlineScript-a1` | 大纲子Agent-AI1 | subAgent |
| 大纲 | `outlineScript-a2` | 大纲子Agent-AI2 | subAgent |
| 大纲 | `outlineScript-director` | 大纲子Agent-导演 | subAgent |
| 剧本 | `script` | 剧本 | system |
| 分镜 | `storyboard-main` | 分镜主Agent | mainAgent |
| 分镜 | `storyboard-segment` | 分镜分段Agent | subAgent |
| 分镜 | `storyboard-shot` | 分镜逐镜Agent | subAgent |
| 分镜 | `generateImagePrompts` | 图片提示词生成 | system |
| 资产 | `role-polish` | 角色润色 | system |
| 资产 | `role-generateImage` | 角色图片生成 | system |
| 资产 | `scene-polish` | 场景润色 | system |
| 资产 | `scene-generateImage` | 场景图片生成 | system |
| 资产 | `storyboard-polish` | 分镜润色 | system |
| 资产 | `storyboard-generateImage` | 分镜图片生成 | system |
| 资产 | `tool-polish` | 道具润色 | system |
| 资产 | `tool-generateImage` | 道具图片生成 | system |
| 视频 | `video-main` | 视频主提示词 | mainAgent |
| 视频 | `video-startEnd` | 首尾帧模式 | subAgent |
| 视频 | `video-multi` | 宫格模式 | subAgent |
| 视频 | `video-single` | 单图模式 | subAgent |
| 视频 | `video-text` | 文本模式 | subAgent |

### 代码硬编码提示词（9个）

内嵌在路由/工具文件中，修改需编辑源码。

| 文件 | 说明 |
|------|------|
| `02-script/script-user-template.md` | 剧本生成的用户消息模板 |
| `04-assets/assets-generate-templates.md` | 4种资产图片生成的用户消息模板 |
| `04-assets/assets-polish-templates.md` | 4种资产润色的用户消息模板 |
| `05-video/motion-prompt.md` | 静态分镜→动态Motion Prompt的系统提示词 |
| `05-video/video-generate-user-template.md` | 视频提示词生成的用户消息模板 |
| `06-utils/editImage.md` | 图片编辑的系统提示词 |
| `06-utils/batchSuperScore.md` | 图片超分辨率的提示词 |
| `06-utils/assets-filter.md` | AI资产筛选与映射提示词 |
| `06-utils/generateImagePrompts-user-template.md` | 分镜提示词优化的用户消息模板 |

---

## 创作管线流程

```
小说原文
  │
  ▼
┌─────────────┐
│ 01-outline   │  大纲生成（多Agent协作）
│              │  main → a1(故事家) + a2(编剧) → director(导演)
└──────┬───────┘
       │
       ▼
┌─────────────┐
│ 02-script    │  剧本生成
│              │  system提示词 + episode结构化数据 + 原文参考
└──────┬───────┘
       │
       ▼
┌─────────────┐
│ 03-storyboard│  分镜生成（多Agent协作）
│              │  main → segment(分段) → shot(逐镜) → 图片优化
└──────┬───────┘
       │
       ▼
┌─────────────┐
│ 04-assets    │  资产生成
│              │  润色提示词 → 生成图片（角色/场景/道具/分镜）
└──────┬───────┘
       │
       ▼
┌─────────────┐
│ 05-video     │  视频生成
│              │  Motion Prompt → 视频提示词（4种模式）→ 生成视频
└─────────────┘
```

---

## 修改指南

### 修改数据库提示词（推荐）

在系统设置中修改对应提示词的 `customValue` 字段即可覆盖默认值，优先级：`customValue` > `defaultValue`。

### 修改代码硬编码提示词

需编辑对应的 TypeScript 源文件，修改后需重新编译。各文件的具体修改位置已在对应的 `.md` 文件中标注。

### AI 模型配置

AI 模型通过 `t_aiModelMap` 表配置，每个功能组绑定不同的模型：

| 配置组 | 使用场景 |
|--------|----------|
| `outlineScriptAgent` | 大纲生成 |
| `generateScript` | 剧本生成 |
| `storyboardAgent` | 分镜Agent + 提示词优化 |
| `storyboardImage` | 分镜图片生成 + 超分 |
| `assetsPrompt` | 资产润色 |
| `assetsImage` | 资产图片生成 |
| `videoPrompt` | 视频提示词生成 |
| `editImage` | 图片编辑 |
