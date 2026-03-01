# TVC Storyboard Creator - 自我学习与升级系统

## 概述

本系统实现 skill 的自我学习能力，通过记录用户行为、分析反馈数据、持续优化推荐算法，实现越用越智能的效果。

---

## 核心机制

### 1. 数据收集层 (Data Collection)

#### 1.1 用户行为日志

**记录内容**:
```json
{
  "session_id": "uuid",
  "timestamp": "2026-02-15T10:30:00Z",
  "product_info": {
    "category": "beauty/skincare",
    "keywords": ["anti-aging", "natural", "luxury"],
    "price_range": "high-end"
  },
  "user_choices": {
    "step_3_style": {
      "recommended": ["Mocha Mousse", "Prada Style"],
      "selected": "Bold Color Blocking",
      "recommendation_accepted": false,
      "selection_time_seconds": 45
    },
    "step_4_weight": {
      "recommended": "60% product",
      "selected": "80% product",
      "deviation": "+20%"
    }
  },
  "final_output_rating": 4.5,
  "revision_count": 2,
  "completion_time_minutes": 12
}
```

**收集维度**:
- 推荐采纳率（是否选择AI推荐的选项）
- 决策时间（犹豫越久，推荐可能越不准）
- 修正次数（需要多次修改 = 推荐不理想）
- 满意度评分（用户主动评价）
- 产品-风格-权重的最终匹配结果

#### 1.2 成功案例库

**高满意度案例存档**:
```json
{
  "case_id": "case_001",
  "product_profile": {
    "category": "luxury_beauty",
    "attributes": ["premium", "texture_focus", "mature_women"]
  },
  "winning_combination": {
    "style": "Sculptural Lighting",
    "weight": "85% product",
    "duration": "15s",
    "pacing": "cinematic"
  },
  "satisfaction_score": 5.0,
  "usage_count": 3,
  "last_used": "2026-02-10"
}
```

---

### 2. 学习算法层 (Learning Engine)

#### 2.1 推荐准确性评估

**准确率计算**:
```python
def calculate_recommendation_accuracy():
    """
    评估推荐系统的准确性
    """
    total_sessions = get_total_sessions()
    
    # 一级推荐采纳率
    primary_acceptance = sessions_where_first_recommendation_selected / total_sessions
    
    # 前三推荐采纳率
    top3_acceptance = sessions_where_selected_in_top3 / total_sessions
    
    # 满意度加权
    satisfaction_weighted = sum(rating * confidence) / total_sessions
    
    return {
        "primary_accuracy": primary_acceptance,  # 目标: >70%
        "top3_accuracy": top3_acceptance,        # 目标: >90%
        "satisfaction_score": satisfaction_weighted  # 目标: >4.2/5
    }
```

#### 2.2 风格-产品关联学习

**关联矩阵更新**:
```
                    故事性需求    产品性需求
                    低    中    高
                ┌─────┬─────┬─────┐
Mocha Mousse    │ 0.7 │ 0.8 │ 0.9 │ ← 产品性越高，匹配度越高
                ├─────┼─────┼─────┤
Wes Anderson    │ 0.9 │ 0.7 │ 0.4 │ ← 故事性越高，匹配度越高
                ├─────┼─────┼─────┤
Prada Style     │ 0.3 │ 0.6 │ 0.95│ ← 纯产品展示
                └─────┴─────┴─────┘

矩阵通过用户使用数据持续更新
```

#### 2.3 关键词权重优化

**卖点关键词学习**:
```python
# 初始权重
keyword_weights = {
    "luxury": {"product_focus": 0.8, "style": "Prada/Mocha"},
    "handmade": {"product_focus": 0.9, "style": "Sculptural"},
    "family": {"story_focus": 0.9, "style": "Wes Anderson"},
    "innovation": {"product_focus": 0.7, "style": "Cyberpunk"}
}

# 根据用户反馈调整
if user_selected_style != recommended_style:
    # 降低该关键词的当前推荐权重
    adjust_keyword_weight(keyword, recommended_style, -0.1)
    # 提升用户实际选择的方向
    adjust_keyword_weight(keyword, selected_style, +0.1)
```

---

### 3. 模型优化层 (Model Optimization)

#### 3.1 定期重训练

**触发条件**:
- 每收集100个新session
- 或每周一次（取较早者）
- 准确率低于阈值时立即触发

**重训练流程**:
```
1. 导出最近N个session的数据
2. 清洗和标注数据
3. 重新计算风格-产品关联矩阵
4. 更新关键词权重
5. 验证准确率是否提升
6. 生成新版本模型
7. A/B测试（小流量验证）
8. 全量发布
```

#### 3.2 A/B测试框架

**测试场景**:
```
测试组A: 使用旧版推荐算法
测试组B: 使用新版推荐算法

对比指标:
- 推荐采纳率
- 决策时间（越短越好）
- 修正次数（越少越好）
- 满意度评分

胜出新版标准:
- 采纳率提升 >5%
- 决策时间减少 >10%
- 满意度提升 >0.2分
```

---

### 4. 反馈循环层 (Feedback Loop)

#### 4.1 显式反馈收集

**用户主动评价**:
```
═══════════════════════════════════════════
  📊 满意度评价
═══════════════════════════════════════════

生成的分镜表是否符合您的预期？

⭐⭐⭐⭐⭐ 完美，超出预期
⭐⭐⭐⭐☆ 很好，基本符合
⭐⭐⭐☆☆ 一般，需要修改
⭐⭐☆☆☆ 不太符合
⭐☆☆☆☆ 完全不符合

【反馈有助于AI学习，让推荐更精准】
```

**显式纠正**:
```
您选择了 "Bold Color Blocking"，
而AI推荐的是 "Mocha Mousse"。

请问为什么放弃推荐选项？
□ 风格不符合产品调性
□ 想要更前卫/更保守的风格
□ 没注意到推荐选项
□ 其他原因：______

【您的反馈将改进推荐算法】
```

#### 4.2 隐式反馈分析

**行为信号解读**:
| 行为 | 含义 | 学习动作 |
|------|------|----------|
| 快速选择（<10秒） | 推荐准确或要求低 | 记录为正面样本 |
| 长时间犹豫（>60秒） | 推荐不够精准 | 分析原因，调整权重 |
| 多次修改 | 初始推荐偏差大 | 记录为负面样本 |
| 反复查看某风格 | 对该风格感兴趣 | 提升该风格权重 |
| 放弃生成 | 严重不符合预期 | 紧急分析，修复bug |

---

### 5. 版本管理 (Version Control)

#### 5.1 模型版本号

```
v2.3.1
├─ 主版本号 2: 重大架构更新
├─ 次版本号 3: 新功能/优化
└─ 修订号 1: Bug修复
```

#### 5.2 版本发布日志

```markdown
## v2.3.1 (2026-02-15)

### 数据表现
- 总学习样本: 1,247 sessions
- 推荐采纳率: 73% (↑5% from v2.3.0)
- 平均满意度: 4.4/5 (↑0.2)

### 优化内容
1. **风格矩阵更新**
   - 新增: Bold Color Blocking × 美妆品类关联度 +15%
   - 调整: Wes Anderson × 故事性权重 +10%
   - 优化: 关键词"handmade"→Sculptural Lighting 准确率提升至89%

2. **新产品类别支持**
   - 新增: 宠物用品类别推荐模型
   - 基于: 87个宠物用品session学习

3. **Bug修复**
   - 修复: 价格带分析时偶发的空指针异常
   - 修复: 双语输出时的术语映射错误

### 训练数据
- 数据来源: 2026-01-15 至 2026-02-14
- 样本分布: 美妆35%, 3C25%, 食品20%, 其他20%
- 用户反馈: 892条显式反馈, 1,247条隐式反馈
```

#### 5.3 回滚机制

```python
def rollback_to_version(version_id):
    """
    当新版本表现不佳时回滚
    """
    if current_accuracy < previous_accuracy - 0.1:
        # 自动回滚
        restore_model(version_id)
        notify_admin("Auto-rollback triggered")
        
    # 保留数据用于后续分析
    archive_session_data(since_version=version_id)
```

---

### 6. 知识库自更新 (Auto-Update)

#### 6.1 趋势自动追踪

**自动抓取**:
```python
# 每周自动搜索最新趋势
weekly_trends = fetch_trends_from(
    sources=["Pantone", "Vogue", "Behance", "Fashion Week"],
    keywords=["color trend", "visual style", "advertising 2025"]
)

# 检测新趋势
if is_new_trend(weekly_trends, existing_knowledge_base):
    draft_new_style_entry(weekly_trends)
    flag_for_human_review()
```

#### 6.2 用户贡献

**用户提交新风格**:
```
【发现新趋势？】

您想建议添加新的视觉风格吗？

风格名称: ___________
参考案例: ___________（品牌/广告片）
适用产品: ___________
参考图片: [上传]

【社区审核后将加入知识库】
```

---

### 7. 学习效果监控面板

```
╔══════════════════════════════════════════════════════╗
║  🤖 AI学习系统监控面板                               ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  📊 整体表现                                          ║
║  ┌────────────────────────────────────────────┐     ║
║  │ 推荐采纳率        73%     ████████░░ 目标:70%    ║
║  │ Top3采纳率        91%     █████████░ 目标:90%    ║
║  │ 平均满意度        4.4/5   ████████░░ 目标:4.2    ║
║  │ 决策时间          28秒    ██████░░░░ 目标:<30s   ║
║  └────────────────────────────────────────────┘     ║
║                                                      ║
║  📈 学习进度                                          ║
║  已学习样本: 1,247 sessions                         ║
║  上次更新: 3天前                                     ║
║  下次训练: 还剩53个样本                             ║
║                                                      ║
║  🎯 近期优化                                          ║
║  ✓ 美妆×Sculptural Lighting 准确率 +12%             ║
║  ✓ 关键词"organic"权重调整                          ║
║  ✗ 食品类推荐需改进（采纳率仅58%）                  ║
║                                                      ║
║  📦 版本信息                                          ║
║  当前: v2.3.1 (稳定)                                 ║
║  最新: v2.4.0-beta (测试中)                         ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

---

### 8. 伦理与隐私

#### 8.1 数据匿名化

```python
# 存储前移除敏感信息
def anonymize_session_data(session):
    return {
        "product_category": session.category,  # 保留类别
        "product_keywords": session.keywords,  # 保留关键词
        # "brand_name": REMOVED               # 移除品牌名
        # "user_id": HASHED                    # 哈希化用户ID
        "choices": session.choices,
        "timestamp": session.timestamp
    }
```

#### 8.2 用户控制

```
【隐私设置】

☑ 允许匿名使用数据用于AI学习
☐ 允许分享成功案例（去标识化）
☐ 接收个性化推荐优化通知

您的数据仅用于改进推荐质量，
不会用于其他商业目的。
```

---

## 实施路线图

### Phase 1: 基础数据收集 (v2.1)
- [x] 用户行为日志系统
- [x] 满意度评分收集
- [x] 基础统计面板

### Phase 2: 初级学习 (v2.2)
- [ ] 简单权重调整算法
- [ ] 成功案例库构建
- [ ] 推荐准确性评估

### Phase 3: 深度学习 (v2.3)
- [ ] 关联矩阵自动更新
- [ ] 关键词权重优化
- [ ] A/B测试框架

### Phase 4: 持续进化 (v2.4+)
- [ ] 自动趋势追踪
- [ ] 用户贡献系统
- [ ] 跨品类迁移学习

---

**让这个 skill 越用越聪明！** 🧠✨
