---
name: "scene-breakdown"
description: "Breaks down storyboard projects into detailed scenes with shot lists, camera movements, and visual descriptions. Invoke when creative concept is ready and need detailed scene planning."
---

# Scene Breakdown

Breaks down storyboard projects into detailed scenes with shot lists and camera movements.

## When to Invoke

- Creative concept has been established
- Need detailed scene planning
- Preparing for storyboard image generation
- User wants specific scene structure

## Input

```json
{
  "requirement": "string - Project requirement",
  "genre": "string - Project genre",
  "director": "string - Selected director",
  "concept": "object - Creative concept output",
  "scenes_count": "number - Number of scenes to generate",
  "color_style": "object - Color style (optional)"
}
```

## Output

```json
{
  "scenes": [
    {
      "scene_number": "number",
      "title": "string - Scene title",
      "description": "string - Scene description",
      "shots": [
        {
          "shot_number": "string - e.g., '1A', '1B'",
          "type": "string - Shot type (WS, MS, CU, ECU, OTS, etc.)",
          "description": "string - Visual description",
          "camera_movement": "string - Camera action",
          "duration": "string - Estimated duration in seconds",
          "prompt": "string - AI image generation prompt (English)"
        }
      ],
      "mood": "string - Scene mood",
      "key_props": ["array of important props"],
      "color_notes": "string - Color usage for this scene"
    }
  ],
  "total_shots": "number",
  "estimated_duration": "string - Total duration estimate",
  "pacing_notes": "string - Overall pacing description"
}
```

## Shot Types

### By Framing
- **WS (Wide Shot)**: Establishes location and scale
- **EWS (Extreme Wide Shot)**: Emphasizes environment over subject
- **MS (Medium Shot)**: Shows character and environment
- **MCU (Medium Close-Up)**: Waist up, dialogue scenes
- **CU (Close-Up)**: Focuses on emotion or detail
- **ECU (Extreme Close-Up)**: Intense detail focus (eyes, hands)
- **OTS (Over-the-Shoulder)**: Dialogue scenes
- **POV (Point of View)**: Character's perspective

### By Movement
- **Static**: Fixed camera position
- **Pan**: Horizontal camera movement
- **Tilt**: Vertical camera movement
- **Dolly**: Camera moves forward/backward
- **Truck**: Camera moves left/right
- **Crane**: Elevated sweeping movements
- **Handheld**: Documentary-style movement
- **Steadicam**: Smooth following movement
- **Zoom**: Lens focal length change
- **Rack Focus**: Shift focus between subjects

## Prompt Generation Rules

For each shot, generate an image generation prompt following this structure:

```
[Shot Type], [Subject Description], [Action/Pose], [Environment/Background], 
[Lighting Description], [Camera Details], [Director Style Reference], 
[Color Palette], [Mood/Atmosphere], [Technical Quality], [Aspect Ratio]
```

### Example Prompts

**Wide Shot:**
```
Wide shot, futuristic soldier in exoskeleton armor, standing on battlefield 
looking at horizon, destroyed city in background with smoke rising, 
dramatic sunset lighting with rays through clouds, cinematic composition, 
Denis Villeneuve style, teal and orange color grading with sand tones, 
epic and somber mood, 35mm film look, 8k resolution, 16:9 aspect ratio
```

**Close-Up:**
```
Extreme close-up, soldier's eye reflecting destroyed city, 
single tear rolling down, dust particles floating in air, 
soft natural side lighting, shallow depth of field, 
Roger Deakins cinematography style, muted earthy tones, 
intimate and emotional mood, photorealistic, 8k resolution
```

## Prompt Template

```
你是一位专业的分镜设计师。请为以下项目创作详细的分镜脚本：

项目需求：{requirement}
项目类型：{genre}
参考导演：{director}
核心概念：{concept}
场景数量：{scenes_count}
色彩风格：{color_style}

要求：
1. 为每个场景设计标题和描述
2. 每个场景包含3-5个镜头
3. 每个镜头包含：
   - 镜头编号（如 1A, 1B）
   - 镜头类型（WS, MS, CU, ECU, OTS 等）
   - 视觉描述（画面内容）
   - 镜头运动（Static, Pan, Dolly, Handheld 等）
   - 预估时长（秒）
   - AI生图提示词（英文，详细描述视觉元素，包含景别、主体、动作、环境、光影、导演风格、色彩、氛围、技术规格）
4. 标注场景氛围和关键道具
5. 添加色彩使用说明

以JSON格式返回结果。
```

## Example

Input:
```json
{
  "requirement": "未来战争科幻短片，士兵在废墟中寻找希望",
  "genre": "scifi",
  "director": "Denis Villeneuve",
  "concept": {"core_concept": "末日废墟中的人性微光"},
  "scenes_count": 3,
  "color_style": {"name": "kurosawa"}
}
```

Output:
```json
{
  "scenes": [
    {
      "scene_number": 1,
      "title": "废墟中的觉醒",
      "description": "士兵从废墟中醒来，环顾四周的毁灭景象",
      "shots": [
        {
          "shot_number": "1A",
          "type": "EWS",
          "description": "航拍废墟全景，士兵渺小身影躺在瓦砾中",
          "camera_movement": "Slow dolly down from sky",
          "duration": "5s",
          "prompt": "Extreme wide aerial shot, lone soldier lying in massive destroyed city ruins, smoke rising in distance, dramatic dawn lighting with orange and blue sky, cinematic composition, Denis Villeneuve style, high contrast, epic and desolate mood, 35mm film look, 8k resolution"
        },
        {
          "shot_number": "1B",
          "type": "CU",
          "description": "士兵睁开眼睛，瞳孔中反射废墟景象",
          "camera_movement": "Static",
          "duration": "3s",
          "prompt": "Extreme close-up of soldier's eye opening, reflection of destroyed buildings in iris, dust particles floating, soft morning light, shallow depth of field, Roger Deakins cinematography, muted earthy tones, intimate and vulnerable mood, photorealistic, 8k resolution"
        }
      ],
      "mood": "desolate but hopeful",
      "key_props": ["破损的头盔", "灰尘", "阳光"],
      "color_notes": "冷暖对比，废墟的灰蓝色与晨光的暖橙色"
    }
  ],
  "total_shots": 6,
  "estimated_duration": "45 seconds",
  "pacing_notes": "开场缓慢建立氛围，中段加快节奏，结尾回归静谧"
}
```