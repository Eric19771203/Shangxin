# 技术参数配置

## 工具说明
提供分辨率建议、质量标签体系、镜头语言等技术参数配置，帮助优化生成质量

## 核心功能
- 提供三种分辨率格式（竖屏/横屏/方形）
- 提供通用高质量标签和负面标签
- 提供镜头语言参考（景别/机位/运镜）

## 使用场景
- 调整视频分辨率
- 设置质量标签
- 选择镜头语言

## 提示词模板

### 中文模板
```
[分辨率选择]
竖屏短剧：9:16比例，1080x1920(1080p)或2160x3840(4K)，竖屏视频，移动格式

横屏短剧：16:9比例，1920x1080(1080p)或3840x2160(4K)，宽屏，电影级比例

方形视频：1:1比例，1080x1080或2160x2160，方形格式

[质量标签]
高质量标签：[根据制作类型选择]
负面标签：[根据制作类型选择]

[镜头语言]
景别：[远景/全景/中景/近景/特写]
机位：[平视/仰角/俯角/侧面/斜角]
运镜：[固定/推镜/拉镜/摇镜/跟拍/环绕/升降]
```

### English Template
```
[Resolution Choice]
Vertical Short Drama: 9:16 aspect ratio, 1080x1920 (1080p) or 2160x3840 (4K), vertical video, mobile format

Widescreen Short Drama: 16:9 aspect ratio, 1920x1080 (1080p) or 3840x2160 (4K), widescreen, cinematic aspect ratio

Square Video: 1:1 aspect ratio, 1080x1080 or 2160x2160, square format

[Quality Tags]
High Quality Tags: [Choose by production type]
Negative Tags: [Choose by production type]

[Cinematic Language]
Shot Size: [ELS/LS/MS/CU/ECU]
Camera Angle: [eye level/low angle/high angle/side angle/dutch angle]
Camera Movement: [static/push in/pull out/pan/tracking/orbit/crane]
```

## 分辨率建议

### 竖屏短剧（抖音/快手）
```
比例：9:16
分辨率：1080x1920 (1080p) 或 2160x3840 (4K)
关键词：vertical video, mobile format, 9:16 aspect ratio
```

### 横屏短剧（B站/YouTube）
```
比例：16:9
分辨率：1920x1080 (1080p) 或 3840x2160 (4K)
关键词：widescreen, cinematic aspect ratio, 16:9
```

### 方形视频（Instagram）
```
比例：1:1
分辨率：1080x1080 或 2160x2160
关键词：square format, 1:1 aspect ratio
```

## 质量标签体系

### 通用高质量标签
```
REAL写实：
8k uhd, 4k resolution, high resolution,
ultra detailed, highly detailed,
professional photography, masterwork,
award winning, sharp focus

ANIME 2D：
masterpiece, best quality, high quality,
official art, highly detailed,
professional illustration, award winning,
detailed character design

3D渲染：
8k resolution, high poly model,
ray tracing, global illumination,
professional rendering, award winning,
detailed textures, cinematic quality
```

### 通用负面标签
```
REAL写实：
anime, 2D animation, 3D animation, painting, illustration,
3d render, cgi, low quality, blurry,
out of focus, bad quality, amateur

ANIME 2D：
realistic, photo, 3d render,
bad anatomy, bad hands, extra limbs,
deformed, low quality, blurry,
worst quality, bad art

3D渲染：
2d, flat, anime, photo, painting,
low poly (unless intended),
low quality, blurry, bad topology,
bad geometry, artifacts
```

## 镜头语言

### 景别分类
```
远景 (ELS)：Extreme Long Shot, establishing shot
全景 (LS)：Long Shot, full body
中景 (MS)：Medium Shot, waist up
近景 (CU)：Close Up, face
特写 (ECU)：Extreme Close Up, eyes/details
```

### 机位角度
```
平视：eye level, straight on
仰角：low angle, from below, worm's eye view
俯角：high angle, from above, bird's eye view
侧面：side angle, profile view
斜角：dutch angle, tilted camera
```

### 运镜方式
```
固定：static shot, locked camera
推镜：push in, dolly forward
拉镜：pull out, dolly back
摇镜：pan left/right
跟拍：tracking shot, following
环绕：orbit shot, 360 degree
升降：crane shot, boom up/down
```

## 参数说明

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| 竖屏 | 抖音/快手 | 9:16, 1080x1920 |
| 横屏 | B站/YouTube | 16:9, 1920x1080 |
| 方形 | Instagram | 1:1, 1080x1080 |

## 触发词
技术参数、分辨率、质量标签、镜头语言、景别、机位、运镜、technical parameters、resolution、quality tags、cinematic language
