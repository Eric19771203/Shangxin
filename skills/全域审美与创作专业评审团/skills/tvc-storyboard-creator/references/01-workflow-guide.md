# TVC Storyboard Creator - Workflow Guide

## Complete 19-Step Workflow

This guide provides detailed instructions for each step of the TVC storyboard creation process.

---

## Step 1: Product Analysis

### Input Requirements
- Product images (1-10 images)
- Product description and specifications
- Key features and selling points
- Target audience description
- Any existing brand guidelines

### Analysis Process
1. **Visual Feature Extraction**
   - Identify product colors, shapes, materials
   - Note unique design elements
   - Assess visual quality and aesthetics

2. **Category Classification**
   - Map to e-commerce category (see ecommerce-categories.md)
   - Identify category-specific conventions

3. **Selling Point Prioritization**
   - Rank features by uniqueness
   - Identify emotional vs. functional benefits
   - Determine USP (Unique Selling Proposition)

4. **Audience Identification**
   - Demographics
   - Pain points and desires
   - Media consumption habits

### Output
Structured product profile with:
- Product category
- Visual characteristics
- 3-5 key selling points
- Target audience profile
- Recommended creative approach
- **Creative Tone Assessment (基调判断)** ⭐NEW

---

### Step 1.5: Creative Tone Assessment (自动分析) ⭐智能推荐

基于Step 1收集的产品信息，系统自动分析并判定创作基调：

#### 分析维度

**1. 产品类别倾向**
| 产品类别 | 故事性指数 | 产品性指数 | 推荐方向 |
|----------|-----------|-----------|----------|
| 美妆护肤 | 40% | 60% | 偏产品（质感展示） |
| 3C数码 | 30% | 70% | 产品性（科技展示） |
| 食品饮料 | 50% | 50% | 平衡（食欲+场景） |
| 家居生活 | 60% | 40% | 偏故事（生活方式） |
| 母婴用品 | 70% | 30% | 故事性（情感连接） |
| 奢侈品 | 20% | 80% | 强产品（工艺展示） |
| 服装配饰 | 45% | 55% | 平衡（穿搭+细节） |

**2. 核心卖点关键词分析**
```
情感关键词 → 故事性加分：
"温暖、家庭、爱、陪伴、回忆、梦想、自信"

功能关键词 → 产品性加分：
"成分、科技、工艺、材质、效果、创新、专利"

奢华关键词 → 高产品性：
"手工、限量、定制、传承、顶级、专属"
```

**3. 目标人群画像**
| 人群特征 | 推荐风格倾向 |
|----------|-------------|
| Z世代/年轻 | Bold Color Blocking, Vaporwave, Fashion Romantasy |
| 成熟女性 | Mocha Mousse, Prada Jewelry Style, 传统国画 |
| 商务人士 | 北欧极简, Sculptural Lighting, Wes Anderson |
| 潮流先锋 | Cyberpunk, Liquid Metal, 新海诚 |
| 传统保守 | 复古胶片, Xianxia, 迪士尼 |

**4. 价格带定位**
- **平价快消** → 故事性为主（情感共鸣）
- **中端品质** → 平衡型
- **高端奢华** → 产品性为主（ justify高价）

---

#### 智能推荐输出

基于以上分析，系统自动生成：

```
╔════════════════════════════════════════════════╗
║     🎯 智能基调判定结果                        ║
╠════════════════════════════════════════════════╣
║                                                ║
║  【产品】露华燕舍 鲜炖燕窝                      ║
║                                                ║
║  故事性 ◼◼◼◼◼◼◼◻◻◻  70%                      ║
║  产品性 ◼◼◼◼◼◼◻◻◻◻  60%                      ║
║                                                ║
║  💡 判定结论：平衡偏故事型                     ║
║                                                ║
║  📌 理由：                                    ║
║  • 传统滋补品类 → 需要文化背书                 ║
║  • 关键词"匠心、传承" → 情感价值             ║
║  • 目标人群30-50岁女性 → 注重品质生活          ║
║  • 中高端定位 → 可适度展示工艺               ║
║                                                ║
║  🎨 推荐视觉风格（Step 3将标注⭐）：          ║
║  ⭐ Mocha Mousse（2025年度色，契合滋养感）    ║
║  ⭐ 传统国画（文化背书）                      ║
║  ⭐ Wes Anderson（精致生活方式）              ║
║                                                ║
║  ⚖️ 推荐权重（Step 4建议）：                  ║
║     故事性 60% : 产品性 40%                   ║
║                                                ║
╚════════════════════════════════════════════════╝
```

---

## Step 2: Regional Selection

### Regional Options

| Region | Key Cultural Values | Visual Preferences | Considerations |
|--------|---------------------|-------------------|----------------|
| China | Family, status, tradition-modern blend | Red/gold, large scale, celebrity | Face/saving concept, avoid religion |
| Japan/Korea | Quality, detail, emotion | Minimalist, natural, soft tones | Soft-sell approach, avoid over-promising |
| Middle East | Family, religion, tradition | Warm tones, family scenes | Respect Ramadan, no alcohol/exposure |
| South Asia | Family, color, music/dance | Vibrant, group scenes, emotional | Avoid caste/religious conflicts |
| Western Europe | Quality, sustainability, individualism | Natural light, authentic, minimal | Avoid stereotypes, environmental focus |
| North America | Individual achievement, humor, speed | High contrast, direct, celebrity | Avoid discrimination, political topics |
| South America | Family,热情, music | Bright colors, warm atmosphere | Avoid poverty stereotypes |
| Africa | Community, optimism, heritage | Earth tones, nature, group scenes | Avoid poverty tourism |
| Eastern Europe/Russia | Heritage, strength, artistry | Cold tones, epic, artistic | Political sensitivity |

### Interaction Script
```
Based on the product analysis, which target region(s) would you like to focus on?

Options:
1. 🇨🇳 China
2. 🇯🇵 Japan / 🇰🇷 Korea
3. 🌙 Middle East
4. 🇮🇳 South Asia
5. 🇪🇺 Western Europe
6. 🇺🇸 North America
7. 🌎 South America
8. 🌍 Africa
9. 🇷🇺 Eastern Europe / Russia
10. 🌐 Global / Multiple Regions

Please select (1-10) or describe your preferred region(s):
```

---

## Step 2.5: Language Selection (INTERACTIVE)

### Output Language Options

| Language | Use Case | Terminology File |
|----------|----------|------------------|
| **中文** | China, Taiwan, Singapore, Malaysia | `zh.md` |
| **English** | Global, US, UK, Australia | `en.md` |
| **العربية (Arabic)** | Middle East, North Africa | `ar.md` |
| **Español (Spanish)** | Latin America, Spain, US Hispanic | `es.md` |
| **日本語 (Japanese)** | Japan market | `ja.md` |
| **한국어 (Korean)** | Korea market | `ko.md` |

### Selection Logic

- **Default**: Based on selected region (Chinese for China, Arabic for Middle East, etc.)
- **Bilingual**: Option for dual-language output (e.g., Chinese + English for export products)
- **Global**: English as universal fallback

### Interaction Script
```
Select output language for your storyboard:

1. 🇨🇳 中文 (Chinese)
2. 🇬🇧 English
3. 🇸🇦 العربية (Arabic)
4. 🇪🇸 Español (Spanish)
5. 🇯🇵 日本語 (Japanese)
6. 🇰🇷 한국어 (Korean)
7. 🌐 Bilingual (specify which two)

Current recommendation based on [selected region]: [Recommendation]

Please select (1-7):
```

---

## Step 3: Visual Style Selection

### Style Options

#### 1. Wes Anderson
- **Characteristics**: Symmetrical composition, pastel color palette, vintage aesthetic, quirky characters, centered framing
- **AI Keywords**: `symmetrical composition, pastel color palette, vintage aesthetic, centered framing, quirky characters, flat design, miniature style`
- **Best For**: Premium products, quirky brands, attention-grabbing

#### 2. Makoto Shinkai
- **Characteristics**: Photorealistic backgrounds, dramatic clouds/sky, golden hour lighting, lens flare, anime aesthetic, emotional depth
- **AI Keywords**: `Makoto Shinkai style, photorealistic background, dramatic clouds, golden hour lighting, lens flare, anime aesthetic, emotional atmosphere`
- **Best For**: Youth products, emotional storytelling, tech products

#### 3. Disney Animation
- **Characteristics**: Vibrant colors, expressive characters, magical atmosphere, smooth gradients, warm tones, fairy tale quality
- **AI Keywords**: `Disney animation style, vibrant colors, expressive characters, magical atmosphere, smooth gradients, warm tones, fairy tale aesthetic`
- **Best For**: Family products, aspirational brands, entertainment

#### 4. Traditional Chinese (水墨画)
- **Characteristics**: Ink painting style, negative space, landscape framing, monochrome with accent colors, poetic atmosphere
- **AI Keywords**: `traditional Chinese ink painting, negative space, landscape composition, monochrome, poetic atmosphere, brush stroke aesthetic`
- **Best For**: Traditional products, cultural heritage brands, luxury

#### 5. Xianxia (仙侠)
- **Characteristics**: Flowing robes, ancient architecture, ethereal lighting, magical effects, misty mountains, swords and cultivation
- **AI Keywords**: `xianxia fantasy style, flowing robes, ancient Chinese architecture, ethereal lighting, magical effects, misty mountains, Chinese fantasy`
- **Best For**: Chinese cultural products, gaming, aspirational

#### 6. Cyberpunk
- **Characteristics**: Neon lights, rain-soaked streets, high contrast, futuristic technology, dark atmosphere, blue/pink accents
- **AI Keywords**: `cyberpunk style, neon lights, rain-soaked streets, high contrast, futuristic technology, dark atmosphere, blue pink neon`
- **Best For**: Tech products, gaming, edgy brands

#### 7. Scandinavian Minimalist
- **Characteristics**: White backgrounds, natural lighting, clean lines, minimal props, hygge atmosphere, muted colors
- **AI Keywords**: `Scandinavian minimalism, white background, natural lighting, clean lines, minimal, hygge atmosphere, muted colors`
- **Best For**: Premium, eco-friendly, clean products

#### 8. Vintage Film
- **Characteristics**: Film grain, faded colors, nostalgic atmosphere, 35mm look, warm tones, imperfections
- **AI Keywords**: `vintage film grain, faded colors, nostalgic atmosphere, 35mm film look, warm tones, film grain texture, retro aesthetic`
- **Best For**: Heritage brands, authenticity, emotional

#### 9. Vaporwave
- **Characteristics**: Pink purple gradient, glitch art, retro-futuristic, 80s nostalgia, digital aesthetics
- **AI Keywords**: `vaporwave aesthetic, pink purple gradient, glitch art, retro-futuristic, 80s nostalgia, digital aesthetics, neon surreal`
- **Best For**: Youth, music, gaming, trendy products

---

### 2025-2026 Trending Styles ⭐NEW

#### 10. Bold Color Blocking
- **Characteristics**: Large flat color fields, high contrast, geometric composition, pop-art aesthetic
- **AI Keywords**: `bold color blocking, flat geometric background, vibrant colors, high saturation, minimalist composition, fashion editorial`
- **Best For**: Products with strong visual identity, fashion, beauty, making bold statement
- **Trend Source**: 2025-2026 Fashion Week, Valentino, Gucci campaigns

#### 11. Fashion Romantasy
- **Characteristics**: Tech meets nature, bioluminescent elements, AI-generated organic forms, dreamy tech aesthetic
- **AI Keywords**: `fashion romantasy, bioluminescent flowers, digital butterflies, crystal fiber optics, dreamy pastel tech, AI-generated nature`
- **Best For**: Future-forward brands, beauty tech, sustainable luxury
- **Trend Source**: 2025 Taipei Fashion Week "Fashion Romantasy" theme

#### 12. Prada Jewelry Style
- **Characteristics**: Black & white background/subject, product in vibrant selective color, high contrast, artistic portrait feel
- **AI Keywords**: `prada jewelry style, selective color, black and white background, product in vibrant color, high contrast, luxury fashion photography`
- **Best For**: Jewelry, premium cosmetics, luxury accessories
- **Trend Source**: Prada Couleur Vivante 2025 campaign

#### 13. Sculptural Lighting
- **Characteristics**: Light as composition, volumetric beams, dramatic shadows, light carving texture
- **AI Keywords**: `sculptural lighting, dramatic light beams, volumetric lighting, light carving texture, cinematic lighting, professional studio`
- **Best For**: Products where material quality is key, luxury goods, craftsmanship showcase
- **Trend Source**: 2025 beauty product photography trends

#### 14. Mocha Mousse (Pantone 2025)
- **Characteristics**: Warm chocolate brown, earthy luxury, sophisticated warmth, nourishing aesthetic
- **AI Keywords**: `mocha mousse pantone 2025, warm chocolate brown, earthy luxury, sophisticated warmth, natural elegance`
- **Best For**: Food, wellness, skincare, autumn/winter campaigns
- **Trend Source**: Pantone Color of the Year 2025

#### 15. Liquid Metal / Chrome
- **Characteristics**: Reflective surfaces, mirror-like quality, futuristic tech aesthetic, Y2K revival
- **AI Keywords**: `liquid metal texture, chrome reflections, futuristic aesthetic, y2k revival, mirror surfaces, high-tech glamour`
- **Best For**: Tech products, futuristic brands, youth-oriented campaigns
- **Trend Source**: 2026 future fashion trends

### Style Mixing

Users can request style mixing. Common combinations:
- Wes Anderson + Xianxia = Symmetrical ancient Chinese scenes
- Makoto Shinkai + Cyberpunk = Anime-style futuristic city
- Disney + Traditional Chinese = Animated ink style
- Vintage + Vaporwave = Retro-futuristic nostalgia
- **Bold Color Blocking + Sculptural Lighting** = Maximum product impact
- **Mocha Mousse + Prada Style** = Selective warm luxury

---

### Smart Recommendation Display ⭐基于Step 1.5分析

Based on the Creative Tone Assessment from Step 1.5, styles will be marked:

```
╔════════════════════════════════════════════════════════╗
║  🎨 视觉风格选择 (Visual Style Selection)              ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  【基于您的产品分析，智能推荐】                        ║
║                                                        ║
║  ⭐⭐⭐ 强烈推荐 (95%匹配度)                           ║
║  10. 🤎 Mocha Mousse                                   ║
║      理由: 产品类别"传统滋补" + 关键词"滋养"         ║
║           + 2025年度色契合"温暖、大地、滋养"感       ║
║                                                        ║
║  ⭐⭐ 高度推荐 (85%匹配度)                            ║
║  12. 💎 Prada Jewelry Style                           ║
║      理由: 中高端定位 + 需要展示产品质感             ║
║                                                        ║
║  ⭐ 适合考虑 (70%匹配度)                              ║
║  4. 🖼️ 传统国画                                       ║
║      理由: 文化类产品 + 目标人群30-50岁              ║
║                                                        ║
║  ──────────────────────────────────────────           ║
║  【其他可选风格】                                      ║
║  1. 🎬 Wes Anderson                                    ║
║  2. 🌌 Makoto Shinkai                                  ║
║  5. 🗡️ Xianxia                                         ║
║  ...                                                   ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

### Interaction Script
```
Select your preferred visual style:

【智能推荐】
⭐⭐⭐ 10. 🤎 Mocha Mousse - 2025年度色, 温暖滋养
⭐⭐  12. 💎 Prada Jewelry Style - 高级产品展示
⭐    4. 🖼️ 传统国画 - 文化背书

【全部风格】
经典风格:
1. 🎬 Wes Anderson - Symmetrical, pastel, vintage
2. 🌌 Makoto Shinkai - Anime, photorealistic sky
...

2025-2026趋势:
10. 🤎 Mocha Mousse - Pantone 2025, warm chocolate
11. ✨ Fashion Romantasy - Tech meets nature
12. 💎 Prada Jewelry Style - Selective color luxury
...

Or describe a style combination you'd like:
```

---

## Step 4: Narrative vs. Product Focus Selection (INTERACTIVE) ⭐CRITICAL

### Overview

Now that you've selected a visual style, determine how to execute it:
- **Story-focused**: Use the style for emotional narrative and world-building
- **Product-focused**: Use the style to showcase product details and craftsmanship

### Style-Weight Pairing Guide

| Visual Style | Recommended Weight | Rationale |
|--------------|-------------------|-----------|
| **Bold Color Blocking** | 70-90% Product | Graphic impact needs product focus |
| **Prada Jewelry Style** | 80-100% Product | Selective color technique is product-centric |
| **Sculptural Lighting** | 70-90% Product | Light sculpting is about product form |
| **Mocha Mousse** | 60-80% Product | Warm tones + product detail = luxury |
| **Wes Anderson** | 40-60% Balanced | Symmetry works for both story and product |
| **Makoto Shinkai** | 50-70% Story | Atmospheric style needs narrative context |
| **Xianxia** | 60-80% Story | Fantasy world requires scene-setting |

---

## Step 5: Duration Selection

### Duration Options

| Duration | Modules | Total Shots (6/15s) | Use Case |
|----------|---------|---------------------|----------|
| 15s | 1 | 4-6 | Social media, pre-roll |
| 30s | 2 | 8-12 | Standard TVC |
| 45s | 3 | 12-18 | Extended brand story |
| 60s | 4 | 16-24 | Hero content |

### Interaction Script
```
Select the total duration for your TVC:

1. ⏱️ 15 seconds (1 module, 4-6 shots)
   - Social media, YouTube pre-roll, quick impact

2. ⏱️ 30 seconds (2 modules, 8-12 shots)
   - Standard TVC, balanced storytelling

3. ⏱️ 45 seconds (3 modules, 12-18 shots)
   - Extended brand storytelling

4. ⏱️ 60 seconds (4 modules, 16-24 shots)
   - Hero content, brand film

Please select (1-4):
```

---

## Step 6: Pacing Recommendation

### Pacing Options

| Pacing | Shots per 15s | Time per Shot | Characteristics |
|--------|---------------|---------------|-----------------|
| Cinematic | 4 | 3.75s | Calm, premium, emotional |
| Standard | 6 | 2.5s | Balanced, versatile |
| Dynamic | 9 | 1.67s | Fast, energetic, attention |

### Selection Factors

**Cinematic (4 shots/15s)** recommended for:
- Premium/luxury products
- Emotional storytelling
- Complex narratives
- High-end brands

**Standard (6 shots/15s)** recommended for:
- Most e-commerce products
- Balanced information delivery
- General audience

**Dynamic (9 shots/15s)** recommended for:
- Tech products
- Fast-paced brands
- Attention-grabbing openings
- Youth audience

### Interaction Script
```
Based on [product category], [selected region], and [visual style], I recommend:

🎬 **[Recommended Pacing]** - [X shots per 15 seconds]

Rationale: [Explanation based on factors]

Options:
1. ✅ Confirm recommended pacing
2. 🔄 Switch to Cinematic (4 shots/15s)
3. 🔄 Switch to Standard (6 shots/15s)
4. 🔄 Switch to Dynamic (9 shots/15s)

Please confirm or select (1-4):
```

---

## Step 7: Creative Concept Generation

### Concept Structure

Each concept includes:

1. **Hook** (0-3s)
   - Attention-grabbing opening
   - Visual or narrative hook

2. **Core Insight** (3-10s)
   - Consumer truth or problem
   - Product solution

3. **Twist** (10-13s)
   - Unique angle or surprise
   - Emotional turn

4. **Payoff** (13-15s)
   - Product hero shot
   - Call to action

### Generation Process

1. Analyze product attributes
2. Consider regional cultural values
3. Apply visual style elements
4. Generate 3-5 distinct directions

### Concept Presentation Format

```
Concept 1: [Title]
━━━━━━━━━━━━━━━━━━━━━━━━
🎯 Hook: [Description]
💡 Insight: [Consumer truth]
✨ Twist: [Unique angle]
🎬 Tone: [Emotional quality]

[Why it works for [region] + [style]]
```

---

## Step 8: Concept Selection (INTERACTIVE)

### Interaction Script
```
Here are [X] creative concepts for your review:

[Present all concepts]

Please select:
1. ✅ Concept [X] - [Confirm]
2. 🔄 [Request modification of specific concept]
3. ✏️ [Request hybrid of multiple concepts]
4. 🆕 [Request all-new concept with direction]

Your choice:
```

---

## Step 9: Creative Weight Selection (INTERACTIVE)

### Traditional vs. Extraordinary Imagination

This step allows fine-tuning the creative direction balance:

#### Weight Scale

```
0% ─────────────────────────────────── 100%
传统/写实                              超凡想象/奇幻
Traditional/Realistic                  Extraordinary/Fantasy
```

| Weight | Approach | Description | Best For |
|--------|----------|-------------|----------|
| **0-20%** | Highly Traditional | Real-world scenarios, authentic situations, documentary style | Trust, authenticity, practical products |
| **21-40%** | Mostly Traditional | Realistic with slight stylization | Mainstream products, broad appeal |
| **41-60%** | Balanced | Mix of real and imaginative elements | Most products, versatile approach |
| **61-80%** | Mostly Extraordinary | Fantasy elements, surreal situations, high imagination | Entertainment, gaming, creative products |
| **81-100%** | Highly Extraordinary | Fully fantastical, magical realism, dreamlike | Luxury, aspirational, artistic brands |

#### Style-Specific Recommendations

| Visual Style | Default Weight | Rationale |
|--------------|----------------|-----------|
| Wes Anderson | 50-70% | Quirky but grounded |
| Makoto Shinkai | 70-90% | Fantasy anime world |
| Disney | 80-100% | Full fantasy |
| Traditional Chinese | 40-60% | Poetic realism |
| Xianxia | 90-100% | Full fantasy |
| Cyberpunk | 70-90% | Futuristic fantasy |
| Scandinavian | 20-40% | Minimal realism |
| Vintage Film | 30-50% | Nostalgic realism |
| Vaporwave | 60-80% | Retro-futuristic |

#### Regional Considerations

| Region | Recommended Range | Notes |
|--------|-------------------|-------|
| China | 50-80% | Mix acceptable, fantastical elements popular |
| Japan | 40-70% | Balance preferred, subtle fantasy |
| Middle East | 60-90% | Luxury/aspirational fantasy effective |
| South Asia | 70-100% | High drama, fantastical popular |
| Western Europe | 30-60% | Realism preferred, understated |
| North America | 40-70% | Moderate fantasy acceptable |
| South America | 60-90% | Emotional, colorful fantasy |
| Africa | 50-80% | Optimistic, aspirational fantasy |
| Eastern Europe | 40-70% | Moderate, artistic |

### Interaction Script
```
Adjust creative weight: Traditional ↔ Extraordinary Imagination

Based on your selections:
- Product: [Category]
- Region: [Region]
- Visual Style: [Style]

Recommended Weight: [X]% [Traditional/Extraordinary]

Scale:
0%  ─────┬─────┬─────┬─────┬─────  100%
      20%  40%  60%  80%
    Traditional      Extraordinary

Options:
1. ✅ Accept recommended: [X]%
2. 🎯 Traditional focus (20-40%)
3. ⚖️  Balanced (50%)
4. ✨ Extraordinary focus (70-90%)
5. 🔮 Full fantasy (100%)
6. ✏️ Custom percentage: [Input]

Your choice:
```

### Application to Concepts

Once weight is selected:
- **Traditional** (0-40%): Emphasize real scenarios, authentic moments, practical benefits
- **Balanced** (41-60%): Mix realistic setup with imaginative payoff
- **Extraordinary** (61-100%): Fantasy scenarios, magical transformations, dreamlike quality

---

## Step 10: Script Development

### Script Template

```
TIMELINE | SCENE | VISUAL | AUDIO | DURATION
----------|-------|--------|-------|----------
00:00-00:03 | Opening | [Visual description] | [VO/Narration] | 3s
00:03-00:06 | Setup | [Visual description] | [VO/Music] | 3s
...
```

### Elements Included

- **Scene descriptions**: Clear visual direction
- **Voiceover**: Scripted narration
- **Sound effects**: Environmental sounds
- **Music cues**: Background atmosphere
- **On-screen text**: Graphics and super
- **Timing**: Second-by-second breakdown

---

## Step 11: Script Confirmation (INTERACTIVE)

### Interaction Script
```
📜 Full Script Review
━━━━━━━━━━━━━━━━━━━━━━━━

[Present complete script with timing]

Please confirm:
1. ✅ Approve script, continue to storyboard
2. 🔄 Request specific changes: [Describe]
3. ✏️ Edit section: [Specify which part]

Your choice:
```

---

## Step 12: Storyboard Breakdown

### Shot Elements

Each shot includes:
- **Shot Number**: Sequential identifier
- **Timestamp**: Start and end time
- **Shot Type**: CU/MS/WS/ECU/etc.
- **Camera Movement**: Static/Pan/Tilt/Dolly/etc.
- **Visual Description**: Detailed scene description
- **Audio**: VO, SFX, Music cues
- **AI Prompt**: Generation prompt for images

---

## Step 13: Storyboard Logic Confirmation (INTERACTIVE)

### Interaction Script
```
🎬 Shot Breakdown
━━━━━━━━━━━━━━━━━━━━━━━━

[Present shot list in table format]

Shot count: [X] shots in [Y] seconds
Pacing: [Average time per shot]

Please confirm:
1. ✅ Approve breakdown, continue to details
2. 🔄 Adjust shots: [Specify changes]
3. ✏️ Reorder sequence: [Specify new order]

Your choice:
```

---

## Step 14: Detailed Storyboard Generation

### Output Format

| Shot | Time | Type | Movement | Description | Audio | AI Prompt |
|------|------|------|----------|-------------|-------|-----------|
| 01 | 0:00-0:03 | CU | Fixed | [Detailed description] | [VO text] | [Gemini 3 prompt] |

### AI Prompt Generation

For each shot, generate:
1. **Gemini 3 format**: JSON with model parameters
2. **Midjourney format**: Text prompt with parameters

---

## Step 15: Storyboard Confirmation (INTERACTIVE)

### Interaction Script
```
🎬 Complete Storyboard
━━━━━━━━━━━━━━━━━━━━━━━━

[Present full storyboard table]

AI prompts generated for: [X] shots

Please confirm:
1. ✅ Approve storyboard
2. 🔄 Modify specific shot: [Shot number]
3. ✏️ Adjust AI prompts: [Specify]
4. 🔁 Regenerate with different style

Your choice:
```

---

## Step 16: Narrative Review

### Review Checklist

1. **Narrative Coherence**
   - Do shots flow logically?
   - Is there a clear beginning/middle/end?
   - Are transitions smooth?

2. **Timing Accuracy**
   - Does total time match selected duration?
   - Are shot durations realistic?
   - Is pacing consistent?

3. **Information Hierarchy**
   - Is key message clear?
   - Are product features adequately shown?
   - Is CTA present and clear?

4. **Emotional Arc**
   - Does emotional tone progress appropriately?
   - Is there a satisfying payoff?

5. **Cultural Sensitivity**
   - Are regional values respected?
   - Any potential offensive elements?
   - Brand guidelines followed?

### Output Format

```
📋 Narrative Review Results
━━━━━━━━━━━━━━━━━━━━━━━━

✅ PASSED:
- [Item 1]
- [Item 2]

⚠️ SUGGESTIONS:
- [Issue 1]: [Recommendation]
- [Issue 2]: [Recommendation]

[If issues found, present for user decision]
```

---

## Step 17: Review Confirmation (INTERACTIVE)

### Interaction Script
```
📋 Review Complete
━━━━━━━━━━━━━━━━━━━━━━━━

[Present review results]

Please choose:
1. ✅ Accept suggestions and apply
2. 🔄 Keep original (accept risk)
3. ✏️ Make specific adjustments

Your choice:
```

---

## Step 18: Final Polish

Apply any approved changes:
- Modify shots based on feedback
- Update AI prompts
- Adjust timing
- Refine script

---

## Step 19: Final Output

### Document Components

1. **Header**: Project metadata
2. **Creative Concept**: Summary of selected concept
3. **Script**: Full script with timing
4. **Storyboard Table**: Complete shot breakdown
5. **AI Prompts**: Gemini 3 and Midjourney formats
6. **Technical Notes**: Production considerations
7. **Glossary**: Multi-language terminology (if applicable)

### Delivery Format

- Primary: Markdown (.md)
- Optional: Export to PDF/HTML

---

## Quick Reference

### Timing Standards

- 15s module = 4-9 shots
- Standard pacing (6 shots) = 2.5s per shot
- Minimum shot duration = 1.5s
- Transition time = 0.25-0.5s

### Regional Quick Guide

| Region | Do | Don't |
|--------|-----|-------|
| China | Red/gold, family, celebrity | Religion, politics |
| Japan | Quality focus, nature, soft-sell | Over-promising |
| Middle East | Family, Ramadan respect | Alcohol, exposure |
| US | Direct, humor, celebrity | Discrimination |

### Style Quick Keywords

| Style | Key Words |
|-------|-----------|
| Wes Anderson | Symmetrical, pastel, vintage |
| Shinkai | Sky, light, anime, emotional |
| Disney | Magic, color, character |
| Xianxia | Fantasy, mist, swords |
| Cyberpunk | Neon, rain, future |
