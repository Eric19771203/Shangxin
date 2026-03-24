# Seedance焚决项目组

## 项目定位
工业级AI视频生产联合引擎，整合Seedance 2.0导演系统与焚决制作系统，实现从创意到成片的全自动化流程。

## 核心能力
| 能力 | 说明 |
|------|------|
| **导演系统** | Seedance 2.0 融合版，支持12位大师风格匹配 |
| **制作系统** | 焚决1.0 影视制作系统，全链路自动化 |
| **分镜引擎** | 影视工业化分镜架构，Beat Board+Sequence Board分层设计 |
| **AI生成** | 图像+视频全栈生成能力 |
| **一致性控制** | 视觉一致性控制中枢，保证画面连贯性 |

## 目录结构
```
seedance-fenjue/
├── src/                # 核心代码
│   ├── seedance-director/    # Seedance 2.0导演融合系统
│   └── fenjue-system/        # 焚决1.0制作系统
├── docs/               # 文档
│   ├── Seedance系列手册
│   └── 焚决.md
├── templates/          # 模板
│   ├── 分镜模板
│   ├── 风格模板
│   └── 剧本模板
├── config/             # 配置文件
├── output/             # 生成结果输出
└── assets/             # 资源文件（参考图、音乐等）
```

## 工作流程
1. 创意输入 → Seedance导演系统生成风格+分镜
2. 分镜审核 → 焚决系统执行生成
3. 后期处理 → 一致性控制+剪辑
4. 成片输出 → 自动打包交付

## 快速开始
```
# 调用导演系统
openclaw skill run seedance-director-fusion --prompt "你的创意描述"

# 调用焚决生成
openclaw skill run fenjue --storyboard 分镜文件.json
```

## 版本
- Seedance：v2.0 焚梦融合版
- 焚决：v1.0
- 项目组版本：v1.0 2026-03-24
