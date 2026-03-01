# 图片编辑 - 系统提示词

| 属性 | 值 |
|------|------|
| **源文件** | `src/utils/editImage.ts` |
| **类型** | 硬编码系统提示词 |
| **AI配置组** | `editImage` |
| **输出** | 编辑后的图片（base64） |
| **修改方式** | 需修改源文件中的 `systemPrompt` |

---

## 系统提示词原文

```
根据用户提供的具体修改指令，对上传的图片进行智能编辑。
```

---

## 工作机制

### 别名引用系统

用户通过 `@别名` 的方式引用图片，系统自动将别名替换为 `图N` 编号：

```javascript
// 输入示例
images = {
  "@图8": "456",   // key: 图片别名, value: 图片ID
  "@图10": "123"
}
directive = "将@图10中圈起来的部分换成@图8"

// 处理后
prompt = "将图2中圈起来的部分换成图1"
images = [base64_of_456, base64_of_123]
```

### 图片来源支持

| 类型 | 判断条件 | 说明 |
|------|----------|------|
| base64 | 以 `data:image/` 开头 | 直接使用 |
| 图片ID | 数字类型 | 从 `t_assets` 表查询 `filePath`，再通过 OSS 获取 |
| URL | 包含 `http` | 直接下载转 base64 |

### AI 调用参数

```javascript
u.ai.image({
  systemPrompt: "根据用户提供的具体修改指令，对上传的图片进行智能编辑。",
  prompt: prompt,         // 替换别名后的指令
  imageBase64: base64Images, // 所有引用图片的 base64 数组
  aspectRatio: "16:9",
  size: "1K",
})
```
