# 视觉规范指南 (Visual Style Guide)

## 1. 核心视觉原则 (Core Visual Principles)

**原则一：电影级质感 (Cinematic Quality)**
*   **光影**：注重光源、阴影、色温的对比，营造氛围。
*   **构图**：使用三分法、引导线、对称、极简等经典构图。
*   **景深**：合理运用虚实对比（Bokeh），突出主体。
*   **色彩**：确立世界的主色调（如：赛博朋克的霓虹色、废土的灰黄色）。

**原则二：细节真实感 (Realistic Details)**
*   **材质**：强调物体表面的纹理（如：金属的锈迹、皮肤的毛孔、布料的织纹）。
*   **生活痕迹**：场景中要有使用过的痕迹（如：磨损的武器、涂鸦的墙壁），而非全新的模型。
*   **环境互动**：角色与环境的交互（如：雨中的倒影、风中的衣摆）。

**原则三：漫剧适配性 (Manhua Adaptability)**
*   **分镜逻辑**：场景设计要便于分镜拆解（远景交代环境、中景展示动作、特写刻画情绪）。
*   **视觉符号**：确立独特的视觉标识（如：势力的徽章、角色的特征道具）。
*   **清晰度**：画面元素层次分明，避免杂乱无章，确保手机竖屏阅读体验。

## 2. 场景描述要素 (Scene Description Elements)

### 2.1 基础信息
*   **场景名称**：准确、易懂。
*   **时间/天气**：日夜、晴雨、季节。
*   **视角**：俯视、仰视、平视、广角、长焦。

### 2.2 视觉细节
*   **主体**：场景中的核心物体或建筑。
*   **背景**：烘托氛围的环境元素。
*   **光影**：主光源、辅助光、环境光。
*   **色彩**：主色调、点缀色。
*   **材质**：关键物体的质感描述。

### 2.3 氛围与情绪
*   **整体基调**：压抑、宏大、神秘、温馨。
*   **动态元素**：飘动的旗帜、飞舞的尘埃、流动的人群。

## 3. AI生成提示词规范 (AI Prompt Standard)

### 3.1 结构公式
`[画质词] + [场景主体] + [环境细节] + [光影色彩] + [构图视角] + [风格修饰]`

### 3.2 常用词汇库

*   **画质词**：masterpiece, best quality, 8K, UHD, ultra realistic, photorealistic, cinematic lighting, movie still, octane render.
*   **光影词**：dramatic lighting, volumetric lighting, ray tracing, soft shadows, rim light.
*   **构图词**：wide angle, depth of field, symmetry, rule of thirds, dynamic composition.
*   **风格词**：cyberpunk, steampunk, fantasy, post-apocalyptic, noir, anime style.

### 3.3 示例 (Example)

**中文描述**：
> 电影级漫剧分镜概念图，8K超清，极致细节。
> **场景**：异能都市地下黑市。
> **细节**：昏暗的地下空间，管道纵横，随处可见非法异能交易，墙面画满禁忌异能涂鸦，暗处有安保人员巡逻。
> **光影**：霓虹灯光斑驳，冷暖对比强烈。
> **氛围**：紧张、压抑、混乱。

**英文Prompt**：
> masterpiece, best quality, 8K, ultra realistic, cinematic lighting,
> cyberpunk underground black market, intricate pipes, illegal superpower trading, graffiti on walls, security guards in shadows,
> neon lights, cold and warm contrast, dramatic atmosphere, wide angle, depth of field, octane render.
