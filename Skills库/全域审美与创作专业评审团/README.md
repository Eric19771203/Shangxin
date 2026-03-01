# 工作流整合系统 v1.0

## 📁 目录结构

```
工作流整合系统/
├── 📄 README.md                          # 本文件
├── 📄 主编排器-MasterOrchestrator.md      # 系统入口（重要！）
├── 📄 快速开始指南.md                     # 新手教程
├── 📄 自动注册工具.md                     # Skill注册工具
├── 📄 工作流整合系统设计.md               # 架构设计文档
│
├── 📁 skills/                            # Skill知识库目录
│   ├── 全域审美与创作专业评审团.md         # 已注册：NODE-001
│   └── [你的其他skill文件...]            # 移动到这里
│
├── 📁 agents/                            # SubAgent定义目录
│   └── agent-registry.json               # Agent注册表
│
├── 📁 workflows/                         # 工作流定义目录
│   ├── workflow-registry.json            # 工作流注册表
│   └── single-review.yaml                # 单独评审工作流
│
├── 📁 integrations/                      # 整合配置目录
│   └── node-registry.json                # 节点注册表（核心）
│
└── 📁 docs/                              # 文档目录
    ├── 架构对比分析.md                    # 架构选择说明
    ├── Skill协同标准规范.md               # 协同标准
    └── 技能调度中心.md                    # 调度中心设计
```

---

## 🚀 快速开始

### 第1步：移动你的skill文件

将你现有的所有skill文件移动到 `skills/` 目录：

```bash
# 示例
move ../你的skill文件.md skills/
```

### 第2步：注册新的skill

移动完成后，告诉我文件名，我会帮你注册。或者使用自动注册工具：

```
@注册工具 扫描skills目录
```

### 第3步：开始使用

通过主编排器调用任何已注册的skill：

```
@编排器 列出所有节点
@编排器 执行节点 NODE-001
```

---

## 💡 核心概念

### Skill（技能）
- 知识库/规则集，定义了某个功能的标准和流程
- 存放在 `skills/` 目录
- 例如：全域审美与创作专业评审团.md

### Node（节点）
- 功能单元，对应一个skill
- 在 `integrations/node-registry.json` 中注册
- 例如：NODE-001（内容评审节点）

### Agent（代理）
- 独立的AI执行实例，加载skill并执行
- 在 `agents/agent-registry.json` 中注册
- 例如：content-review-agent

### Workflow（工作流）
- 多个节点的组合，定义执行顺序
- 在 `workflows/` 目录中定义
- 例如：WF-001（单独评审）

---

## 📊 当前系统状态

### 已注册节点：1个
- ✅ NODE-001: 内容评审节点

### 已注册Agent：1个
- ✅ content-review-agent: 内容评审代理

### 已注册工作流：1个
- ✅ WF-001: 单独评审

### 待注册：
- ⏳ 等待你移动其他skill文件...

---

## 🎯 使用示例

### 示例1：快速评审

```
评审我的短视频脚本：
[脚本内容]
```

主编排器会自动：
1. 识别需求（评审）
2. 匹配节点（NODE-001）
3. 调用Agent（content-review-agent）
4. 返回评审报告

### 示例2：执行工作流

```
@编排器 执行工作流 WF-001
内容：[作品内容]
类型：短视频脚本
```

### 示例3：查看可用资源

```
@编排器 列出所有节点
@编排器 列出所有工作流
@编排器 查看节点 NODE-001
```

---

## 🔧 添加新功能

### 添加新Skill

1. 将skill文件移动到 `skills/` 目录
2. 使用自动注册工具注册
3. 配置Agent（如需要）
4. 定义工作流（如需要）

### 创建新工作流

1. 在 `workflows/` 目录创建 `.yaml` 文件
2. 定义步骤和节点调用
3. 在 `workflow-registry.json` 中注册
4. 通过主编排器调用

---

## 📚 文档导航

### 新手必读
1. 📖 [快速开始指南.md](快速开始指南.md) - 手把手教程
2. 📖 [主编排器-MasterOrchestrator.md](主编排器-MasterOrchestrator.md) - 系统入口

### 进阶阅读
3. 📖 [工作流整合系统设计.md](工作流整合系统设计.md) - 架构设计
4. 📖 [自动注册工具.md](自动注册工具.md) - 注册工具使用

### 技术文档
5. 📖 [docs/架构对比分析.md](docs/架构对比分析.md) - 为什么选择SubAgent架构
6. 📖 [docs/Skill协同标准规范.md](docs/Skill协同标准规范.md) - 协同标准

---

## ⚙️ 配置文件说明

### integrations/node-registry.json
所有节点的注册信息，包括：
- 节点ID、名称、路径
- 功能描述、关键词
- 输入输出格式
- 关联的Agent

### agents/agent-registry.json
所有SubAgent的配置，包括：
- Agent ID、名称
- 加载的Skill路径
- 工具权限
- System Prompt模板

### workflows/workflow-registry.json
所有工作流的索引，包括：
- 工作流ID、名称
- 涉及的节点
- 定义文件路径
- 使用场景

---

## 🎉 系统优势

### ✅ 统一管理
所有skill在一个系统中，统一调用、统一管理

### ✅ 灵活组合
可以动态组合任意节点，创建自定义工作流

### ✅ 易于扩展
新增skill只需移动文件+注册，无需修改代码

### ✅ 智能路由
主编排器自动识别需求，调用合适的节点

### ✅ 基于SubAgent
充分利用Kiro的原生能力，真正的委托执行

---

## 🔄 下一步

### 立即行动
1. ✅ 目录结构已创建
2. ✅ 注册表模板已准备
3. ⏳ 等待你移动其他skill文件
4. ⏳ 注册新的skill
5. ⏳ 定义常用工作流
6. ⏳ 开始使用完整系统

### 需要帮助？
- 查看 [快速开始指南.md](快速开始指南.md)
- 使用 [自动注册工具.md](自动注册工具.md)
- 阅读 [主编排器-MasterOrchestrator.md](主编排器-MasterOrchestrator.md)

---

## 📞 支持

移动完skill文件后，请告诉我：
1. 有哪些新文件
2. 每个文件的主要功能
3. 你最常用的工作流

我将立即帮你：
- ✅ 注册所有节点
- ✅ 配置Agent
- ✅ 定义工作流
- ✅ 提供使用示例

**准备好了吗？开始移动你的skill文件吧！** 🚀
