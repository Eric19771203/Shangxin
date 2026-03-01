---
id: SKILL-010
name: tvc-storyboard-creator
version: 2.1.0
description: AI-powered TVC commercial storyboard generator with interactive customization workflow. Provides step-by-step selection of creative direction, visual style, pacing, and other parameters before generating final storyboard.
category: tvc-production
author: TVC Technical Team
created_at: 2026-02-18
updated_at: 2026-02-18
---

# TVC Storyboard Creator v2.1

## Overview

This skill generates professional TVC commercial storyboard prompts through an interactive workflow. It guides users through multiple customization steps before producing the final storyboard document with shot-by-shot breakdowns, timing, camera directions, and AI image generation prompts.

**Core Value Proposition**: Transform product inputs into production-ready storyboard documents through an intuitive, step-by-step customization process.

## Key Features

- **Interactive Workflow**: 19+ interaction points for full creative control
- **15-Second Modular Pacing**: Storyboards designed for 15s/30s/45s/60s durations
- **Multi-Regional Adaptation**: Culturally adapted creative for 9 global regions
- **Visual Style Library**: 15+ distinct visual styles with style mixing capability
- **Multi-Language Support**: Chinese, English, Arabic, Spanish, Japanese, Korean
- **AI-Ready Prompts**: Pre-built prompts for Gemini 3 and Midjourney
- **Smart Style Recommendation**: AI-powered analysis with confidence ratings
- **Real-time Preview**: Visual style previews at each selection step

## Input Parameters

### Initial Input
```json
{
  "product": {
    "name": "string - Product name",
    "description": "string - Product description",
    "category": "string - Product category",
    "image_url": "string - Optional product image URL"
  },
  "basic_info": {
    "duration": "string - 15s/30s/45s/60s",
    "region": "string - Target region",
    "language": "string - Output language"
  }
}
```

### Interactive Steps Input
```json
{
  "step": "number - Current step",
  "selection": "object - User selection for current step",
  "previous_selections": "object - Previous step selections"
}
```

## Output Format

### Interactive Step Output
```json
{
  "success": "boolean",
  "data": {
    "step": "number - Current step",
    "options": "array - Available options for selection",
    "preview": "string - Visual preview (if applicable)",
    "recommendations": "object - AI recommendations"
  },
  "message": "string - Step instructions",
  "metadata": {
    "version": "string - Skill version",
    "timestamp": "string - Execution time"
  }
}
```

### Final Output
```json
{
  "success": "boolean",
  "data": {
    "storyboard": "string - Generated storyboard",
    "script": "string - TVC script",
    "ai_prompts": {
      "gemini": "array - Gemini 3 prompts",
      "midjourney": "array - Midjourney prompts"
    },
    "selections": "object - All user selections"
  },
  "message": "string - Execution message",
  "metadata": {
    "version": "string - Skill version",
    "timestamp": "string - Execution time"
  }
}
```

## Interactive Workflow

### Step 1: Product Analysis
- Analyze product information and image
- Extract key features and selling points
- Generate initial creative recommendations

### Step 2: Regional Selection
- Present 9 regional options with cultural considerations
- Ask user to select target region(s)

### Step 3: Language Selection
- Select output language for storyboard document
- Support bilingual options

### Step 4: 2026 Creative Trend Selection
- **Trend 1**: Absurdist + High-Impact Narrative
- **Trend 2**: Anime/IP Deep Integration
- **Trend 3**: Cinematic Industrial + Game CG
- **Trend 4**: Ultimate Sophistication Aesthetic
- **Option**: Supreme Sophistication Channel (Advanced)

### Step 5: Visual Style Selection
- Present style options based on selected trend
- Include classic styles (Wes Anderson, Makoto Shinkai, etc.)
- Show style previews and recommendations

### Step 6: Narrative vs. Product Focus
- **Option A**: Story/Narrative-Focused
- **Option B**: Product/Performance-Focused
- **Option C**: Balanced Hybrid
- Provide style-weight pairing recommendations

### Step 7: Duration Confirmation
- Confirm selected duration
- Present shot count breakdown

### Step 8: Pacing Recommendation
- **Option A**: Cinematic/Slow (4 shots per 15s)
- **Option B**: Standard (6 shots per 15s)
- **Option C**: Fast/Dynamic (9 shots per 15s)

### Step 9: Creative Concept Generation
- Generate 3-5 creative concepts
- Present with hook, insight, twist, and emotional tone

### Step 10: Concept Selection
- User selects preferred concept
- Option to request modifications

### Step 11: Creative Imagination Weight
- Adjust balance between Traditional and Extraordinary Imagination
- Scale: 0% (Traditional) to 100% (Extraordinary)

### Step 12: Transformation Framework Selection
- **Option A**: Before-After-Bridge
- **Option B**: Dimensional Shift
- **Option C**: Hybrid Transformation

### Step 13: Script Preview
- Present draft script based on selections
- User confirms or requests changes

### Step 14: Storyboard Logic Confirmation
- Present shot breakdown
- User adjusts shots as needed

### Step 15: Final Confirmation
- Summary of all selections
- Final approval before generation

### Step 16: Storyboard Generation
- Generate complete storyboard document
- Include AI image prompts

## Usage Example

### Initial Call
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  product:
    name: "露华燕舍鲜炖燕窝"
    description: "高品质鲜炖燕窝，净含量250g，营养丰富，口感顺滑"
    category: "health and beauty"
  basic_info:
    duration: "30s"
    region: "China"
    language: "Chinese"
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### Step-by-Step Interaction
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 2
  selection:
    region: "China"
  previous_selections:
    step_1: {
      "analysis_complete": true
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

## Interactive Demo

### Example Workflow for 露华燕舍鲜炖燕窝

#### Step 1: Product Analysis
- **Input**: Product information and image
- **Output**: Initial analysis with creative recommendations

#### Step 2: Regional Selection
- **Options**: China, Japan/Korea, Middle East, etc.
- **Selection**: China

#### Step 3: Language Selection
- **Options**: Chinese, English, Bilingual
- **Selection**: Chinese

#### Step 4: Creative Trend Selection
- **Options**: Trend 1-4, Supreme Sophistication
- **Selection**: Trend 4 (Ultimate Sophistication)

#### Step 5: Visual Style Selection
- **Options**: Mocha Mousse, Scandinavian, Film Grain, etc.
- **Selection**: Mocha Mousse + Sculptural Lighting

#### Step 6: Focus Selection
- **Options**: Narrative, Product, Balanced
- **Selection**: Product (80% product focus)

#### Step 7-15: Remaining steps with user selections

#### Step 16: Final Storyboard Generation
- **Output**: Complete TVC storyboard document

## References

This skill uses comprehensive reference materials including:
- Workflow guides and product category analysis
- Regional cultural adaptation guides
- Visual style guides with AI prompts
- Timing frameworks and film terminology
- Narrative checklists and AI image generation guides

## Error Handling

- **Missing Input**: Prompt user for required information
- **Invalid Selection**: Provide validation feedback
- **Generation Errors**: Offer troubleshooting options
- **Timeout**: Resume workflow from last completed step

## Performance Optimization

- **Lazy Loading**: Load reference materials on demand
- **Caching**: Cache frequently used style data
- **Parallel Processing**: Generate options while user reviews previous selections
- **Progressive Loading**: Stream large preview data

## Version History

### v2.1.0 (2026-02-18)
- Added interactive workflow support
- Enhanced real-time preview capabilities
- Improved step-by-step selection process
- Added visual style previews
- Updated error handling for interactive steps

### v2.0.0 (2026-02-16)
- Initial interactive workflow implementation
- Multi-regional and multi-language support
- AI prompt generation for Gemini 3 and Midjourney