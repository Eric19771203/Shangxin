# 分镜工具 - 专业故事板生成系统

## 概述

这是一个专业的分镜工具，整合了电影、短剧、漫剧、TVC广告等多种视频类型的叙事知识和分镜技巧。根据用户输入的内容类型，自动生成符合专业标准的9宫格（3×3）或12宫格（4×3）分镜方案。

## 系统架构

```
storyboard_tool/
├── core/                       # 核心框架
│   ├── base_framework.py       # 3×3和4×3基础框架
│   └── grammar_rules.py        # 电影语法规则（30°原则、视线匹配等）
├── knowledge_base/             # 知识库
│   ├── movie/                  # 电影分类
│   │   ├── war.py              # 战争片
│   │   └── __init__.py         # 文艺片、悬疑片、动作片、爱情片
│   ├── short_drama/            # 短剧分类
│   │   └── __init__.py         # 打斗戏、感情戏、都市戏、悬疑戏
│   ├── comic_drama/            # 漫剧分类
│   │   └── __init__.py         # 战斗漫剧、恋爱漫剧、剧情漫剧
│   └── tvc/                    # TVC广告分类
│       └── __init__.py         # 产品型、品牌型、促销型、企业形象型
├── lens_library/               # 镜头语言库
│   └── shots.py                # 景别系统
├── generator.py                # 主生成器
├── examples/                   # 使用示例
│   └── example_usage.py        # 完整示例代码
└── README.md                   # 本文件
```

## 核心功能

### 1. 故事板框架

#### 3×3标准叙事板（精简节奏）
- 9格经典叙事结构
- 从空间建立到结局留白
- 适用于大多数叙事场景

#### 4×3沉浸式故事板（史诗节奏）
- 12格史诗结构
- 三行递进：世界展开→人物轨迹→冲突核心
- 适用于宏大叙事

### 2. 电影语法注入

- **30°原则**：相邻镜头角度差≥30°，避免跳切
- **视线匹配**：关键帧（第2/5/8格）保持视线连贯
- **动作轴线**：3×3用内三角轴线，4×3用Z型轴线
- **色调演进**：根据情感基调渐变
- **声景提示**：关键帧标注声音元素

### 3. 内容类型支持

#### 电影
- **战争片**：大规模场面调度、多线叙事、真实感
- **文艺片**：长镜头、情绪留白、美学构图
- **悬疑/惊悚片**：心理镜头、悬念递进、视觉误导
- **动作片**：快速剪辑、连贯动作、视觉冲击
- **爱情片**：情绪递进、眼神交流、浪漫构图

#### 短剧
- **打斗戏**：快节奏、蜂巢式叙事结构（预热→爆发→收尾）
- **感情戏**：眼神匹配、情绪积累、细节刻画
- **都市戏**：现代感、时尚构图、快节奏生活
- **悬疑戏**：黄金3秒钩子+情绪递进+高互动结尾

#### 漫剧
- **战斗漫剧**：速度线、冲击画面、动作分解
- **恋爱漫剧**：竖格强调、浪漫特效、情感递进
- **剧情漫剧**：起承转合、格子节奏、信息密度

#### TVC广告
- **产品功能型**：问题→解决方案→产品展示
- **品牌故事型**：情感共鸣→品牌价值→记忆点
- **促销型**：价格突出→限时紧迫→行动号召
- **企业形象型**：企业实力→社会责任→愿景

## 快速开始

### 安装

```bash
# 克隆或下载项目
cd storyboard_tool

# 无需额外依赖，纯Python实现
```

### 基本使用

```python
from generator import generate_storyboard, list_types

# 查看所有可用类型
print(list_types())

# 生成战争片分镜
result = generate_storyboard(
    content_type="movie",
    subtype="war",
    board_type="3x3",
    scene_description="诺曼底登陆场景"
)

# 打印结果
from generator import StoryboardGenerator
generator = StoryboardGenerator()
print(generator.format_output(result))
```

### 更多示例

```python
# 生成短剧分镜
result = generate_storyboard(
    content_type="short_drama",
    subtype="action",
    board_type="3x3"
)

# 生成漫剧分镜
result = generate_storyboard(
    content_type="comic_drama",
    subtype="romance",
    board_type="3x3"
)

# 生成TVC广告分镜
result = generate_storyboard(
    content_type="tvc",
    subtype="product",
    board_type="3x3",
    scene_description="护肤品广告"
)

# 使用4×3史诗叙事板
result = generate_storyboard(
    content_type="movie",
    subtype="war",
    board_type="4x3"
)
```

## 输出格式

### 3×3标准叙事板输出

```json
{
  "content_info": {
    "type": "movie",
    "subtype": "war",
    "board_type": "3x3",
    "scene_description": "诺曼底登陆场景"
  },
  "storyboard": {
    "template_name": "战争片标准3×3",
    "shots": [
      {
        "index": 1,
        "name": "战场全景",
        "shot_type": "大远景(ELS)",
        "angle": "俯视或平视",
        "movement": "缓慢横移或固定",
        "description": "展现战场规模，烟雾弥漫，远处火光",
        "sound": "环境音：炮火轰鸣，飞机轰鸣",
        "color": "desaturated，偏灰蓝或土黄",
        "prompt": "Epic war scene, vast battlefield, smoke and fire in distance..."
      },
      // ... 更多镜头
    ]
  },
  "grammar_rules": {
    "angle_30_rule": {...},
    "eyeline_match": {...},
    "action_axis": {...},
    "color_evolution": {...},
    "soundscape": {...}
  },
  "color_evolution": [...],
  "usage_guide": {...}
}
```

### 4×3史诗叙事板输出

```json
{
  "storyboard": {
    "template_name": "战争片史诗4×3",
    "rows": [
      {
        "name": "战争机器",
        "shots": [...]
      },
      {
        "name": "前线士兵",
        "shots": [...]
      },
      {
        "name": "战争创伤",
        "shots": [...]
      }
    ]
  }
}
```

## 高级功能

### 自定义提示词

```python
# 自定义某些镜头的提示词
custom_prompts = {
    1: "Custom wide shot of a futuristic city, cyberpunk style...",
    5: "Custom close-up of protagonist's face, determination..."
}

result = generator.generate(
    content_type="movie",
    subtype="action",
    board_type="3x3",
    custom_prompts=custom_prompts
)
```

### 导出为JSON

```python
generator.export_to_json(result, "my_storyboard.json")
```

### 查看色调演进

```python
colors = result['color_evolution']
for color in colors:
    print(f"镜头{color['shot_index']}: {color['emotion']} - {color['primary_color']}")
```

## 完整示例

运行示例文件查看所有功能：

```bash
cd examples
python example_usage.py
```

## 使用指南

### 1. 选择内容类型

根据你的创作内容选择合适的大类：
- `movie` - 电影
- `short_drama` - 短剧
- `comic_drama` - 漫剧
- `tvc` - TVC广告

### 2. 选择子类型

每个大类下有多个子类型，根据具体场景选择：
- 电影：`war`, `art`, `thriller`, `action`, `romance`
- 短剧：`action`, `emotion`, `urban`, `suspense`
- 漫剧：`battle`, `romance`, `story`
- TVC：`product`, `brand`, `promo`, `corporate`

### 3. 选择故事板类型

- `3x3` - 标准叙事板，适用于大多数场景
- `4x3` - 史诗叙事板，适用于宏大叙事

### 4. 使用生成的Prompt

每个镜头都包含一个AI图像生成提示词（Prompt），可用于：
- Midjourney
- DALL-E
- Stable Diffusion
- 其他AI绘画工具

### 5. 应用电影语法

系统会自动生成语法规则建议：
- 检查30°原则
- 确保视线匹配
- 维护动作轴线
- 调整色调演进
- 设计声景

## 技术细节

### 景别系统

- **ELS** - 大远景：史诗感、环境建立
- **LS** - 远景：人物全身、空间关系
- **FS** - 全景：完整展示、正式感
- **MLS** - 中全景：膝盖以上、社交距离
- **MS** - 中景：腰部以上、对话标准
- **MCU** - 中近景：胸部以上、情绪表达
- **CU** - 近景：头部肩部、情绪强烈
- **ECU** - 大特写：面部局部、心理深度

### 30°原则

相邻镜头角度差应≥30°，避免跳切造成的视觉跳跃。系统会自动计算并建议角度序列。

### 色调映射

- **平静**：冷色调，低饱和度
- **紧张**：暗色调，高对比度
- **喜悦**：暖色调，高饱和度
- **悲伤**：灰蓝色调，低饱和度
- **神秘**：深紫蓝色调
- **激情**：红橙色调，高饱和度
- **怀旧**：暖棕色调

## 扩展开发

### 添加新的内容类型

1. 在 `knowledge_base/` 下创建新的模块
2. 定义知识库类，包含 `CHARACTERISTICS` 和 `STORYBOARD_3X3`
3. 在 `generator.py` 的 `CONTENT_TYPES` 中注册

### 修改模板

编辑对应知识库文件中的 `STORYBOARD_3X3` 或 `STORYBOARD_4X3` 字典。

### 自定义语法规则

编辑 `core/grammar_rules.py` 中的规则类。

## 参考资料

### 电影理论
- 希区柯克分镜技巧
- 诺兰叙事结构
- 斯皮尔伯格场面调度

### 短剧创作
- 蜂巢式叙事结构
- 黄金3秒钩子
- 情绪递进技巧

### 漫剧分镜
- 日本漫画分镜技法
- 速度线运用
- 格子布局美学

### TVC广告
- 15秒/30秒广告结构
- AIDA模型
- 品牌故事叙述

## 许可证

MIT License

## 更新日志

### v1.0.0
- 初始版本发布
- 支持电影、短剧、漫剧、TVC四大类型
- 完整的3×3和4×3故事板框架
- 电影语法规则系统
- 色调演进建议
- 声景提示
