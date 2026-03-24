# Seedance 2.0 漫剧视频提示词模板

**适用场景**：《代码修真》等系列漫剧的视频生成  
**核心目标**：角色一致性 + 场景一致性 + 镜头可控 + 风格统一

---

## 提示词结构模板

```
[风格锁定] [角色/场景描述] [动作/情绪] [镜头运动] [时长/节奏] [技术参数] [排除项]
```

---

## 1. 风格锁定（必选，放最前面）

**作用**：确保整个系列视频风格统一

```
3D semi-realistic 8K Chinese fantasy cultivation anime style, consistent with episode 3 visual reference
```

**变体**：
- 如果要强调某一集的特定色调：
  ```
  3D semi-realistic 8K, warm golden lighting with blue-gray tones, Chinese cultivation aesthetic
  ```

---

## 2. 角色/场景描述（核心主体）

### 2.1 角色出镜

**单人镜头**：
```
Lin Chen (protagonist), young male in gray outer sect robes, determined expression, standing in cultivation chamber
```

**多人镜头**：
```
Lin Chen facing Elder Liu, both in sect main hall, tense confrontation atmosphere
```

**群像镜头**：
```
Outer sect disciples gathered in trial arena, Lin Chen at center, others watching with mixed expressions of jealousy and shock
```

### 2.2 场景为主

**空镜头**：
```
Sect main hall interior, jade pillars with golden accents, soft ambient lighting, empty and solemn
```

**场景+氛围**：
```
Misty forest at dawn, ancient trees with ethereal fog, spiritual energy flowing through the air
```

---

## 3. 动作/情绪（让画面动起来）

### 3.1 人物动作

**静态 → 微动**：
```
Lin Chen standing still, slight breeze moving his robes, focused gaze
```

**中等动作**：
```
Lin Chen slowly raising his hand, spiritual energy gathering in his palm, glowing blue light
```

**大幅动作**：
```
Lin Chen leaping forward, executing a cultivation technique, energy burst effect
```

**对话/表情**：
```
Elder Liu speaking with stern expression, slight head tilt, authoritative presence
```

### 3.2 场景动态

**自然元素**：
```
Wind blowing through misty forest, leaves gently falling, fog drifting
```

**灵气/法术特效**：
```
Spiritual energy swirling around Lin Chen, blue-white glow intensifying, runes appearing in the air
```

---

## 4. 镜头运动（导演语言）

### 4.1 基础运镜

**推进（Push in）**：
```
Camera slowly pushing forward toward Lin Chen's face, revealing determined expression
```

**拉远（Pull out）**：
```
Camera pulling back to reveal the full trial arena, Lin Chen at center
```

**环绕（Orbit）**：
```
Camera orbiting around Lin Chen as he channels spiritual energy, 360-degree reveal
```

**俯拍（Overhead）**：
```
Aerial view descending toward sect complex, revealing grand architecture
```

**仰拍（Low angle）**：
```
Low angle shot looking up at Elder Liu on the high platform, emphasizing authority
```

**跟随（Follow）**：
```
Camera following Lin Chen as he walks through the sect courtyard, steady tracking shot
```

### 4.2 组合运镜

**推进 + 聚焦**：
```
Camera pushing in while focusing on Lin Chen's eyes, background gradually blurring
```

**环绕 + 上升**：
```
Camera orbiting and rising around the trial arena, revealing the full scene from above
```

---

## 5. 时长/节奏控制

**慢节奏（适合氛围、情绪）**：
```
Slow paced, contemplative mood, 5-second duration
```

**中速（适合对话、日常）**：
```
Natural pacing, conversational rhythm, 8-second duration
```

**快节奏（适合动作、冲突）**：
```
Dynamic pacing, intense action, 3-second quick cut
```

---

## 6. 技术参数（根据平台能力调整）

```
1080p resolution, 24fps, smooth motion, high detail preservation
```

**如果支持首尾帧**：
```
Start frame: [描述起始画面], End frame: [描述结束画面]
```

**如果支持参考图**：
```
Reference image: [上传角色/场景设定图], maintain character consistency
```

---

## 7. 排除项（避免崩坏）

```
No text, no logo, no watermark, no distortion, no style inconsistency, no character face change
```

**针对性排除**：
- 避免角色崩坏：`maintain Lin Chen's facial features and robe design`
- 避免场景变化：`keep sect main hall architecture consistent`
- 避免多余元素：`no modern objects, no anachronistic elements`

---

## 完整示例提示词

### 示例 1：角色特写 + 情绪 + 推进镜头

```
3D semi-realistic 8K Chinese fantasy cultivation anime style, consistent with episode 3 visual reference. Lin Chen (protagonist), young male in gray outer sect robes, determined expression, eyes glowing with spiritual energy. Camera slowly pushing forward toward his face, revealing intense focus. Slow paced, contemplative mood, 5-second duration. 1080p, 24fps, smooth motion. No text, no logo, maintain Lin Chen's facial features.
```

---

### 示例 2：场景空镜 + 氛围 + 俯拍

```
3D semi-realistic 8K, warm golden lighting with blue-gray tones, Chinese cultivation aesthetic. Sect main hall interior, jade pillars with golden accents, soft ambient lighting, empty and solemn. Aerial view descending toward the hall, revealing grand architecture and spatial depth. Slow paced, establishing shot, 6-second duration. 1080p, 24fps, high detail preservation. No text, no logo, keep sect main hall architecture consistent.
```

---

### 示例 3：对抗场景 + 多人 + 环绕镜头

```
3D semi-realistic 8K Chinese fantasy cultivation anime style. Lin Chen facing Zhao Hu in trial arena, both in combat stance, spiritual energy crackling between them. Camera orbiting around the two characters, 180-degree arc, revealing tense confrontation. Dynamic pacing, intense action, 4-second duration. 1080p, 24fps, smooth motion. No text, no logo, maintain character consistency for both Lin Chen and Zhao Hu.
```

---

### 示例 4：法术特效 + 动作 + 推进+聚焦

```
3D semi-realistic 8K, blue-white spiritual energy glow, Chinese cultivation aesthetic. Lin Chen executing cultivation technique, hand raised, energy burst forming in his palm, runes appearing in the air. Camera pushing in while focusing on the glowing energy sphere, background gradually blurring. Medium pacing, 5-second duration. 1080p, 24fps, high detail on energy effects. No text, no logo, no distortion.
```

---

### 示例 5：环境动态 + 跟随镜头

```
3D semi-realistic 8K, misty forest at dawn, ethereal atmosphere, Chinese fantasy cultivation setting. Lin Chen walking through ancient trees, fog drifting around him, spiritual energy faintly visible in the air. Camera following Lin Chen from behind, steady tracking shot, revealing the forest path ahead. Natural pacing, 7-second duration. 1080p, 24fps, smooth motion. No text, no logo, maintain forest environment consistency.
```

---

## 分镜脚本 → 提示词转换流程

### 第4集第1幕示例

**分镜描述**：
> 镜头1：宗门大殿外景，清晨，俯拍  
> 镜头2：林辰走进大殿，推进镜头  
> 镜头3：柳长老坐在高台，仰拍  
> 镜头4：林辰与柳长老对话，正反打

**转换为 Seedance 2.0 提示词**：

#### 镜头1
```
3D semi-realistic 8K, warm golden morning light, Chinese cultivation sect architecture. Sect main hall exterior at dawn, jade roof tiles, stone steps leading up, misty clouds surrounding. Aerial view descending toward the entrance, revealing grand scale. Slow paced, establishing shot, 6-second duration. 1080p, 24fps. No text, no logo.
```

#### 镜头2
```
3D semi-realistic 8K Chinese fantasy cultivation anime style. Lin Chen walking into sect main hall, gray outer sect robes, calm determined expression. Camera pushing forward following his movement, revealing the interior space. Natural pacing, 5-second duration. 1080p, 24fps. No text, maintain Lin Chen's character design.
```

#### 镜头3
```
3D semi-realistic 8K, authoritative atmosphere, Chinese cultivation aesthetic. Elder Liu seated on high platform in main hall, white elder robes, stern expression, hands resting on armrests. Low angle shot looking up, emphasizing authority and power. Slow paced, 4-second duration. 1080p, 24fps. No text, maintain Elder Liu's character design.
```

#### 镜头4（正打）
```
3D semi-realistic 8K Chinese fantasy cultivation anime style. Lin Chen speaking, slight head tilt, respectful but firm expression, facing Elder Liu. Medium shot from Elder Liu's perspective. Natural pacing, conversational rhythm, 3-second duration. 1080p, 24fps. No text, maintain Lin Chen's facial features.
```

#### 镜头4（反打）
```
3D semi-realistic 8K, authoritative presence, Chinese cultivation aesthetic. Elder Liu responding, slight frown, evaluating gaze, facing Lin Chen. Medium shot from Lin Chen's perspective. Natural pacing, conversational rhythm, 3-second duration. 1080p, 24fps. No text, maintain Elder Liu's character design.
```

---

## 提示词优化技巧

### 1. 角色一致性强化
在每个涉及同一角色的提示词中，重复关键特征：
```
Lin Chen (gray outer sect robes, determined expression, young male protagonist)
```

### 2. 场景一致性强化
在同一场景的多个镜头中，重复场景核心元素：
```
Sect main hall (jade pillars, golden accents, high platform)
```

### 3. 风格一致性强化
每个提示词开头都带上统一的风格描述：
```
3D semi-realistic 8K Chinese fantasy cultivation anime style, consistent with episode 3 visual reference
```

### 4. 镜头衔接优化
如果平台支持首尾帧，在连续镜头间明确指定：
```
镜头A结束帧 = 镜头B起始帧
```

### 5. 动作幅度控制
- 小动作：`slight`, `subtle`, `gentle`
- 中等动作：`moderate`, `natural`, `steady`
- 大动作：`dynamic`, `intense`, `dramatic`

---

## 常见问题与解决方案

### Q1: 角色在不同镜头中长相不一致
**解决**：
1. 每次都带上角色的核心特征描述
2. 如果平台支持，上传角色参考图
3. 在提示词末尾加 `maintain [角色名]'s facial features and design`

### Q2: 场景风格在不同镜头中飘移
**解决**：
1. 统一使用同一套场景描述模板
2. 明确指定色调和光照
3. 在提示词末尾加 `keep [场景名] architecture/environment consistent`

### Q3: 镜头运动不自然或过度
**解决**：
1. 明确指定运镜速度：`slowly`, `steadily`, `smoothly`
2. 限制运镜幅度：`slight push in`, `gentle orbit`
3. 避免复杂组合运镜，优先单一运镜

### Q4: 生成的视频时长不符合预期
**解决**：
1. 明确指定时长：`5-second duration`
2. 配合节奏描述：`slow paced` / `dynamic pacing`
3. 如果平台不支持精确时长，用"快慢"描述代替

### Q5: 特效过度或不足
**解决**：
1. 明确特效强度：`subtle glow` / `intense energy burst`
2. 指定特效颜色和形态：`blue-white spiritual energy, swirling pattern`
3. 在排除项中加 `no over-exaggerated effects`

---

## 批量生产工作流建议

### 第1步：准备资产库
- 角色设定图（正面、侧面、背面）
- 场景参考图（多角度）
- 道具/特效参考图

### 第2步：编写分镜脚本
- 明确每个镜头的：主体、动作、镜头运动、时长

### 第3步：转换为提示词
- 使用本模板批量生成提示词
- 保持同一场景/角色的描述一致

### 第4步：分批生成测试
- 先生成关键镜头（角色特写、场景建立镜头）
- 检查一致性
- 调整提示词模板

### 第5步：全量生成
- 按场景分组批量生成
- 记录每个镜头的提示词和生成参数
- 建立提示词版本库

### 第6步：后期衔接
- 检查镜头间的连贯性
- 必要时补拍过渡镜头
- 统一调色和节奏

---

## 提示词模板库（快速复用）

### 角色情绪模板
```
[角色名], [服装], [情绪] expression, [微动作]
```

示例：
- `Lin Chen, gray robes, determined expression, eyes glowing slightly`
- `Elder Liu, white elder robes, stern expression, slight frown`
- `Zhao Hu, outer sect robes, jealous expression, clenched fists`

### 场景氛围模板
```
[场景名], [时间], [光照], [氛围元素]
```

示例：
- `Sect main hall, morning, warm golden light, solemn atmosphere`
- `Trial arena, noon, bright sunlight, tense atmosphere`
- `Misty forest, dawn, soft diffused light, mysterious atmosphere`

### 镜头运动模板
```
Camera [运动方式] [方向/路径], [速度], [焦点变化]
```

示例：
- `Camera slowly pushing forward toward character's face, revealing expression`
- `Camera orbiting around the scene, 180-degree arc, maintaining focus on center`
- `Camera pulling back to reveal full environment, steady smooth motion`

### 动作描述模板
```
[角色] [动作动词] [动作对象], [动作细节], [特效/反馈]
```

示例：
- `Lin Chen raising his hand, spiritual energy gathering in palm, blue glow intensifying`
- `Elder Liu standing up from throne, robes flowing, authoritative presence`
- `Zhao Hu lunging forward, fist clenched, energy crackling around his body`

---

**最后更新**：2026-03-08  
**版本**：1.0  
**维护者**：Jarvis (OpenClaw Agent)  
**项目**：《代码修真》系列漫剧制作
