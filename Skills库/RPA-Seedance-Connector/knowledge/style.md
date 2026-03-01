# RPA Seedance Connector 风格指南 (Style Guide)

## 1. 代码风格 (Python)
*   **框架**：严格使用 `playwright.sync_api` (同步模式)，便于线性逻辑控制。
*   **类型注解**：所有函数参数必须包含 Type Hints。
*   **配置化**：所有选择器 (Selectors) 必须提取到常量配置中，禁止硬编码在逻辑里。

## 2. UI 交互规范
*   **用户干预**：当遇到验证码或登录失效时，必须通过 `input("Press Enter to continue...")` 暂停脚本，允许用户手动操作。
*   **控制台输出**：使用 Emoji 增强可读性。
    *   🟢 [INFO] 正常步骤
    *   🟡 [WARN] 需要注意 (如：等待登录)
    *   🔴 [ERROR] 发生错误

## 3. 文件命名
*   **脚本**：`seedance_rpa.py`
*   **配置**：`selectors.json`
*   **输出**：`output/seedance_{timestamp}.mp4`
