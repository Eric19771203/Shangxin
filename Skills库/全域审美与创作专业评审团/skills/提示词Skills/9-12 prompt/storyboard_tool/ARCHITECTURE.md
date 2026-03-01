# CineBoard Pro - 系统架构逻辑

## 📐 整体架构

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           用户接口层 (Interface)                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐              │
│  │   命令行界面     │  │   Python API    │  │   测试脚本      │              │
│  │   (CLI)         │  │   (Import)      │  │   (Test)        │              │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘              │
└───────────┼────────────────────┼────────────────────┼────────────────────────┘
            │                    │                    │
            └────────────────────┼────────────────────┘
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          核心生成层 (Core Engine)                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    StoryboardGenerator                               │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐ │   │
│  │  │  模板系统    │  │  导演风格    │  │  语法规则    │  │  色彩风格  │ │   │
│  │  │  Templates  │  │  Directors  │  │   Grammar   │  │   Color   │ │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘ │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                 AIEnhancedGenerator (可选)                          │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │   │
│  │  │  LLM服务    │  │  图像生成    │  │  智能增强    │                 │   │
│  │  │  Gemini 3   │  │  聚合平台    │  │  AI优化      │                 │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          知识库层 (Knowledge Base)                            │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   内容类型库     │  │   导演风格库     │  │   分镜理论库     │             │
│  │  Content Types  │  │  Director Styles│  │ Storyboard Theory│             │
│  │                 │  │                 │  │                  │             │
│  │  • 电影类型     │  │  • 18位导演     │  │  • 参考书籍      │             │
│  │  • 短剧类型     │  │  • 风格模板     │  │  • 理论知识      │             │
│  │  • 漫剧类型     │  │  • 技巧应用     │  │  • 视觉术语      │             │
│  │  • TVC广告      │  │                 │  │                  │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐                                  │
│  │   色彩风格库     │  │   核心框架       │                                  │
│  │  Color Styles   │  │  Core Framework │                                  │
│  │                 │  │                 │                                  │
│  │  • 宋代古风     │  │  • 基础生成器    │                                  │
│  │  • 邵氏武侠     │  │  • 语法规则      │                                  │
│  │  • 赛博朋克     │  │  • 工具函数      │                                  │
│  │  • ...          │  │                 │                                  │
│  └─────────────────┘  └─────────────────┘                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          输出层 (Output)                                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   分镜方案       │  │   AI提示词       │  │   图像文件       │             │
│  │   Storyboard    │  │   AI Prompts    │  │   Images        │             │
│  │                 │  │                 │  │                 │             │
│  │  • 镜头列表     │  │  • 英文提示词    │  │  • 分镜图       │             │
│  │  • 景别角度     │  │  • 风格关键词    │  │  • 参考图       │             │
│  │  • 色彩演进     │  │  • 技术参数      │  │                 │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 🔄 数据流逻辑

### 1. 标准生成流程

```
用户输入
    │
    ├── 内容类型 (movie/short_drama/comic_drama/tvc)
    ├── 子类型 (war/art/thriller/action...)
    ├── 分镜板类型 (3x3/4x3)
    ├── 场景描述 (自然语言)
    └── 导演风格 (可选)
    │
    ▼
StoryboardGenerator
    │
    ├── 1. 选择模板
    │      └── 根据 (类型+子类型+板型) 选择对应模板
    │
    ├── 2. 应用导演风格
    │      └── 加载导演技巧 → 应用到每个镜头
    │
    ├── 3. 生成基础提示词
    │      └── 模板 + 场景描述 + 导演风格
    │
    ├── 4. 应用语法规则
    │      └── 30度原则/视线匹配/色彩演进
    │
    └── 5. 输出分镜方案
           │
           ├── shots: 镜头列表
           ├── prompts: AI提示词
           ├── color_evolution: 色彩演进
           └── director_info: 导演信息
```

### 2. AI增强流程（可选）

```
基础分镜方案
    │
    ▼
AIEnhancedGenerator
    │
    ├── 1. 检查AI服务可用性
    │      └── Gemini 3 / API聚合平台
    │
    ├── 2. AI提示词增强
    │      └── LLMService.enhance_storyboard_prompt()
    │          └── 输入: 基础提示词
    │          └── 处理: Gemini 3 优化
    │          └── 输出: 增强后提示词
    │
    ├── 3. 场景分析（可选）
    │      └── analyze_scene_with_ai()
    │
    └── 4. 图像生成（可选）
           └── ImageService.generate_storyboard_images()
               └── 输入: 提示词列表
               └── 处理: 聚合平台 → Midjourney/DALL-E/SD
               └── 输出: 图像URL列表
```

## 🧩 核心模块详解

### 1. StoryboardGenerator (generator.py)

**职责**: 基础分镜生成

```python
class StoryboardGenerator:
    # 核心方法
    generate(content_type, subtype, board_type, scene_description, director_style)
    
    # 内部流程
    1. _select_template()      → 选择分镜模板
    2. _apply_director_style() → 应用导演风格
    3. _generate_prompts()     → 生成AI提示词
    4. _apply_grammar_rules()  → 应用语法规则
    5. _build_color_evolution()→ 构建色彩演进
```

### 2. AIEnhancedGenerator (generator_ai.py)

**职责**: AI增强分镜生成

```python
class AIEnhancedGenerator(StoryboardGenerator):
    # 扩展方法
    generate(..., use_ai_enhancement=False, generate_images=False)
    generate_with_full_ai(...)  # 完全AI生成
    analyze_scene_with_ai(...)  # AI场景分析
    
    # AI服务
    llm_service: LLMService      # 语言模型
    image_service: ImageService  # 图像生成
```

### 3. 知识库系统

#### 3.1 导演风格库 (knowledge_base/director_styles/)

```
director_styles/
├── war_directors.py      # 战争片导演 (斯皮尔伯格、诺兰等)
├── art_directors.py      # 文艺片导演 (王家卫、小津安二郎等)
├── thriller_directors.py # 惊悚片导演 (芬奇、波兰斯基等)
├── action_directors.py   # 动作片导演 (吴宇森、斯科特等)
├── animation_directors.py# 动画导演 (宫崎骏、新海诚等)
├── modern_directors.py   # 现代导演 (维伦纽瓦、安德erson等)
└── __init__.py           # 统一接口
```

**数据结构**:
```python
class DirectorStyle:
    INFO: Dict          # 导演信息
    TECHNIQUES: Dict    # 拍摄技巧
    AI_PROMPT_TEMPLATE: str  # AI提示词模板
    
    apply_style(prompt) → styled_prompt
```

#### 3.2 内容类型库 (knowledge_base/)

```
knowledge_base/
├── movie/           # 电影类型
│   ├── war.py      # 战争片
│   ├── art.py      # 文艺片
│   ├── thriller.py # 惊悚片
│   └── ...
├── short_drama/    # 短剧类型
├── comic_drama/    # 漫剧类型
├── tvc/            # TVC广告类型
└── color_styles.py # 色彩风格库
```

**数据结构**:
```python
class ContentType:
    TEMPLATES: Dict     # 分镜模板
    GRAMMAR: Dict       # 语法规则
    SHOT_TYPES: List    # 推荐景别
    ANGLES: List        # 推荐角度
```

#### 3.3 分镜理论库 (knowledge_base/storyboard_theory/)

```
storyboard_theory/
├── books.py          # 参考书籍
├── theory.py         # 理论知识
├── visual_terms.py   # 视觉术语词典
└── __init__.py
```

### 4. AI服务层 (ai_services/)

```
ai_services/
├── config.py         # AI配置管理
├── llm_service.py    # 语言模型服务
│   ├── Gemini 3 API
│   └── API聚合平台
└── image_service.py  # 图像生成服务
    └── 聚合平台 → Midjourney/DALL-E/SD
```

**配置逻辑**:
```python
AIConfig:
    gemini_api_key: str         # Gemini 3 密钥
    aggregator_enabled: bool    # 是否启用聚合平台
    aggregator_api_key: str     # 聚合平台密钥
    image_provider: str         # 图像提供商
```

## 📊 核心数据结构

### 1. 分镜方案 (Storyboard)

```python
{
    "content_type": "movie",
    "subtype": "war",
    "board_type": "3x3",
    "template_name": "战争片-经典叙事-3x3",
    
    "shots": [
        {
            "index": 1,
            "name": "战场全景",
            "shot_type": "大远景(ELS)",
            "angle": "鸟瞰",
            "movement": "横移",
            "description": "...",
            "prompt": "...",           # AI提示词
            "enhanced_prompt": "...",  # AI增强后
            "image_url": "..."         # 生成图像
        }
    ],
    
    "color_evolution": [
        {
            "shot_index": 1,
            "emotion": "紧张",
            "primary_color": "#8B0000",
            "lighting": "冷色侧光"
        }
    ],
    
    "ai_enhanced": True,
    "images_generated": True
}
```

### 2. 导演风格 (DirectorStyle)

```python
{
    "id": "spielberg",
    "name": "史蒂文·斯皮尔伯格",
    "style": "沉浸式纪实",
    
    "techniques": [
        "手持摄影增强临场感",
        "低角度仰拍展现英雄主义",
        "..."
    ],
    
    "color_palette": {
        "primary": ["#8B7355", "#D2B48C"],
        "mood": "sepia_warm"
    },
    
    "ai_prompt_keywords": [
        "Steven Spielberg style",
        "immersive documentary",
        "..."
    ]
}
```

### 3. 色彩风格 (ColorStyle)

```python
{
    "name": "宋代古风",
    "primary_colors": ["#D4C4B0", "#B8A99A", "#9B8B7A"],
    "saturation": "low",
    "brightness": "medium",
    "contrast": "low",
    
    "ai_prompt_keywords": [
        "Song Dynasty aesthetic",
        "muted earth tones",
        "..."
    ]
}
```

## 🔌 扩展点设计

### 1. 添加新导演

```python
# 1. 在 director_styles/ 创建新文件
class NewDirector(DirectorStyle):
    INFO = {...}
    TECHNIQUES = {...}

# 2. 在 __init__.py 注册
ALL_DIRECTORS["new_director"] = NewDirector
```

### 2. 添加新色彩风格

```python
# 在 color_styles.py 添加
NEW_STYLE = ColorStyle(
    name="新风格",
    primary_colors=[...],
    ...
)

ALL_COLOR_STYLES["new_style"] = NEW_STYLE
```

### 3. 添加新AI提供商

```python
# 在 llm_service.py 添加新方法
def _call_new_provider(self, prompt, **kwargs):
    # 实现新提供商API调用
    ...
```

## 🎯 设计原则

1. **分层架构**: 接口层 → 核心层 → 知识库层 → 输出层
2. **模块化**: 每个功能独立模块，便于扩展
3. **可配置**: 通过环境变量/配置文件灵活配置
4. **向后兼容**: 基础功能不依赖AI服务
5. **插件化**: AI服务作为可选插件

## 📈 性能考虑

- **缓存机制**: AI生成结果可缓存
- **批量处理**: 支持批量生成图像
- **异步支持**: 图像生成可异步处理
- **降级策略**: AI服务不可用时自动降级
