# RPA Seedance Connector 方法论 (Methodology)

## 1. 核心原理
本工具采用 **Playwright + Chrome CDP (Chrome DevTools Protocol)** 技术，实现对“即梦 (Seedance)”网页端的全自动化控制。
核心逻辑是：**模拟人类操作 (Human Simulation)**，而非逆向 API。

## 2. 关键流程 (Critical Path)

### 2.1 初始化 (Initialization)
1.  **浏览器启动**：必须使用 `launch_persistent_context` 模式。
    *   **User Data Dir**：指定本地目录存储 Cookie/LocalStorage，实现“免登录”。
    *   **Channel**：指定 `chrome` 或 `msedge`，复用本地浏览器环境。
    *   **Headless**：建议 `False` (有头模式)，方便用户观察和干预。

### 2.2 页面导航与检测 (Navigation)
1.  **URL**: `https://jimeng.jianying.com/ai-tool/video/generate`
2.  **登录检查**：
    *   检测页面是否存在“登录”按钮或 URL 跳转。
    *   如果未登录，**暂停脚本**，提示用户手动扫码，直到检测到登录成功信号（如 Cookie 变化或 URL 变回生成页）。

### 2.3 参数注入 (Injection)
利用 Playwright 的 Locator 定位策略，精准操作 DOM：
*   **Prompt 输入框**：`textarea[placeholder*='描述']` -> `fill()`
*   **模型选择**：点击下拉框 -> 等待选项渲染 -> 点击目标选项。
*   **生成按钮**：定位 `button:has-text("生成")` -> `click()`

### 2.4 任务监控 (Monitoring)
*   **轮询机制**：生成点击后，监控“历史记录”列表的第一个元素。
*   **状态判断**：
    *   `Pending`: 进度条/百分比。
    *   `Success`: 出现“下载”或“播放”图标。
    *   `Failed`: 出现“重试”或错误提示。

## 3. 异常处理 (Error Handling)
*   **超时 (Timeout)**：生成过程可能长达数分钟，需设置超长 `timeout` (如 300s)。
*   **风控 (Anti-Bot)**：
    *   **随机延迟**：在点击和输入之间加入 `random.uniform(0.5, 2.0)` 秒的延迟。
    *   **鼠标轨迹**：(可选) 模拟非直线鼠标移动。

## 4. 输出规范
*   **日志**：实时输出当前步骤 (Step 1/5: Opening Browser...)。
*   **结果**：下载生成的 MP4 文件到指定目录，或返回视频 URL。
