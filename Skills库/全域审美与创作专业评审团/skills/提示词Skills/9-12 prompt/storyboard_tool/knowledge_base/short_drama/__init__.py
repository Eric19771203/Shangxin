"""
短剧分类知识库模块
包含打斗戏、感情戏、都市戏、悬疑戏等类型的专业知识
"""

from typing import List, Dict, Any


# 打斗戏知识库
class ActionDramaKnowledge:
    """短剧-打斗戏知识库"""
    
    CHARACTERISTICS = {
        "name": "短剧-打斗戏",
        "description": "快节奏动作场景，强调视觉冲击和紧张感",
        "key_elements": ["快节奏剪辑", "动作连贯性", "冲击感", "能量爆发", "视觉张力"],
        "typical_duration": "1-3分钟",
        "typical_shot_count": "30-60个镜头",
        "pacing": "极快，1-2秒/镜"
    }
    
    # 蜂巢式叙事结构
    HONEYCOMB_STRUCTURE = {
        "preheat": {
            "duration": "0-30秒",
            "shots": "10-15个",
            "purpose": "抛出核心矛盾",
            "techniques": ["快速建立冲突", "人物立场展示", "紧张氛围铺垫"]
        },
        "explosion": {
            "duration": "31-90秒",
            "shots": "20-35个",
            "purpose": "三次情绪峰值",
            "techniques": ["第一次交锋", "转折与反击", "高潮对决"]
        },
        "resolution": {
            "duration": "91-120秒",
            "shots": "5-10个",
            "purpose": "开放式结局+悬念钩子",
            "techniques": ["胜负揭晓", "后果展示", "悬念延续"]
        }
    }
    
    SHOT_TECHNIQUES = {
        "wide_coverage": {
            "description": "全景覆盖",
            "lens": "24-35mm广角",
            "purpose": "展示动作范围和空间关系"
        },
        "medium_action": {
            "description": "中景动作",
            "lens": "35-50mm",
            "purpose": "捕捉主要动作和反应"
        },
        "close_impact": {
            "description": "近景冲击",
            "lens": "50-85mm",
            "purpose": "强调打击感和表情"
        },
        "extreme_detail": {
            "description": "特写细节",
            "lens": "85-135mm",
            "purpose": "武器、伤口、汗水等细节"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "短剧打斗高能3×3",
        "shots": [
            {"index": 1, "name": "冲突场景", "shot_type": "远景", "duration": "2秒", "prompt": "Action confrontation wide shot, urban alley or warehouse, dramatic lighting, establishing tension, cinematic"},
            {"index": 2, "name": "双方登场", "shot_type": "全景", "duration": "1.5秒", "prompt": "Opponents facing off, combat stances, wide framing, intense eye contact, ready to fight"},
            {"index": 3, "name": "对峙张力", "shot_type": "中全景", "duration": "1.5秒", "prompt": "Standoff moment, tension building, two-shot composition, dramatic angle, pre-fight atmosphere"},
            {"index": 4, "name": "第一击", "shot_type": "中景", "duration": "1秒", "prompt": "First strike, explosive movement, fast shutter, impact moment, dynamic action"},
            {"index": 5, "name": "关键打击", "shot_type": "中近景", "duration": "0.8秒", "prompt": "Critical hit, punch or kick impact, slow motion potential, intense expression, decisive moment"},
            {"index": 6, "name": "武器特写", "shot_type": "近景", "duration": "1秒", "prompt": "Weapon close-up, blade or fist, motion blur, high detail, action prop"},
            {"index": 7, "name": "汗水/血迹", "shot_type": "特写A", "duration": "0.8秒", "prompt": "Sweat or blood extreme close-up, gritty detail, visceral reality, fight intensity"},
            {"index": 8, "name": "不屈眼神", "shot_type": "特写B", "duration": "1秒", "prompt": "Determined eyes, never give up, intense close-up, dramatic lighting, fighting spirit"},
            {"index": 9, "name": "胜负揭晓", "shot_type": "远景", "duration": "2秒", "prompt": "Aftermath wide shot, victor standing, defeated opponent, dramatic composition, fight conclusion"},
        ]
    }


# 感情戏知识库
class EmotionalDramaKnowledge:
    """短剧-感情戏知识库"""
    
    CHARACTERISTICS = {
        "name": "短剧-感情戏",
        "description": "情感细腻，强调人物关系和情绪递进",
        "key_elements": ["眼神交流", "情绪积累", "细节刻画", "氛围营造", "情感共鸣"],
        "typical_duration": "1-3分钟",
        "typical_shot_count": "20-40个镜头",
        "pacing": "慢到快，情绪递进"
    }
    
    SHOT_TECHNIQUES = {
        "establishing_relationship": {
            "description": "关系建立",
            "lens": "70-100mm",
            "distance": "1.5-2米",
            "technique": "推镜+焦点转移"
        },
        "emotional_closeup": {
            "description": "情绪特写",
            "lens": "85-135mm",
            "purpose": "捕捉微表情和情绪变化"
        },
        "two_shot": {
            "description": "双人镜头",
            "lens": "50-85mm",
            "purpose": "展示人物关系和互动"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "短剧感情细腻3×3",
        "shots": [
            {"index": 1, "name": "情感空间", "shot_type": "远景", "prompt": "Emotional setting wide shot, intimate location, soft lighting, romantic or melancholic atmosphere"},
            {"index": 2, "name": "人物出现", "shot_type": "全景", "prompt": "Character entrance, full body, emotional state visible, natural movement, establishing presence"},
            {"index": 3, "name": "关系建立", "shot_type": "中全景", "prompt": "Two-shot, relationship dynamics, comfortable or tense distance, body language tells story"},
            {"index": 4, "name": "情感交流", "shot_type": "中景", "prompt": "Emotional exchange, meaningful dialogue, over-shoulder shot, growing connection or conflict"},
            {"index": 5, "name": "情绪高潮", "shot_type": "中近景", "prompt": "Emotional peak, tear or smile, intense feeling, soft focus, heart-touching moment"},
            {"index": 6, "name": "亲密细节", "shot_type": "近景", "prompt": "Intimate detail, hand touching, loving gesture, soft lighting, tactile emotion"},
            {"index": 7, "name": "情感信物", "shot_type": "特写A", "prompt": "Sentimental object extreme close-up, gift or memory token, emotional weight, warm tones"},
            {"index": 8, "name": "泪眼/笑眼", "shot_type": "特写B", "prompt": "Eyes with tears or joy, extreme close-up, emotional release, soft focus, soul window"},
            {"index": 9, "name": "情感余韵", "shot_type": "远景", "prompt": "Emotional aftermath wide shot, characters in space, lingering feeling, open composition, story continues"},
        ]
    }


# 都市戏知识库
class UrbanDramaKnowledge:
    """短剧-都市戏知识库"""
    
    CHARACTERISTICS = {
        "name": "短剧-都市戏",
        "description": "现代都市生活，时尚感和快节奏",
        "key_elements": ["都市景观", "时尚元素", "快节奏", "现代感", "生活气息"],
        "typical_duration": "1-3分钟",
        "typical_shot_count": "25-50个镜头",
        "pacing": "中等偏快"
    }
    
    SHOT_TECHNIQUES = {
        "city_establishing": {
            "description": "城市建立",
            "lens": "24mm广角",
            "angle": "俯拍",
            "effect": "畸变增强空间感"
        },
        "street_level": {
            "description": "街景",
            "lens": "35-50mm",
            "purpose": "展现都市生活气息"
        },
        "fashion_detail": {
            "description": "时尚细节",
            "lens": "50-85mm",
            "purpose": "服装、配饰展示"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "短剧都市时尚3×3",
        "shots": [
            {"index": 1, "name": "都市全景", "shot_type": "大远景", "prompt": "City skyline wide shot, modern metropolis, glass buildings, urban energy, establishing shot"},
            {"index": 2, "name": "主角登场", "shot_type": "全景", "prompt": "Protagonist in urban setting, full body fashion, confident walk, city backdrop, stylish entrance"},
            {"index": 3, "name": "都市互动", "shot_type": "中全景", "prompt": "Urban interaction, cafe or office, modern lifestyle, professional or casual, city vibe"},
            {"index": 4, "name": "职场/生活", "shot_type": "中景", "prompt": "Work or life scene, modern interior, contemporary setting, daily routine, urban rhythm"},
            {"index": 5, "name": "情绪瞬间", "shot_type": "中近景", "prompt": "Urban emotion, success or struggle, professional expression, city pressure, human moment"},
            {"index": 6, "name": "时尚细节", "shot_type": "近景", "prompt": "Fashion detail close-up, watch or phone, accessory shot, modern lifestyle, style statement"},
            {"index": 7, "name": "城市符号", "shot_type": "特写A", "prompt": "City symbol extreme close-up, coffee cup or tech device, urban artifact, lifestyle detail"},
            {"index": 8, "name": "都市眼神", "shot_type": "特写B", "prompt": "City eyes, ambition or fatigue, extreme close-up, urban reflection, modern soul"},
            {"index": 9, "name": "都市归宿", "shot_type": "远景", "prompt": "Urban ending wide shot, character in cityscape, night lights or sunset, belonging or isolation"},
        ]
    }


# 悬疑戏知识库
class SuspenseDramaKnowledge:
    """短剧-悬疑戏知识库"""
    
    CHARACTERISTICS = {
        "name": "短剧-悬疑戏",
        "description": "黄金3秒钩子+情绪递进+高互动结尾",
        "key_elements": ["悬念钩子", "信息延迟", "节奏控制", "意外反转", "观众参与"],
        "typical_duration": "1-3分钟",
        "typical_shot_count": "20-40个镜头",
        "pacing": "快慢交替，悬念递进"
    }
    
    # 黄金3秒钩子类型
    HOOK_TYPES = {
        "question": {
            "name": "疑问钩子",
            "example": "你绝对想不到接下来发生了什么...",
            "effect": "激发好奇心"
        },
        "contrarian": {
            "name": "反常识钩子",
            "example": "所有人都错了，真相其实是...",
            "effect": "打破预期"
        },
        "pain_point": {
            "name": "痛点钩子",
            "example": "如果你也经历过这种绝望...",
            "effect": "情感共鸣"
        },
        "visual": {
            "name": "视觉冲击钩子",
            "example": "（震撼画面直接呈现）",
            "effect": "视觉冲击"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "短剧悬疑紧张3×3",
        "shots": [
            {"index": 1, "name": "神秘场景", "shot_type": "远景", "prompt": "Mysterious location wide shot, foggy or dark, ominous atmosphere, suspense establishing, uneasy feeling"},
            {"index": 2, "name": "异常发现", "shot_type": "全景", "prompt": "Something is off, subtle clue, observational camera, building mystery, curious discovery"},
            {"index": 3, "name": "怀疑开始", "shot_type": "中全景", "prompt": "Suspicion arising, character questioning, over-shoulder shot, psychological tension, doubt forming"},
            {"index": 4, "name": "线索浮现", "shot_type": "中景", "prompt": "Clue emerging, discovery moment, important detail, revelation lighting, puzzle piece"},
            {"index": 5, "name": "真相逼近", "shot_type": "中近景", "prompt": "Truth approaching, character realization, intense focus, dramatic lighting, dawning horror"},
            {"index": 6, "name": "关键证据", "shot_type": "近景", "prompt": "Crucial evidence close-up, telling detail, forensic view, sharp focus, game changer"},
            {"index": 7, "name": "隐藏线索", "shot_type": "特写A", "prompt": "Hidden clue extreme close-up, missed detail, sharp focus, mystery element, crucial hint"},
            {"index": 8, "name": "震惊表情", "shot_type": "特写B", "prompt": "Shocked expression, extreme close-up, disbelief, dramatic revelation, emotional impact"},
            {"index": 9, "name": "悬念延续", "shot_type": "远景", "prompt": "Cliffhanger wide shot, unanswered question, open ending, mysterious atmosphere, to be continued"},
        ]
    }


# 导出所有知识库
SHORT_DRAMA_KNOWLEDGE_BASES = {
    "action": ActionDramaKnowledge,
    "emotion": EmotionalDramaKnowledge,
    "urban": UrbanDramaKnowledge,
    "suspense": SuspenseDramaKnowledge,
}


def get_short_drama_knowledge(drama_type: str):
    """获取指定类型的短剧知识库"""
    return SHORT_DRAMA_KNOWLEDGE_BASES.get(drama_type)


def get_short_drama_storyboard(drama_type: str, board_type: str = "3x3"):
    """获取指定类型的分镜模板"""
    knowledge = get_short_drama_knowledge(drama_type)
    if knowledge:
        return knowledge.STORYBOARD_3X3
    return None


def list_short_drama_types():
    """列出所有可用的短剧类型"""
    return list(SHORT_DRAMA_KNOWLEDGE_BASES.keys())


__all__ = [
    'ActionDramaKnowledge',
    'EmotionalDramaKnowledge',
    'UrbanDramaKnowledge',
    'SuspenseDramaKnowledge',
    'get_short_drama_knowledge',
    'get_short_drama_storyboard',
    'list_short_drama_types',
]
