# 视频提示词模板 (Video Prompt Templates)

> **源文件**: `services/promptManager.ts` 第 283-447 行
> **类**: `PromptManager`
> **目标模型**: 视频生成模型 (Sora / Luma / Runway / Veo 等)

此文件包含三套视频生成提示词模板，每套都有中英文双版本。模板中的 `{变量}` 在运行时由代码动态填充。

---

## 1. 分镜图视频提示词 (Storyboard Video)

**函数**: `buildStoryboardVideoPrompt()`

### 中文版

```
{SCENE_DESCRIPTION}

运镜要求：
{CAMERA_MOVEMENT}

视觉风格：
{VISUAL_STYLE}

角色：
{CHARACTERS}

关键约束：
- 视频时长：{DURATION}
- 保持场景连续性和一致性
- 流畅的运镜和自然的动作
- 高质量视频输出，避免帧率不稳定
- 遵循分镜图描述的构图和氛围
```

### 英文版

```
{SCENE_DESCRIPTION}

Camera Movement:
{CAMERA_MOVEMENT}

Visual Style:
{VISUAL_STYLE}

Characters:
{CHARACTERS}

Key Constraints:
- Video Duration: {DURATION}
- Maintain scene continuity and consistency
- Smooth camera movement and natural motion
- High quality video output, avoid frame rate instability
- Follow the composition and atmosphere described in the storyboard
```

### 参数说明

| 参数 | 默认值 |
|------|--------|
| `{SCENE_DESCRIPTION}` | (必填) |
| `{CAMERA_MOVEMENT}` | 平滑运镜，自然过渡 |
| `{VISUAL_STYLE}` | 高质量3D动漫风格 |
| `{CHARACTERS}` | 主要角色表演 |
| `{DURATION}` | 5秒 |

---

## 2. 电影感视频提示词 (Cinematic Video)

**函数**: `buildCinematicVideoPrompt()`

### 中文版

```
电影感视频生成，专业级电影摄影质感。

场景描述：{SCENE}

摄影参数：
- 光线：{LIGHTING}
- 色调：{COLOR_GRADE}
- 运镜：{CAMERA_WORK}
- 景别：{SHOT_SIZE}

技术要求：
- 4K分辨率，电影级画质
- 专业色彩分级，电影质感调色
- 平滑的摄像机运动
- 自然的演员表演和动作
- 环境光和阴影的真实处理
- 高动态范围（HDR）质量

输出要求：
- 视频时长：{DURATION}
- 帧率：24fps 或 30fps
- 无抖动、无闪烁
- 流畅的镜头过渡
```

### 英文版

```
Cinematic video generation, professional movie-quality cinematography.

Scene Description: {SCENE}

Cinematography Parameters:
- Lighting: {LIGHTING}
- Color Grade: {COLOR_GRADE}
- Camera Work: {CAMERA_WORK}
- Shot Size: {SHOT_SIZE}

Technical Requirements:
- 4K resolution, movie-grade quality
- Professional color grading, cinematic color timing
- Smooth camera movement
- Natural acting and motion
- Realistic handling of ambient light and shadows
- High Dynamic Range (HDR) quality

Output Requirements:
- Video Duration: {DURATION}
- Frame Rate: 24fps or 30fps
- No shaking, no flickering
- Smooth shot transitions
```

### 参数说明

| 参数 | 默认值 |
|------|--------|
| `{SCENE}` | (必填) |
| `{LIGHTING}` | 专业电影灯光，自然光与环境光结合 |
| `{COLOR_GRADE}` | 电影级色彩分级，暖色调 |
| `{CAMERA_WORK}` | 平滑的电影摄像机运动 |
| `{SHOT_SIZE}` | 中景 |
| `{DURATION}` | 5秒 |

---

## 3. Sora 专用视频提示词 (Sora Video)

**函数**: `buildSoraVideoPrompt()`

### 中文版

```
AI视频生成提示词，适用于Sora等高质量视频生成模型。

场景描述：{SCENE}

详细视觉要求：
{VISUAL_DETAILS}

镜头语言：
- 运镜方式：{CAMERA_MOVEMENT}
- 景别：{SHOT_SIZE}
- 拍摄角度：{ANGLE}
- 镜头语言：{LANGUAGE_OF_LENS}

环境与氛围：
- 场景设定：{ENVIRONMENT}
- 灯光：{LIGHTING}
- 色调：{MOOD}
- 氛围感：{ATMOSPHERE}

人物与动作：
{CHARACTERS_AND_ACTIONS}

技术规范：
- 视频比例：{ASPECT_RATIO}
- 视频时长：{DURATION}
- 画质质量：{QUALITY}

创作风格：
{STYLE_GUIDANCE}

质量要求：
- 高度连贯的时序一致性
- 物理准确的运动和互动
- 稳定的画面质量，无闪烁或突变
- 自然的过渡和流畅的动作
- 符合现实世界的物理规律
```

### 英文版

```
AI video generation prompt, optimized for high-quality video generation models like Sora.

Scene Description: {SCENE}

Detailed Visual Requirements:
{VISUAL_DETAILS}

Cinematography:
- Camera Movement: {CAMERA_MOVEMENT}
- Shot Size: {SHOT_SIZE}
- Camera Angle: {ANGLE}
- Lens Language: {LANGUAGE_OF_LENS}

Environment and Atmosphere:
- Scene Setting: {ENVIRONMENT}
- Lighting: {LIGHTING}
- Color Tone: {MOOD}
- Atmosphere: {ATMOSPHERE}

Characters and Actions:
{CHARACTERS_AND_ACTIONS}

Technical Specifications:
- Aspect Ratio: {ASPECT_RATIO}
- Duration: {DURATION}
- Quality: {QUALITY}

Creative Style:
{STYLE_GUIDANCE}

Quality Requirements:
- High degree of temporal consistency
- Physically accurate motion and interactions
- Stable image quality, no flickering or sudden changes
- Natural transitions and smooth motion
- Consistent with real-world physics
```

### 参数说明

| 参数 | 默认值 |
|------|--------|
| `{SCENE}` | (必填) |
| `{VISUAL_DETAILS}` | 高精度细节，电影级画质 |
| `{CAMERA_MOVEMENT}` | 平滑运镜 |
| `{SHOT_SIZE}` | 中景 |
| `{ANGLE}` | 平视 |
| `{LANGUAGE_OF_LENS}` | 标准镜头 |
| `{ENVIRONMENT}` | 室内场景 |
| `{LIGHTING}` | 自然光 |
| `{MOOD}` | 暖色调 |
| `{ATMOSPHERE}` | 舒适氛围 |
| `{CHARACTERS_AND_ACTIONS}` | 角色自然表演 |
| `{ASPECT_RATIO}` | 16:9 |
| `{DURATION}` | 5秒 |
| `{QUALITY}` | hd (高清) / sd (标清) |
| `{STYLE_GUIDANCE}` | 写实风格 |
