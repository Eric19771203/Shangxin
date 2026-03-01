---
name: "storyboard-generator"
description: "Generates storyboard images using AI image generation APIs based on scene breakdown prompts. Supports Gemini 3 and API aggregator platforms. Invoke when scene breakdown is complete and need visual storyboards."
---

# Storyboard Generator

Generates storyboard images using AI image generation APIs.

## When to Invoke

- Scene breakdown with prompts is ready
- Need to generate visual storyboards
- User wants to see the visual realization
- Final output generation stage

## Input

```json
{
  "scenes": "array - Scene breakdown with shot prompts",
  "config": {
    "provider": "string - Image gen provider (gemini, aggregator)",
    "style_preset": "string - Style preset name",
    "aspect_ratio": "string - 16:9, 2.39:1, 4:3, 1:1, 9:16",
    "quality": "string - low, medium, high, ultra",
    "output_format": "string - png, jpg, webp"
  },
  "director": "string - Director for style consistency",
  "color_style": "object - Color style configuration"
}
```

## Output

```json
{
  "generated_images": [
    {
      "scene_number": "number",
      "shot_number": "string",
      "prompt": "string - Original prompt used",
      "image_url": "string - Generated image URL or local path",
      "status": "string - success, error, pending",
      "error": "string - Error message if failed",
      "metadata": {
        "provider": "string",
        "generation_time": "string",
        "seed": "number"
      }
    }
  ],
  "summary": {
    "total_requested": "number",
    "successful": "number",
    "failed": "number",
    "output_directory": "string",
    "generation_time": "string"
  },
  "storyboard_pdf": "string - Path to generated PDF (optional)"
}
```

## Supported Providers

### Gemini 3
- **Provider ID**: `gemini`
- **Strengths**: High quality, good composition understanding
- **Best for**: Cinematic shots, complex scenes
- **Rate limits**: Check current API documentation
- **API Key**: `GEMINI_API_KEY` environment variable

### API Aggregator
- **Provider ID**: `aggregator`
- **Strengths**: Multiple backend options, fallback support
- **Best for**: Batch generation, cost optimization
- **Features**: Auto-fallback on failure
- **API Key**: `API_AGGREGATOR_KEY` environment variable

## Image Generation Configuration

### Style Presets
- **cinematic**: Film-like quality, dramatic lighting, anamorphic feel
- **realistic**: Photorealistic rendering, natural lighting
- **illustrated**: Artistic illustration, concept art style
- **anime**: Japanese animation style, clean lines
- **noir**: High contrast black and white, dramatic shadows

### Aspect Ratios
- `16:9` - Standard widescreen (1920x1080)
- `2.39:1` - Cinematic anamorphic (2560x1080)
- `4:3` - Classic TV format (1440x1080)
- `1:1` - Square format (1080x1080)
- `9:16` - Vertical/mobile (1080x1920)

### Quality Settings
- `low` - Fast generation, draft quality
- `medium` - Balanced speed and quality
- `high` - Best quality, slower generation
- `ultra` - Maximum quality, slowest generation

## Prompt Enhancement

### Base Prompt Structure
```
[Shot Type], [Subject], [Action], [Environment], 
[Lighting], [Camera Details], [Style Reference], 
[Color Palette], [Mood], [Technical Specs]
```

### Enhancement Rules
1. Add director name for style consistency
2. Include technical specs (8k, photorealistic, etc.)
3. Specify aspect ratio in prompt
4. Add negative prompts for unwanted elements

### Negative Prompts (Common)
```
blurry, low quality, distorted, deformed, 
bad anatomy, watermark, text, logo, 
oversaturated, underexposed
```

## Prompt Template

```
你是一位AI图像生成专家。请优化以下分镜提示词用于图像生成：

原始提示词：{prompt}
导演风格：{director}
风格预设：{style_preset}
画面比例：{aspect_ratio}
质量设置：{quality}

请：
1. 优化提示词以提高图像质量
2. 添加导演风格特征关键词
3. 确保构图符合镜头类型
4. 添加技术规格（分辨率、画质等）
5. 提供负面提示词（需要避免的内容）

返回优化后的：
- enhanced_prompt: 优化后的英文提示词
- negative_prompt: 负面提示词
- style_keywords: 风格关键词列表
```

## Example

Input:
```json
{
  "scenes": [
    {
      "scene_number": 1,
      "shots": [
        {
          "shot_number": "1A",
          "prompt": "Wide shot, futuristic soldier in exoskeleton armor, standing on battlefield"
        }
      ]
    }
  ],
  "config": {
    "provider": "gemini",
    "style_preset": "cinematic",
    "aspect_ratio": "16:9",
    "quality": "high"
  },
  "director": "Denis Villeneuve",
  "color_style": {"name": "kurosawa"}
}
```

Output:
```json
{
  "generated_images": [
    {
      "scene_number": 1,
      "shot_number": "1A",
      "prompt": "Wide shot, futuristic soldier in exoskeleton armor...",
      "image_url": "./output/scene_01_shot_1A.png",
      "status": "success",
      "error": null,
      "metadata": {
        "provider": "gemini",
        "generation_time": "2024-01-15T10:30:00Z",
        "seed": 123456
      }
    }
  ],
  "summary": {
    "total_requested": 1,
    "successful": 1,
    "failed": 0,
    "output_directory": "./output",
    "generation_time": "15 seconds"
  },
  "storyboard_pdf": "./output/storyboard.pdf"
}
```

## Error Handling

### Retry Logic
- Max 3 retry attempts per image
- Exponential backoff between retries
- Switch provider on repeated failures

### Fallback Strategy
1. Try primary provider (Gemini)
2. Fallback to aggregator on failure
3. Use lower quality setting if needed
4. Report partial success if some images fail

### Common Errors
- **Rate Limit**: Wait and retry
- **Content Policy**: Modify prompt
- **Timeout**: Reduce complexity
- **API Error**: Switch provider