# TVC案例库与模仿复刻系统

## 概述

用户可以上传或描述优秀的TVC案例，系统自动解析其创意结构、视觉风格、叙事技巧，并提供模仿或复刻方案。

---

## 核心功能

### 1. 案例输入方式

**方式A: 视频文件**
- 上传TVC视频（支持MP4/MOV/AVI）
- 自动提取关键帧
- 音频转文字（旁白/对白）
- 时长自动检测

**方式B: 链接**
- YouTube/Bilibili/抖音等平台链接
- 自动抓取视频
- 提取标题、描述、标签

**方式C: 文字描述**
- 用户描述TVC内容
- 关键画面描述
- 创意概念阐述
- 参考风格说明

---

### 2. 智能解析引擎

#### 2.1 视觉分析

```python
class TVCAnalyzer:
    def analyze_visual(self, video_path):
        """
        分析TVC的视觉元素
        """
        return {
            "color_palette": self._extract_colors(),      # 主色调、配色方案
            "composition_style": self._analyze_composition(),  # 构图方式
            "lighting_mood": self._analyze_lighting(),    # 光效氛围
            "shot_types": self._identify_shots(),         # 镜头类型分布
            "pacing_rhythm": self._analyze_pacing(),      # 节奏分析
            "visual_style": self._match_style(),          # 匹配已知风格
            "camera_movement": self._track_camera(),      # 运镜方式
            "transitions": self._identify_transitions()   # 转场技巧
        }
```

**解析维度**:

| 维度 | 分析内容 | 输出示例 |
|------|----------|----------|
| **色彩** | 主色、辅色、色调倾向 | "Mocha Mousse暖棕+金色" |
| **构图** | 三分法、对称、框架等 | "70%对称构图" |
| **光效** | 自然光、人工光、氛围 | "Sculptural Lighting雕刻光" |
| **镜头** | 景别分布、运镜方式 | "80%极近特写+环绕运镜" |
| **节奏** | 剪辑速度、镜头时长 | "电影感4镜/15秒" |
| **风格** | 匹配知识库风格 | "Prada珠宝风+产品性为主" |

---

#### 2.2 叙事结构分析

```python
def analyze_narrative(self, transcript, scenes):
    """
    分析TVC的叙事结构
    """
    return {
        "story_arc": self._identify_story_arc(),      # 故事弧线
        "hook_type": self._classify_hook(),           # Hook类型
        "emotional_curve": self._map_emotions(),      # 情绪曲线
        "cta_placement": self._find_cta(),            # CTA位置
        "brand_reveal": self._analyze_branding(),     # 品牌露出策略
        "narrative_model": self._match_model()        # 匹配叙事模型(AIDA等)
    }
```

**故事模型识别**:

```
常见TVC叙事模型:

1. 问题-解决方案模型
   [问题] → [产品出现] → [解决] → [效果]

2. 情感共鸣模型  
   [场景建立] → [情感高潮] → [产品融入] → [情感升华]

3. 对比展示模型
   [Before] → [After] → [产品桥梁] → [CTA]

4. 奇幻旅程模型
   [现实] → [奇幻世界] → [体验] → [回归+改变]

5. 证言推荐模型
   [使用者] → [真实体验] → [产品展示] → [推荐]
```

---

#### 2.3 创意元素提取

**创新点识别**:
- 独特的视觉手法
- 新颖的转场方式
- 记忆符号（视觉锤）
- 金句/口号设计
- 音效运用技巧

**标签自动生成**:
```
输入: Apple iPhone 15 Pro TVC

自动标签:
- 视觉: #SculpturalLighting #极近特写 #产品为主
- 叙事: #极简叙事 #产品即主角 #技术展示
- 风格: #Apple风格 #科技美学 #纯净画面
- 技巧: #慢动作 #细节放大 #质感强调
- 情感: #专业感 #未来感 #精致生活
```

---

### 3. 模仿复刻方案生成

#### 3.1 模仿模式

**A. 直接复刻 (Direct Copy)**
- 完全相同的结构
- 替换产品/品牌
- 保持所有创意元素
- **适用**: 学习练习、内部测试

**B. 风格借鉴 (Style Reference)**
- 采用相同的视觉风格
- 类似的叙事节奏
- 适配不同产品
- **适用**: 同品类产品、竞品对标

**C. 概念改编 (Concept Adaptation)**
- 核心创意概念
- 本土化/产品化改编
- 创新演绎
- **适用**: 跨品类借鉴、区域适配

**D. 元素提取 (Element Extraction)**
- 提取单一技巧（如转场、光效）
- 融入其他创意
- 混合创新
- **适用**: 技巧学习、融合创作

---

#### 3.2 自动适配系统

```python
def generate_adaptation(self, reference_tvc, user_product):
    """
    基于参考TVC生成适配方案
    """
    reference_analysis = self.analyze(reference_tvc)
    
    adaptation_plan = {
        "mode": self._suggest_mode(reference_analysis, user_product),
        "structure": self._adapt_structure(reference_analysis),
        "visual_style": self._adapt_visuals(reference_analysis, user_product),
        "narrative": self._adapt_story(reference_analysis, user_product),
        "technical_specs": self._generate_specs(reference_analysis),
        "ai_prompts": self._generate_prompts(reference_analysis),
        "modifications": self._suggest_changes(reference_analysis, user_product)
    }
    
    return adaptation_plan
```

---

### 4. 案例分析报告

#### 4.1 完整解析报告

```markdown
# TVC案例分析报告

## 基础信息
- **品牌**: Apple
- **产品**: iPhone 15 Pro
- **时长**: 30秒
- **发布年份**: 2023
- **地区**: 全球

## 视觉分析
- **主色调**: 冷银灰 + 产品本色
- **构图风格**: 中心对称构图（85%）
- **光效**: Sculptural Lighting雕刻光效
- **镜头分布**: ECU 70%, CU 20%, WS 10%
- **风格匹配**: Apple风格 + 产品性100%

## 叙事结构
- **模型**: 产品展示型
- **Hook**: 0-3秒 产品特写（吸引注意）
- **发展**: 3-24秒 功能展示（材质/摄像头/性能）
- **高潮**: 24-28秒 综合展示（多机位快剪）
- **CTA**: 28-30秒 品牌+产品名

## 创意亮点
1. **极近特写**: 每个功能都用微距展示
2. **慢动作**: 强调质感和工艺
3. **纯净背景**: 无干扰，产品即焦点
4. **音效设计**: 机械精密感的声音

## 可借鉴元素
- ✅ 极近特写+环绕运镜组合
- ✅ 产品为主的故事性权重
- ✅ 纯净色彩的极简美学
- ⚠️ 需注意: Apple风格强，其他品牌用易显模仿

## 复刻建议

### 方案A: 直接复刻（适合练习）
结构: 完全按照Apple的30秒结构
替换: 将iPhone换成您的产品
调整: 根据产品特性调整展示内容

### 方案B: 风格借鉴（适合竞品）
保留: 极近特写+雕刻光效的风格
调整: 加入故事性元素（40%权重）
创新: 添加品牌独特的视觉符号

### 方案C: 概念改编（适合跨品类）
核心概念: "产品细节的极致追求"
改编方向: 用于非科技类产品（如护肤品、工艺品）
本土化: 结合东方美学（水墨质感+极简）
```

---

### 5. 用户交互流程

```
用户输入TVC
    ↓
┌─────────────────────────────────────────┐
│  Step 1: 解析                            │
│  - 上传视频/链接/描述                    │
│  - AI自动分析视觉+叙事                   │
│  - 生成结构分析报告                      │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│  Step 2: 选择复刻模式                    │
│  A. 直接复刻（学习练习）                 │
│  B. 风格借鉴（同品类）                   │
│  C. 概念改编（跨品类）                   │
│  D. 元素提取（单一技巧）                 │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│  Step 3: 输入您的产品信息                │
│  - 产品名称、类别、卖点                  │
│  - 目标人群、品牌调性                    │
│  - 参考TVC的差异点说明                   │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│  Step 4: 生成复刻方案                    │
│  - 结构对照表（参考vs您的）              │
│  - 调整建议（哪些保留/修改）             │
│  - 完整分镜表                            │
│  - AI提示词                              │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│  Step 5: 优化调整                        │
│  - 用户反馈修改意见                      │
│  - 迭代生成新版本                        │
│  - 最终确认输出                          │
└─────────────────────────────────────────┘
```

---

### 6. 案例库管理

#### 6.1 案例存储结构

```
case-library/
├── by-brand/                    # 按品牌分类
│   ├── apple/
│   │   ├── iphone15.json
│   │   └── macbook.json
│   ├── nike/
│   └── chanel/
├── by-category/                 # 按品类分类
│   ├── beauty/
│   ├── tech/
│   └── food/
├── by-style/                    # 按风格分类
│   ├── sculptural-lighting/
│   ├── color-blocking/
│   └── wes-anderson/
└── analysis-reports/            # 分析报告
    ├── report-template.md
    └── case-001-apple-iphone15.md
```

#### 6.2 案例标签系统

```json
{
  "case_id": "case_001",
  "brand": "Apple",
  "product": "iPhone 15 Pro",
  "duration": 30,
  "year": 2023,
  "region": "global",
  "tags": {
    "visual": ["Sculptural Lighting", "极端特写", "对称构图"],
    "narrative": ["产品展示型", "零叙事", "技术展示"],
    "style": ["Apple风格", "极简主义", "科技美学"],
    "technique": ["慢动作", "环绕运镜", "质感强调"],
    "emotion": ["专业", "未来", "精致"]
  },
  "reference_score": 9.2,
  "learning_value": "高",
  "imitation_difficulty": "中",
  "budget_estimate": "高（需专业设备）"
}
```

---

### 7. 使用示例

#### 示例1: 分析Apple广告并复刻

```
用户: 我想模仿Apple iPhone 15的TVC风格
      用于我们的高端护肤品

系统: 
┌─ 案例分析 ─┐
│ 已识别: Apple风格 + Sculptural Lighting
│ 核心: 极近特写展示产品质感
│ 结构: 纯产品展示，零叙事
└────────────┘

推荐复刻模式: B. 风格借鉴
原因: 护肤品与iPhone同为高端质感产品
      适合极近特写+雕刻光效
      但需增加10-20%故事性（使用场景）

生成方案:
- 保留: 极近特写、环绕运镜、纯净背景
- 调整: 添加女性使用场景（15%时长）
- 创新: 结合Mocha Mousse暖色调（适合护肤品）
- 输出: 完整30秒分镜表 + AI提示词
```

#### 示例2: 跨品类借鉴

```
用户: 我喜欢Nike广告的动感节奏
      但我们是卖茶叶的
      怎么结合？

系统:
┌─ 案例分析 ─┐
│ Nike核心: 动感、激情、快节奏剪辑
│ 技巧: 动态模糊、多角度快切、音乐驱动
└────────────┘

推荐复刻模式: C. 概念改编

创意方案:
"茶叶的动感旅程"
- 借鉴Nike的快节奏剪辑
- 但内容是茶叶从采摘到冲泡的过程
- 动态模糊用于水流、蒸汽
- 音乐: 东方元素+现代节拍
- 调性: 活力但不失茶文化的雅致

风险提示: 避免过于运动化，保持茶品类的优雅调性
```

---

### 8. 伦理与版权提示

```
⚠️ 重要声明

本系统提供的"模仿/复刻"功能仅用于:
✅ 学习优秀案例的创意技巧
✅ 理解TVC的叙事结构
✅ 获取灵感和参考
✅ 内部练习和测试

禁止用于:
❌ 直接抄袭商用（侵犯版权）
❌ 恶意模仿竞品造成混淆
❌ 未经授权使用他人创意

建议做法:
- 借鉴技巧，创新内容
- 学习结构，改编概念
- 参考风格，发展自我
- 灵感来源，独立创作

最终输出的分镜方案应确保:
- 不侵犯原作品版权
- 具有原创性改编
- 符合品牌自身调性
- 合法合规使用
```

---

## 实施方案

### Phase 1: 基础功能
- [x] 案例输入（文字描述）
- [ ] 视频文件上传
- [ ] 平台链接抓取
- [ ] 基础分析模板

### Phase 2: AI分析
- [ ] 视觉元素识别
- [ ] 叙事结构分析
- [ ] 风格匹配算法
- [ ] 自动标签生成

### Phase 3: 复刻生成
- [ ] 四种复刻模式
- [ ] 自动适配系统
- [ ] 分镜表生成
- [ ] AI提示词生成

### Phase 4: 案例库
- [ ] 案例存储系统
- [ ] 标签管理
- [ ] 搜索功能
- [ ] 社区分享

---

**现在您可以：**
1. 发送TVC视频/链接/描述给我
2. 我会自动分析其创意结构
3. 提供模仿/复刻方案
4. 生成适合您产品的分镜表

**请发送您想分析的优秀TVC！** 🎬✨
