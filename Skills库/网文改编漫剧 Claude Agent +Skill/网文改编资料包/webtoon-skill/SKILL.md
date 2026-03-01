---
id: SKILL-009
name: webtoon-skill
version: 1.0.0
description: 网文改编漫剧剧本创作技能包。执行剧情分解、剧本改编的专业创作，基于网文改编法则和漫剧化写作风格生成高质量漫剧内容。
category: drama-writing
author: system
created_at: 2026-02-18
updated_at: 2026-02-18
---

# 网文改编漫剧创作 Skill

## 技能说明
专业的网文改编漫剧剧本创作技能包，覆盖剧情分解、剧本改编全流程。根据不同创作阶段，读取对应的创作资源并生成符合漫剧化规范的改编内容。

## 文件结构
```
.claude/skills/webtoon-skill/
├── SKILL.md                        # 本文件（技能包核心配置）
├── adapt-method.md                 # 改编方法论
├── output-style.md                # 写作风格（含剧本创作方法）
├── examples/
│   ├── plot-breakdown-example.md   # 剧情分解示例
│   └── script-example.md           # 剧本示例
└── templates/
    ├── plot-breakdown-template.md   # 剧情分解模板
    └── script-template.md           # 剧本模板
```

## 核心能力
- **创作阶段理解**：识别当前处于剧情分解还是剧本改编阶段
- **资源整合**：读取模板、方法论、风格、示例等多维度资源
- **专业创作**：基于资源和上下文创作符合漫剧化规范的改编内容
- **风格把控**：确保创作内容符合漫剧化的视觉化写作风格
- **模板遵循**：严格按照模板格式生成文档结构
- **上下文理解**：理解已有文档内容，确保创作连贯性

## 输入参数
```json
{
  "stage": "string - 创作阶段 (plot/script)",
  "context": "object - 上下文信息",
  "content": "string - 创作内容或需求",
  "config": {
    "style": "string - 写作风格",
    "length": "string - 内容长度"
  }
}
```

## 输出格式
```json
{
  "success": "boolean",
  "data": {
    "content": "string - 生成的创作内容",
    "format": "string - 文档格式",
    "stage": "string - 创作阶段"
  },
  "message": "string - 执行结果消息",
  "metadata": {
    "version": "string - skill版本",
    "timestamp": "string - 执行时间"
  }
}
```

## 执行流程
1. **理解创作需求**
   - 识别当前创作阶段
   - 分析用户输入内容

2. **读取创作资源**
   - 根据创作阶段读取相应的模板和方法论
   - 参考示例文件确保风格一致

3. **执行专业创作**
   - 基于资源和上下文生成改编内容
   - 确保符合漫剧化的视觉化写作风格

4. **返回创作成果**
   - 按照标准格式返回创作内容
   - 包含执行结果和元数据

## 创作原则
- **模板遵循原则**：严格按照模板格式生成文档结构
- **风格一致性原则**：保持漫剧化的视觉化写作风格统一
- **上下文连贯性原则**：确保前后内容不矛盾，逻辑连贯
- **质量标准原则**：确保创作内容质量符合专业标准

## 示例调用
```markdown
[SKILL_CALL]
skill_id: SKILL-009
mode: full
input:
  stage: "plot"
  content: "改编一个关于都市修仙的网文"
output_to: plot-breakdown.md
[/SKILL_CALL]
```

## 错误处理
- **参数错误**：当输入参数不完整或格式错误时，返回错误提示
- **资源缺失**：当所需模板或方法论文件缺失时，返回错误提示
- **创作失败**：当创作过程中出现问题时，返回详细的错误信息