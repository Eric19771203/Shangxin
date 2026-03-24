# AI Image Generation - Gemini 3 (Google)

## Overview

This guide provides optimized prompts for Gemini 3 image generation (Gemini 2.0 Flash Experimental).

---

## Gemini 3 Prompt Structure

### Base Formula

```
[Subject] + [Scene/Setting] + [Lighting] + [Camera/Composition] + [Style] + [Technical Specs]
```

### Key Differences from Midjourney

- Gemini 3 understands natural language better
- Can handle more complex scene descriptions
- Supports longer prompts
- More flexible with style mixing
- Better at text rendering

---

## Product Photography Prompts

### Product Hero Shot

```
A sleek wireless earphones product shot on a clean white background, studio lighting with soft box, professional commercial photography, high detail, product centered, modern minimalist design, 8k resolution, sharp focus
```

### Lifestyle Shot

```
A young professional using a laptop at a modern coffee shop, natural daylight from large windows, warm and inviting atmosphere, lifestyle photography, authentic moment, shallow depth of field, professional commercial quality
```

### Product in Use

```
A person wearing wireless headphones during an intense workout at a modern gym, dynamic action pose, energetic fitness setting, motion blur on background, professional commercial photography, bold and vibrant
```

---

## Scene-Based Prompts

### Establishing Shot

```
Wide establishing shot of a modern smart home living room, sunlight streaming through floor-to-ceiling windows, minimalist scandinavian furniture, warm wood tones, morning light atmosphere, cinematic composition, professional interior photography
```

### Emotional Moment

```
Close-up of a woman's face showing pure joy and contentment while using a premium skincare product, soft natural lighting from window, dreamy bokeh background, beauty commercial style, magazine cover quality, emotional and aspirational
```

### Product Feature Demo

```
Macro close-up shot of a watch mechanism showing intricate details, Swiss watch craftsmanship, dramatic spotlight lighting, dark moody background, luxury product photography, high-end timepiece advertisement style
```

---

## Gemini 3 Specific Parameters

### Aspect Ratio

Gemini 3 supports various aspect ratios - specify in prompt:
- "16:9 aspect ratio for cinematic look"
- "1:1 square format for social media"
- "9:16 vertical for stories"

### Quality Enhancers

```
professional commercial photography, 8k ultra detailed, sharp focus, studio quality, high resolution, post-production finished
```

### Lighting Keywords

```
soft box lighting, golden hour, blue hour, cinematic lighting, three-point lighting, Rembrandt lighting, natural window light, backlit, rim lighting
```

---

## Style-Specific Prompts

### Wes Anderson Style

```
A product showcase with Wes Anderson's distinctive style, symmetrical composition, pastel color palette, centered framing, vintage 1970s aesthetic, flat lighting, whimsical and quirky atmosphere, miniature set design look
```

### Makoto Shinkai Style

```
Anime-style product shot in Makoto Shinkai's signature aesthetic, photorealistic background with dramatic clouds, golden hour sunset sky, lens flare effects, emotional atmosphere, Japanese anime quality, dreamy and romantic
```

### Disney Animation Style

```
Product as an animated Disney-style character, vibrant saturated colors, magical sparkle effects, fairy tale lighting, smooth gradient backgrounds, expressive character design, heartwarming animated commercial style
```

### Xianxia Fantasy Style

```
Product in xianxia fantasy setting, ancient Chinese architecture with flowing curtains, ethereal misty mountains, jade and gold color palette, mystical atmosphere, Chinese fantasy art style, magical glowing effects
```

### Cyberpunk Style

```
Product in cyberpunk dystopian world, neon pink and cyan lights, rain-soaked futuristic street, wet reflective surfaces, high contrast, dark atmospheric mood, Blade Runner aesthetic
```

---

## Regional Variation Prompts

### China Market

```
Modern Chinese family celebrating Chinese New Year, red and gold festive decorations, warm lighting, premium quality, family gathering scene, traditional modern blend, aspirational lifestyle photography
```

### Middle East Market

```
Elegant Arabian family setting, warm golden ambient lighting, luxurious traditional-modern blend, premium quality, family togetherness, professional commercial photography, Middle Eastern aesthetic
```

### Japan Market

```
Minimalist Japanese lifestyle scene, natural soft lighting, clean composition with negative space, zen aesthetic, seasonal elements, high quality commercial photography, Japanese craftsmanship feel
```

### USA Market

```
All-American lifestyle scene, bold colors, high contrast, confident people, dynamic energy, direct camera contact, professional commercial photography, aspirational and bold
```

---

## Technical Specifications

### Camera Settings

```
85mm portrait lens, f/1.8 shallow depth of field, professional studio lighting, medium format camera quality, sharp subject focus
```

### Post-Processing

```
professional color grading, cinematic look, high contrast, sharp details, finished commercial quality, magazine advertisement level
```

---

## Gemini 3 Best Practices

1. **Be Descriptive**: Use detailed natural language
2. **Specify Mood**: Describe emotional tone
3. **Include Lighting**: Light description is crucial
4. **State Format**: Mention aspect ratio desired
5. **Quality Markers**: Add "professional", "commercial quality"

---

## Example Storyboard Prompts (30s TVC)

### Shot 1 - Product Hero (0-3s)

```
Close-up product shot of wireless earphones, clean white studio background, professional commercial lighting, high detail, sleek modern design, sharp focus, product centered, 8k quality
```

### Shot 2 - Lifestyle Introduction (3-8s)

```
A stylish person in casual attire walking through a modern urban street, natural daylight, confident posture, lifestyle photography, aspirational mood, professional commercial quality
```

### Shot 3 - Product in Use (8-15s)

```
The same person wearing the wireless earphones, close-up of happy expression while listening, urban coffee shop background, natural warm lighting, lifestyle moment, professional photography
```

### Shot 4 - Feature Highlight (15-22s)

```
Medium shot showing earphones being charged on wireless charging pad, soft glow indicator light, modern minimalist desk setup, product features demonstration, clean commercial lighting
```

### Shot 5 - Hero Shot + CTA (22-30s)

```
Final product hero shot with brand logo, clean white background, professional studio lighting, premium quality, bold confident presentation, commercial advertisement style
```

---

## JSON Output Format (For Integration)

```json
{
  "shots": [
    {
      "shot_number": 1,
      "timestamp": "0:00-0:03",
      "gemini_prompt": "Close-up product shot of wireless earphones, clean white studio background, professional commercial lighting, high detail, sleek modern design, sharp focus, product centered, 8k quality",
      "aspect_ratio": "16:9",
      "mood": "professional"
    }
  ]
}
```
