# AIYOU Prompts 提示词资源目录

本目录包含 AIYOU 漫剧创作平台中所有 AI 提示词的**原文提取**和分类整理。

## 目录结构

```
prompts/
├── README.md                    # 本文件
├── AIYOU_PROMPTS_GUIDE.md       # 提示词总览与分析指南
│
├── 01-剧本创作/                  # 剧本大纲 & 分集剧本
│   ├── script-planner.md        # 剧本大纲生成提示词
│   └── script-episode.md        # 分集剧本生成提示词
│
├── 02-角色设计/                  # 角色提取、档案、表情图、三视图
│   ├── character-extraction.md  # 角色名提取
│   ├── character-profile.md     # 主角档案生成
│   ├── supporting-character.md  # 配角档案生成
│   ├── expression-sheet.md      # 表情图生成（3D/REAL/ANIME）
│   └── three-view-sheet.md      # 三视图生成（3D/REAL/ANIME）
│
├── 03-剧集分析/                  # 剧集分析 & 精炼
│   └── drama-analyzer.md        # 剧集深度分析
│
├── 04-分镜生成/                  # 电影分镜 & 详细分镜 & 增强
│   ├── cinematic-storyboard.md  # 电影级分镜
│   ├── detailed-storyboard.md   # 详细分镜脚本
│   └── shot-enhancer.md         # 分镜智能增强
│
├── 05-视频生成/                  # 各平台视频提示词构建
│   ├── video-orchestrator.md    # 视频编排提示词
│   ├── sora2-builder.md         # Sora 2 Story Mode 构建器
│   ├── generic-builder.md       # 通用多镜头构建器（Luma/Runway/Veo等）
│   ├── simple-builder.md        # 简单文本构建器
│   ├── sora-professional.md     # Sora 专业提示词（Legacy）
│   ├── sensitive-words.md       # 敏感词净化
│   └── video-templates.md       # 视频提示词模板（分镜图/电影感/Sora）
│
├── 06-图像处理/                  # 图片检测 & 修复
│   ├── text-detection.md        # 图片文字检测
│   └── image-restoration.md     # 图像高保真修复
│
├── 07-风格预设/                  # 场景/人物风格模板生成
│   ├── scene-style.md           # 场景风格模板
│   └── character-style.md       # 人物风格模板
│
├── 08-AI助手/                   # 助手面板系统指令
│   └── assistant-modes.md       # 多模式系统指令
│
└── 09-术语知识库/                # 影视术语常量定义
    └── storyboard-terms.md      # 景别/角度/运镜术语表
```

## 使用说明

- 每个 `.md` 文件包含对应提示词的**完整原文**，可直接复制使用或修改
- 文件顶部标注了原始源文件路径和行号，方便定位代码
- 提示词中的 `{变量名}` 为动态参数占位符，运行时由代码填充
- 修改提示词后需同步更新对应的源代码文件

## 提示词修改指南

1. 在本目录中修改提示词原文
2. 将修改后的内容复制到对应的源代码文件中
3. 测试验证效果
4. 更新 `AIYOU_PROMPTS_GUIDE.md` 中的说明（如有必要）

## 源文件对照表

| 提示词文件 | 源代码文件 | 行号范围 |
|-----------|-----------|---------|
| `01-剧本创作/script-planner.md` | `services/geminiService.ts` | 438-620 |
| `01-剧本创作/script-episode.md` | `services/geminiService.ts` | 622-707 |
| `02-角色设计/character-extraction.md` | `services/geminiService.ts` | 268-273 |
| `02-角色设计/character-profile.md` | `services/geminiService.ts` | 275-334 |
| `02-角色设计/supporting-character.md` | `services/geminiService.ts` | 336-387 |
| `02-角色设计/expression-sheet.md` | `services/promptManager.ts` | 27-229 |
| `02-角色设计/three-view-sheet.md` | `services/promptManager.ts` | 61-276 |
| `03-剧集分析/drama-analyzer.md` | `services/geminiService.ts` | 389-413 |
| `04-分镜生成/cinematic-storyboard.md` | `services/geminiService.ts` | 709-743 |
| `04-分镜生成/detailed-storyboard.md` | `services/geminiService.ts` | 745-923 |
| `04-分镜生成/shot-enhancer.md` | `services/shotEnhancer.ts` | 29-68 |
| `05-视频生成/video-orchestrator.md` | `services/geminiService.ts` | 415-436 |
| `05-视频生成/sora-professional.md` | `services/soraPromptBuilder.ts` | 70-94 |
| `05-视频生成/sensitive-words.md` | `services/soraPromptBuilder.ts` | 288-320 |
| `05-视频生成/generic-builder.md` | `services/promptBuilders/genericBuilder.ts` | 51-82 |
| `05-视频生成/simple-builder.md` | `services/promptBuilders/simpleBuilder.ts` | 38-58 |
| `05-视频生成/video-templates.md` | `services/promptManager.ts` | 283-447 |
| `06-图像处理/text-detection.md` | `services/geminiService.ts` | 231-241 |
| `06-图像处理/image-restoration.md` | `services/videoStrategies.ts` | 164-181 |
| `07-风格预设/scene-style.md` | `services/geminiService.ts` | 2311-2356 |
| `07-风格预设/character-style.md` | `services/geminiService.ts` | 2358-2407 |
| `08-AI助手/assistant-modes.md` | `components/AssistantPanel.tsx` | 183-190 |
| `09-术语知识库/storyboard-terms.md` | `constants/storyboardTerms.ts` | 1-261 |
