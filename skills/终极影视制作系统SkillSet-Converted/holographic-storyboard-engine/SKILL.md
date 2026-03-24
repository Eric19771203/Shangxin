# SKILL: 终极全息影视分镜生成引擎 (Ultimate Holographic Storyboard Engine)

## 元数据
- **ID**: ultimate-storyboard-07
- **名称**: 终极全息影视分镜生成引擎
- **类型**: file
- **分类**: 分镜设计
- **标签": ["分镜", "引擎", "九宫格", "全息", "五维融合", "AI生成"]

## 描述
集成了**导演思维、摄影指导 (DP) 审美与 AIGC 提示词工程**的终极分镜生成引擎。接收来自上游五大子系统的数据，熔炼为**视觉连贯、风格统一、叙事精准**的9连张分镜提示词组。

## 五维数据熔炼协议

1. **剧情骨架 (From 故事架构大师)** - 决定画面的**张力 (Tension)** 和 **叙事重点 (Focal Point)**
2. **角色灵魂 (From 角色开发指南)** - 决定人物的**微表情 (Micro-expressions)** 和 **肢体语言 (Body Language)**
3. **视觉符号 (From 定妆生成系统)** - 决定人物的**几何轮廓 (Silhouette)** 和 **服道化细节 (Assets)**
4. **世界舞台 (From 环境叙事大师)** - 决定**光影逻辑 (Lighting Logic)** 和 **空间氛围 (Atmosphere)**
5. **画风宪法 (From 一致性控制中枢)** - 决定**渲染风格 (Art Style)**、**色彩映射 (Color Grading)** 和 **技术参数 (Tech Specs)**

## 九宫格分镜逻辑 (The 9-Grid Scene Protocol)

对于任何输入的"场景 (Scene)"，必须拆解为 **9个关键镜头**，形成完整叙事闭环：

1. **EST (Establishing Shot)** - 定场镜头，交代环境与氛围（侧重环境叙事）
2. **MASTER (Master Shot)** - 全景主镜头，交代人物与环境的位置关系（侧重站位）
3. **MED (Medium Shot)** - 中景，表现主角的核心动作或状态
4. **OTS (Over-The-Shoulder)** - 过肩/关系镜头，表现对话或对峙
5. **CU (Close-Up)** - 特写，捕捉关键情绪或微表情
6. **POV (Point of View)** - 主观视角，增强代入感
7. **INSERT (Detail Shot)** - 关键道具或细节特写（叙事线索）
8. **DYNAMIC (Low/High Angle)** - 极致角度，体现权力关系或动态张力
9. **MOOD (Atmospheric Shot)** - 空镜或背影，收束场景情绪

## 提示词构建范式

**输出结构**:
```markdown
**[Shot Type]**
/imagine prompt: [Global Art Style via Consistency Hub] + [Camera Angle/Lens] + [Subject (Character Visuals + Action)] + [Environment (Lighting + B-Roll Details)] + [Tech Parameters] --ar [Ratio] --stylize [Value]
```

## 启动逻辑
**请等待用户输入五大系统的源数据。一旦接收，立即按照"九宫格分镜"逻辑输出。**

## 示例演示

### 【模拟输入数据】

**1. 故事架构 (剧情)**:
- **场景**: 雨夜，霓虹贫民窟的拉面摊
- **冲突**: 落魄侦探"K"与线人"老瞎子"接头。K必须拿到存有证据的芯片，但警察正在逼近

**2. 角色开发 (表演)**:
- **K**: 疲惫、警惕、右手始终按在风衣下的枪套上
- **老瞎子**: 贪婪但恐惧，手指不停地敲击桌面（神经质）

**3. 定妆系统 (视觉)**:
- **K**: 湿透的旧战术风衣，义眼发出微弱红光，脸上有义体排异反应的伤痕
- **老瞎子**: 带着多镜片电子护目镜，身穿油腻的维修工连体服

**4. 环境叙事 (氛围)**:
- **环境**: 充满蒸汽和全息广告的狭窄巷弄，绿色和紫色的霓虹灯光反射在湿漉漉的地面
- **天气**: 酸雨暴雨

**5. 一致性中枢 (风格)**:
- **风格**: Cinematic Concept Art, Syd Mead meets Roger Deakins
- **色调**: Cyberpunk Noir, High Contrast, Bioluminescent accents
- **参数**: `--ar 2.39:1 --v 6.0 --style raw`

### 【系统输出：9组分镜头】

#### Shot 1: EST - 环境定调
> **分析**: 利用【环境叙事】建立压抑感，使用大俯拍展示渺小感
```
/imagine prompt: Cinematic concept art, Cyberpunk Noir style, extreme wide shot, high angle looking down into a narrow, rain-drenched alleyway, neon green and purple holographic advertisements reflecting on wet asphalt, steam rising from a small ramshackle ramen stall in the corner, heavy acid rain falling, distinct volumetric lighting, Syd Mead aesthetic, gloomy atmosphere --ar 2.39:1 --v 6.0 --style raw
```

#### Shot 2: MASTER - 关系确立
> **分析**: 交代K和老瞎子的位置，利用【角色开发】中的肢体语言
```
/imagine prompt: Cinematic concept art, two subjects at a ramen counter, medium long shot, Detective K stands with a weary posture, wearing a soaked tactical trench coat, The Old Blind Man sits hunched over in greasy mechanic overalls, steam from ramen bowls obscuring their faces slightly, silhouette interaction, dirty neon city background, heavy rain texture, moody chiaroscuro lighting --ar 2.39:1 --v 6.0 --style raw
```

*(Shot 3-9 按同样逻辑生成...)*

## 优化说明
1. **一致性锚点**: 每个Prompt强制调用统一风格和比例
2. **叙事完整性**: 从定场到特写再到离场，严格遵循电影剪辑逻辑
3. **多源融合**: 角色特征、动作、环境、剧情有机结合

## 使用场景
- 完整场景分镜生成
- 九宫格分镜创作
- 多系统数据融合
- 电影级分镜设计

## 调用方式
```
SKILL_CALL ultimate-storyboard-07
```
