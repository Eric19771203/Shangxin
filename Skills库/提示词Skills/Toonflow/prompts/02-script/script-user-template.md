# 剧本生成 - 用户消息模板

| 属性 | 值 |
|------|------|
| **源文件** | `src/utils/generateScript.ts` |
| **函数** | `generateScript()` / `formatEpisodePrompt()` |
| **系统提示词** | 数据库 `t_prompts` code=`script` |
| **AI配置组** | `generateScript` |
| **修改方式** | 此为代码中硬编码的用户消息模板，需修改源文件 |

---

## 用户消息模板原文

```
请根据以下结构化大纲生成剧本。

【⚠️ 最高优先级：剧情主干(outline)是唯一权威】
剧本必须严格按照【剧情主干】的叙事顺序展开，不得调整、跳跃或打乱顺序！

【强制要求】
1. ⚠️ 【开场镜头】必须是剧本的第一个镜头（这是outline开头的视觉化）
2. ⚠️ 严格按【剧情主干】顺序展开剧情，这是剧本的唯一权威
3. ⚠️ 【剧情节点】四步必须严格按顺序呈现：起→承→转→合，不输出标记
4. emotionalCurve必须在对应剧情节点体现
5. classicQuotes必须原文出现在高潮段落
6. endingHook必须作为收尾
7. scenes/characters/props必须全部使用，按出场顺序
8. visualHighlights中的镜头必须按剧情主干顺序全部呈现
9. 500-800字
10. 以【黑屏】结尾

═══════════════════════════════════════
大纲数据
═══════════════════════════════════════
${episodePrompt}

═══════════════════════════════════════
原文参考（仅用于补充细节和对话优化）
═══════════════════════════════════════
${novelData}
```

---

## Episode 格式化模板 (formatEpisodePrompt)

Episode 对象被格式化为以下结构：

```
═══════════════════════════════════════
第${episodeIndex}集：${title}
关联章节：第${chapterRange}章
═══════════════════════════════════════

【场景列表】必须全部使用（按出场顺序排列）
  场景1：${scene.name}
    环境描写：${scene.description}

【出场角色】必须全部使用（按出场顺序排列），首次出场需完整描述外貌
  角色1：${character.name}
    人设样貌：${character.description}

【关键道具】必须全部展示（按出场顺序排列）
  道具1：${prop.name}
    样式描写：${prop.description}

【核心矛盾】贯穿全集的主线冲突
${coreConflict}

【剧情主干】⚠️ 最高优先级，剧本必须严格按此顺序展开
${outline}

【开场镜头】⚠️ 必须作为剧本第一个镜头（outline开头的视觉化）
${openingHook}

【剧情节点】必须严格按顺序呈现（起→承→转→合），顺序与剧情主干一致
  【起】${keyEvents[0]}
  【承】${keyEvents[1]}
  【转】${keyEvents[2]}
  【合】${keyEvents[3]}

【情绪曲线】必须在对应剧情节点体现情绪强度
${emotionalCurve}

【视觉重点】标志性镜头，必须按剧情主干顺序呈现
  镜头1：${visualHighlights[0]}

【结尾悬念】必须作为收尾，后接【黑屏】
${endingHook}

【黄金金句】必须原文出现在剧本高潮段落
  金句1：「${classicQuotes[0]}」
```

---

## Episode 接口定义

```typescript
interface Episode {
  episodeIndex: number;
  title: string;
  chapterRange: number[];
  scenes: Scene[];       // 按 outline 出场顺序排列
  characters: Character[]; // 按 outline 出场顺序排列
  props: Prop[];         // 按 outline 出场顺序排列
  coreConflict: string;
  outline: string;       // 最高优先级，剧本生成的唯一权威
  openingHook: string;   // outline 第一句话的视觉化
  keyEvents: string[];   // [起, 承, 转, 合]
  emotionalCurve: string;
  visualHighlights: string[];
  endingHook: string;
  classicQuotes: string[];
}
```
