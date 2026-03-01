# Skill协同标准规范 v1.0

## 一、Skill元数据标准

每个skill文档开头必须包含以下元数据：

```yaml
---
skill_metadata:
  id: "SKILL-001"
  name: "全域审美与创作专业评审团"
  version: "4.0"
  category: "内容评审"
  
  capabilities:
    - "全品类内容专业评审"
    - "多维度量化打分"
    - "可落地优化建议"
    - "商业价值评估"
    - "合规风险识别"
  
  input_format:
    required:
      - "作品内容（文本/描述）"
      - "作品品类"
    optional:
      - "目标受众"
      - "商业诉求"
      - "发行场景"
  
  output_format:
    - "最终综合评分"
    - "评分等级"
    - "全维度单项评分详情"
    - "四大专项报告"
    - "优化指导方案"
    - "赛道适配建议"
  
  keywords:
    - "评审"
    - "点评"
    - "打分"
    - "优化"
    - "作品分析"
    - "内容评估"
  
  dependencies:
    - skill_id: "SKILL-XXX"
      reason: "需要先进行内容提取"
      optional: true
  
  compatible_skills:
    - "SKILL-002: 内容优化重写"
    - "SKILL-003: 商业策划"
  
  execution_time: "5-10分钟"
  
  author: "系统"
  created: "2024-01-01"
  updated: "2024-01-15"
---
```

## 二、Skill调用接口标准

### 标准调用格式

```markdown
[SKILL_CALL]
skill_id: SKILL-001
mode: full_review
input:
  content: |
    [作品内容]
  metadata:
    type: "短视频"
    duration: "60s"
    audience: "18-35岁"
output_to: next_skill
[/SKILL_CALL]
```

### 链式调用格式

```markdown
[SKILL_CHAIN]
chain_name: "内容创作全流程"

step_1:
  skill_id: SKILL-XXX
  action: "生成创意"
  output_var: "creative_idea"

step_2:
  skill_id: SKILL-001
  action: "评审创意"
  input_from: "creative_idea"
  output_var: "review_report"

step_3:
  skill_id: SKILL-XXX
  action: "优化创意"
  input_from: ["creative_idea", "review_report"]
  output_var: "optimized_idea"

step_4:
  skill_id: SKILL-001
  action: "终审"
  input_from: "optimized_idea"
  output_var: "final_report"

[/SKILL_CHAIN]
```

## 三、数据传递标准

### 标准数据包格式

```json
{
  "data_package": {
    "id": "PKG-20240115-001",
    "timestamp": "2024-01-15T10:30:00Z",
    "source_skill": "SKILL-001",
    "target_skill": "SKILL-002",
    "content": {
      "original_work": "原始作品内容",
      "review_result": {
        "score": 135.5,
        "grade": "优秀级",
        "suggestions": [
          {
            "priority": "紧急必改",
            "category": "剧作结构",
            "issue": "问题描述",
            "solution": "优化方案"
          }
        ]
      }
    },
    "context": {
      "user_goal": "用户最终目标",
      "execution_history": ["SKILL-XXX", "SKILL-001"],
      "remaining_steps": ["SKILL-002", "SKILL-003"]
    }
  }
}
```

## 四、Skill协同模式库

### 模式1：评审-优化循环

```
[WORKFLOW: review_optimize_loop]

初始输入：原始作品

循环条件：评分 < 120分 且 迭代次数 < 3

循环体：
  1. 调用 SKILL-001（评审）→ 获取评分和建议
  2. 如果评分达标 → 退出循环
  3. 调用 SKILL-XXX（优化）→ 根据建议优化作品
  4. 更新作品内容
  5. 迭代次数 +1

输出：最终优化版本 + 评审报告
```

### 模式2：多维度并行评估

```
[WORKFLOW: parallel_evaluation]

输入：待评估作品

并行执行：
  线程1：SKILL-001（艺术评审）
  线程2：SKILL-001（商业评审）
  线程3：SKILL-001（合规评审）
  线程4：SKILL-XXX（受众测试）

等待所有线程完成

结果整合：
  - 汇总所有评分
  - 识别冲突建议
  - 生成综合报告

输出：多维度综合评估报告
```

### 模式3：条件分支执行

```
[WORKFLOW: conditional_branch]

输入：作品 + 需求类型

条件判断：
  IF 需求类型 == "商业广告"
    → 调用 [SKILL-001商业评审, SKILL-XXX品牌适配, SKILL-XXX转化优化]
  
  ELSE IF 需求类型 == "艺术创作"
    → 调用 [SKILL-001艺术评审, SKILL-XXX文化解读, SKILL-XXX赛事推荐]
  
  ELSE IF 需求类型 == "短视频"
    → 调用 [SKILL-001新媒体评审, SKILL-XXX流量优化, SKILL-XXX平台适配]

输出：针对性的专业方案
```

## 五、实现示例

### 示例1：在评审团Skill中添加协同接口

在"全域审美与创作专业评审团.md"文件开头添加：

```markdown
---
[元数据如上所示]
---

## 协同接口

### 接收其他Skill的输入
本skill可以接收以下格式的输入：

1. 来自内容生成skill的创意方案
2. 来自优化skill的改进版本
3. 来自用户的原始作品

### 输出给其他Skill
本skill的输出可以传递给：

1. 内容优化skill（传递优化建议）
2. 商业策划skill（传递商业评分）
3. 合规审核skill（传递风险提示）

### 调用示例
\`\`\`
@评审团 评审作品
输入来源：@创意生成skill 的输出
评审模式：快速评审
输出目标：@优化重写skill
\`\`\`
```

### 示例2：创建工作流配置文件

```yaml
# workflow_content_creation.yaml

workflow:
  name: "短视频内容创作全流程"
  description: "从创意到成片的完整工作流"
  
  steps:
    - id: "step_1"
      name: "创意生成"
      skill: "SKILL-XXX"
      action: "generate_idea"
      input:
        topic: "${user_input.topic}"
        style: "${user_input.style}"
      output_var: "idea"
    
    - id: "step_2"
      name: "创意初审"
      skill: "SKILL-001"
      action: "quick_review"
      input:
        content: "${step_1.idea}"
        type: "创意方案"
      output_var: "initial_review"
      
    - id: "step_3"
      name: "脚本撰写"
      skill: "SKILL-XXX"
      action: "write_script"
      input:
        idea: "${step_1.idea}"
        suggestions: "${step_2.initial_review.suggestions}"
      output_var: "script"
    
    - id: "step_4"
      name: "脚本终审"
      skill: "SKILL-001"
      action: "full_review"
      input:
        content: "${step_3.script}"
        type: "短视频脚本"
      output_var: "final_review"
      
    - id: "step_5"
      name: "拍摄计划"
      skill: "SKILL-XXX"
      action: "create_shooting_plan"
      input:
        script: "${step_3.script}"
        review: "${step_4.final_review}"
      output_var: "shooting_plan"
  
  output:
    - "${step_3.script}"
    - "${step_4.final_review}"
    - "${step_5.shooting_plan}"
```

## 六、使用方法

### 方法1：直接在对话中调用

```
用户：请帮我完成短视频创作全流程

AI：收到，我将调用以下技能协同工作：
1. @创意生成 → 生成创意方案
2. @评审团 → 初审创意
3. @脚本撰写 → 编写脚本
4. @评审团 → 终审脚本
5. @拍摄计划 → 生成拍摄方案

开始执行...
```

### 方法2：使用工作流模板

```
用户：@调度中心 执行工作流 "短视频内容创作全流程"
输入：
- 主题：美食探店
- 风格：轻松幽默
- 时长：60秒

AI：工作流已启动，预计10分钟完成...
```

### 方法3：自定义协同链

```
用户：我要自定义一个流程：
1. 先用评审团评估我的脚本
2. 根据评审结果，用优化工具改进
3. 再次评审，直到达到"优秀级"

AI：已创建自定义工作流，开始执行...
```

## 七、最佳实践建议

1. **模块化设计**：每个skill专注做好一件事
2. **标准化接口**：统一输入输出格式
3. **清晰的依赖关系**：明确skill之间的调用关系
4. **错误处理机制**：每个环节都要有fallback方案
5. **版本兼容性**：保持向后兼容
6. **文档完整性**：详细记录每个skill的能力和限制

---

通过这套标准规范，你可以轻松实现多个skill的协同工作！
```
