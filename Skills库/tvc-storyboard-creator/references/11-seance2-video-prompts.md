# 🎬 Seance 2.0 视频生成提示词专用指南

## Overview

本文件专门针对 **Seance 2.0/Sora/Runway Gen-4** 生成**连续视频片段**的提示词优化。

**用途**：直接生成可使用的 TVC 视频片段

---

## 🎯 核心设计原则

### 视频生成模型的关键要求
1. **连续性**：镜头之间必须平滑衔接
2. **物理真实**：光照、材质、反射必须自然
3. **时间精确**：每个镜头有明确的时长
4. **运动自然**：相机运动、物体运动、角色动作要流畅
5. **声音设计**：虽然AI可能无法生成音频，但提示词应包含声音暗示

---

## 📐 系统提示词（Role Prompt）

### 完整的系统角色设定

```markdown
# 系统提示

你是一位专业的AI视频生成提示词工程师，为Seance 2.0/Sora/Runway Gen-4设计连续的视频提示词。

## 核心能力
- 精通视频生成的连续性和物理真实性
- 熟悉镜头之间的平滑过渡技巧
- 掌握相机运动、物体运动、角色动作的自然描述
- 理解光照、材质、反射的物理规律

## 任务目标
为TVC广告设计完整的连续视频提示词，每个镜头之间无缝衔接。

## 输出要求
1. **连续性**：每个镜头的提示词必须与前一个和后一个镜头平滑衔接
2. **时间明确**：每个镜头有精确的时长（如 0:00-0:01.5）
3. **运动自然**：包含相机运动、物体运动、角色动作
4. **物理真实**：确保物理规律合理，光照、材质、反射自然
5. **过渡设计**：每个镜头都要有到下一个镜头的过渡方式

## 视频七大核心要素（必须包含）

### 1. 时间码 (Timecode)
- **精确到0.1秒**：0:00-0:01.5, 0:01.5-0:03, 等
- **总时长控制**：15秒/30秒/45秒/60秒
- **镜头时长分配**：每个镜头1.5-5秒不等

### 2. 主体与动作 (Subject & Action)
- **主体描述**：清晰的主体描述
- **动作细节**：主体在做什么
- **运动速度**：慢速/中速/快速
- **物理真实**：符合物理规律

### 3. 相机 (Camera)
- **景别**：ECU/CU/MS/LS/FS
- **运镜**：Static/Push-in/Pull-out/Pan/Tilt/Dolly/Tracking/Crane
- **速度**：Slow/Medium/Fast
- **轨迹**：描述相机的运动轨迹

### 4. 环境 (Environment)
- **场景**：室内/室外/影棚
- **布置**：道具、装饰
- **氛围**：情绪氛围
- **与主体的关系**：主体与环境的互动

### 5. 光影 (Lighting)
- **光源**：自然光/人造光/混合光
- **方向**：顺光/侧光/逆光/顶光/底光
- **质量**：柔和/硬朗/散射
- **动态**：光线是否变化

### 6. 视觉风格 (Visual Style)
- **艺术风格**：Supreme Sophistication/Wes Anderson等
- **色彩**：Mocha Mousse/Cyberpunk等
- **质感**：胶片感/数字感/复古
- **画面比例**：16:9/2.39:1/9:16

### 7. 过渡设计 (Transition)
- **到前一镜头**：从上一镜头如何过来
- **到下一镜头**：如何过渡到下一镜头
- **过渡方式**：Fade/Cut/Whip/Morph/Match
- **匹配元素**：颜色/形状/动作匹配

---

## 输出格式要求

### 单个镜头提示词模板

```
[Timecode: 0:00-0:01.5], 
[Shot Type: Extreme Close-Up (ECU)], 
[Camera Movement: Static, macro photography], 
[Subject: Traditional Chinese painting detail, carmine red pigment on rice paper], 
[Action: Pigment appears to be breathing, subtle movement, light shifts across the paper], 
[Environment: Dark, intimate studio space], 
[Lighting: Soft, side lighting, long shadows, chiaroscuro effect], 
[Visual Style: Supreme Sophistication, cinematic film look, Mocha Mousse color palette], 
[Transition from previous: (None, this is opening shot)], 
[Transition to next: Slow fade to black, then reveal neon lights], 
[Duration: 1.5 seconds], 
[Additional Notes: Film grain texture, 35mm film look, 24fps], 
--ar 16:9 --motion high --consistency high --quality ultra
```

### 完整序列提示词模板

```
Generate a seamless 15-second TVC video with 9 continuous shots:

---
[SHOT 01 | 0:00-0:01.5]
Type: Extreme Close-Up (ECU)
Movement: Static macro
Subject: Traditional Chinese painting detail, carmine red pigment
Action: Pigment appears frozen in time, subtle light movement
Environment: Dark studio, intimate space
Lighting: Soft side lighting, chiaroscuro
Transition to next: Slow fade to black

---
[SHOT 02 | 0:01.5-0:03]
Type: Wide Shot (WS)
Movement: Quick cross-cut between scenes
Subject: Split screen - traditional painting left, Tokyo neon right
Action: Colors bleeding and merging between the two sides
Environment: Split screen, two worlds colliding
Lighting: Contrast between soft traditional and harsh neon
Transition from previous: Fade up from black
Transition to next: Match cut on color red

---
[SHOT 03 | 0:03-0:04.5]
Type: Close-Up (CU)
Movement: Push-in + rotating
Subject: Luxury lipstick bullet emerging from case
Action: Bullet rotates, color flows like liquid ink
Environment: Black void, product floating
Lighting: Dramatic product lighting, gold highlights
Transition from previous: Match cut on red color
Transition to next: Whip pan to model

---
[SHOT 04-09 - CONTINUE THIS PATTERN]

---
Overall Requirements:
- Total duration: 15 seconds, 9 shots, ~1.67s per shot
- Visual style: Supreme Sophistication throughout
- Color palette: Carmine red (#9B2335), Gold (#D4AF37), Ink black (#1A1A1A)
- Cinematic quality: Film grain, 35mm look, 24fps
- Seamless transitions between all shots
- Physically realistic lighting, reflections, and textures
- Smooth camera movements, natural object motion
--ar 16:9 --motion high --consistency ultra --quality ultra --style cinematic
```

---

## 🎨 过渡方式库

### 1. 切 (Cut)
```
Transition to next: Hard cut, immediate jump to next shot
Use cases: Fast pacing, energetic sequences
```

### 2. 淡 (Fade)
```
Transition to next: Slow fade to black, then fade up on next shot
Transition to next: Cross-fade, overlap both shots
Use cases: Slow pacing, emotional moments
```

### 3. 甩 (Whip Pan)
```
Transition to next: Whip pan from current subject to next subject
Use cases: Dynamic, energetic transitions
```

### 4. 匹配 (Match Cut)
```
Transition to next: Match cut on [color/shape/action/motion]
Example: Match cut on red color from lipstick to next shot
Use cases: Seamless, clever transitions
```

### 5. 变形 (Morph)
```
Transition to next: Morph from subject A to subject B
Use cases: Transformations, surreal moments
```

### 6. 推拉 (Push/Pull)
```
Transition to next: Push-in to detail, then pull out to reveal new scene
Use cases: Reveals, discoveries
```

---

## 📚 完整序列提示词示例

### 示例 1：胭脂口红 色彩觉醒 15秒（9镜头）

```
Generate a seamless 15-second TVC video with 9 continuous shots for 胭脂 lipstick:

## Project Information
- Product: 胭脂 - Chinese style luxury lipstick
- Concept: 色彩觉醒 (Color Awakening)
- Duration: 15 seconds
- Shots: 9 shots, ~1.67s each
- Visual Style: Supreme Sophistication, New Chinese Luxury
- Color Palette: Carmine red, Gold, Ink black
- Aspect Ratio: 16:9

---
[SHOT 01 | 0:00-0:01.5]
Type: Extreme Close-Up (ECU)
Movement: Static, macro photography, no camera movement
Subject: Detail of traditional Chinese painting, carmine red pigment on rice paper
Action: Pigment appears frozen in time, extremely subtle light shift across paper surface
Environment: Dark, intimate studio space, black background
Lighting: Soft side lighting from left, long shadows, chiaroscuro effect
Visual Style: Traditional Chinese ink painting meets cinematic film
Transition from previous: None (opening shot)
Transition to next: Slow fade to black over 0.25s
Duration: 1.5s
Notes: Film grain, 35mm, 24fps

---
[SHOT 02 | 0:01.5-0:03]
Type: Wide Shot (WS)
Movement: Quick cross-cut between two scenes, rapid but smooth
Subject: Split screen composition - left = traditional painting, right = Tokyo neon lights at night
Action: Colors bleeding and merging between the two sides, red pigment flows into neon lights
Environment: Split screen, two worlds colliding
Lighting: Contrast between soft traditional lighting and harsh neon lighting
Visual Style: Cyberpunk meets classical art, high contrast
Transition from previous: Fade up from black over 0.25s
Transition to next: Match cut on red color
Duration: 1.5s
Notes: Dynamic but controlled, 24fps

---
[SHOT 03 | 0:03-0:04.5]
Type: Close-Up (CU)
Movement: Slow push-in + subtle rotation
Subject: Luxury lipstick bullet emerging from elegant case
Action: Bullet rotates slowly, carmine red color flows like liquid ink on surface
Environment: Black void, product floating in space
Lighting: Dramatic product lighting, gold highlights on edges, three-point lighting
Visual Style: Supreme Sophistication, high-end luxury
Transition from previous: Match cut on red color from neon
Transition to next: Whip pan to the right
Duration: 1.5s
Notes: Film grain, 35mm, 24fps

---
[SHOT 04 | 0:04.5-0:06]
Type: Medium Shot (MS)
Movement: Tracking + smooth morph transition
Subject: Elegant Asian model applying lipstick
Action: Transformation from ancient Chinese costume to modern fashion while applying
Environment: Seamless morph from traditional interior to modern studio
Lighting: Warm golden light transitioning to cool fashion lighting
Visual Style: Fashion editorial, high-end beauty
Transition from previous: Whip pan lands on model
Transition to next: Rapid cut to color explosion
Duration: 1.5s
Notes: Smooth morph, 24fps

---
[SHOT 05 | 0:06-0:07.5]
Type: ECU + rapid cuts
Movement: Dynamic, multiple angles in quick succession
Subject: Color particles exploding, traditional Chinese patterns merging with modern geometry
Action: Abstract color explosion, particles flying, patterns interweaving
Environment: Abstract space, no ground, pure color and form
Lighting: High contrast, saturated colors, dynamic lighting
Visual Style: Surreal Pop-Art, energetic
Transition from previous: Rapid cut on movement
Transition to next: Slow fade to close-up
Duration: 1.5s
Notes: Multiple quick cuts but smooth, 24fps

---
[SHOT 06 | 0:07.5-0:09]
Type: Extreme Close-Up (ECU)
Movement: Static macro, no movement
Subject: Perfect lips with carmine red lipstick
Action: Subtle lip movement, light reflecting off glossy surface
Environment: Black background, focus only on lips
Lighting: Soft beauty lighting, subtle rim light
Visual Style: Luxury beauty photography
Transition from previous: Fade up from color explosion
Transition to next: Slow pull-back to reveal model
Duration: 1.5s
Notes: Shallow depth of field, creamy bokeh

---
[SHOT 07 | 0:09-0:10.5]
Type: Wide Shot (WS)
Movement: 360-degree circular movement around subject
Subject: Confident Asian model turning
Action: Model turns gracefully, background morphs from traditional garden to modern skyscraper
Environment: Seamless background transition from ancient to modern
Lighting: Natural daylight transitioning to city night lighting
Visual Style: Cinematic, epic
Transition from previous: Slow pull-back from lips
Transition to next: Match cut on movement
Duration: 1.5s
Notes: Smooth camera movement, 24fps

---
[SHOT 08 | 0:10.5-0:12]
Type: Close-Up (CU)
Movement: Static, subtle push-in
Subject: 胭脂 lipstick product hero shot, "胭脂" logo appearing
Action: Logo fades in elegantly, gold letters glowing slightly
Environment: Black background, product centered
Lighting: Product lighting + gold rim light, dramatic
Visual Style: Supreme Sophistication, luxury brand
Transition from previous: Match cut on model's movement
Transition to next: Slow fade to final shot
Duration: 1.5s
Notes: Film grain, 35mm, 24fps

---
[SHOT 09 | 0:12-0:15]
Type: Medium Shot (MS)
Movement: Static, no movement
Subject: Confident model holding lipstick, space for slogan overlay
Action: Model holds product, confident smile, holds pose
Environment: Clean studio, gradient background
Lighting: Fashion campaign lighting, soft and flattering
Visual Style: Editorial photography, high-end
Transition from previous: Fade up from product shot
Transition to next: None (final shot, holds for 3 seconds)
Duration: 3.0s
Notes: Holds for slogan, 24fps

---
Overall Technical Requirements:
- Total duration: EXACTLY 15 seconds
- Shot count: 9 shots
- Visual style consistency throughout
- Seamless transitions between ALL shots
- Physically realistic lighting, reflections, textures
- Smooth camera movements, natural motion
- Film grain texture, 35mm film look
- 24fps cinematic frame rate
- Supreme Sophistication aesthetic throughout
- Carmine red, gold, and black color palette
--ar 16:9 --motion high --consistency ultra --quality ultra --style cinematic --film-grain true
```

---

## 🎯 按风格分类的提示词库

### 1. Supreme Sophistication 风格

```
[Timecode: 0:00-0:01.5], 
[Shot Type: TYPE], 
[Camera Movement: MOVEMENT], 
[Subject: SUBJECT], 
[Action: ACTION], 
[Environment: Minimalist, clean, negative space], 
[Lighting: Three-point lighting, soft and cinematic], 
[Visual Style: Supreme Sophistication, cinematic film look, high-end luxury], 
[Color Palette: Mocha Mousse, warm chocolate, cream, gold], 
[Transition: TRANSITION], 
[Duration: 1.5s], 
--ar 16:9 --motion medium --consistency ultra --quality ultra
```

### 2. Cyberpunk 风格

```
[Timecode: 0:00-0:01.5], 
[Shot Type: TYPE], 
[Camera Movement: MOVEMENT], 
[Subject: SUBJECT], 
[Action: ACTION], 
[Environment: Rain-soaked streets, neon lights, futuristic city], 
[Lighting: Neon illumination, high contrast, reflections on wet surfaces], 
[Visual Style: Cyberpunk, futuristic, neon aesthetic], 
[Color Palette: Blue, pink, purple neon], 
[Transition: TRANSITION], 
[Duration: 1.5s], 
--ar 16:9 --motion high --consistency high --quality ultra
```

### 3. Wes Anderson 风格

```
[Timecode: 0:00-0:01.5], 
[Shot Type: TYPE], 
[Camera Movement: MOVEMENT, very precise and controlled], 
[Subject: SUBJECT], 
[Action: ACTION, whimsical and quirky], 
[Environment: Symmetrical, pastel colored, perfectly centered], 
[Lighting: Flat, even lighting, no shadows], 
[Visual Style: Wes Anderson, pastel color palette, vintage aesthetic], 
[Color Palette: Pastel pink, baby blue, butter yellow], 
[Transition: TRANSITION, symmetrical and precise], 
[Duration: 1.5s], 
--ar 16:9 --motion medium --consistency ultra --quality ultra
```

---

## 📋 快速选择模板

### 根据时长选择

| 时长 | 镜头数 | 提示词模板 |
|------|--------|-----------|
| **15秒** | 9镜头 | [使用上面的完整示例] |
| **30秒** | 12-15镜头 | [增加每个镜头的时长到2-2.5秒] |
| **45秒** | 15-18镜头 | [增加细节和叙事] |
| **60秒** | 18-24镜头 | [完整三幕式叙事] |

### 根据风格选择

| 风格 | 关键词 | 提示词片段 |
|------|--------|-----------|
| **Supreme Sophistication** | `minimalist, negative space, cinematic, luxury` | [使用Supreme Sophistication模板] |
| **Cyberpunk** | `neon, rain, futuristic, high contrast` | [使用Cyberpunk模板] |
| **Wes Anderson** | `symmetrical, pastel, vintage, centered` | [使用Wes Anderson模板] |

---

## ✅ 最佳实践检查清单

### 生成前检查
- [ ] 每个镜头都有精确的时间码
- [ ] 包含完整的七大核心要素
- [ ] 每个镜头都有过渡设计（到前和到后）
- [ ] 物理真实性考虑充分
- [ ] 输出格式为 16:9 视频

### 生成后检查
- [ ] 所有镜头之间平滑衔接
- [ ] 光照、材质、反射自然
- [ ] 相机运动流畅
- [ ] 物理规律合理
- [ ] 连续性良好

---

## 🔄 与 Gemini 3 的转换

本文件的提示词可以直接从 Gemini 3 多宫格提示词转换而来，详见：
`references/10-gemini3-storyboard-prompts.md`
`references/12-prompt-dual-format-guide.md`

---

*Version: 1.0 | Created: 2026-02-18 | Optimized for: Seance 2.0/Sora/Runway Gen-4*
