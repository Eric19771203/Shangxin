# SKILL: 终极电影人物定妆生成系统 (Ultimate Cinematic Character Costume Design)

## 元数据
- **ID**: ultimate-costume-03
- **名称**: 终极电影人物定妆生成系统
- **类型**: file
- **分类**: 角色设计
- **标签": ["定妆", "角色", "全身", "服装", "造型", "七层解析"]

## 描述
由好莱坞顶尖美术指导、传奇摄影师与资深AI提示词工程师共同训练的视觉生成核心。根据用户输入的模糊概念，反向推导出**极度写实、全身可见、细节丰富**的电影定妆设定。

## 核心目标
确立角色的**整体剪影（Silhouette）、体态语言（Body Language）与服装搭配逻辑**。

## 运行准则
1. **强制全身 (Mandatory Full Body)** - 默认必须生成从头到脚的完整画面
2. **剪影优先 (Silhouette First)** - 关注身体比例、站姿重心、服装整体轮廓
3. **鞋履与接触面** - 必须描述鞋子细节以及脚与地面的接触
4. **材质与物理** - 强调布料在全身动态下的物理表现

## 七层定妆解析法 (全身版)

### 1. 体型与比例 (Physique & Proportions)
- 身高、头身比（如8头身）
- 骨架大小、肌肉量
- 肢体长度

### 2. 皮相与质感 (Skin & Texture)
- 皮肤色调
- 全身可见的皮肤细节（手臂血管、腿部伤痕）
- 皮肤在环境光下的光泽

### 3. 体态与肢体语言 (Pose & Body Language)
- **Stance**: 站姿（松弛、警戒、格斗态）、重心分布
- **Action**: 正在进行的动作（行走、依靠、悬浮）

### 4. 全套服化道 (Full Costume & Gear)
- **Head**: 帽子、发饰、眼镜
- **Body**: 外套、内搭、面料材质、剪裁风格
- **Legs & Feet**: 裤型、鞋履细节、护膝/腿带

### 5. 环境与地面 (Environment & Ground)
- **Ground**: 地面材质（湿润沥青、泥土、反光地板）
- **Atmosphere**: 空间透视感、背景景深

### 6. 光影雕刻 (Lighting Sculpting)
- 利用光线勾勒全身轮廓（Rim Light）
- 确保深色衣服与背景分离

### 7. 电影摄影 (Cinematography)
- **Framing**: Wide Shot, Full Body Shot, Low Angle, Eye Level
- **Lens**: 35mm 或 50mm

## 输出协议

### 【全身定妆视觉解析】
- **体型体态**: ...
- **全套服装**: ... (包含鞋子)
- **环境地面**: ...
- **光影构图**: ...

### 【AI 绘画终极指令】
**Prompt结构**:
```
[Subject Description (Full Body)], [Physique & Pose], [Detailed Costume from Head to Toe], [Footwear Details], [Environment & Ground Interaction], [Lighting & Atmosphere], [Camera: Wide Shot/Full Body], [Aesthetic Tags] --v 6.0 --style raw --ar [Aspect Ratio]
```

**关键参数**:
- 强制加入 `Head to Toe` 和 `Shoes visible`
- 镜头：35mm/50mm
- 构图：Wide Shot / Full Body Shot
- 比例：--ar 9:16（竖构图最适合单人全身像）

## 使用场景
- AI角色全身定妆生成
- 影视角色造型设计
- 服装搭配参考
- 摄影构图指导

## 调用方式
```
SKILL_CALL ultimate-costume-03
```
