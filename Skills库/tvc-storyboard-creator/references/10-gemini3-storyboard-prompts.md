# 🎬 Gemini 3 多宫格分镜提示词专用指南

## Overview

本文件专门针对 **Gemini 3** 生成**3×3或2×4多宫格分镜图**的提示词优化。

**用途**：导演快速预览、选择最佳分镜方案

---

## 🎯 核心设计原则

### Gemini 3 的优势
- 强大的多模态理解能力
- 能同时处理文本和图像
- 1M tokens 长上下文支持
- 优秀的推理能力

### 多宫格分镜的关键要求
1. **网格布局**：3×3 或 2×4 清晰排列
2. **可对比性**：各镜头风格统一，便于选择
3. **信息完整**：每个镜头必须标注技术参数
4. **电影感**：专业的电影摄影风格

---

## 📐 系统提示词（Role Prompt）

### 完整的系统角色设定

```markdown
# 系统提示

你是一位获得过戛纳狮子奖的顶级TVC分镜设计师，拥有20年以上的专业经验。

## 核心能力
- 精通15+视觉风格（Wes Anderson、Makoto Shinkai、Cyberpunk等）
- 熟悉9大区域文化适配
- 掌握2026四大创意趋势
- 擅长15/30/45/60秒TVC节奏设计

## 任务目标
为TVC广告设计专业的多宫格分镜图，供导演选择最佳方案。

## 输出要求
1. **格式**：3×3或2×4的网格布局分镜图
2. **标注**：每个分镜必须标注技术参数
3. **风格**：统一的视觉风格，便于对比
4. **质量**：电影级摄影质量，专业构图

## 分镜四大核心参数（必须标注）

### 1. 景别 (Shot Type)
- **ECU (Extreme Close-Up)**：大特写，只有眼睛/嘴巴/细节
- **CU (Close-Up)**：特写，头部/手部
- **MS (Medium Shot)**：中景，胸部以上
- **LS (Long Shot)**：全景，全身
- **FS (Full Shot)**：大全景，环境与人

### 2. 运镜 (Camera Movement)
- **Static**：固定镜头
- **Push-in**：推镜，强调
- **Pull-out**：拉镜，揭示环境
- **Pan**：摇镜，左右观察
- **Tilt**：移镜，上下观察
- **Dolly**：推拉轨，跟随
- **Tracking**：跟拍，速度感
- **Crane**：升降镜，宏大

### 3. 构图 (Composition)
- **Rule of Thirds**：三分法，主体在交叉点
- **Symmetrical**：对称构图，庄重稳定
- **Leading Lines**：引导线，利用线条引导视线
- **Negative Space**：留白，极简风格
- **Centered Framing**：居中构图

### 4. 光影 (Lighting)
- **Three-Point Lighting**：三点布光，专业标准
- **Rembrandt Lighting**：伦勃朗光，三角形光斑
- **Chiaroscuro**：明暗对比，戏剧化
- **Side Lighting**：侧光，强调质感
- **Back Lighting**：逆光，轮廓光
- **Golden Hour**：黄金时刻，温暖柔和
- **Studio Lighting**：影棚布光，精准控制

---

## 输出格式要求

### 3×3 网格布局（9镜头）

```
┌─────────┬─────────┬─────────┐
│ Shot 01 │ Shot 02 │ Shot 03 │
│ Opening │ Reveal  │ Trans.  │
├─────────┼─────────┼─────────┤
│ Shot 04 │ Shot 05 │ Shot 06 │
│ Action  │ Emotion │ Metaphor│
├─────────┼─────────┼─────────┤
│ Shot 07 │ Shot 08 │ Shot 09 │
│ Brand   │ Hero    │ Payoff  │
└─────────┴─────────┴─────────┘
```

### 2×4 网格布局（8镜头）

```
┌─────────┬─────────┬─────────┬─────────┐
│ Shot 01 │ Shot 02 │ Shot 03 │ Shot 04 │
├─────────┼─────────┼─────────┼─────────┤
│ Shot 05 │ Shot 06 │ Shot 07 │ Shot 08 │
└─────────┴─────────┴─────────┴─────────┘
```

---

## 🎨 单镜头提示词模板

### 基础模板

```
[Shot XX], 
[Subject Description], 
[Shot Type: TYPE], 
[Camera Movement: MOVEMENT], 
[Composition: COMPOSITION], 
[Lighting: LIGHTING], 
[Visual Style: STYLE], 
[Color Palette: PALETTE], 
[Mood: MOOD], 
[Additional Notes: NOTES]
```

### 完整示例模板

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
[Additional Notes: Film grain texture, 35mm film look, no text overlay], 
--ar 1:1 --quality ultra --detail high
```

---

## 📚 完整多宫格提示词示例

### 示例 1：9镜头 3×3 网格（胭脂口红 色彩觉醒）

```
Generate a professional 3×3 storyboard panel for a 15-second TVC commercial:

## Project Information
- Product: 胭脂 - Chinese style luxury lipstick
- Concept: 色彩觉醒 (Color Awakening) - Awakening traditional Eastern colors
- Duration: 15 seconds, 9 shots
- Visual Style: Supreme Sophistication, New Chinese Luxury
- Color Palette: Carmine red (#9B2335), Gold (#D4AF37), Ink black (#1A1A1A)

## Grid Layout (3×3)

### Row 1 - Opening (Shots 01-03)
[Shot 01], [Ancient Chinese painting detail, carmine red pigment frozen in time], [Shot Type: ECU], [Camera Movement: Static macro], [Composition: Negative space, 80% empty], [Lighting: Soft side lighting, chiaroscuro], [Visual Style: Traditional Chinese ink painting], [Mood: Mysterious, still]

[Shot 02], [Split screen, traditional painting left, Tokyo neon lights right], [Shot Type: WS], [Camera Movement: Quick cross-cut], [Composition: Split screen, 50/50], [Lighting: Contrast between soft and harsh neon], [Visual Style: Cyberpunk meets classical], [Mood: Clash, awakening]

[Shot 03], [Luxury lipstick bullet emerging from case], [Shot Type: CU], [Camera Movement: Push-in + rotate], [Composition: Centered framing], [Lighting: Dramatic product lighting, gold highlights], [Visual Style: Supreme Sophistication], [Mood: Luxury, revelation]

### Row 2 - Development (Shots 04-06)
[Shot 04], [Model applying lipstick, transformation from ancient to modern], [Shot Type: MS], [Camera Movement: Tracking + morph], [Composition: Rule of Thirds], [Lighting: Warm to cool transition], [Visual Style: Fashion editorial], [Mood: Transformation, confidence]

[Shot 05], [Color particles exploding, traditional patterns merging with geometry], [Shot Type: ECU + rapid cuts], [Camera Movement: Dynamic, multiple angles], [Composition: Abstract, energetic], [Lighting: High contrast, saturated colors], [Visual Style: Surreal Pop-Art], [Mood: Energy, explosion]

[Shot 06], [Perfect lips with carmine red lipstick], [Shot Type: ECU], [Camera Movement: Static macro], [Composition: Centered], [Lighting: Soft beauty lighting], [Visual Style: Luxury beauty], [Mood: Sensual, perfect]

### Row 3 - Closing (Shots 07-09)
[Shot 07], [Model turning, background morphing from garden to skyscraper], [Shot Type: WS], [Camera Movement: 360° circular], [Composition: Wide angle, epic], [Lighting: Natural to city night transition], [Visual Style: Cinematic], [Mood: Empowerment, timeless]

[Shot 08], [Product hero shot, "胭脂" logo appearing], [Shot Type: CU], [Camera Movement: Static + logo animation], [Composition: Centered], [Lighting: Product lighting + gold rim light], [Visual Style: Supreme Sophistication], [Mood: Brand, luxury]

[Shot 09], [Confident model with product, space for slogan], [Shot Type: MS], [Camera Movement: Static], [Composition: Rule of Thirds], [Lighting: Fashion campaign lighting], [Visual Style: Editorial], [Mood: Confidence, perfection]

## Technical Requirements
- 3×3 grid layout, each panel clearly separated
- Each shot labeled with shot number and description
- All shots in consistent visual style for easy comparison
- Film grain texture, 35mm film look
- No text overlay on the images themselves
- Professional commercial photography quality
--ar 1:1 --quality ultra --detail high --style raw
```

---

## 🎯 按风格分类的提示词库

### 1. Wes Anderson 风格

```
[Shot XX], [Subject Description], [Shot Type: TYPE], [Camera Movement: MOVEMENT], [Composition: Symmetrical, centered framing], [Lighting: Flat, even lighting], [Visual Style: Wes Anderson, pastel color palette, vintage aesthetic, quirky], [Color Palette: Pastel pink, baby blue, butter yellow], [Mood: Whimsical, quirky, precise], --ar 1:1 --quality ultra
```

### 2. Makoto Shinkai 风格

```
[Shot XX], [Subject Description], [Shot Type: TYPE], [Camera Movement: MOVEMENT], [Composition: Rule of Thirds], [Lighting: Golden hour, dramatic clouds, lens flare], [Visual Style: Makoto Shinkai, photorealistic background, anime aesthetic, emotional], [Color Palette: Vibrant sky colors, warm oranges, deep blues], [Mood: Emotional, atmospheric, beautiful], --ar 1:1 --quality ultra
```

### 3. Supreme Sophistication 风格

```
[Shot XX], [Subject Description], [Shot Type: TYPE], [Camera Movement: MOVEMENT], [Composition: Negative space, minimalist], [Lighting: Three-point lighting, soft and cinematic], [Visual Style: Supreme Sophistication, cinematic film look, high-end luxury], [Color Palette: Mocha Mousse, warm chocolate, cream, gold], [Mood: Sophisticated, luxurious, restrained], --ar 1:1 --quality ultra
```

### 4. Cyberpunk 风格

```
[Shot XX], [Subject Description], [Shot Type: TYPE], [Camera Movement: MOVEMENT], [Composition: Dynamic angles], [Lighting: Neon lights, rain-soaked streets, high contrast], [Visual Style: Cyberpunk, futuristic, neon aesthetic], [Color Palette: Blue, pink, purple neon], [Mood: Edgy, futuristic, intense], --ar 1:1 --quality ultra
```

---

## 📋 快速选择模板

### 根据时长选择

| 时长 | 推荐网格 | 提示词模板 |
|------|---------|-----------|
| **15秒** | 3×3 (9镜头) | [使用上面的完整示例] |
| **30秒** | 3×3 (9镜头) 或 2×4 (8镜头) | [调整每个镜头的描述] |
| **45秒** | 2×4 (8镜头) + 1个备用 | [增加每个镜头的细节] |
| **60秒** | 2×4 (8镜头) + 4个备用 | [详细的叙事描述] |

### 根据风格选择

| 风格 | 关键词 | 提示词片段 |
|------|--------|-----------|
| **Wes Anderson** | `symmetrical, pastel, vintage, centered` | [使用Wes Anderson模板] |
| **Makoto Shinkai** | `golden hour, clouds, anime, emotional` | [使用Makoto Shinkai模板] |
| **Supreme Sophistication** | `minimalist, negative space, cinematic, luxury` | [使用Supreme Sophistication模板] |
| **Cyberpunk** | `neon, rain, futuristic, high contrast` | [使用Cyberpunk模板] |

---

## ✅ 最佳实践检查清单

### 生成前检查
- [ ] 已包含完整的系统提示词
- [ ] 明确了网格布局（3×3或2×4）
- [ ] 每个镜头都有四大核心参数
- [ ] 风格统一，便于对比
- [ ] 输出格式为 1:1 正方形

### 生成后检查
- [ ] 所有镜头风格统一
- [ ] 技术参数清晰可辨
- [ ] 网格布局规整
- [ ] 电影感充足
- [ ] 便于导演选择

---

## 🔄 与 Seance 2.0 的转换

本文件的提示词可以直接转换为 Seance 2.0 视频生成提示词，详见：
`references/11-seance2-video-prompts.md`
`references/12-prompt-dual-format-guide.md`

---

*Version: 1.0 | Created: 2026-02-18 | Optimized for: Gemini 3*
