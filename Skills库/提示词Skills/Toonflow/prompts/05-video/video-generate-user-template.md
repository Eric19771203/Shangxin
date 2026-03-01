# 视频提示词生成 - 用户消息模板

| 属性 | 值 |
|------|------|
| **源文件** | `src/routes/video/generatePrompt.ts` |
| **系统提示词** | 数据库 `t_prompts` code=`video-main` + 模式对应的子提示词 |
| **AI配置组** | `videoPrompt` |
| **修改方式** | 系统提示词可在数据库中修改；用户消息模板需修改源文件 |

---

## 系统提示词组合逻辑

系统提示词由两部分拼接而成：

```
${video-main}

${模式对应的子提示词}
```

| 模式 | 子提示词 code | 说明 |
|------|---------------|------|
| `startEnd` | `video-startEnd` | 首尾帧模式 |
| `multi` | `video-multi` | 宫格模式 |
| `single` | `video-single` | 单图模式 |
| `text` | `video-text` | 文本模式 |

各提示词原文见：
- `05-video/video-main.md`
- `05-video/video-startEnd.md`
- `05-video/video-multi.md`
- `05-video/video-single.md`
- `05-video/video-text.md`

---

## 用户消息模板原文

```
Mode: ${getModeDescription(mode)}

Reference Images:
${imagePrompts}

Script:
${prompt}
${videoConfigData ? `script content:\n${videoConfigData.content}` : ""}


Parameters:
- Total Duration: ${duration}s
- Shot Count: ${shotCount}
- Average Duration: ${avgDuration}s per shot

Generate storyboard prompts:
```

---

## 参数说明

| 参数 | 来源 | 说明 |
|------|------|------|
| `mode` | 请求参数 `type` | 生成模式：startEnd/multi/single/text |
| `getModeDescription(mode)` | 内部映射 | 模式中文名（首尾帧模式/宫格模式/单图模式/文本模式） |
| `imagePrompts` | 请求参数 `images` | 格式为 `Image 1: ${prompt}\nImage 2: ${prompt}...` |
| `prompt` | 请求参数 | 剧本/脚本内容 |
| `videoConfigData.content` | `t_script.content` | 通过 `videoConfigId` 关联的剧本内容（可选） |
| `duration` | 请求参数 | 总时长（秒） |
| `shotCount` | 计算值 | `images.length` |
| `avgDuration` | 计算值 | `duration / shotCount`，保留1位小数 |
