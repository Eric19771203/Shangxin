## 方案概述

为分镜工具添加真实的大模型API调用功能，包括语言模型和图像生成模型。

## 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                    分镜工具核心 (Python)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  分镜生成器   │  │  导演风格应用 │  │  知识库查询  │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                 │                 │              │
│         └─────────────────┼─────────────────┘              │
│                           ▼                                │
│  ┌────────────────────────────────────────────────────┐   │
│  │              AI服务层 (ai_services/)                │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │   │
│  │  │ 语言模型服务 │  │ 图像生成服务 │  │ 配置管理   │ │   │
│  │  │ - OpenAI    │  │ - Midjourney│  │ - API密钥  │ │   │
│  │  │ - Claude    │  │ - DALL-E    │  │ - 模型选择 │ │   │
│  │  │ - 本地模型   │  │ - SD        │  │ - 参数设置 │ │   │
│  │  └─────────────┘  └─────────────┘  └────────────┘ │   │
│  └────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## 功能模块

### 1. 语言模型服务 (llm_service.py)
- 支持 OpenAI GPT-4/GPT-3.5
- 支持 Claude 3 (Anthropic)
- 支持本地模型 (Ollama/LM Studio)
- 功能：
  - 智能解析场景描述
  - 优化分镜提示词
  - 导演风格深度分析
  - 多轮对话优化

### 2. 图像生成服务 (image_service.py)
- 支持 Midjourney API
- 支持 DALL-E 3
- 支持 Stable Diffusion
- 支持本地 SD WebUI
- 功能：
  - 分镜图像生成
  - 风格一致性控制
  - 批量生成
  - 图像变体

### 3. 配置系统 (config.py)
- API密钥管理 (.env)
- 模型参数配置
- 服务提供商选择
- 成本控制和限制

### 4. 集成到生成器
- 可选启用AI增强
- 智能提示词优化
- 自动图像生成
- 结果缓存

## 文件结构

```
storyboard_tool/
├── ai_services/
│   ├── __init__.py
│   ├── llm_service.py      # 语言模型服务
│   ├── image_service.py    # 图像生成服务
│   ├── config.py           # 配置管理
│   └── prompts.py          # 提示词模板
├── .env.example            # 环境变量示例
├── config.yaml             # 配置文件
└── generator.py            # 集成AI服务
```

## 使用方式

```python
# 基础使用（不调用AI）
generator.generate(...)

# 启用AI增强
generator.generate(
    ...,
    use_ai_enhancement=True,
    generate_images=True
)
```

## 环境变量

```bash
# OpenAI
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-3-opus-20240229

# Midjourney
MIDJOURNEY_API_KEY=...
MIDJOURNEY_CHANNEL_ID=...

# Stable Diffusion
SD_WEBUI_URL=http://localhost:7860
```

请确认此方案，我将开始实现AI服务集成。