# SKILL: 剪辑思维与视觉桥接 (Editorial Thinking & Visual Bridging)

## 元数据
- **ID**: editorial-thinking-01
- **名称**: 剪辑思维与视觉桥接
- **类型**: file
- **分类**: 后期制作
- **标签": ["剪辑", "思维", "视觉桥接", "转场", "蒙太奇", "电影感"]

## 描述
基于好莱坞经典剪辑蒙太奇逻辑，提供镜头之间无缝衔接的"视觉桥接"方案。不依赖AI变形过渡，而是通过图形匹配、视线引导、动作接续等经典技法，确保镜头切换时如巧克力般丝滑流畅。

## 核心功能
1. 推轨穿透 (The Push-Through) - 空间穿越转场
2. 轴向跳切 (Axial Cut) - 动作连续性剪辑
3. 视线匹配 (Eyeline Match) - 主观视角衔接
4. 图形匹配 (Graphic Match) - 视觉元素转场
5. 烟雾转场 (Steam Wipe) - 遮挡式过渡
6. 光影突变 (Lighting Shock) - 情绪转换
7. 动作接续 (Action Match) - 动作连贯性
8. 留白剪辑 (The Void Cut) - 意境留白

## 场景衔接指引

### 1. 推轨穿透 [Shot 1] ➡️ [Shot 2]
**衔接逻辑**：镜头1向窗户推进直到窗框填满画面；镜头2从背影开始，仿佛穿过窗户进入室内。

**Shot 1 (End Prompt)**:
```
...camera continues to dolly forward, getting closer and closer to the station window until the window frame dominates the view.
```

**Shot 2 (Start Prompt)**:
```
...camera starts close behind the astronaut's dark silhouette, establishing the interior immediately.
```

### 2. 轴向跳切 [Shot 2] ➡️ [Shot 3]
**衔接逻辑**：利用举杯动作作为剪辑点。全景中刚要举杯，中景里杯子正好送到嘴边。

**Shot 2 (End Prompt)**:
```
...the astronaut begins to lift his elbow slightly, preparing to drink.
```

**Shot 3 (Start Prompt)**:
```
...the cup is already raised near the chin level, continuing the upward motion seamlessly.
```

### 3. 视线匹配 [Shot 3] ➡️ [Shot 4]
**衔接逻辑**：角色看向窗外 -> 观众看到他看的东西。

**Shot 3 (End Prompt)**:
```
...Luo Mo stops moving and stares intensely at a specific point outside the window. Rack focus to the reflection in his eye.
```

**Shot 4 (Start Prompt)**:
```
...Start with the view of Jupiter already in focus, matching the angle of his gaze.
```

### 4. 图形匹配 [Shot 4] ➡️ [Shot 5] ⭐ 最高级转场
**衔接逻辑**：利用木星的大红斑(圆)与茶杯里的漩涡(圆)进行视觉重叠。宏观与微观的极致对比。

**Shot 4 (End Prompt)**:
```
...Focus centers on the Great Red Spot of the flattened Jupiter, which is swirling slowly.
```

**Shot 5 (Start Prompt)**:
```
...Top-down angle or macro shot. The circular rim of the tea glass matches the position of Jupiter. The swirling tea leaves mimic the storm clouds.
```

### 5. 烟雾转场 [Shot 5] ➡️ [Shot 6]
**衔接逻辑**：利用茶杯升起的蒸汽遮挡镜头，再从蒸汽中浮现出角色脸部。

**Shot 5 (End Prompt)**:
```
...The steam rises thicker and moves towards the camera lens, slightly obscuring the view (natural fade out).
```

**Shot 6 (Start Prompt)**:
```
...The shot begins with a thin layer of steam/haze clearing, revealing the extreme close-up of the eyes.
```

### 6. 光影突变 [Shot 6] ➡️ [Shot 7]
**衔接逻辑**：Shot 6结尾光线突然变暗或变色，Shot 7以同样诡异的光线开始，伴随镜头倾斜。

**Shot 6 (End Prompt)**:
```
...Suddenly, a harsh shadow falls over the eyes. The warm light turns into a flat, unnatural red glow.
```

**Shot 7 (Start Prompt)**:
```
...Start with the Dutch angle tilt immediately. The room is already bathed in that same harsh red flat lighting.
```

### 7. 动作接续 [Shot 7] ➡️ [Shot 8]
**衔接逻辑**：Shot 7中角色伸手去触碰虚空，Shot 8直接接他的主观视角看这只手。

**Shot 7 (End Prompt)**:
```
...Luo Mo slowly raises his hand towards the camera/window as the room distorts.
```

**Shot 8 (Start Prompt)**:
```
...First person view. The hand is already raised in the frame, matching the previous motion, and begins to dissolve.
```

### 8. 留白剪辑 [Shot 8] ➡️ [Shot 9]
**衔接逻辑**：手部完全消失成粒子（画面变空/变亮），切到原本就空无一人的静物画面。

**Shot 8 (End Prompt)**:
```
...The hand completely dissolves into particles, leaving only the bright void of the 2D universe visible.
```

**Shot 9 (Start Prompt)**:
```
...Static shot. The empty chair and the tea flask. The light is consistent with the previous void, but now silence reigns.
```

## 后期剪辑建议

### 转场特效应用

| 转场类型 | 适用场景 | 特效建议 | 时长 |
|---------|---------|---------|------|
| Dissolve (叠化) | Shot 4→Shot 5 (木星变茶杯) | 让木星慢慢变成茶杯 | 0.5-1秒 |
| Hard Cut (硬切) | Shot 7→Shot 8 (崩塌到POV) | 视觉冲击力最强帧直接切断 | 即时 |

### 声音设计 (Sound Design)

| 镜头 | 音效建议 |
|-----|---------|
| 前3个镜头 | 微弱的机器嗡嗡声 |
| Shot 4 (木星) | 低频轰鸣声 (Low Rumble) |
| Shot 5 (茶杯) | 轰鸣声消失，变成清晰的倒水声或茶叶碰撞玻璃的清脆声 |
| Shot 9 (结尾) | 绝对寂静，只有秒针走动的一声"嗒" |

## 使用场景
- AI视频后期剪辑规划
- 镜头衔接设计
- 电影感转场创作
- 蒙太奇逻辑学习
- 视觉叙事提升

## 核心价值
> 有了这套衔接提示词，您的视频将不再是"9张动图的幻灯片"，而是一部**连贯流畅的微电影**。

## 调用方式
```
SKILL_CALL editorial-thinking-01
```
