# 资产图片生成 - 用户消息模板

| 属性 | 值 |
|------|------|
| **源文件** | `src/routes/assets/generateAssets.ts` |
| **系统提示词** | 数据库 `t_prompts` code=`role-generateImage` / `scene-generateImage` / `tool-generateImage` / `storyboard-generateImage` |
| **AI配置组** | `assetsImage` |
| **输出** | 图片（2K，16:9） |
| **修改方式** | 此为代码中硬编码的用户消息模板，需修改源文件 |

---

## 角色生成 (type="role")

**系统提示词**: `role-generateImage` (见 `04-assets/role-generateImage.md`)

```
请根据以下参数生成角色标准四视图：

**基础参数：**
- 画风风格: ${project.artStyle || "未指定"}

**角色设定：**
- 名称:${name},
- 提示词:${prompt},

请严格按照系统规范生成人物角色四视图。
```

---

## 场景生成 (type="scene")

**系统提示词**: `scene-generateImage` (见 `04-assets/scene-generateImage.md`)

```
请根据以下参数生成标准场景图：

**基础参数：**
- 画风风格: ${project.artStyle || "未指定"}

**场景设定：**
- 名称:${name},
- 提示词:${prompt},

请严格按照系统规范生成标准场景图。
```

---

## 道具生成 (type="props")

**系统提示词**: `tool-generateImage` (见 `04-assets/tool-generateImage.md`)

```
请根据以下参数生成标准道具图：

**基础参数：**
- 画风风格: ${project.artStyle || "未指定"}

**道具设定：**
- 名称:${name},
- 提示词:${prompt},

请严格按照系统规范生成标准道具图。
```

---

## 分镜生成 (type="storyboard")

**系统提示词**: `storyboard-generateImage` (见 `04-assets/storyboard-generateImage.md`)

```
请根据以下参数生成标准分镜图：

**基础参数：**
- 画风风格: ${project.artStyle || "未指定"}

**分镜设定：**
- 名称:${name},
- 提示词:${prompt},

请严格按照系统规范生成标准分镜图。
```

---

## 参数说明

| 参数 | 来源 | 说明 |
|------|------|------|
| `project.artStyle` | `t_project.artStyle` | 项目画风风格 |
| `name` | 请求参数 | 资产名称 |
| `prompt` | 请求参数 | 资产描述提示词 |
| `base64` | 请求参数（可选） | 参考图片的 base64 编码 |
