---
name: "creative-concept"
description: "Generates creative concepts and visual ideas for storyboard projects based on requirements and director style. Invoke when need to develop visual concepts and artistic direction."
---

# Creative Concept

Generates creative concepts and visual ideas for storyboard projects.

## When to Invoke

- Requirements have been analyzed
- Director style has been selected
- Need to establish visual language for the project
- Preparing for detailed scene breakdown

## Input

```json
{
  "requirement": "string - Project requirement",
  "genre": "string - Project genre",
  "director": "string - Selected director name",
  "style": "string - Visual style preference",
  "tone": "string - Emotional tone"
}
```

## Output

```json
{
  "core_concept": "string - Main creative concept in one sentence",
  "visual_metaphors": ["array of visual metaphors"],
  "key_elements": {
    "lighting": "string - Lighting approach",
    "composition": "string - Composition style",
    "color_approach": "string - Color philosophy",
    "texture": "string - Texture and material feel"
  },
  "scene_archetypes": [
    {
      "type": "string - Scene type (establishing, character, action, emotional, transition)",
      "description": "string - How to visualize this archetype",
      "reference": "string - Visual reference or example"
    }
  ],
  "mood_keywords": ["array of 10 mood descriptors"],
  "visual_references": ["array of film/art references"]
}
```

## Concept Development Framework

### Core Concept
A single sentence that captures the visual essence of the project.

### Visual Metaphors
- Identify core themes from requirements
- Find visual symbols that represent themes
- Develop metaphorical imagery
- Ensure consistency with director style

### Key Elements
- **Lighting**: Naturalistic, dramatic, high-contrast, soft, chiaroscuro, neon
- **Composition**: Symmetrical, dynamic, rule of thirds, centered, off-center, layered
- **Color**: Monochromatic, complementary, analogous, triadic, desaturated, vibrant
- **Texture**: Smooth, gritty, organic, synthetic, weathered, polished

### Scene Archetypes
- **Establishing Shot**: Sets the scene and atmosphere
- **Character Introduction**: Reveals personality through visuals
- **Action Sequence**: Dynamic movement and energy
- **Emotional Beat**: Intimate character moments
- **Transition**: Smooth scene changes

## Prompt Template

```
你是一位资深的视觉概念设计师。请为以下项目创作核心视觉概念：

项目需求：{requirement}
项目类型：{genre}
参考导演：{director}
视觉风格：{style}
情感基调：{tone}

请创作：
1. 核心创意概念（一句话概括视觉主题）
2. 3-5个视觉隐喻（用视觉元素表达抽象概念）
3. 关键视觉元素定义：
   - 光影处理方式（自然光/戏剧光/高对比/柔和等）
   - 构图风格（对称/动态/三分法/居中/分层等）
   - 色彩哲学（单色/互补/类似/三角色/饱和度等）
   - 材质质感（光滑/粗糙/有机/合成/风化等）
4. 5种场景原型的视觉处理建议（开场、人物、动作、情感、转场）
5. 10个氛围关键词
6. 3-5个视觉参考作品

以JSON格式返回结果。
```

## Example

Input:
```json
{
  "requirement": "未来战争科幻短片，讲述士兵在废墟中寻找希望",
  "genre": "scifi",
  "director": "Denis Villeneuve",
  "style": "cinematic",
  "tone": "epic"
}
```

Output:
```json
{
  "core_concept": "在末日废墟中，人性的微光穿透战争的阴霾，如同沙漠中的绿洲般珍贵",
  "visual_metaphors": [
    "废墟中的绿植象征希望",
    "尘埃中的光线象征救赎",
    "破损的镜子反映人性",
    "远方的地平线象征未来"
  ],
  "key_elements": {
    "lighting": "自然光与戏剧光结合，强调尘埃中的光束和剪影",
    "composition": "宏大广角与 intimate 特写交替，强调孤独感",
    "color_approach": "沙色调为主，点缀希望的绿色和温暖的金色",
    "texture": "粗糙的废墟质感与光滑的科技感装备形成对比"
  },
  "scene_archetypes": [
    {
      "type": "establishing",
      "description": "航拍废墟全景，缓慢推近，建立世界规模",
      "reference": "《沙丘》开场沙漠镜头"
    },
    {
      "type": "character",
      "description": "逆光剪影，面部细节在阴影中若隐若现",
      "reference": "《降临》中Amy Adams的特写"
    },
    {
      "type": "action",
      "description": "手持摄影跟随，强调真实感和紧张感",
      "reference": "《边境杀手》追车戏"
    },
    {
      "type": "emotional",
      "description": "极浅景深，焦点在眼神，背景完全虚化",
      "reference": "《银翼杀手2049》K与Joi的场景"
    },
    {
      "type": "transition",
      "description": "匹配剪辑，从废墟到回忆的流畅过渡",
      "reference": "《降临》的时间线切换"
    }
  ],
  "mood_keywords": ["史诗", "孤独", "希望", "废墟", "未来", "人性", "救赎", "宏大", "静谧", "庄严"],
  "visual_references": ["《沙丘》", "《降临》", "《银翼杀手2049》", "《疯狂的麦克斯：狂暴之路》"]
}
```