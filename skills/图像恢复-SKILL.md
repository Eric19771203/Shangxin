# 图像恢复 Skill

## 使用工具
- Gemini

## 核心功能
将低分辨率裁剪图像恢复并放大到 4K 高清质量

## 使用场景
SceneDirector 视频生成模式、局部分镜高清化

## 节点类型
VIDEO_GENERATOR (视频生成节点 - SceneDirector 模式)

## 核心功能
- 严格保持原始构图和相机角度
- 修复模糊和噪点
- 添加皮肤纹理和真实细节
- 防止 AI 产生幻觉和额外内容

## 完整提示词

```
CRITICAL IMAGE RESTORATION TASK:
1. Input is a low-resolution crop. Your goal is to UPSCALE and RESTORE it to 4K quality.
2. STRICTLY PRESERVE the original composition, character pose, camera angle, and object placement.
3. DO NOT reframe, DO NOT zoom out, DO NOT change the perspective.
4. Fix blurriness and noise. Add skin texture and realistic details matching the description: "${prompt}".
5. Ensure the style matches: "${upstreamContextStyle || 'Cinematic, High Fidelity'}".
6. Output a single, high-quality image that looks exactly like the input but sharper.

NEGATIVE CONSTRAINTS:
- DO NOT add new people, characters, or subjects.
- The number of people MUST remain exactly the same as the input.
- DO NOT hallucinate extra limbs, faces, or background figures.

STRUCTURAL INTEGRITY:
- Treat the input image as the absolute ground truth for composition.
- Only enhance existing pixels, do not invent new geometry.
```

## 中文版说明

```
关键图像恢复任务：
1. 输入是低分辨率裁剪图像。你的目标是将它放大并恢复到 4K 质量。
2. 严格保持原始构图、角色姿势、相机角度和物体位置。
3. 不要重新构图，不要拉远镜头，不要改变视角。
4. 修复模糊和噪点。添加皮肤纹理和真实细节，匹配描述："${prompt}"。
5. 确保风格匹配："${upstreamContextStyle || '电影级，高保真'}"。
6. 输出单张高质量图像，看起来与输入完全一致但更清晰。

负面约束：
- 不要添加新的人物、角色或主体。
- 人物数量必须与输入完全一致。
- 不要产生幻觉，添加额外的肢体、脸部或背景人物。

结构完整性：
- 将输入图像视为构图的绝对真相。
- 只增强现有像素，不要发明新的几何结构。
```

## 参数说明

**动态变量：**

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `${prompt}` | 用户提供的场景描述 | "青年男子手持长剑，眼神坚定" |
| `${upstreamContextStyle}` | 上游视频的视觉风格分析 | "Cinematic, High Fidelity" 或 "电影级，高保真" |

## 使用场景

**1. SceneDirector 模式（局部分镜）：**

当用户在视频中框选局部区域生成新视频时：
- 用户框选区域 → 生成低分辨率裁剪图像
- 使用本提示词恢复到 4K 高清
- 使用高清图像作为 Veo 视频生成的输入
- 确保生成的视频质量高、细节丰富

**2. 工作流程：**

```
原视频 (1080p)
    ↓
用户框选局部区域
    ↓
低分辨率裁剪 (如 270p)
    ↓
图像恢复提示词 (本 Prompt)
    ↓
4K 高清恢复图像 (3840x2160)
    ↓
Veo 视频生成
    ↓
高质量局部视频
```

## 关键约束

**构图保持（最重要）：**
- ❌ 不允许重新构图
- ❌ 不允许拉远镜头
- ❌ 不允许改变透视
- ✅ 必须保持原始构图
- ✅ 必须保持原始相机角度
- ✅ 必须保持物体位置

**防止幻觉：**
- ❌ 不能添加新人物
- ❌ 不能添加额外肢体
- ❌ 不能添加背景人物
- ✅ 人物数量必须与输入一致

**增强策略：**
- ✅ 增强现有像素质量
- ✅ 添加皮肤纹理细节
- ✅ 修复模糊和噪点
- ✅ 匹配用户描述的场景
- ✅ 匹配上游视频风格

## 输入输出规格

| 项目 | 规格 |
|------|------|
| 输入分辨率 | 任意（通常为 270p - 720p 的裁剪图像） |
| 输出分辨率 | 4K (3840×2160 或 2880×3840) |
| 输出数量 | 1 张 |
| 宽高比 | 保持输入宽高比 |
| 处理时间 | 通常 5-15 秒（取决于模型） |

## 触发词
- "图像恢复"
- "低分辨率放大"
- "4K高清恢复"

---
*来源：AI-Prompts-文档.md*
*最后更新：2026-02-19*
