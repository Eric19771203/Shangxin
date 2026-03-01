# TVC广告片交互式创建演示

## 产品信息
![露华燕舍鲜炖燕窝](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=premium%20bird%27s%20nest%20jar%20with%20blue-green%20lid%2C%20transparent%20glass%20bottle%20containing%20white%20bird%27s%20nest%2C%20purple%20gradient%20background%2C%20elegant%20light%20effects%2C%20product%20photography%2C%20cinematic%20quality&image_size=square_hd)

- **产品名称**：露华燕舍鲜炖燕窝
- **净含量**：250g
- **产品描述**：高品质鲜炖燕窝，采用传统工艺与现代技术相结合，营养丰富，口感顺滑，是现代都市女性的健康美容选择。
- **目标受众**：25-45岁女性，注重健康和美容，有一定消费能力

## 交互式创建流程

### 步骤1：初始调用
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  product:
    name: "露华燕舍鲜炖燕窝"
    description: "高品质鲜炖燕窝，净含量250g，营养丰富，口感顺滑，采用传统工艺与现代技术相结合，是现代都市女性的健康美容选择。"
    category: "health and beauty"
  basic_info:
    duration: "30s"
    region: "China"
    language: "Chinese"
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤2：产品分析结果
```json
{
  "success": true,
  "data": {
    "step": 1,
    "analysis": {
      "product_type": "health supplement",
      "key_features": ["高品质", "鲜炖工艺", "营养丰富", "口感顺滑"],
      "target_audience": "25-45岁女性",
      "recommended_style": "Mocha Mousse + Sculptural Lighting",
      "confidence": 0.92
    },
    "message": "产品分析完成，建议使用Mocha Mousse风格突出产品质感"
  }
}
```

### 步骤3：区域选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 2
  selection:
    region: "China"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤4：语言选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 3
  selection:
    language: "Chinese"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤5：创意趋势选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 4
  selection:
    trend: "Trend 4"
    trend_name: "极致高级感美学"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤6：视觉风格选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 5
  selection:
    style: "Mocha Mousse + Sculptural Lighting"
    style_description: "摩卡慕斯风格配合雕塑式灯光，温暖高级"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 4",
      "trend_name": "极致高级感美学"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤7：叙事焦点选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 6
  selection:
    focus: "product"
    focus_level: "80%"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 4",
      "trend_name": "极致高级感美学"
    },
    step_5: {
      "style": "Mocha Mousse + Sculptural Lighting",
      "style_description": "摩卡慕斯风格配合雕塑式灯光，温暖高级"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤8：时长确认
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 7
  selection:
    duration: "30s"
    shot_count: "12"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 4",
      "trend_name": "极致高级感美学"
    },
    step_5: {
      "style": "Mocha Mousse + Sculptural Lighting",
      "style_description": "摩卡慕斯风格配合雕塑式灯光，温暖高级"
    },
    step_6: {
      "focus": "product",
      "focus_level": "80%"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤9：节奏选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 8
  selection:
    pacing: "Standard"
    shots_per_15s: "6"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 4",
      "trend_name": "极致高级感美学"
    },
    step_5: {
      "style": "Mocha Mousse + Sculptural Lighting",
      "style_description": "摩卡慕斯风格配合雕塑式灯光，温暖高级"
    },
    step_6: {
      "focus": "product",
      "focus_level": "80%"
    },
    step_7: {
      "duration": "30s",
      "shot_count": "12"
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤10：创意概念选择
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 10
  selection:
    concept: "concept_1"
    concept_name: "品质滋养，绽放内在美"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 4",
      "trend_name": "极致高级感美学"
    },
    step_5: {
      "style": "Mocha Mousse + Sculptural Lighting",
      "style_description": "摩卡慕斯风格配合雕塑式灯光，温暖高级"
    },
    step_6: {
      "focus": "product",
      "focus_level": "80%"
    },
    step_7: {
      "duration": "30s",
      "shot_count": "12"
    },
    step_8: {
      "pacing": "Standard",
      "shots_per_15s": "6"
    },
    step_9: {
      "concepts_generated": true
    }
output_to: tvc_workflow.json
[/SKILL_CALL]
```

### 步骤11-15：后续步骤
（省略具体交互步骤，直接展示最终结果）

### 步骤16：最终故事板生成
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  step: 16
  selection:
    final_approval: true
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Mocha Mousse + Sculptural Lighting"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 4",
      "trend_name": "极致高级感美学"
    },
    step_5: {
      "style": "Mocha Mousse + Sculptural Lighting",
      "style_description": "摩卡慕斯风格配合雕塑式灯光，温暖高级"
    },
    step_6: {
      "focus": "product",
      "focus_level": "80%"
    },
    step_7: {
      "duration": "30s",
      "shot_count": "12"
    },
    step_8: {
      "pacing": "Standard",
      "shots_per_15s": "6"
    },
    step_10: {
      "concept": "concept_1",
      "concept_name": "品质滋养，绽放内在美"
    },
    step_11: {
      "imagination_weight": "60%"
    },
    step_12: {
      "framework": "Before-After-Bridge"
    },
    step_13: {
      "script_approved": true
    },
    step_14: {
      "storyboard_logic_approved": true
    },
    step_15: {
      "final_confirmation": true
    }
output_to: tvc_final_storyboard.md
[/SKILL_CALL]
```

## 最终生成的TVC故事板

### 项目信息
- **产品**：露华燕舍鲜炖燕窝
- **时长**：30秒
- **区域**：中国
- **视觉风格**：Mocha Mousse + Sculptural Lighting
- **语言**：中文
- **焦点**：产品 (80%)

### 创意概念
**主题**: 品质滋养，绽放内在美

**创意概念**:
- **Hook**: 精致的燕窝产品特写，展现质感和品质
- **Core Insight**: 现代女性注重内在健康与外在美丽的平衡
- **Twist**: 通过光影变化，展现燕窝从原料到成品的精致工艺
- **Emotional Tone**: 优雅、温馨、高品质

### 30秒 TVC 脚本

| 时间 | 画面 | 旁白 | 音效 |
|------|------|------|------|
| 0-5秒 | 特写：露华燕舍鲜炖燕窝瓶身，光影流转 | "品质生活，从内在滋养开始" | 轻柔钢琴前奏 |
| 5-10秒 | 中景：燕窝在瓶中晃动，展现顺滑质感 | "露华燕舍鲜炖燕窝" | 水流声 |
| 10-15秒 | 特写：燕窝原料，纯净透明 | "精选优质原料" | 自然环境音效 |
| 15-20秒 | 近景：炖煮过程，蒸汽升腾 | "传统工艺，现代技术" | 炖煮声 |
| 20-25秒 | 特写：成品燕窝，晶莹剔透 | "营养丰富，口感顺滑" | 优雅音乐高潮 |
| 25-30秒 | 全景：产品摆放在精致环境中，品牌logo | "露华燕舍，绽放内在美" | 品牌音乐 |

### 分镜设计

| 镜头 | 时间 | 类型 | 镜头运动 | 画面描述 | 音效 | AI提示词 |
|------|------|------|----------|----------|------|----------|
| 1 | 0-5秒 | CU | 缓慢推近 | 露华燕舍鲜炖燕窝瓶身特写，蓝绿色瓶盖，瓶中燕窝晶莹剔透，背景渐变紫色光晕，光影在瓶身流转 | 轻柔钢琴前奏 | Professional product photography, close-up of bird's nest jar with blue-green lid, mocha mousse lighting, sculptural light and shadow, purple gradient background, glass bottle with transparent bird's nest inside, cinematic quality, product-focused, high-end beauty product |
| 2 | 5-10秒 | MS | 轻微晃动 | 中景拍摄燕窝瓶，瓶身倾斜45度，燕窝在瓶中自然流动，展现顺滑质感，光线从侧面照射，突出产品纹理 | 水流声 | Medium shot of bird's nest jar tilting, bird's nest flowing smoothly inside, mocha mousse lighting, sculptural light highlighting texture, transparent glass bottle, blue-green lid, cinematic quality, product-focused |
| 3 | 10-15秒 | CU | 固定 | 燕窝原料特写，纯净透明的燕窝丝，背景模糊，光线从上方照射，突出原料的纯净质感 | 自然环境音效 | Close-up of bird's nest raw material, pure transparent bird's nest strands, mocha mousse lighting, soft top lighting, blurred background, high-end food photography, product-focused, cinematic quality |
| 4 | 15-20秒 | MS | 缓慢拉升 | 炖煮过程近景，燕窝在炖盅中炖煮，蒸汽轻轻升腾，光线温暖柔和，展现传统工艺的精致 | 炖煮声 | Medium shot of bird's nest being stewed, steam rising gently, warm mocha mousse lighting, traditional cooking process, cinematic quality, product-focused, soft lighting |
| 5 | 20-25秒 | CU | 缓慢旋转 | 成品燕窝特写，瓶中的燕窝晶莹剔透，光线从多角度照射，展现产品的质感和品质 | 优雅音乐高潮 | Close-up of finished bird's nest, crystal clear texture, mocha mousse lighting, sculptural light from multiple angles, transparent glass bottle, blue-green lid, cinematic quality, product-focused, high-end beauty product |
| 6 | 25-30秒 | WS | 缓慢拉远 | 全景：产品摆放在精致的木质托盘上，周围点缀鲜花，背景柔和光晕，品牌logo清晰可见 | 品牌音乐 | Wide shot of bird's nest jar on elegant wooden tray, surrounded by fresh flowers, mocha mousse lighting, soft gradient background, brand logo visible, cinematic quality, product-focused, high-end presentation |

### AI生图提示词

**Gemini 3格式**:
- 镜头1: Professional product photography of a premium bird's nest jar with blue-green lid, close-up shot, mocha mousse lighting with sculptural light and shadow, purple gradient background, glass bottle containing transparent bird's nest, cinematic quality, high-end beauty product, sharp focus on product details, smooth reflections, 4K resolution
- （其他镜头提示词省略）

**Midjourney格式**:
- 镜头1: Close-up product photography of premium bird's nest jar with blue-green lid, mocha mousse lighting, sculptural light and shadow, purple gradient background, glass bottle with transparent bird's nest inside, cinematic, high-end, product-focused, sharp details, 4K --ar 16:9 --quality 5
- （其他镜头提示词省略）

## 技术说明

### 制作考虑因素
- **灯光**：使用mocha mousse风格的暖色调灯光，配合雕塑式光影，突出产品质感
- **相机**：采用专业产品摄影镜头，确保细节清晰
- **道具**：选择与产品调性匹配的精致道具，如木质托盘、新鲜花朵
- **背景**：渐变紫色背景，营造优雅氛围
- **剪辑**：节奏舒缓，重点突出产品细节和质感
- **音乐**：选择轻柔优雅的钢琴音乐，增强产品的高品质感

### 后期制作
- **色彩分级**：保持mocha mousse风格的暖色调，增强产品的质感和高级感
- **音效设计**：轻柔的环境音效，配合产品特性
- **文字叠加**：简洁的产品信息和品牌标语
- **Logo放置**：在结尾清晰展示品牌logo

## 总结

本交互式TVC创建流程成功为露华燕舍鲜炖燕窝生成了一个高品质的30秒广告片。通过16个交互式步骤，用户可以完全控制创意方向，从产品分析到最终故事板生成，确保每一个细节都符合品牌调性和目标受众需求。

最终生成的TVC广告片通过精致的画面和优雅的叙事，展现了露华燕舍鲜炖燕窝的高品质和滋养功效，符合现代女性对健康美容的追求，能够有效传达产品价值和品牌形象。