"""
漫剧分类知识库模块
包含战斗漫剧、恋爱漫剧、剧情漫剧等类型的专业知识
"""

from typing import List, Dict, Any


# 战斗漫剧知识库
class BattleComicKnowledge:
    """漫剧-战斗类知识库"""
    
    CHARACTERISTICS = {
        "name": "漫剧-战斗类",
        "description": "强调视觉冲击、速度感和力量感",
        "key_elements": ["速度线", "冲击画面", "动作分解", "能量特效", "视觉张力"],
        "typical_duration": "1-2分钟",
        "typical_shot_count": "40-60个镜头",
        "pacing": "极快，1-2秒/格"
    }
    
    # 格子布局技巧
    PANEL_TECHNIQUES = {
        "main_panel": {
            "name": "主格",
            "size": "大格子",
            "usage": "重要场景或冲击画面",
            "effect": "视觉焦点，翻页冲击"
        },
        "action_sequence": {
            "name": "动作序列",
            "layout": "横向连续格",
            "usage": "动作分解展示",
            "effect": "时间延展，动作连贯"
        },
        "speed_lines": {
            "name": "速度线",
            "technique": "放射状或水平线条",
            "usage": "强调速度和冲击力",
            "effect": "动态感，视觉冲击"
        },
        "break_panel": {
            "name": "破格",
            "technique": "人物超出格子边界",
            "usage": "增强层次感和动感",
            "effect": "突破平面限制"
        }
    }
    
    # 视觉引导
    VISUAL_GUIDE = {
        "z_pattern": "Z字形阅读路径，适用于动作场景",
        "eye_catch": "眼球捕捉效果，左上角大格吸引注意",
        "flow_lines": "流动线引导视线",
        "impact_frames": "冲击帧放在翻页位置"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "战斗漫剧冲击3×3",
        "shots": [
            {
                "index": 1, 
                "name": "战场环境", 
                "shot_type": "大远景",
                "panel_type": "主格",
                "prompt": "Battlefield establishing shot, destroyed landscape, dramatic sky, wide angle, comic book style, detailed background"
            },
            {
                "index": 2, 
                "name": "角色登场", 
                "shot_type": "全景",
                "panel_type": "标准格",
                "prompt": "Hero entrance, dynamic pose, wind effect, full body, confident stance, manga style, speed lines"
            },
            {
                "index": 3, 
                "name": "对峙构图", 
                "shot_type": "中全景",
                "panel_type": "标准格",
                "prompt": "Confrontation two-shot, opponents facing, tension building, dramatic angle, comic panel layout"
            },
            {
                "index": 4, 
                "name": "动作发起", 
                "shot_type": "中景",
                "panel_type": "动作序列",
                "prompt": "Action initiation, attack movement, motion blur, dynamic pose, speed lines, impact frame"
            },
            {
                "index": 5, 
                "name": "关键打击", 
                "shot_type": "中近景",
                "panel_type": "主格/破格",
                "prompt": "Critical hit impact, extreme action, punch or kick, motion lines, explosion effect, character breaking panel border"
            },
            {
                "index": 6, 
                "name": "技能特效", 
                "shot_type": "近景",
                "panel_type": "特效格",
                "prompt": "Special ability effect, energy burst, power visual, glowing effects, detailed rendering, comic style"
            },
            {
                "index": 7, 
                "name": "武器/力量", 
                "shot_type": "特写A",
                "panel_type": "细节格",
                "prompt": "Weapon or power extreme close-up, energy detail, glowing weapon, intricate design, macro shot"
            },
            {
                "index": 8, 
                "name": "战斗意志", 
                "shot_type": "特写B",
                "panel_type": "表情格",
                "prompt": "Determined eyes, fighting spirit, intense expression, extreme close-up, dramatic shading, manga style"
            },
            {
                "index": 9, 
                "name": "胜负揭晓", 
                "shot_type": "远景",
                "panel_type": "主格",
                "prompt": "Aftermath wide shot, victor standing, defeated enemy, dramatic composition, smoke and dust, epic ending"
            }
        ]
    }


# 恋爱漫剧知识库
class RomanceComicKnowledge:
    """漫剧-恋爱类知识库"""
    
    CHARACTERISTICS = {
        "name": "漫剧-恋爱类",
        "description": "强调情感表达、浪漫氛围和人物关系",
        "key_elements": ["竖格强调", "眼神交流", "浪漫特效", "情感递进", "甜蜜细节"],
        "typical_duration": "1-2分钟",
        "typical_shot_count": "30-50个镜头",
        "pacing": "温柔流畅"
    }
    
    PANEL_TECHNIQUES = {
        "vertical_panel": {
            "name": "竖格",
            "usage": "强调人物，特别是全身或半身",
            "effect": "优雅、修长、聚焦"
        },
        "horizontal_panel": {
            "name": "横格",
            "usage": "展现场景和环境",
            "effect": "开阔、空间感"
        },
        "flower_effect": {
            "name": "花特效",
            "usage": "浪漫氛围营造",
            "effect": "梦幻、甜蜜"
        },
        "sparkle_effect": {
            "name": "闪光特效",
            "usage": "心动瞬间",
            "effect": "闪耀、心动"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "恋爱漫剧甜蜜3×3",
        "shots": [
            {
                "index": 1, 
                "name": "浪漫场景", 
                "shot_type": "远景",
                "panel_type": "横格",
                "prompt": "Romantic location wide shot, cherry blossoms or sunset, dreamy atmosphere, shoujo manga style, soft colors"
            },
            {
                "index": 2, 
                "name": "主角登场", 
                "shot_type": "全景",
                "panel_type": "竖格",
                "prompt": "Protagonist entrance, full body, flowing hair, elegant pose, shoujo style, sparkle effects"
            },
            {
                "index": 3, 
                "name": "相遇瞬间", 
                "shot_type": "中全景",
                "panel_type": "标准格",
                "prompt": "Fateful meeting, two figures, romantic tension, flower petals, soft focus, manga romance"
            },
            {
                "index": 4, 
                "name": "情感交流", 
                "shot_type": "中景",
                "panel_type": "标准格",
                "prompt": "Emotional exchange, blushing faces, romantic atmosphere, sparkles, emotional manga style"
            },
            {
                "index": 5, 
                "name": "心动时刻", 
                "shot_type": "中近景",
                "panel_type": "主格",
                "prompt": "Heart flutter moment, romantic realization, soft lighting, flower background, shoujo manga aesthetic"
            },
            {
                "index": 6, 
                "name": "亲密细节", 
                "shot_type": "近景",
                "panel_type": "细节格",
                "prompt": "Intimate detail, hands almost touching, romantic tension, soft focus, delicate rendering"
            },
            {
                "index": 7, 
                "name": "定情信物", 
                "shot_type": "特写A",
                "panel_type": "细节格",
                "prompt": "Love token extreme close-up, jewelry or gift, sentimental value, sparkle effects, romantic symbolism"
            },
            {
                "index": 8, 
                "name": "深情凝视", 
                "shot_type": "特写B",
                "panel_type": "表情格",
                "prompt": "Loving gaze, detailed eyes, shoujo style, sparkle in eyes, emotional depth, romantic close-up"
            },
            {
                "index": 9, 
                "name": "幸福结局", 
                "shot_type": "远景",
                "panel_type": "横格",
                "prompt": "Happy ending wide shot, couple together, romantic sunset, flower frame, shoujo manga ending"
            }
        ]
    }


# 剧情漫剧知识库
class StoryComicKnowledge:
    """漫剧-剧情类知识库"""
    
    CHARACTERISTICS = {
        "name": "漫剧-剧情类",
        "description": "强调叙事、人物发展和情节推进",
        "key_elements": ["起承转合", "格子节奏", "信息密度", "情绪递进", "故事完整性"],
        "typical_duration": "1-2分钟",
        "typical_shot_count": "35-55个镜头",
        "pacing": "根据情节调整"
    }
    
    NARRATIVE_STRUCTURE = {
        "setup": {
            "name": "起",
            "purpose": "建立人物和背景",
            "panel_style": "稳定格子，信息清晰"
        },
        "development": {
            "name": "承",
            "purpose": "情节发展，冲突出现",
            "panel_style": "格子变化，节奏加快"
        },
        "climax": {
            "name": "转",
            "purpose": "高潮转折，情绪爆发",
            "panel_style": "大格冲击，破格效果"
        },
        "resolution": {
            "name": "合",
            "purpose": "结局收束，余韵留存",
            "panel_style": "稳定格子，开放式或闭合式"
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "剧情漫剧叙事3×3",
        "shots": [
            {
                "index": 1, 
                "name": "世界建立", 
                "shot_type": "远景",
                "panel_type": "横格",
                "prompt": "World establishing shot, setting the scene, detailed background, story context, manga establishing panel"
            },
            {
                "index": 2, 
                "name": "人物介绍", 
                "shot_type": "全景",
                "panel_type": "标准格",
                "prompt": "Character introduction, full body, personality shown through pose, character design, manga style"
            },
            {
                "index": 3, 
                "name": "关系展示", 
                "shot_type": "中全景",
                "panel_type": "标准格",
                "prompt": "Relationship dynamics, character interaction, body language, social context, manga storytelling"
            },
            {
                "index": 4, 
                "name": "冲突开始", 
                "shot_type": "中景",
                "panel_type": "变化格",
                "prompt": "Conflict initiation, problem arises, tension building, story complication, dramatic manga panel"
            },
            {
                "index": 5, 
                "name": "转折高潮", 
                "shot_type": "中近景",
                "panel_type": "主格",
                "prompt": "Turning point climax, emotional peak, dramatic revelation, story pivot, impactful manga frame"
            },
            {
                "index": 6, 
                "name": "关键细节", 
                "shot_type": "近景",
                "panel_type": "细节格",
                "prompt": "Crucial detail close-up, important object or expression, story element, manga detail panel"
            },
            {
                "index": 7, 
                "name": "象征元素", 
                "shot_type": "特写A",
                "panel_type": "细节格",
                "prompt": "Symbolic element extreme close-up, metaphorical object, story symbolism, manga symbolism"
            },
            {
                "index": 8, 
                "name": "内心揭示", 
                "shot_type": "特写B",
                "panel_type": "表情格",
                "prompt": "Inner revelation, emotional expression, character growth, psychological depth, manga emotion"
            },
            {
                "index": 9, 
                "name": "故事收束", 
                "shot_type": "远景",
                "panel_type": "横格",
                "prompt": "Story resolution wide shot, conclusion or new beginning, thematic ending, manga final panel"
            }
        ]
    }


# 导出所有知识库
COMIC_KNOWLEDGE_BASES = {
    "battle": BattleComicKnowledge,
    "romance": RomanceComicKnowledge,
    "story": StoryComicKnowledge,
}


def get_comic_knowledge(comic_type: str):
    """获取指定类型的漫剧知识库"""
    return COMIC_KNOWLEDGE_BASES.get(comic_type)


def get_comic_storyboard(comic_type: str, board_type: str = "3x3"):
    """获取指定类型的分镜模板"""
    knowledge = get_comic_knowledge(comic_type)
    if knowledge:
        return knowledge.STORYBOARD_3X3
    return None


def list_comic_types():
    """列出所有可用的漫剧类型"""
    return list(COMIC_KNOWLEDGE_BASES.keys())


__all__ = [
    'BattleComicKnowledge',
    'RomanceComicKnowledge',
    'StoryComicKnowledge',
    'get_comic_knowledge',
    'get_comic_storyboard',
    'list_comic_types',
]
