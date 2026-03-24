# AI Image Generation - n8n/AI Format

## Overview

This guide provides n8n/AI compatible JSON prompts for automated image generation.

---

## JSON Structure

### Basic Shot Prompt

```json
{
  "shot_number": 1,
  "prompt": "product close-up, studio lighting, commercial photography",
  "negative_prompt": "text, watermark, low quality",
  "aspect_ratio": "16:9",
  "style": "commercial"
}
```

---

## Full Storyboard Example

```json
{
  "project": {
    "name": "Product TVC",
    "duration": "30s",
    "style": "cinematic"
  },
  "shots": [
    {
      "shot_number": 1,
      "timestamp": "0:00-0:03",
      "shot_type": "CU",
      "prompt": "wireless earphones product close-up, clean white background, studio lighting, professional commercial photography, high detail, product focus, sleek modern design",
      "negative_prompt": "text, watermark, low quality, blurry, cluttered background",
      "aspect_ratio": "16:9",
      "style": "product",
      "lighting": "soft box",
      "camera": "fixed"
    },
    {
      "shot_number": 2,
      "timestamp": "0:03-0:06",
      "shot_type": "MS",
      "prompt": "person wearing wireless earphones, urban street setting, natural daylight, lifestyle photography, confident expression, modern casual attire",
      "negative_prompt": "text, watermark, low quality, ugly, deformed",
      "aspect_ratio": "16:9",
      "style": "lifestyle",
      "lighting": "natural",
      "camera": "tracking"
    },
    {
      "shot_number": 3,
      "timestamp": "0:06-0:10",
      "shot_type": "WS",
      "prompt": "person wearing wireless earphones during workout, fitness gym setting, energetic atmosphere, dynamic action, professional commercial photography",
      "negative_prompt": "text, watermark, low quality, dark, cluttered",
      "aspect_ratio": "16:9",
      "style": "action",
      "lighting": "mixed",
      "camera": "dolly"
    }
  ]
}
```

---

## Style Presets

### Product

```json
{
  "style": "product",
  "parameters": {
    "lighting": "studio",
    "background": "clean",
    "focus": "product",
    "mood": "professional"
  }
}
```

### Lifestyle

```json
{
  "style": "lifestyle",
  "parameters": {
    "lighting": "natural",
    "background": "authentic",
    "focus": "emotion",
    "mood": "aspirational"
  }
}
```

### Cinematic

```json
{
  "style": "cinematic",
  "parameters": {
    "lighting": "dramatic",
    "background": "atmospheric",
    "focus": "story",
    "mood": "emotional"
  }
}
```

---

## Regional Adaptations

### China

```json
{
  "regional_keywords": ["chinese lifestyle", "family gathering", "red gold", "premium"],
  "cultural_notes": "warm, family-oriented, celebratory"
}
```

### Middle East

```json
{
  "regional_keywords": ["elegant arabian", "golden lighting", "traditional modern"],
  "cultural_notes": "warm, family, premium"
}
```

### Japan

```json
{
  "regional_keywords": ["minimalist japanese", "natural light", "zen"],
  "cultural_notes": "clean, subtle, quality"
}
```

---

## Batch Generation

```json
{
  "batch_mode": true,
  "shots": [
    {"shot_number": 1},
    {"shot_number": 2},
    {"shot_number": 3}
  ],
  "common_settings": {
    "aspect_ratio": "16:9",
    "quality": "high",
    "style": "commercial"
  }
}
```
