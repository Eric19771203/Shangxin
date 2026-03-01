# 🔄 双格式提示词转换指南

## Overview

本文件说明如何在 **Gemini 3 多宫格分镜提示词** 和 **Seance 2.0 视频生成提示词** 之间进行转换。

**用途**：灵活切换两种工作流，从导演预览到视频生成

---

## 📊 双格式对比总览

| 维度 | **Gemini 3 多宫格** | **Seance 2.0 视频** |
|------|-------------------|-------------------|
| **用途** | 导演快速预览、选择最佳分镜 | 直接生成可使用的 TVC 视频片段 |
| **输出格式** | 3×3 / 2×4 多宫格图像 | 15-60秒连续视频 |
| **画幅比** | 1:1 (正方形网格) | 16:9 (标准视频) |
| **关键要素** | 景别、运镜、构图、光影 | 时间、运动、连续性、物理真实 |
| **连续性** | 独立镜头，可对比 | 必须平滑衔接 |
| **标注需求** | 必须标注技术参数 | 可以隐含在描述中 |
| **交互性** | 静态，选择导向 | 动态，生成导向 |

---

## 🔄 转换流程：Gemini 3 → Seance 2.0

### 步骤 1：提取核心信息

从 Gemini 3 提示词中提取：
- ✅ 项目信息（产品、概念、时长、风格、色彩）
- ✅ 每个镜头的四大核心参数（景别、运镜、构图、光影）
- ✅ 视觉风格和色彩方案

### 步骤 2：添加视频专用要素

为每个镜头添加：
- ⏱️ **精确时间码**：0:00-0:01.5, 0:01.5-0:03, 等
- 🎬 **过渡设计**：到前一镜头和到下一镜头的过渡方式
- 🌊 **运动细节**：相机运动、物体运动、角色动作的更详细描述
- 🔦 **动态光影**：光线是否变化、如何变化
- 🌍 **环境互动**：主体与环境的关系

### 步骤 3：重构为序列格式

从网格布局转换为时间序列：
```
Gemini 3 (网格) → Seance 2.0 (序列)
Row 1, Col 1 → Shot 01 | 0:00-0:01.5
Row 1, Col 2 → Shot 02 | 0:01.5-0:03
Row 1, Col 3 → Shot 03 | 0:03-0:04.5
Row 2, Col 1 → Shot 04 | 0:04.5-0:06
...
```

---

## 📝 具体转换示例

### 示例：单个镜头转换

#### Gemini 3 原始提示词
```
[Shot 01], 
[Traditional Chinese painting detail, carmine red pigment on rice paper], 
[Shot Type: Extreme Close-Up (ECU)], 
[Camera Movement: Static, macro photography], 
[Composition: Rule of Thirds, pigment placed at left intersection], 
[Lighting: Soft side lighting, long shadows, chiaroscuro effect], 
[Visual Style: Supreme Sophistication, cinematic film look], 
[Color Palette: Mocha Mousse, warm chocolate brown, cream accents, gold highlights], 
[Mood: Mysterious, timeless, waiting to be awakened], 
--ar 1:1 --quality ultra --detail high
```

#### 转换为 Seance 2.0 提示词
```
[SHOT 01 | 0:00-0:01.5]
Type: Extreme Close-Up (ECU)
Movement: Static macro photography, no camera movement at all
Subject: Detail of traditional Chinese painting, carmine red pigment on rice paper
Action: Pigment appears frozen in time, extremely subtle light shift across paper surface, almost imperceptible movement
Environment: Dark, intimate studio space, black background, no other distractions
Lighting: Soft side lighting from left, long shadows, chiaroscuro effect, light quality remains consistent
Visual Style: Supreme Sophistication, cinematic film look
Color Palette: Mocha Mousse, warm chocolate brown, cream accents, gold highlights
Transition from previous: None (this is the opening shot)
Transition to next: Slow fade to black over 0.25 seconds at the end of the shot
Duration: 1.5 seconds exactly
Additional Notes: Film grain texture, 35mm film look, 24fps frame rate
--ar 16:9 --motion low --consistency ultra --quality ultra
```

---

### 转换对照表

| Gemini 3 元素 | Seance 2.0 对应元素 | 增强内容 |
|--------------|-------------------|---------|
| `[Shot XX]` | `[SHOT XX \| 0:00-0:01.5]` | 添加精确时间码 |
| `[Subject Description]` | `Subject: [description]` + `Action: [detailed action]` | 增加动作细节描述 |
| `[Shot Type: TYPE]` | `Type: TYPE` | 保持不变 |
| `[Camera Movement: MOVEMENT]` | `Movement: MOVEMENT + [detailed speed/trajectory]` | 增加速度和轨迹细节 |
| `[Composition: COMPOSITION]` | 隐含在 Environment/Subject 中 | 转换为环境描述 |
| `[Lighting: LIGHTING]` | `Lighting: LIGHTING + [dynamic changes]` | 增加光影变化描述 |
| `[Visual Style: STYLE]` | `Visual Style: STYLE` | 保持不变 |
| `[Color Palette: PALETTE]` | `Color Palette: PALETTE` | 保持不变 |
| `[Mood: MOOD]` | 隐含在整体描述中 | 转换为氛围描述 |
| `--ar 1:1` | `--ar 16:9` | 改为视频画幅 |
| （无） | `Transition from previous: TRANSITION` | 添加从前一镜头的过渡 |
| （无） | `Transition to next: TRANSITION` | 添加到下一镜头的过渡 |
| （无） | `Duration: X.X seconds` | 添加精确时长 |
| （无） | `Environment: description` | 添加环境描述 |
| （无） | `Additional Notes: details` | 添加技术细节 |

---

## 🔄 转换流程：Seance 2.0 → Gemini 3

### 步骤 1：提取核心信息

从 Seance 2.0 提示词中提取：
- ✅ 项目信息（产品、概念、风格、色彩）
- ✅ 每个镜头的景别、运镜、光影、视觉风格
- ✅ 去掉时间码、过渡、环境等视频专用要素

### 步骤 2：简化为多宫格格式

去掉视频专用要素，简化描述：
- ❌ 时间码
- ❌ 过渡设计
- ❌ 过度详细的运动描述
- ❌ 环境互动细节
- ❌ 物理真实的过度描述

### 步骤 3：重组为网格布局

从时间序列转换为网格：
```
Seance 2.0 (序列) → Gemini 3 (网格)
Shot 01 | 0:00-0:01.5 → Row 1, Col 1
Shot 02 | 0:01.5-0:03 → Row 1, Col 2
Shot 03 | 0:03-0:04.5 → Row 1, Col 3
Shot 04 | 0:04.5-0:06 → Row 2, Col 1
...
```

---

## 📝 完整转换示例

### 胭脂口红 色彩觉醒 完整转换

#### Gemini 3 → Seance 2.0 完整流程

**输入**：Gemini 3 多宫格提示词（见 `10-gemini3-storyboard-prompts.md`）

**转换过程**：
1. 提取 9 个镜头的核心信息
2. 为每个镜头添加时间码（1.5秒每个，共15秒）
3. 为每个镜头添加过渡设计（到前和到后）
4. 增强运动描述、光影变化、环境互动
5. 重组为时间序列格式
6. 添加整体技术要求

**输出**：Seance 2.0 视频生成提示词（见 `11-seance2-video-prompts.md`）

---

## 🎯 快速转换对照表

### 常用过渡方式

| Gemini 3 (静态) | Seance 2.0 (动态) | 使用场景 |
|----------------|------------------|---------|
| （无） | `Transition to next: Slow fade to black` | 开场、情感时刻 |
| （无） | `Transition to next: Hard cut, immediate` | 快节奏、活力 |
| （无） | `Transition to next: Match cut on [color/shape]` | 无缝、巧妙 |
| （无） | `Transition to next: Whip pan` | 动感、能量 |
| （无） | `Transition to next: Morph from A to B` | 变形、超现实 |

### 画幅比转换

| 用途 | Gemini 3 | Seance 2.0 |
|------|----------|-----------|
| 导演预览、选择 | `--ar 1:1` | （不适用）|
| 最终视频生成 | （不适用）| `--ar 16:9` |
| 社交媒体竖屏 | `--ar 9:16` | `--ar 9:16` |
| 宽银幕电影 | （不适用）| `--ar 2.39:1` |

### 参数调整

| Gemini 3 参数 | Seance 2.0 参数 | 说明 |
|-------------|---------------|------|
| `--quality ultra` | `--quality ultra` | 保持高质量 |
| `--detail high` | `--consistency ultra` | 改为连续性优先 |
| `--style raw` | `--style cinematic` | 改为电影风格 |
| （无）| `--motion [low/medium/high]` | 添加运动控制 |
| （无）| `--film-grain true` | 添加胶片质感 |

---

## ✅ 最佳实践检查清单

### Gemini 3 → Seance 2.0 转换检查
- [ ] 所有镜头都有精确时间码
- [ ] 每个镜头都有过渡设计（到前和到后）
- [ ] 运动描述更加详细和自然
- [ ] 增加了光影变化描述
- [ ] 增加了环境互动描述
- [ ] 画幅比改为 16:9
- [ ] 增加了整体技术要求
- [ ] 物理真实性考虑充分

### Seance 2.0 → Gemini 3 转换检查
- [ ] 去掉了所有时间码
- [ ] 去掉了过渡设计
- [ ] 简化了过度详细的描述
- [ ] 保留了四大核心参数
- [ ] 画幅比改为 1:1
- [ ] 网格布局清晰
- [ ] 风格统一便于对比

---

## 📚 相关文件

- **Gemini 3 多宫格提示词**：`references/10-gemini3-storyboard-prompts.md`
- **Seance 2.0 视频生成提示词**：`references/11-seance2-video-prompts.md`

---

## 💡 使用建议

### 推荐工作流

1. **第一步**：使用 Gemini 3 生成多宫格分镜
   - 快速预览多个方案
   - 导演选择最佳分镜

2. **第二步**：将选中的分镜转换为 Seance 2.0 格式
   - 使用本指南进行转换
   - 增加视频专用要素

3. **第三步**：使用 Seance 2.0 生成最终视频
   - 直接生成可使用的视频片段
   - 高质量、连续性好

---

*Version: 1.0 | Created: 2026-02-18 | Dual Format: Gemini 3 ↔ Seance 2.0*
