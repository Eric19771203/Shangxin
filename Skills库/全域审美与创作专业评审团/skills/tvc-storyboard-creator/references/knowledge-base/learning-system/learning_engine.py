# learning_engine.py
# TVC Storyboard Creator - Self-Learning Engine
# Simplified implementation example

import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import random


class LearningEngine:
    """
    自学习引擎核心类
    负责数据收集、分析和模型优化
    """

    def __init__(self, knowledge_base_path: str = "./learning_data/"):
        self.kb_path = knowledge_base_path
        self.session_log = []
        self.style_matrix = self._load_style_matrix()
        self.keyword_weights = self._load_keyword_weights()

    def _load_style_matrix(self) -> Dict:
        """加载风格-产品关联矩阵"""
        try:
            with open(f"{self.kb_path}style_matrix.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            # 初始化默认矩阵
            return {
                "general": {
                    "Mocha Mousse": {
                        "product_focus": 0.6,
                        "story_focus": 0.7,
                        "confidence": 0.75,
                    },
                    "Wes Anderson": {
                        "product_focus": 0.5,
                        "story_focus": 0.8,
                        "confidence": 0.70,
                    },
                },
                "beauty/skincare": {
                    "Mocha Mousse": {
                        "product_focus": 0.8,
                        "story_focus": 0.6,
                        "confidence": 0.85,
                    },
                    "Prada Jewelry Style": {
                        "product_focus": 0.95,
                        "story_focus": 0.3,
                        "confidence": 0.82,
                    },
                    "Bold Color Blocking": {
                        "product_focus": 0.9,
                        "story_focus": 0.4,
                        "confidence": 0.78,
                    },
                    "Wes Anderson": {
                        "product_focus": 0.4,
                        "story_focus": 0.9,
                        "confidence": 0.75,
                    },
                },
                "food/beverage": {
                    "Mocha Mousse": {
                        "product_focus": 0.6,
                        "story_focus": 0.8,
                        "confidence": 0.80,
                    },
                    "Fashion Romantasy": {
                        "product_focus": 0.5,
                        "story_focus": 0.9,
                        "confidence": 0.72,
                    },
                },
                "3c/tech": {
                    "Sculptural Lighting": {
                        "product_focus": 0.95,
                        "story_focus": 0.2,
                        "confidence": 0.88,
                    },
                    "Liquid Metal": {
                        "product_focus": 0.9,
                        "story_focus": 0.3,
                        "confidence": 0.85,
                    },
                    "Cyberpunk": {
                        "product_focus": 0.8,
                        "story_focus": 0.5,
                        "confidence": 0.83,
                    },
                },
            }

    def _load_keyword_weights(self) -> Dict:
        """加载关键词权重"""
        try:
            with open(
                f"{self.kb_path}keyword_weights.json", "r", encoding="utf-8"
            ) as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "luxury": {
                    "weight": 1.0,
                    "product_bias": 0.8,
                    "styles": ["Prada", "Mocha"],
                },
                "handmade": {
                    "weight": 1.0,
                    "product_bias": 0.9,
                    "styles": ["Sculptural"],
                },
                "family": {
                    "weight": 1.0,
                    "product_bias": 0.2,
                    "styles": ["Wes Anderson"],
                },
                "innovation": {
                    "weight": 1.0,
                    "product_bias": 0.7,
                    "styles": ["Cyberpunk", "Romantasy"],
                },
                "natural": {
                    "weight": 1.0,
                    "product_bias": 0.4,
                    "styles": ["Mocha", "Scandinavian"],
                },
                "premium": {
                    "weight": 1.0,
                    "product_bias": 0.85,
                    "styles": ["Prada", "Sculptural"],
                },
            }

    def record_session(self, session_data: Dict) -> str:
        """
        记录用户会话数据

        Args:
            session_data: 包含用户选择的完整数据

        Returns:
            session_id: 本次会话的唯一ID
        """
        session_id = str(uuid.uuid4())

        enriched_data = {
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
            **session_data,
            "learning_metadata": {
                "model_version": "2.3.1",
                "recommendation_algorithm": "weighted_matrix_v2",
            },
        }

        self.session_log.append(enriched_data)

        # 实时学习：如果偏差大，立即调整
        self._realtime_learning(enriched_data)

        # 每50个session触发一次批量分析
        if len(self.session_log) % 50 == 0:
            self._batch_analysis()

        return session_id

    def recommend_styles(self, product_profile: Dict) -> List[Tuple[str, float, str]]:
        """
        基于产品画像推荐视觉风格

        Args:
            product_profile: {
                "category": "beauty/skincare",
                "keywords": ["luxury", "anti-aging"],
                "target_audience": "30-50 women",
                "price_range": "high-end"
            }

        Returns:
            [(style_name, confidence_score, reason), ...]
            按置信度排序，返回前5个推荐
        """
        category = product_profile.get("category", "general")
        keywords = product_profile.get("keywords", [])

        # 1. 基于类别的初始匹配
        category_styles = self.style_matrix.get(category, self.style_matrix["general"])

        # 2. 基于关键词的加权
        keyword_boost = {}
        for keyword in keywords:
            if keyword in self.keyword_weights:
                weight_data = self.keyword_weights[keyword]
                for style in weight_data["styles"]:
                    if style not in keyword_boost:
                        keyword_boost[style] = 0
                    keyword_boost[style] += weight_data["weight"] * 0.1

        # 3. 计算综合得分
        recommendations = []
        for style_name, metrics in category_styles.items():
            base_score = (metrics["product_focus"] + metrics["story_focus"]) / 2
            confidence = metrics["confidence"]
            keyword_bonus = keyword_boost.get(style_name, 0)

            final_score = (
                base_score * 0.6 + confidence * 0.3 + keyword_bonus * 0.1
            ) * 100

            # 生成推荐理由
            reason = self._generate_reason(style_name, metrics, keyword_bonus)

            recommendations.append((style_name, final_score, reason))

        # 4. 排序并返回Top 5
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:5]

    def _generate_reason(
        self, style_name: str, metrics: Dict, keyword_bonus: float
    ) -> str:
        """生成推荐理由"""
        reasons = []

        if metrics["confidence"] > 0.85:
            reasons.append(f"高置信度匹配({metrics['confidence']:.0%})")

        if metrics["product_focus"] > 0.8:
            reasons.append("适合产品细节展示")
        elif metrics["story_focus"] > 0.8:
            reasons.append("适合情感叙事")

        if keyword_bonus > 0:
            reasons.append("契合产品关键词")

        return "；".join(reasons) if reasons else "综合推荐"

    def _realtime_learning(self, session_data: Dict):
        """实时学习：根据用户选择调整权重"""
        try:
            recommended = session_data["user_choices"]["step_3_style"]["recommended"]
            selected = session_data["user_choices"]["step_3_style"]["selected"]

            if selected not in recommended:
                # 用户没有选择推荐项，分析原因
                self._analyze_deviation(session_data)
        except KeyError:
            pass

    def _analyze_deviation(self, session_data: Dict):
        """分析用户为什么偏离推荐"""
        product_keywords = session_data.get("product_info", {}).get("keywords", [])
        selected_style = session_data["user_choices"]["step_3_style"]["selected"]

        # 检查是否是关键词理解偏差
        for keyword in product_keywords:
            if keyword in self.keyword_weights:
                current_styles = set(self.keyword_weights[keyword]["styles"])
                if selected_style not in current_styles:
                    # 用户实际选择的风格不在关键词关联中，需要添加
                    print(
                        f"[学习] 发现新关联: 关键词'{keyword}' → 风格'{selected_style}'"
                    )
                    # 实际实现中这里会更新权重文件

    def _batch_analysis(self):
        """批量分析最近的会话数据"""
        recent_sessions = self.session_log[-50:]

        # 计算各类指标
        stats = {
            "total": len(recent_sessions),
            "primary_acceptance": 0,
            "top3_acceptance": 0,
            "avg_satisfaction": 0,
            "avg_decision_time": 0,
        }

        for session in recent_sessions:
            try:
                style_choice = session["user_choices"]["step_3_style"]
                recommended = style_choice["recommended"]
                selected = style_choice["selected"]

                if selected == recommended[0]:
                    stats["primary_acceptance"] += 1
                if selected in recommended:
                    stats["top3_acceptance"] += 1

                stats["avg_satisfaction"] += session.get("final_output_rating", 4)
                stats["avg_decision_time"] += session.get("selection_time_seconds", 30)
            except KeyError:
                continue

        # 计算平均值
        if stats["total"] > 0:
            stats["primary_acceptance_rate"] = (
                stats["primary_acceptance"] / stats["total"]
            )
            stats["top3_acceptance_rate"] = stats["top3_acceptance"] / stats["total"]
            stats["avg_satisfaction"] /= stats["total"]
            stats["avg_decision_time"] /= stats["total"]

        print(f"\n[批量分析报告] 最近50个session:")
        print(f"  一级推荐采纳率: {stats['primary_acceptance_rate']:.1%}")
        print(f"  Top3推荐采纳率: {stats['top3_acceptance_rate']:.1%}")
        print(f"  平均满意度: {stats['avg_satisfaction']:.2f}/5")
        print(f"  平均决策时间: {stats['avg_decision_time']:.1f}秒")

        # 如果表现不佳，标记需要人工审查
        if stats["primary_acceptance_rate"] < 0.6:
            print(f"  ⚠️ 警告: 推荐准确率低于60%，建议检查模型")

    def export_training_report(self) -> str:
        """导出训练报告"""
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_sessions": len(self.session_log),
            "model_version": "2.3.1",
            "style_matrix_stats": {
                "categories": len(self.style_matrix),
                "total_style_pairs": sum(len(v) for v in self.style_matrix.values()),
            },
            "keyword_weights_count": len(self.keyword_weights),
            "recent_performance": self._calculate_recent_performance(),
        }

        return json.dumps(report, indent=2, ensure_ascii=False)

    def _calculate_recent_performance(self) -> Dict:
        """计算最近表现"""
        recent = (
            self.session_log[-100:]
            if len(self.session_log) >= 100
            else self.session_log
        )

        if not recent:
            return {"status": "insufficient_data"}

        accepted = sum(
            1
            for s in recent
            if s.get("user_choices", {}).get("step_3_style", {}).get("selected")
            in s.get("user_choices", {}).get("step_3_style", {}).get("recommended", [])
        )

        return {
            "sample_size": len(recent),
            "acceptance_rate": accepted / len(recent),
            "status": "good" if accepted / len(recent) > 0.7 else "needs_improvement",
        }


# 使用示例
if __name__ == "__main__":
    # 初始化学习引擎
    engine = LearningEngine()

    # 示例1: 产品分析后的风格推荐
    print("=" * 60)
    print("🎨 智能风格推荐示例")
    print("=" * 60)

    product = {
        "category": "beauty/skincare",
        "keywords": ["luxury", "anti-aging", "natural"],
        "target_audience": "30-50 women",
        "price_range": "high-end",
    }

    recommendations = engine.recommend_styles(product)

    print(f"\n产品: 高端抗衰老护肤品")
    print(f"关键词: {', '.join(product['keywords'])}\n")
    print("推荐风格:")
    for i, (style, score, reason) in enumerate(recommendations, 1):
        stars = "⭐" * (3 if score > 85 else 2 if score > 75 else 1)
        print(f"{i}. {stars} {style}")
        print(f"   匹配度: {score:.0f}%")
        print(f"   理由: {reason}\n")

    # 示例2: 记录用户会话
    print("=" * 60)
    print("📝 记录用户选择")
    print("=" * 60)

    session_data = {
        "product_info": product,
        "user_choices": {
            "step_3_style": {
                "recommended": ["Mocha Mousse", "Prada Jewelry Style"],
                "selected": "Mocha Mousse",  # 用户接受了推荐！
                "recommendation_accepted": True,
                "selection_time_seconds": 15,
            },
            "step_4_weight": {
                "recommended": "70% product",
                "selected": "70% product",
                "deviation": "0%",
            },
        },
        "final_output_rating": 5,
        "revision_count": 0,
    }

    session_id = engine.record_session(session_data)
    print(f"✅ 会话已记录 (ID: {session_id[:8]}...)")
    print(f"   推荐采纳: ✓ 是")
    print(f"   满意度: ⭐⭐⭐⭐⭐")

    # 示例3: 导出报告
    print("\n" + "=" * 60)
    print("📊 训练数据报告")
    print("=" * 60)
    print(engine.export_training_report())
