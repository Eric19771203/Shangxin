# 口红TVC广告创建演示

## 产品信息
![高端口红产品](https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=premium%20luxury%20lipstick%20in%20elegant%20packaging%2C%20red%20lipstick%20with%20gold%20accents%2C%20professional%20product%20photography%2C%20soft%20lighting%2C%20cinematic%20quality%2C%20high-end%20beauty%20product&image_size=square_hd)

- **产品名称**：璀璨红唇口红
- **产品描述**：高端奢华口红，采用进口原料，持久显色，滋润不拔干，打造完美唇妆，是现代女性展现自信魅力的必备美妆产品。
- **目标受众**：20-40岁女性，注重个人形象，追求高品质生活，有一定消费能力
- **产品卖点**：持久显色、滋润保湿、奢华包装、多种色号、适合各种场合

## 交互式创建流程

### 步骤1：初始调用
```markdown
[SKILL_CALL]
skill_id: SKILL-010
mode: interactive
input:
  product:
    name: "璀璨红唇口红"
    description: "高端奢华口红，采用进口原料，持久显色，滋润不拔干，打造完美唇妆，是现代女性展现自信魅力的必备美妆产品。"
    category: "beauty"
  basic_info:
    duration: "30s"
    region: "China"
    language: "Chinese"
output_to: lipstick_tvc_workflow.json
[/SKILL_CALL]
```

### 步骤2：产品分析结果
```json
{
  "success": true,
  "data": {
    "step": 1,
    "analysis": {
      "product_type": "beauty_cosmetics",
      "key_features": ["高端奢华", "持久显色", "滋润保湿", "奢华包装"],
      "target_audience": "20-40岁女性",
      "recommended_style": "Wes Anderson + Bold Color Blocking",
      "confidence": 0.95
    },
    "message": "产品分析完成，建议使用Wes Anderson风格突出产品的时尚感和奢华感"
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
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    }
output_to: lipstick_tvc_workflow.json
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
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    }
output_to: lipstick_tvc_workflow.json
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
    trend: "Trend 2"
    trend_name: "二次元IP深度绑定"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    }
output_to: lipstick_tvc_workflow.json
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
    style: "Wes Anderson + Bold Color Blocking"
    style_description: "韦斯·安德森风格配合大胆色彩块，时尚感强"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 2",
      "trend_name": "二次元IP深度绑定"
    }
output_to: lipstick_tvc_workflow.json
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
    focus: "balanced"
    focus_level: "60%产品，40%叙事"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 2",
      "trend_name": "二次元IP深度绑定"
    },
    step_5: {
      "style": "Wes Anderson + Bold Color Blocking",
      "style_description": "韦斯·安德森风格配合大胆色彩块，时尚感强"
    }
output_to: lipstick_tvc_workflow.json
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
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 2",
      "trend_name": "二次元IP深度绑定"
    },
    step_5: {
      "style": "Wes Anderson + Bold Color Blocking",
      "style_description": "韦斯·安德森风格配合大胆色彩块，时尚感强"
    },
    step_6: {
      "focus": "balanced",
      "focus_level": "60%产品，40%叙事"
    }
output_to: lipstick_tvc_workflow.json
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
    pacing: "Fast/Dynamic"
    shots_per_15s: "9"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 2",
      "trend_name": "二次元IP深度绑定"
    },
    step_5: {
      "style": "Wes Anderson + Bold Color Blocking",
      "style_description": "韦斯·安德森风格配合大胆色彩块，时尚感强"
    },
    step_6: {
      "focus": "balanced",
      "focus_level": "60%产品，40%叙事"
    },
    step_7: {
      "duration": "30s",
      "shot_count": "12"
    }
output_to: lipstick_tvc_workflow.json
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
    concept: "concept_2"
    concept_name: "自信魅力，由唇开始"
  previous_selections:
    step_1: {
      "analysis_complete": true,
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 2",
      "trend_name": "二次元IP深度绑定"
    },
    step_5: {
      "style": "Wes Anderson + Bold Color Blocking",
      "style_description": "韦斯·安德森风格配合大胆色彩块，时尚感强"
    },
    step_6: {
      "focus": "balanced",
      "focus_level": "60%产品，40%叙事"
    },
    step_7: {
      "duration": "30s",
      "shot_count": "12"
    },
    step_8: {
      "pacing": "Fast/Dynamic",
      "shots_per_15s": "9"
    },
    step_9: {
      "concepts_generated": true
    }
output_to: lipstick_tvc_workflow.json
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
      "recommended_style": "Wes Anderson + Bold Color Blocking"
    },
    step_2: {
      "region": "China"
    },
    step_3: {
      "language": "Chinese"
    },
    step_4: {
      "trend": "Trend 2",
      "trend_name": "二次元IP深度绑定"
    },
    step_5: {
      "style": "Wes Anderson + Bold Color Blocking",
      "style_description": "韦斯·安德森风格配合大胆色彩块，时尚感强"
    },
    step_6: {
      "focus": "balanced",
      "focus_level": "60%产品，40%叙事"
    },
    step_7: {
      "duration": "30s",
      "shot_count": "12"
    },
    step_8: {
      "pacing": "Fast/Dynamic",
      "shots_per_15s": "9"
    },
    step_10: {
      "concept": "concept_2",
      "concept_name": "自信魅力，由唇开始"
    },
    step_11: {
      "imagination_weight": "70%"
    },
    step_12: {
      "framework": "Dimensional Shift"
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
output_to: lipstick_tvc_final.md
[/SKILL_CALL]
```

## 最终生成的口红TVC故事板

### 项目信息
- **产品**：璀璨红唇口红
- **时长**：30秒
- **区域**：中国
- **视觉风格**：Wes Anderson + Bold Color Blocking
- **语言**：中文
- **焦点**：平衡型 (60%产品，40%叙事)

### 创意概念
**主题**: 自信魅力，由唇开始

**创意概念**:
- **Hook**: 时尚女性涂抹口红的特写，展现产品质感
- **Core Insight**: 口红是女性展现自信魅力的重要工具
- **Twist**: 通过不同场景的切换，展示口红在各种场合的适用性
- **Emotional Tone**: 时尚、自信、活力、高端

### 30秒 TVC 脚本

| 时间 | 画面 | 旁白 | 音效 |
|------|------|------|------|
| 0-5秒 | 特写：璀璨红唇口红奢华包装，镜头环绕展现细节 | "璀璨红唇，自信之选" | 时尚动感音乐前奏 |
| 5-10秒 | 中景：时尚女性打开口红，准备涂抹 | "奢华质感，触手可及" | 包装开启声 |
| 10-15秒 | 特写：口红涂抹过程，色彩饱满均匀 | "持久显色，一步到位" | 涂抹声 |
| 15-20秒 | 快速切换：女性在不同场合展现唇妆魅力 | "无论是职场还是派对" | 场景切换音效 |
| 20-25秒 | 特写：女性微笑，红唇特写，产品摆放 | "璀璨红唇，绽放魅力" | 音乐高潮 |
| 25-30秒 | 全景：产品阵列，品牌logo，slogan | "璀璨红唇口红，自信魅力之选" | 品牌音乐 |

### 分镜设计

| 镜头 | 时间 | 类型 | 镜头运动 | 画面描述 | 音效 | AI提示词 |
|------|------|------|----------|----------|------|----------|
| 1 | 0-5秒 | CU | 环绕运动 | 璀璨红唇口红奢华包装特写，金色瓶盖，红色管身，镜头360度环绕展现细节，背景是几何色块 | 时尚动感音乐前奏 | Close-up of luxury lipstick packaging, red tube with gold accents, 360-degree camera movement, Wes Anderson style with bold color blocking background, geometric patterns, cinematic quality, high-end beauty product |
| 2 | 5-10秒 | MS | 推近 | 时尚女性手持口红，手指优雅地旋转打开瓶盖，准备涂抹，背景是明亮的化妆间 | 包装开启声 | Medium shot of stylish woman opening lipstick, elegant hand movements, modern makeup room setting, Wes Anderson aesthetic, bold color blocking, cinematic lighting, fashion editorial style |
| 3 | 10-15秒 | CU | 固定 | 口红涂抹过程特写，色彩饱满均匀地覆盖双唇，展现产品质地和显色度 | 涂抹声 | Extreme close-up of lipstick application, vibrant red color gliding smoothly across lips, detailed texture, Wes Anderson style lighting, bold color palette, professional beauty photography |
| 4 | 15-20秒 | MS | 快速切换 | 快速切换三个场景：职场会议、朋友聚会、浪漫约会，女性在不同场合展现唇妆魅力 | 场景切换音效 | Rapid sequence of three scenes: business meeting, friends gathering, romantic date, woman showcasing lipstick in different settings, Wes Anderson aesthetic, bold color blocking, dynamic editing, fashion commercial style |
| 5 | 20-25秒 | CU | 缓慢拉远 | 女性微笑特写，红唇清晰可见，然后镜头拉远展示完整妆容和自信表情，产品摆放在旁边 | 音乐高潮 | Close-up of woman's smile with perfect red lips, camera slowly pulling back to show full face and confident expression, lipstick product visible in foreground, Wes Anderson lighting, bold color palette, cinematic quality |
| 6 | 25-30秒 | WS | 缓慢推近 | 多个色号的璀璨红唇口红整齐排列，背景是几何色块，品牌logo和slogan清晰可见 | 品牌音乐 | Wide shot of multiple lipstick shades arranged elegantly, geometric color blocking background, brand logo "璀璨红唇" visible, Wes Anderson style composition, bold colors, cinematic lighting, luxury beauty product display |

### AI生图提示词

**Gemini 3格式**:
- 镜头1: Close-up of luxury lipstick packaging, red tube with gold accents, 360-degree camera movement, Wes Anderson style with bold color blocking background, geometric patterns, cinematic quality, high-end beauty product, professional product photography, sharp details, vibrant colors, 4K resolution
- 镜头2: Medium shot of stylish young woman opening lipstick, elegant hand movements, modern makeup room setting with bold color blocking walls, Wes Anderson aesthetic, cinematic lighting, fashion editorial style, professional beauty photography, 4K resolution
- 镜头3: Extreme close-up of lipstick application on lips, vibrant red color gliding smoothly, detailed lip texture, soft natural lighting, Wes Anderson style composition, bold color palette, professional beauty photography, sharp focus, 4K resolution
- 镜头4: Rapid sequence of three scenes (business meeting, friends gathering, romantic date), woman with red lipstick in different settings, Wes Anderson aesthetic with bold color blocking, dynamic editing, fashion commercial style, professional photography, 4K resolution
- 镜头5: Close-up of woman's smile with perfect red lips, camera pulling back to show full face and confident expression, lipstick product in foreground, Wes Anderson lighting, bold color palette, cinematic quality, fashion editorial style, 4K resolution
- 镜头6: Wide shot of multiple lipstick shades arranged elegantly on geometric display, bold color blocking background, brand logo visible, Wes Anderson style composition, vibrant colors, cinematic lighting, luxury beauty product photography, 4K resolution

**Midjourney格式**:
- 镜头1: Close-up luxury lipstick packaging, red tube gold accents, 360 camera movement, Wes Anderson style, bold color blocking background, geometric patterns, cinematic, high-end beauty product, professional photography --ar 16:9 --quality 5
- 镜头2: Medium shot stylish woman opening lipstick, elegant hands, modern makeup room, Wes Anderson aesthetic, bold color blocking, cinematic lighting, fashion editorial --ar 16:9 --quality 5
- 镜头3: Extreme close-up lipstick application on lips, vibrant red color, smooth texture, Wes Anderson style, bold colors, professional beauty photography --ar 16:9 --quality 5
- 镜头4: Sequence of three scenes, woman with red lipstick in business meeting, friends gathering, romantic date, Wes Anderson aesthetic, bold color blocking, dynamic editing, fashion commercial --ar 16:9 --quality 5
- 镜头5: Close-up woman's smile with red lips, camera pulling back, lipstick in foreground, Wes Anderson lighting, bold color palette, fashion editorial --ar 16:9 --quality 5
- 镜头6: Wide shot multiple lipstick shades arranged elegantly, geometric display, bold color blocking background, brand logo, Wes Anderson composition, luxury beauty product --ar 16:9 --quality 5

### 技术说明

**制作考虑因素**:
- **灯光**：使用Wes Anderson风格的对称照明，配合大胆的色彩块，突出产品质感
- **相机**：采用专业美容产品摄影镜头，确保细节清晰
- **道具**：选择与产品调性匹配的时尚道具，如现代化妆间、几何装饰
- **背景**：大胆的色彩块和几何图案，营造时尚感
- **剪辑**：快速动感的剪辑节奏，适合口红产品的时尚定位
- **音乐**：选择时尚动感的音乐，增强产品的现代感

**后期制作**:
- **色彩分级**：保持Wes Anderson风格的鲜明色彩，增强产品的时尚感
- **音效设计**：添加时尚的音效，增强画面的动感
- **文字叠加**：简洁的产品信息和品牌标语
- **Logo放置**：在结尾清晰展示品牌logo和slogan

## 总结

本交互式TVC创建流程成功为璀璨红唇口红生成了一个时尚动感的30秒广告片。通过16个交互式步骤，用户可以完全控制创意方向，从产品分析到最终故事板生成，确保每一个细节都符合品牌调性和目标受众需求。

最终生成的TVC广告片通过时尚动感的画面和节奏，展现了璀璨红唇口红的奢华质感和时尚魅力，符合现代女性对美妆产品的追求，能够有效传达产品价值和品牌形象。