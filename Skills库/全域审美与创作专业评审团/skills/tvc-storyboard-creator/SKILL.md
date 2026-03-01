---
name: tvc-storyboard-creator
version: 2.0.0
description: AI-powered TVC commercial storyboard generator for e-commerce products. Creates professional storyboard prompts with 15-second modular pacing, multi-regional cultural adaptation, visual style selection (Wes Anderson, Makoto Shinkai, Disney, Xianxia, etc.), multi-language support (Chinese, English, Arabic, Spanish, Japanese, Korean), and AI image generation prompts for Gemini 3 (Google) and Midjourney. Features interactive step-by-step confirmation workflow for creative direction, script development, storyboard breakdown, and final output in standard markdown format.
author: TVC Technical Team
license: MIT
---

# TVC Storyboard Creator v2.0

## Overview

This skill generates professional TVC commercial storyboard prompts from product images, descriptions, and requirements. It produces standardized storyboard documents with shot-by-shot breakdowns, timing, camera directions, and AI image generation prompts.

**Core Value Proposition**: Transform product inputs into production-ready storyboard documents with 95%+ automation accuracy.

## Key Features

- **15-Second Modular Pacing**: Storyboards designed for 15s/30s/45s/60s durations with 4/6/9 shots per 15s module
- **Multi-Regional Adaptation**: Culturally adapted creative for 9 global regions (China, Japan/Korea, Middle East, South Asia, Western Europe, North America, South America, Africa, Eastern Europe/Russia)
- **Visual Style Library**: 15+ distinct visual styles including:
  - Classic: Wes Anderson, Makoto Shinkai, Disney, Traditional Chinese, Xianxia
  - 2025-2026 Trends: Bold Color Blocking, Fashion Romantasy, Prada Jewelry Style, Sculptural Lighting, Liquid Metal
  - Niche: Cyberpunk, Scandinavian, Vintage Film, Vaporwave, Mocha Mousse
- **Style Mixing**: Ability to combine styles for unique creative directions
- **Multi-Language Support**: Chinese, English, Arabic, Spanish, Japanese, Korean with professional film terminology
- **AI-Ready Prompts**: Pre-built prompts for Gemini 3 (Google) and Midjourney image generation
- **Interactive Workflow**: Step-by-step confirmation at each stage (19+ interaction points)
- **Narrative vs. Product Focus**: Post-style-selection weight choice for optimal pairing
- **Smart Style Recommendation**: AI-powered analysis of product info to suggest best-fitting visual styles with confidence ratings

## When to Use This Skill

Use this skill when:
- Creating TVC commercials for e-commerce products
- Needing culturally adapted advertising for specific regional markets
- Requiring professional storyboard documents with shot breakdowns
- Generating AI image prompts for commercial production
- Producing multi-duration ads (15s/30s/45s/60s)
- Needing multi-language storyboard documentation

## System Requirements

- **Node.js**: >= 18.0.0
- **Runtime Environment**: Compatible with Claude, GPT-4, Gemini Pro
- **Memory**: Minimum 512MB available
- **File Access**: Read access to `./references/` and `./assets/` directories

## Workflow

### Step 1: Product Analysis
Analyze provided product images and descriptions to extract:
- Product category and type
- Core features and selling points
- Visual characteristics
- Target audience
- **Creative Tone Assessment (基调分析)** ⭐智能推荐

### Step 1.5: Smart Creative Analysis (自动) ⭐NEW
Based on detailed product information:
- Analyze product category tendencies (story vs. product focus)
- Parse selling point keywords (emotional vs. functional)
- Match target audience to visual styles
- **Generate style recommendations with confidence scores**
- Display in Step 3 with ⭐ rating system

### Step 2: Regional Selection (INTERACTIVE)
Present regional options and cultural considerations:
- China, Japan/Korea, Middle East, South Asia
- Western Europe, North America, South America
- Africa, Eastern Europe/Russia

Ask user to select target region(s).

### Step 2.5: Language Selection (INTERACTIVE)
Select output language for the storyboard document:
- Chinese, English, Arabic, Spanish, Japanese, Korean
- Bilingual options available
- Default based on selected region

### Step 3: 2026 Creative Trend Selection (INTERACTIVE) ⭐UPDATED
Based on 2026 Global TVC Trends Report, present trend direction options:

**Trend 1: Absurdist + High-Impact Narrative (荒诞无厘头+强爆点)**
- **Characteristics**: Anti-logic, surreal, unexpected twists every 5 seconds
- **Best for**: Breaking attention barriers, viral potential, social sharing
- **Structure**: 3s anti-logic hook → 2 absurdist reversals → divine product placement
- **Visual approach**: Surreal imagery, exaggerated performances, meme-worthy moments
- **Reference**: Coca-Cola 2026 "Nonsense Happiness Water" campaign

**Trend 2: Anime/IP Deep Integration (二次元IP深度绑定)**
- **Characteristics**: IP character world-building, easter eggs, original voice actors
- **Best for**: Gen Z engagement, fandom penetration, long-term brand affinity
- **Structure**: IP character personality + brand value alignment → narrative integration
- **Visual approach**: Anime aesthetics, game CG quality, original art style preservation
- **Reference**: Xiaomi × Genshin Impact 2026 collaboration

**Trend 3: Cinematic Industrial + Game CG (电影级工业化+游戏CG)**
- **Characteristics**: Unreal Engine 5, photorealistic CG, 3-act narrative in 15s
- **Best for**: High-tech products, futuristic positioning, immersive experiences
- **Structure**: Cinematic three-act structure even in short format
- **Visual approach**: AAA game graphics, virtual production, AI-assisted workflows
- **Reference**: BMW 2026 full CG campaign using Unreal Engine 5

**Trend 4: Ultimate Sophistication Aesthetic (极致高级感美学)**
- **Characteristics**: Minimalist composition, restrained color palette, film-grade lighting
- **Best for**: Luxury goods, premium positioning, emotional resonance
- **Structure**: Visual storytelling without words, texture-focused, breathing room
- **Visual approach**: 2.39:1 widescreen, 3-point lighting, tactile craft, warm personal style
- **Reference**: Dior 2026 Spring/Summer 60s no-dialogue campaign

**Hybrid Selection**: User can select primary trend or combine 2 trends (e.g., Absurdist + Sophistication for avant-garde luxury)

#### Option B: Supreme Sophistication Channel (顶级高级感专属通道) ⭐NEW
**For brands requiring "Advanced to the point of incomprehension" level sophistication**

**Core Philosophy**: 彻底抛弃商业叙事，用审美排他性、圈层筛选、哲学表达构建品牌精神护城河

**6条不可突破的底层铁律**:
1. 彻底抛弃"问题-解决方案"商业叙事模板
2. 放弃信息传递，只做情绪与哲学表达
3. 用"理解门槛"完成受众圈层筛选
4. 彻底反流量逻辑（拒绝3秒爆点）
5. 极致去品牌化（全程几乎无logo）
6. 彻底反大众审美（构建专属审美壁垒）

**14项核心技法**: 非线性叙事、隐喻符号、零台词、极致留白、去主体构图、极致克制色彩、电影级光影、超长慢镜头、零商业人声、极简配乐、ASMR微观音效、反流量节奏、零冲突高潮、全维度留白

**文档资源**:
- **核心理论**: `references/supreme-sophistication-channel/CORE-PHILOSOPHY-REPORT.md` (500+行，6条铁律+14项技法+完整理论体系)
- **40个案例**: `SUPREME-SOPHISTICATION-GUIDE.md` (香奈儿、苹果、爱马仕等，8维度拆解)
- **AI提示词**: `AI-PROMPTS-CHEATSHEET.md` (场景/时长/品牌全覆盖)
- **速查卡**: `CORE-PRINCIPLES-QUICK-CARD.md` (便携打印版)
- **快速启动**: `QUICK-START-GUIDE.md` (5分钟上手)
- **完整索引**: `INDEX.md` (资源导航)

**复制公式** (15/30/45/60秒):
- **15秒**: 3秒核心隐喻→8秒情绪意象→4秒品牌收尾
- **30秒**: 3秒定调→15秒意象→8秒沉淀→4秒品牌 (⭐推荐)
- **45秒**: 10秒建置→25秒意象→10秒品牌
- **60秒**: 电影三幕式 (15秒定调→25秒意象→20秒沉淀)

**Case Library Includes**:
- 20 × 30-second cases (cross-channel universal)
- 15 × 15-second cases (short video platforms)
- 5 × 45/60-second cases (luxury brand films)

**Reference**: `references/supreme-sophistication-channel/SUPREME-SOPHISTICATION-GUIDE.md`

Ask user to select creative direction: 2026 Trends OR Supreme Sophistication Channel.

### Step 3.5: Visual Style Selection Based on 2026 Trends (INTERACTIVE)
Present visual style options aligned with selected trend:

**For Trend 1 (Absurdist + High-Impact):**
- **Surreal Pop-Art** (Bold Color Blocking + Absurdist imagery)
- **Glitch Aesthetics** (Vaporwave + digital distortion)
- **Meme-Style Visuals** (Internet culture references, exaggerated proportions)
- **Anti-Logic Compositions** (Escher-style impossible spaces)

**For Trend 2 (Anime/IP Integration):**
- **Anime/Manga Style** (Cel-shading, dynamic lines, vibrant colors)
- **Game CG Realistic** (Unreal Engine 5, Genshin Impact quality)
- **Chibi/Cute Aesthetic** (Kawaii culture, super-deformed characters)
- **Anime + Live-Action Hybrid** (Who Framed Roger Rabbit style)

**For Trend 3 (Cinematic + Game CG):**
- **Unreal Engine 5 Photorealism** (AAA game graphics, ray-tracing)
- **Virtual Production** (LED volume, real-time rendering)
- **Cyberpunk Neon Noir** (Blade Runner aesthetics)
- **Sci-Fi Industrial** (Dune/Star Wars production design)

**For Trend 4 (Ultimate Sophistication):**
- **Mocha Mousse + Sculptural Lighting** (Pantone 2025 + dramatic light)
- **Minimalist Scandinavian** (White space, natural light, tactile textures)
- **Film Grain Analog** (Kodak Vision3, vintage cinema)
- **Japanese Wabi-Sabi** (Imperfect beauty, natural materials, muted tones)

**Classic Styles (Always Available):**
- Wes Anderson (symmetrical, pastel, vintage)
- Makoto Shinkai (anime, photorealistic backgrounds, dramatic sky)
- Disney (animated, vibrant, magical)
- Traditional Chinese (ink painting, landscape, monochrome)

Ask user to select visual style(s).

### Step 4: Narrative vs. Product Focus Selection (INTERACTIVE) ⭐CRITICAL
**This decision defines how to execute the selected visual style.**

Based on the chosen visual style, determine the creative execution:

**Option A: Story/Narrative-Focused (故事性强)**
- **Characteristics**: Emotional storytelling, character journey, scene-setting, atmosphere
- **Visual approach**: Wide shots, environmental context, character actions, narrative flow
- **Best for**: Brand building, emotional connection, lifestyle products
- **Works with styles**: Wes Anderson, Makoto Shinkai, Traditional Chinese, Xianxia

**Option B: Product/Performance-Focused (产品性强)** ⭐视觉冲击
- **Characteristics**: Product details, technical excellence, hyper-realistic description, visual impact
- **Visual approach**: Extreme close-ups, macro shots, lighting sculpting, texture emphasis
- **Best for**: Luxury items, tech products, beauty/skincare, showcasing craftsmanship
- **Works with styles**: Bold Color Blocking, Prada Jewelry Style, Sculptural Lighting, Mocha Mousse

**Option C: Balanced Hybrid (平衡型)**
- **Characteristics**: Both narrative context and product excellence
- **Visual approach**: Alternating between scene-setting and product detail
- **Best for**: Most commercial applications

**Style-Weight Pairing Guide**:
| Visual Style | Recommended Weight | Rationale |
|--------------|-------------------|-----------|
| Bold Color Blocking | 70-90% Product | Graphic impact needs product focus |
| Prada Jewelry Style | 80-100% Product | Selective color technique is product-centric |
| Sculptural Lighting | 70-90% Product | Light sculpting is about product form |
| Mocha Mousse | 60-80% Product | Warm tones + product detail = luxury |
| Wes Anderson | 40-60% Balanced | Symmetry works for both story and product |
| Makoto Shinkai | 50-70% Story | Atmospheric style needs narrative context |
| Xianxia | 60-80% Story | Fantasy world requires scene-setting |

This choice will influence:
- Shot composition (wide vs. close-up)
- Lighting style (atmospheric vs. sculptural)
- Pacing (narrative flow vs. impactful cuts)
- AI prompt emphasis

### Step 5: Duration Selection (INTERACTIVE)
Ask user to select total duration:
- 15 seconds (1 module, 4-6 shots)
- 30 seconds (2 modules, 8-12 shots)
- 45 seconds (3 modules, 12-18 shots)
- 60 seconds (4 modules, 16-24 shots)

### Step 6: Pacing Recommendation (INTERACTIVE)
Based on product category, regional preferences, and visual style, recommend pacing:
- Cinematic/Slow (4 shots per 15s)
- Standard (6 shots per 15s)
- Fast/Dynamic (9 shots per 15s)

Ask user to confirm or adjust.

### Step 7: Creative Concept Generation
Generate 3-5 creative concept directions based on:
- Product attributes
- Regional cultural values
- Selected visual style
- Target audience insights

Each concept includes:
- Hook (attention-grabbing opening)
- Core insight (consumer truth)
- Twist (unique angle)
- Emotional tone

### Step 8: Concept Selection (INTERACTIVE)
Present 3-5 concepts with explanations. Ask user to select or request modifications.

### Step 9: Creative Imagination Weight (INTERACTIVE)
Adjust the balance between Traditional (realistic) and Extraordinary Imagination (fantasy):
- Scale: 0% (Traditional) to 100% (Extraordinary)
- Default based on region and visual style
- Examples: 20-40% (Traditional), 50% (Balanced), 70-90% (Extraordinary), 100% (Full Fantasy)

### Step 9.5: Transformation Framework Selection (INTERACTIVE) ⭐NEW
Choose the creative transformation framework to emphasize product value transition:

**Option A: Before-After-Bridge (前后对比)**
- **Structure**: Problem State → Transformation Moment → New Reality
- **Best for**: Demonstrating dramatic change or improvement
- **Applications**: 
  - Skincare: Dull skin → Glowing skin
  - Transportation: Traffic congestion → Smooth journey
  - Lifestyle: Stressful routine → Relaxed state
- **TVC Flow**:
  - Before (30-40%): Establish the pain point/problem
  - Bridge (20-30%): Product introduction/transformation moment
  - After (30-40%): The improved state/benefits

**Option B: Dimensional Shift (维度变换)**
- **Structure**: Limited State → Breaking Boundaries → Expanded Reality
- **Best for**: Products that expand possibilities or break limitations
- **Applications**:
  - "Dull urban commute" → "Free intercity exploration"
  - "Confined space" → "Infinite possibilities"
  - "Ordinary routine" → "Extraordinary experiences"
- **TVC Flow**:
  - Dimension A (30%): Current limited state (e.g., grey city, traffic, routine)
  - Transition (20%): The trigger/product moment
  - Dimension B (40%): New expanded state (e.g., open road, nature, freedom)
  - CTA (10%): Invite to new dimension

**Option C: Hybrid Transformation (混合模式)**
- Combines Before-After with Dimensional Shift
- **Before**: Limited state in Dimension A
- **Bridge**: Product as the dimensional gateway
- **After**: Transformed state in Dimension B
- **Best for**: Maximum emotional impact and transformation demonstration

**User Selection**:
Present the options with specific examples relevant to the product category. Ask user to select framework and define:
- Dimension A state (e.g., "dull urban commute")
- Dimension B state (e.g., "free intercity exploration")
- Transformation trigger (how product enables the shift)

### Step 10: Script Development
Develop complete script including:
- Scene-by-scene descriptions
- Voiceover/narration
- Sound effects and music cues
- On-screen text
- Duration timeline

### Step 11: Script Confirmation (INTERACTIVE)
Present full script. Ask user to confirm or request changes.

### Step 12: Storyboard Breakdown
Convert script into shot-by-shot breakdown:
- Shot number
- Timestamp
- Shot type (CU/MS/WS/etc.)
- Camera movement
- Visual description
- Audio/VO
- AI image prompt

### Step 13: Storyboard Logic Confirmation (INTERACTIVE)
Present shot breakdown. Ask user to confirm or adjust shots.

### Step 14: Detailed Storyboard Generation
Generate complete storyboard with:
- Each shot's detailed description
- Camera specifications
- Lighting notes
- AI generation prompts (Gemini 3 format and Midjourney format)
- Transition notes

### Step 15: Storyboard Confirmation (INTERACTIVE)
Present complete storyboard. Ask user to confirm or request modifications.

### Step 16: Narrative Review
Perform automated review checking:
- Narrative coherence between shots
- Timing accuracy
- Information hierarchy
- Emotional arc progression
- Cultural sensitivity

Provide optimization suggestions if issues found.

### Step 17: Review Confirmation (INTERACTIVE)
Present review results and suggestions. Ask user to approve or make adjustments.

### Step 18: Final Polish
Apply any final adjustments based on user feedback.

### Step 19: Final Output
Generate final markdown document including:
- Project metadata
- Creative concept summary
- Complete script
- Full storyboard table
- AI image prompts (Gemini 3 + Midjourney)
- Technical notes
- Multi-language terminology glossary (if applicable)

## Output Format

The final output is a comprehensive markdown document with:

### Document Structure
```markdown
# TVC Storyboard - [Product Name]

## Project Information
- **Product**: [Name]
- **Duration**: [Xs]
- **Region**: [Target Region]
- **Visual Style**: [Style Name]
- **Language**: [Output Language]

## Creative Concept
[Selected concept with hook, insight, twist]

## Script
[Full script with timing]

## Storyboard

| Shot | Time | Type | Movement | Description | Audio | AI Prompt |
|------|------|------|----------|-------------|-------|-----------|
| ... | ... | ... | ... | ... | ... | ... |

## AI Image Prompts

### Gemini 3 (Google) Format
Natural language prompts optimized for Gemini 3 image generation

### Midjourney Format
Text prompts with parameters for Midjourney

## Technical Notes
[Production considerations]
```

## References

This skill uses the following reference materials:

### Core References
- `references/01-workflow-guide.md` - Detailed workflow instructions
- `references/02-ecommerce-categories.md` - Product category analysis
- `references/03-creative-strategies.md` - Creative strategy library
- `references/04-regional-culture/` - Regional cultural adaptation guides
- `references/05-visual-styles/` - Visual style guides with AI prompts
- `references/06-timing-framework.md` - 15-second modular timing
- `references/07-film-terminology/` - Multi-language film terminology
- `references/08-narrative-checklist.md` - Storyboard review checklist
- `references/09-ai-prompts/` - AI image generation prompt guides
- `assets/storyboard-template.md` - Standard storyboard template

### Knowledge Base (知识库)

**Creative Styles | 创意风格库**
- `references/knowledge-base/creative-styles/director-styles.md` - 全球知名导演视觉风格参考（王家卫、张艺谋、诺兰等）
- More styles: Art movements, Brand visual references, Color psychology

**Cinematography | 分镜摄影库**
- `references/knowledge-base/cinematography/composition-techniques.md` - 专业构图法则与镜头语言
- Shot types, Camera movements, Lighting theories

**TVC Industry | 广告行业库**
- `references/knowledge-base/tvc-industry/advertising-psychology.md` - 广告理论与消费者心理学
- AIDA model, Social proof, Platform strategies, Ethics & regulations

**Product Photography | 产品摄影库**
- `references/knowledge-base/product-photography/lighting-techniques.md` - 商业产品布光方案
- Material rendering, Scene setup, Post-processing LUTs

## Usage Notes

1. Always wait for user confirmation before proceeding to next step
2. Provide clear options at each interaction point
3. Use regional cultural knowledge to enhance creative relevance
4. Ensure AI prompts are specific and actionable
5. Maintain consistent terminology throughout
6. Check narrative coherence between all shots
7. Verify timing accuracy matches selected duration
8. Validate all file paths before reference access
9. Handle missing reference files gracefully
10. Log errors for debugging without exposing sensitive information

## Error Handling

### Common Error Scenarios
1. **Missing Reference Files**: Fall back to default values
2. **Invalid User Input**: Re-prompt with validation message
3. **File System Errors**: Log and continue with in-memory defaults
4. **Memory Constraints**: Stream large outputs in chunks

### Recovery Strategies
- Graceful degradation
- User-friendly error messages
- Automatic retry with exponential backoff
- Fallback to last known good state

## Performance Optimization

### Execution Time Targets
- Product Analysis: < 2 seconds
- Concept Generation: < 5 seconds
- Storyboard Generation: < 10 seconds
- Final Output: < 3 seconds

### Memory Management
- Lazy load reference files only when needed
- Cache frequently accessed templates
- Release memory after each major step
- Stream output for large documents

## Version History

### v2.0.0 (2026-02-16)
- Added comprehensive error handling
- Enhanced documentation with system requirements
- Added performance optimization guidelines
- Implemented graceful degradation strategies
- Added version metadata and license information

### v1.0.0 (Initial Release)
- Core TVC storyboard generation workflow
- 19-step interactive process
- Multi-regional and multi-language support
- AI prompt generation for Gemini 3 and Midjourney
