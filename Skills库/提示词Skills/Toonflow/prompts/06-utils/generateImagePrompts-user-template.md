# 分镜提示词优化 - 用户消息模板

| 属性 | 值 |
|------|------|
| **源文件** | `src/agents/storyboard/generateImagePromptsTool.ts` |
| **系统提示词** | 数据库 `t_prompts` code=`generateImagePrompts` |
| **AI配置组** | `storyboardAgent` |
| **修改方式** | 系统提示词可在数据库中修改；用户消息模板需修改源文件 |

---

## 用户消息模板原文

```
请优化以下分镜提示词：

【布局】${layout.cols}列×${layout.rows}行=${layout.totalCells}格
【比例】${aspectRatio}（${aspectRatioDesc}）
【风格】${style}
${assetsSection}

【原始内容】
${gridPositions.join("\n")}
```

---

## 动态参数说明

### 布局计算 (`calculateGridLayout`)

| 分镜数量 | 布局 | 说明 |
|----------|------|------|
| 1 | 1×1 | 单格 |
| 2 | 2×1 | 横排两格 |
| 3 | 3×1 | 横排三格 |
| 4 | 2×2 | 四宫格 |
| 5-9 | 3×3 | 九宫格（多余格填黑） |
| 10+ | 3×N | 三列多行 |

### 宽高比描述 (`aspectRatioDesc`)

| 比例 | 描述 |
|------|------|
| 16:9 | 电影宽银幕 |
| 9:16 | 竖屏短剧 |
| 21:9 | 超宽银幕史诗感 |
| 1:1 | 方形构图 |
| 4:3 | 经典银幕 |
| 3:4 | 竖版经典 |
| 3:2 | 摄影标准 |
| 2:3 | 竖版摄影 |

### 风格参数 (`style`)

格式为 `类型：${project.type}，风格：${project.artStyle}`

### 资产说明 (`assetsSection`)

当有可用资产时，会追加：

```
【可用资产】
- ${name}：${intro}
- ...

⚠️ 必须使用完整资产名称，禁止简称或代词。
```

### 宫格位置 (`gridPositions`)

每个格子的描述格式：

```
[第1行第1列]: ${prompts[0]}
[第1行第2列]: ${prompts[1]}
[第2行第1列]: ${prompts[2]}
...
[第N行第M列]: 纯黑图    (空位填充)
```

---

## 降级逻辑

当数据库中没有 `generateImagePrompts` 提示词时，使用降级输出：

```
请输出${count}张图片
提示词如下:
第1格: ${prompts[0]}
第2格: ${prompts[1]}
...
```
