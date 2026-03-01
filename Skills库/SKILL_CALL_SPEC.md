# Skill调用格式规范

## 一、标准调用格式

### 单技能调用
```markdown
[SKILL_CALL]
skill_id: SKILL-XXX
mode: full|partial
input:
  stage: "创作阶段"
  content: "创作内容或需求"
  context: "上下文信息"
  config:
    style: "风格配置"
    length: "长度配置"
output_to: "输出文件路径"
[/SKILL_CALL]
```

### 参数说明
- **skill_id**: 技能唯一标识符
- **mode**: 执行模式 (full: 完整执行, partial: 部分执行)
- **input**: 输入参数
- **output_to**: 输出文件路径

### 示例
```markdown
[SKILL_CALL]
skill_id: SKILL-001
mode: full
input:
  stage: "outline"
  content: "创作一个关于宫廷权谋的故事大纲"
  config:
    style: "文白相济"
    length: "medium"
output_to: outline.md
[/SKILL_CALL]
```

## 二、链式调用格式

### 多技能串联调用
```markdown
[SKILL_CHAIN]
chain_name: "创作全流程"

step_1:
  skill_id: SKILL-001
  action: "生成大纲"
  input:
    stage: "outline"
    content: "创作一个关于宫廷权谋的故事大纲"
  output_var: "outline_content"

step_2:
  skill_id: SKILL-001
  action: "生成人物"
  input_from: "outline_content"
  output_var: "character_content"

step_3:
  skill_id: SKILL-001
  action: "生成目录"
  input_from: "character_content"
  output_var: "catalog_content"

step_4:
  skill_id: SKILL-001
  action: "生成章节"
  input_from: "catalog_content"
  output_var: "chapter_content"

step_5:
  skill_id: SKILL-004
  action: "生成分镜"
  input_from: "chapter_content"
  output_var: "storyboard_content"

[/SKILL_CHAIN]
```

### 链式调用说明
- **chain_name**: 链式调用名称
- **step_***: 执行步骤，按顺序执行
- **input_from**: 从上一步骤获取输入
- **output_var**: 输出变量名，用于传递给下一步

## 三、技能ID映射

### 小说创作技能
- **SKILL-001**: gudai-skill (古代权谋小说)
- **SKILL-002**: xianyan-skill (现代言情小说)
- **SKILL-003**: xianshi-skill (现实题材小说)

### 分镜创作技能
- **SKILL-004**: film-storyboard-skill (电影分镜)
- **SKILL-005**: animator-skill (动画分镜)
- **SKILL-006**: storyboard-review-skill (分镜评审)

### 短剧创作技能
- **SKILL-007**: doomsday-skill (末世重生漫剧)
- **SKILL-008**: xuanhuan-skill (玄幻漫剧)
- **SKILL-009**: webtoon-skill (网文改编漫剧)

## 四、标准数据包格式

### 输入数据包
```json
{
  "skill_id": "string - 技能ID",
  "mode": "string - 执行模式",
  "input": {
    "stage": "string - 创作阶段",
    "content": "string - 创作内容",
    "context": "object - 上下文",
    "config": "object - 配置"
  },
  "output_to": "string - 输出路径",
  "metadata": {
    "timestamp": "string - 时间戳",
    "version": "string - 版本"
  }
}
```

### 输出数据包
```json
{
  "success": "boolean - 执行结果",
  "data": {
    "content": "string - 生成内容",
    "format": "string - 格式",
    "stage": "string - 阶段"
  },
  "message": "string - 消息",
  "metadata": {
    "skill_id": "string - 技能ID",
    "version": "string - 版本",
    "timestamp": "string - 时间戳"
  }
}
```

## 五、错误处理

### 错误码
- **400**: 参数错误
- **404**: 技能不存在
- **500**: 执行失败
- **503**: 技能不可用

### 错误响应格式
```json
{
  "success": false,
  "error": {
    "code": "number - 错误码",
    "message": "string - 错误消息",
    "details": "string - 详细信息"
  },
  "metadata": {
    "skill_id": "string - 技能ID",
    "timestamp": "string - 时间戳"
  }
}
```

## 六、使用指南

### 基本使用流程
1. **确定创作需求**：明确需要什么类型的创作内容
2. **选择合适技能**：根据需求选择对应的skill
3. **准备输入参数**：按照格式准备输入内容
4. **执行技能调用**：使用标准调用格式执行技能
5. **处理输出结果**：获取生成的内容并进行后续处理

### 高级使用流程
1. **设计创作流程**：规划完整的创作步骤
2. **配置链式调用**：使用链式调用格式串联多个技能
3. **执行流程**：运行完整的创作流程
4. **监控执行状态**：跟踪每个步骤的执行结果
5. **优化流程**：根据执行结果调整流程配置

### 示例：小说创作全流程
```markdown
[SKILL_CHAIN]
chain_name: "古代权谋小说创作全流程"

step_1:
  skill_id: SKILL-001
  action: "生成大纲"
  input:
    stage: "outline"
    content: "创作一个关于宫廷权谋的故事大纲"
  output_var: "outline"

step_2:
  skill_id: SKILL-001
  action: "生成人物"
  input_from: "outline"
  output_var: "characters"

step_3:
  skill_id: SKILL-001
  action: "生成目录"
  input_from: "characters"
  output_var: "catalog"

step_4:
  skill_id: SKILL-001
  action: "生成章节"
  input_from: "catalog"
  output_var: "chapters"

step_5:
  skill_id: SKILL-004
  action: "生成分镜"
  input_from: "chapters"
  output_var: "storyboard"

[/SKILL_CHAIN]
```

## 七、最佳实践

1. **明确需求**：在调用skill前，确保创作需求清晰明确
2. **选择合适的skill**：根据创作类型选择对应的skill
3. **提供足够的上下文**：为skill提供充分的上下文信息，以获得更好的创作结果
4. **使用链式调用**：对于复杂的创作流程，使用链式调用串联多个技能
5. **合理配置参数**：根据具体需求调整配置参数，如风格、长度等
6. **检查输出结果**：执行完成后，检查输出结果是否符合预期
7. **迭代优化**：根据实际效果，调整调用参数和流程配置

## 八、版本控制

### 版本号格式
`MAJOR.MINOR.PATCH`
- **MAJOR**: 重大变更，不兼容之前版本
- **MINOR**: 新增功能，兼容之前版本
- **PATCH**: 修复bug，兼容之前版本

### 版本管理
- 每个skill独立版本管理
- 链式调用时，指定skill版本
- 定期更新skill版本以获得新功能

### 示例：指定版本调用
```markdown
[SKILL_CALL]
skill_id: SKILL-001
version: "1.0.0"
mode: full
input:
  stage: "outline"
  content: "创作一个关于宫廷权谋的故事大纲"
output_to: outline.md
[/SKILL_CALL]
```