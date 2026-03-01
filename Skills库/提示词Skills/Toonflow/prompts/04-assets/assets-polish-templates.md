# 资产提示词润色 - 用户消息模板

| 属性 | 值 |
|------|------|
| **源文件** | `src/routes/assets/polishPrompt.ts` |
| **系统提示词** | 数据库 `t_prompts` code=`role-polish` / `scene-polish` / `tool-polish` / `storyboard-polish` |
| **AI配置组** | `assetsPrompt` |
| **输出格式** | 结构化输出 `{ prompt: string }` |
| **修改方式** | 此为代码中硬编码的用户消息模板，需修改源文件 |

---

## 角色润色 (type="role")

**系统提示词**: `role-polish` (见 `04-assets/role-polish.md`)

**特点**: 会根据大纲中角色出场章节，查询对应小说原文作为上下文

```
请根据以下参数生成角色标准四视图提示词：

**基础参数：**
- 风格: ${project.artStyle || "未指定"}
- 小说原文：${novelText || "未提供"}
- 小说类型: ${project.type || "未指定"}
- 小说背景: ${project.intro || "未指定"}

**角色设定：**
- 角色名称:${name},
- 角色描述:${describe},

请严格按照系统规范生成人物角色四视图提示词。
```

---

## 场景润色 (type="scene")

**系统提示词**: `scene-polish` (见 `04-assets/scene-polish.md`)

**特点**: 会根据大纲中场景出场章节，查询对应小说原文作为上下文

```
请根据以下参数生成场景图提示词：

**基础参数：**
- 风格: ${project.artStyle || "未指定"}
- 小说原文：${novelText || "未提供"}
- 小说类型: ${project.type || "未指定"}
- 小说背景: ${project.intro || "未指定"}

**场景设定：**
- 场景名称:${name},
- 场景描述:${describe},

请严格按照系统规范生成场景图提示词。
```

---

## 道具润色 (type="props")

**系统提示词**: `tool-polish` (见 `04-assets/tool-polish.md`)

**特点**: 会根据大纲中道具出场章节，查询对应小说原文作为上下文

```
请根据以下参数生成道具图提示词：

**基础参数：**
- 风格: ${project.artStyle || "未指定"}
- 小说原文：${novelText || "未提供"}
- 小说类型: ${project.type || "未指定"}
- 小说背景: ${project.intro || "未指定"}

**道具设定：**
- 道具名称:${name},
- 道具描述:${describe},

请严格按照系统规范生成道具图提示词。
```

---

## 分镜润色 (type="storyboard")

**系统提示词**: `storyboard-polish` (见 `04-assets/storyboard-polish.md`)

**特点**: 不查询小说原文，仅使用项目信息

```
请根据以下参数生成分镜图提示词：

**基础参数：**
- 风格: ${project.artStyle || "未指定"}
- 小说类型: ${project.type || "未指定"}
- 小说背景: ${project.intro || "未指定"}

**分镜设定：**
- 分镜名称:${name},
- 分镜描述:${describe},

请严格按照系统规范生成分镜图提示词。
```

---

## 数据流说明

润色流程会自动从大纲（`t_outline`）中提取角色/场景/道具对应的章节范围（`chapterRange`），然后从小说表（`t_novel`）中查询对应章节的原文内容，将原文拼接后作为 `小说原文` 参数传入，帮助 AI 更准确地生成贴合原著的提示词。
