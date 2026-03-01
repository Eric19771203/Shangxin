# OpenClaw 入门教程：从0到1搭建你的AI助手

---

## 什么是OpenClaw？

OpenClaw 是一个开源的AI助手框架，让你可以：
- 🤖 搭建属于自己的AI助手
- 🛠️ 开发和分享技能
- 🔗 集成各种工具和服务
- 💡 自动化你的工作流

**为什么选择OpenClaw？**
- 完全开源，自由定制
- 丰富的技能生态
- 强大的扩展性
- 活跃的社区

---

## 第一步：安装OpenClaw

### 前置要求
- Node.js 18+ 
- npm 或 pnpm
- 一个AI模型API密钥（推荐 Claude 或 GPT）

### 安装命令

```bash
# 使用 npm 安装
npm install -g openclaw

# 或者使用 pnpm（推荐）
pnpm add -g openclaw
```

### 验证安装

```bash
openclaw --version
```

如果看到版本号，说明安装成功！

---

## 第二步：初始化配置

### 运行配置向导

```bash
openclaw configure
```

这个向导会帮你配置：
- AI模型API密钥
- 聊天渠道（Telegram、Discord、Feishu等）
- 工作区目录

### 或者手动配置

创建 `~/.openclaw/config.json`：

```json
{
  "models": {
    "default": "anthropic/claude-3-opus-20240229",
    "providers": {
      "anthropic": {
        "apiKey": "your-api-key-here"
      }
    }
  }
}
```

---

## 第三步：启动你的第一个助手

### 启动Gateway

```bash
openclaw gateway start
```

### 或者使用系统服务

```bash
# 安装为系统服务
openclaw gateway install

# 启动服务
openclaw gateway start
```

### 检查状态

```bash
openclaw status
```

---

## 第四步：连接聊天渠道

### 以Feishu为例

1. 访问 Feishu 开放平台
2. 创建一个企业自建应用
3. 获取 App ID 和 App Secret
4. 配置事件订阅
5. 运行：

```bash
openclaw channels login feishu
```

按照提示输入配置信息即可。

### 其他渠道

- Telegram: `openclaw channels login telegram`
- Discord: `openclaw channels login discord`
- WhatsApp: `openclaw channels login whatsapp`

---

## 第五步：安装你的第一个技能

### 查看可用技能

```bash
openclaw skills list
```

### 使用ClawHub安装技能

```bash
# 安装ClawHub CLI
npx clawhub

# 搜索技能
npx clawhub search weather

# 安装技能
npx clawhub install weather
```

### 或者手动安装技能

将技能文件夹放入 `~/.openclaw/workspace/skills/` 目录即可。

---

## 第六步：开发你的第一个技能

### 技能目录结构

```
my-first-skill/
├── SKILL.md          # 技能说明文件
├── scripts/          # 脚本目录
│   └── my-script.py  # 你的脚本
└── assets/           # 资源目录（可选）
```

### 编写SKILL.md

```markdown
# My First Skill

## Description
这是我的第一个OpenClaw技能！

## Usage
当用户说"hello"时，激活这个技能。

## Examples
- "hello"
- "你好"
```

### 编写脚本

```python
# scripts/hello.py
print("Hello, OpenClaw!")
```

### 安装技能

将技能文件夹放入 `~/.openclaw/workspace/skills/`，然后重启Gateway。

---

## 第七步：自动化你的工作流

### 使用Cron定时任务

```bash
# 添加定时任务
openclaw cron add \
  --name "每日报告" \
  --cron "0 9 * * *" \
  --message "生成每日工作报告" \
  --announce
```

### 查看定时任务

```bash
openclaw cron list
```

---

## 常用命令速查

```bash
# 查看状态
openclaw status

# 查看技能
openclaw skills list

# 发送消息
openclaw message send --message "Hello!"

# 查看日志
openclaw logs --follow

# 配置Gateway
openclaw gateway --help
```

---

## 下一步

1. 📚 阅读官方文档：https://docs.openclaw.ai
2. 🌐 加入社区：https://discord.gg/clawd
3. 🔍 探索技能：https://clawhub.com
4. 💡 分享你的技能：给OpenClaw社区贡献代码

---

## 常见问题

### Q: OpenClaw和其他AI助手有什么区别？
A: OpenClaw是完全开源的，你可以完全控制你的数据和代码，而不是依赖第三方服务。

### Q: 我需要编程基础吗？
A: 基础使用不需要，但开发技能需要一些编程知识。

### Q: 支持哪些AI模型？
A: 支持Claude、GPT、Gemini等主流模型，也支持本地模型。

### Q: 如何获得帮助？
A: 加入Discord社区，或者在GitHub上提Issue。

---

## 总结

恭喜你！你已经完成了OpenClaw的入门教程！

现在你可以：
- ✅ 安装和配置OpenClaw
- ✅ 连接聊天渠道
- ✅ 安装和使用技能
- ✅ 开发自己的技能
- ✅ 自动化工作流

继续探索，祝你玩得开心！🚀

---

*本教程持续更新，欢迎贡献！*
