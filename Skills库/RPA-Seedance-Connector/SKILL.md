---
name: "RPA-Seedance-Connector"
description: "一个基于 Playwright 的 RPA 连接器 Skill，用于将 ComfyUI 或其他本地工具连接到“即梦 (Seedance)”网页端。支持自动登录保持、参数注入和任务监控。适用于需要自动化生成视频的场景。"
---

# RPA Seedance Connector

## 简介
本 Skill 提供了一套完整的 RPA 解决方案，用于自动化控制“即梦”网页端进行视频生成。它作为一个“中间件”，可以被 ComfyUI 插件、Python 脚本或 CI/CD 流水线调用。

## 核心功能
1.  **自动填参**：自动填写 Prompt、选择模型、设置比例和时长。
2.  **登录保持**：利用本地 Chrome Profile 实现一次登录，永久有效。
3.  **防风控**：内置随机延迟和模拟人类操作轨迹。

## 使用方法

### 1. 生成脚本
使用 `templates/rpa_script_template.py` 作为基础，根据你的具体需求修改选择器。

### 2. 获取选择器 (Selectors)
由于网页结构可能更新，建议使用 Playwright 的录制工具获取最新 Selector：
```bash
playwright codegen https://jimeng.jianying.com/ai-tool/video/generate
```

### 3. 集成到 ComfyUI
将生成的 Python 脚本封装为一个 ComfyUI Custom Node，在 `Execute` 方法中调用 `subprocess.run(['python', 'rpa_script.py', ...])`。

## 目录结构
*   `knowledge/`: 包含 RPA 核心原理和反爬策略。
*   `templates/`: 提供 Python 脚本模板和配置文件模板。
*   `examples/`: (待添加) 完整的 ComfyUI 节点示例代码。
