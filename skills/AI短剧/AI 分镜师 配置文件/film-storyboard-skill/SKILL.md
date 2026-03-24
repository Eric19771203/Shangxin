---
id: SKILL-004
name: film-storyboard-skill
version: 1.0.0
description: 电影分镜创作技能包。执行分镜设计、镜头规划、画面描述的专业创作，基于电影语言和分镜方法论生成高质量分镜内容。
category: storyboard
author: system
created_at: 2026-02-18
updated_at: 2026-02-18
---

# 电影分镜创作 Skill

## 技能说明
专业的电影分镜创作技能包，覆盖分镜设计、镜头规划、画面描述全流程。根据不同创作阶段，读取对应的创作资源并生成符合电影语言规范的分镜内容。

## 文件结构
```
.claude/skills/film-storyboard-skill/
├── SKILL.md                        # 本文件（技能包核心配置）
├── storyboard-methodology-playbook.md   # 分镜方法论
├── gemini-image-prompt-guide.md        # AI生图提示词指南
├── templates/
│   ├── beat-board-template.md          # 节拍板模板
│   ├── beat-breakdown-template.md      # 节拍分解模板
│   └── sequence-board-template.md      # 序列板模板
```

## 核心能力
- **创作阶段理解**：识别当前处于分镜设计的哪个阶段
- **资源整合**：读取模板、方法论、风格、示例等多维度资源
- **专业创作**：基于资源和上下文创作符合电影语言规范的分镜内容
- **风格把控**：确保创作内容符合电影分镜的专业规范
- **模板遵循**：严格按照模板格式生成文档结构
- **上下文理解**：理解已有文档内容，确保创作连贯性

## 输入参数
```json
{
  "stage": "string - 创作阶段 (beat/sequence/scene)",
  "context": "object - 上下文信息",
  "content": "string - 创作内容或需求",
  "config": {
    "style": "string - 分镜风格",
    "format": "string - 输出格式"
  }
}
```

## 输出格式
```json
{
  "success": "boolean",
  "data": {
    "content": "string - 生成的分镜内容",
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
   - 基于资源和上下文生成分镜内容
   - 确保符合电影语言的专业规范

4. **返回创作成果**
   - 按照标准格式返回分镜内容
   - 包含执行结果和元数据

## 创作原则
- **模板遵循原则**：严格按照模板格式生成文档结构
- **风格一致性原则**：保持电影分镜的专业风格统一
- **上下文连贯性原则**：确保前后内容不矛盾，逻辑连贯
- **质量标准原则**：确保创作内容质量符合专业标准

## 示例调用
```markdown
[SKILL_CALL]
skill_id: SKILL-004
mode: full
input:
  stage: "beat"
  content: "创作一个关于追逐戏的节拍板"
output_to: beat-board.md
[/SKILL_CALL]
```

## 错误处理
- **参数错误**：当输入参数不完整或格式错误时，返回错误提示
- **资源缺失**：当所需模板或方法论文件缺失时，返回错误提示
- **创作失败**：当创作过程中出现问题时，返回详细的错误信息