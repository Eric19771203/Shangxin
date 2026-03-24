# 导演风格库 - Director Style Library

## 完整导演风格映射表

### 1. Denis Villeneuve（丹尼斯·维伦纽瓦）
**代表作**: Dune, Blade Runner 2049, Arrival  
**风格标签**: 史诗科幻、宏大构图、极简美学

```yaml
director_id: villeneuve
genre_match: [scifi, epic, war, drama]

visual_language:
  composition: [宏大构图, 极简美学, 留白, 对称]
  lighting: [自然光, 侧逆光, 丁达尔效应, 大气散射]
  camera: [缓慢推镜, 广角镜头, 航拍, 固定长镜头]
  color: 
    primary: [沙色调, 暖黄]
    secondary: [冷蓝, 深灰]
    grading: [去饱和, 高对比, 电影级调色]
  texture: [颗粒感, 胶片质感, 大气透视]

mood_keywords: [史诗感, 孤独感, 哲学性, 静谧, 压迫感, 敬畏]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，宏大构图，极简美学，自然光照射，
  大气透视效果，{{动作描述}}，缓慢推镜Dolly in，广角镜头，
  沙色调与冷蓝对比，电影级调色，颗粒质感，{{情感氛围}}，
  15秒总时长，24fps，8K分辨率，HDR，画面稳定无抖动

shot_preferences:
  wide_shot: 航拍下降建立场景规模
  medium_shot: 人物与环境的关系
  close_up: 情感凝视，眼神特写
  movement: 缓慢、 deliberate、有重量感

camera_movements:
  - "缓慢推镜 Dolly in"
  - "广角环绕 Orbital wide"
  - "航拍下降 Aerial descend"
  - "固定长镜头 Static long take"
  - "缓慢横移 Slow pan"

negative_prompt_additions:
  - "快速剪辑"
  - "手持晃动"
  - "饱和度过高"
  - "卡通风格"
```

---

### 2. Wong Kar-wai（王家卫）
**代表作**: In the Mood for Love, Chungking Express, 2046  
**风格标签**: 都市诗意、抽帧、霓虹美学

```yaml
director_id: wongkarwai
genre_match: [romance, urban, drama, noirlite]

visual_language:
  composition: [倾斜构图, 前景遮挡, 失焦, 反射倒影]
  lighting: [霓虹灯光, 路灯散射, 夜晚环境光, 剪影]
  camera: [缓慢横移, 手持晃动, 跟拍, 慢速推进]
  color:
    primary: [红, 绿]
    secondary: [黄, 蓝]
    grading: [高饱和, 对比强烈, 情绪化调色]
  texture: [颗粒感, 胶片感, 湿润反光]

mood_keywords: [孤独, 暧昧, 怀旧, 疏离, 都市疏离感, 诗意]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，王家卫电影风格，抽帧效果，
  霓虹灯光照射，玻璃倒影，{{动作描述}}，缓慢横移跟拍，
  红绿对比色调，夜晚都市氛围，湿润反光，{{情感氛围}}，
  15秒总时长，24fps，电影质感，情感氛围浓厚

shot_preferences:
  wide_shot: 雨夜街道，霓虹招牌
  medium_shot: 人物在人群中，疏离感
  close_up: 侧脸轮廓，眼神失焦
  movement: 缓慢、流动、情绪化

camera_movements:
  - "缓慢横移 Slow pan"
  - "手持晃动 Handheld"
  - "跟拍 Follow"
  - "慢速推进 Slow push"
  - "抽帧效果 Step printing"

negative_prompt_additions:
  - "明亮日光"
  - "清晰锐利"
  - "稳定固定"
  - "自然色调"
```

---

### 3. Steven Spielberg（史蒂文·斯皮尔伯格）
**代表作**: Saving Private Ryan, ET, Jurassic Park  
**风格标签**: 经典叙事、情感深度、流畅运镜

```yaml
director_id: spielberg
genre_match: [adventure, drama, war, family, scifi]

visual_language:
  composition: [经典三分法, 人物中心, 视线引导]
  lighting: [自然光, 柔和逆光, 魔法时刻, 戏剧光]
  camera: [流畅跟拍, 适度推镜, 稳定器, 主观镜头]
  color:
    primary: [暖调, 自然肤色]
    secondary: [根据类型变化]
    grading: [自然色调, 适度饱和]
  texture: [清晰锐利, 现代电影质感]

mood_keywords: [希望, 冒险, 情感共鸣, 奇观, 人性光辉]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，经典电影叙事风格，
  流畅自然的摄影，{{动作描述}}，稳定跟拍，
  温暖自然色调，情感丰富，{{情感氛围}}，
  15秒总时长，24fps，电影级品质，画面流畅

shot_preferences:
  wide_shot: 建立场景与人物关系
  medium_shot: 对话与互动
  close_up: 情感表达，眼神交流
  movement: 流畅、服务叙事、不炫技

camera_movements:
  - "流畅跟拍 Smooth follow"
  - "适度推镜 Gentle dolly"
  - "稳定器移动 Steadicam"
  - "主观镜头 POV"
  - "环绕展示 Reveal"

negative_prompt_additions:
  - "过度风格化"
  - "抽帧"
  - "手持晃动"
```

---

### 4. Christopher Nolan（克里斯托弗·诺兰）
**代表作**: Inception, Interstellar, The Dark Knight, Dunkirk  
**风格标签**: 非线性叙事、宏大场面、时间错位

```yaml
director_id: nolan
genre_match: [scifi, action, thriller, war, mindbender]

visual_language:
  composition: [复杂构图, 纵深透视, 对称, 几何线条]
  lighting: [高对比, 硬光, IMAX质感, 戏剧光]
  camera: [IMAX画幅, 实拍特技, 旋转, 倾斜]
  color:
    primary: [冷蓝, 金属灰]
    secondary: [暖橙, 火红]
    grading: [高对比, 冷暖对比]
  texture: [IMAX清晰度, 70mm胶片, 宏大质感]

mood_keywords: [烧脑, 紧张, 宏大, 时间压迫感, 智力挑战]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，诺兰电影风格，IMAX质感，
  宏大场面，{{动作描述}}，复杂构图，纵深透视，
  高对比光影，冷蓝与暖橙对比，70mm胶片质感，
  15秒总时长，24fps，宏大史诗感，{{情感氛围}}

shot_preferences:
  wide_shot: 城市折叠、宇宙尺度
  medium_shot: 人物在宏大环境中
  close_up: 紧张表情，时间压力
  movement: 旋转、倾斜、时空扭曲

camera_movements:
  - "IMAX画幅旋转"
  - "走廊旋转 Fight rotation"
  - "倾斜构图 Dutch angle"
  - "实拍特技 Practical"
  - "时间错位 Time shift"

negative_prompt_additions:
  - "CG感过重"
  - "柔和光线"
  - "小格局"
```

---

### 5. Ridley Scott（雷德利·斯科特）
**代表作**: Blade Runner, Alien, Gladiator, The Martian  
**风格标签**: 未来写实、氛围营造、真实质感

```yaml
director_id: scott
genre_match: [scifi, historical, thriller, adventure]

visual_language:
  composition: [细节丰富, 环境沉浸, 层级分明]
  lighting: [环境光, 烟雾, 体积光, 赛博朋克光]
  camera: [环境展示, 细节推进, 航拍]
  color:
    primary: [霓虹色, 金属色]
    secondary: [黑色, 深灰]
    grading: [高饱和霓虹, 暗调基底]
  texture: [真实质感, 做旧, 工业风]

mood_keywords: [未来感, 危险, 生存, 氛围沉浸, 细节控]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，雷德利斯科特风格，
  未来写实主义，赛博朋克灯光，烟雾氛围，
  {{动作描述}}，细节丰富，环境沉浸，
  霓虹色彩点缀暗调基底，工业质感，
  15秒总时长，24fps，电影级氛围

shot_preferences:
  wide_shot: 未来城市全景，环境展示
  medium_shot: 人物与环境互动
  close_up: 科技细节，表情特写
  movement: 环境探索，细节揭示

camera_movements:
  - "环境推进 Environment push"
  - "细节聚焦 Detail focus"
  - "航拍展示 Aerial"
  - "烟雾中穿行 Through haze"

negative_prompt_additions:
  - "过于干净"
  - "明亮日光"
  - "卡通风格"
```

---

### 6. Akira Kurosawa（黑泽明）
**代表作**: Seven Samurai, Rashomon, Ran  
**风格标签**: 武士美学、构图严谨、天气运用

```yaml
director_id: kurosawa
genre_match: [samurai, action, historical, drama]

visual_language:
  composition: [严谨对称, 几何构图, 多人物排列]
  lighting: [自然光, 逆光剪影, 烟雾, 阳光穿透]
  camera: [多机位, 快速剪辑,  telephoto压缩]
  color:
    primary: [根据类型：黑白或鲜艳]
    secondary: [大地色, 血迹红]
    grading: [高对比, 强烈黑白]
  texture: [胶片颗粒, 自然质感]

mood_keywords: [荣誉, 悲壮, 群体, 命运, 仪式感]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，黑泽明电影风格，
  严谨对称构图，自然光照射，逆光剪影，
  {{动作描述}}， telephoto镜头压缩感，
  高对比光影，电影级黑白或大地色调，
  15秒总时长，24fps，史诗仪式感

shot_preferences:
  wide_shot: 群体排列，地形展示
  medium_shot: 武士对决准备
  close_up: 眼神交锋，决心
  movement: 仪式感，群体动作

camera_movements:
  - "固定机位 Static"
  - "快速剪辑 Quick cuts"
  - " telephoto压缩"
  - "天气元素 Weather"

negative_prompt_additions:
  - "随意构图"
  - "柔光"
  - "现代感"
```

---

### 7. Stanley Kubrick（斯坦利·库布里克）
**代表作**: 2001 Space Odyssey, The Shining, A Clockwork Orange  
**风格标签**: 精确冷峻、对称构图、哲学性

```yaml
director_id: kubrick
genre_match: [scifi, horror, psychological, satire]

visual_language:
  composition: [严格对称, 一点透视, 几何精确]
  lighting: [高调光, 硬光, 单点光源]
  camera: [稳定平滑, 长镜头, 推轨]
  color:
    primary: [根据电影：红/白/太空黑]
    secondary: [对比色强调]
    grading: [精确控制, 概念化]
  texture: [超现实, 临床感, 完美主义]

mood_keywords: [不安, 超现实, 冷峻, 智力, 不安的平静]

seedance_prompt_template: |
  @参考图 {{主体描述}}，在{{场景}}，库布里克风格，
  严格对称构图，一点透视，几何精确，
  {{动作描述}}，稳定平滑推轨，长镜头，
  高调光影，超现实质感，
  15秒总时长，24fps，冷峻精确

shot_preferences:
  wide_shot: 严格对称走廊/空间
  medium_shot: 人物在几何环境中
  close_up: 凝视，内心特写
  movement: 平滑、冷漠、机械

camera_movements:
  - "平滑推轨 Smooth dolly"
  - "长镜头 Long take"
  - "对称跟拍 Symmetric follow"
  - "变焦 Zoom"

negative_prompt_additions:
  - "手持晃动"
  - "随意构图"
  - "温暖情感"
```

---

### 8-12. 其他导演

```yaml
# Guillermo del Toro
id: deltoro
genre: [fantasy, horror, fairytale]
keywords: [暗黑童话, 生物设计, 哥特美学, 机械与有机]
template: "@参考图 {{主体}}，在{{场景}}，吉尔莫德尔托罗风格，暗黑童话美学，精细生物设计，哥特氛围..."

# John Woo  
id: woo
genre: [action, crime, thriller]
keywords: [暴力美学, 慢动作, 双枪, 白鸽, 兄弟情]
template: "@参考图 {{主体}}，在{{场景}}，吴宇森风格，暴力美学，慢动作，双枪对峙，白鸽飞舞..."

# Sofia Coppola
id: coppola
genre: [drama, romance, coming_of_age]
keywords: [私密氛围, 轻柔, 空灵感, 粉色系, 青春期]
template: "@参考图 {{主体}}，在{{场景}}，索菲亚科波拉风格，私密氛围，轻柔空灵，粉色调..."

# Wes Anderson
id: anderson
genre: [comedy, drama, family]
keywords: [对称构图, 糖果色, 平面感, 童话风格]
template: "@参考图 {{主体}}，在{{场景}}，韦斯安德森风格，严格对称构图，糖果色调，平面感..."

# Hayao Miyazaki
id: miyazaki
genre: [animation, fantasy, adventure]
keywords: [手绘温暖, 自然, 飞行, 治愈, 吉卜力]
template: "@参考图 {{主体}}，在{{场景}}，宫崎骏风格，吉卜力美学，手绘质感，自然温暖..."
```

---

## 导演匹配算法

```python
def match_director(requirement, genre, tone, style_hint):
    """
    根据需求匹配最佳导演
    """
    scores = {}
    
    for director in director_library:
        score = 0
        
        # 类型匹配
        if genre in director.genre_match:
            score += 30
        
        # 情感基调匹配
        if tone in director.mood_keywords:
            score += 25
            
        # 风格提示词匹配
        if style_hint:
            for keyword in director.keywords:
                if keyword in style_hint:
                    score += 15
        
        scores[director.id] = score
    
    # 返回前三名
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]
```

---

*Director Style Library V1.0*
