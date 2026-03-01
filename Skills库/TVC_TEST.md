# TVC广告片测试

## 测试需求
为露华燕舍鲜炖燕窝创建一个30秒的TVC广告片，突出产品的高品质和营养功效。

## 产品信息
- **产品名称**：露华燕舍鲜炖燕窝
- **净含量**：250g
- **产品描述**：高品质鲜炖燕窝，采用传统工艺与现代技术相结合，营养丰富，口感顺滑，是现代都市女性的健康美容选择。
- **核心功能**：
  - 鲜炖工艺，保留营养
  - 口感顺滑，易于吸收
  - 高品质原料，安全可靠
  - 方便食用，适合现代生活
- **目标受众**：25-45岁女性，注重健康和美容，有一定消费能力

## 广告需求
- **时长**：30秒
- **目标区域**：中国
- **语言**：中文
- **风格**：Mocha Mousse + Sculptural Lighting（高级感风格）
- **重点**：产品性强，突出产品细节和品质

## 技能调用

[SKILL_CALL]
skill_id: SKILL-010
mode: full
input:
  product:
    name: "露华燕舍鲜炖燕窝"
    description: "高品质鲜炖燕窝，净含量250g，营养丰富，口感顺滑，采用传统工艺与现代技术相结合，是现代都市女性的健康美容选择。"
    category: "health and beauty"
    features:
      - "鲜炖工艺，保留营养"
      - "口感顺滑，易于吸收"
      - "高品质原料，安全可靠"
      - "方便食用，适合现代生活"
    target_audience: "25-45岁女性，注重健康和美容，有一定消费能力"
  requirements:
    duration: "30s"
    region: "China"
    language: "Chinese"
    style: "Mocha Mousse + Sculptural Lighting"
    focus: "product"
output_to: tvc_storyboard.md
[/SKILL_CALL]

## 预期结果
- 生成完整的30秒TVC广告脚本
- 包含详细的分镜设计
- 为每个镜头提供AI生图提示词
- 突出产品的高品质和营养功效
- 符合目标受众的审美和需求