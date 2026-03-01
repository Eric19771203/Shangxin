"""
电影分类知识库模块
包含战争片、文艺片、悬疑片、动作片、爱情片等类型的专业知识
"""

from .war import WarFilmKnowledge, get_war_storyboard

# 文艺片知识库
class ArtFilmKnowledge:
    """文艺片知识库"""
    
    CHARACTERISTICS = {
        "name": "文艺片",
        "description": "注重艺术表达、情感深度和美学追求",
        "key_elements": ["长镜头", "情绪留白", "美学构图", "自然光运用", "开放式结局"],
        "typical_duration": "90-150分钟",
        "typical_shot_count": "300-600个镜头",
        "pacing": "缓慢、诗意、冥想式"
    }
    
    SHOT_TECHNIQUES = {
        "long_takes": {
            "description": "长镜头美学",
            "techniques": ["固定机位观察", "缓慢横移", "深焦摄影", "自然时间流逝"],
            "examples": ["侯孝贤《悲情城市》", "小津安二郎《东京物语》"]
        },
        "composition": {
            "description": "构图美学",
            "techniques": ["对称构图", "留白艺术", "低角度拍摄", "画框中的画框"],
            "examples": ["韦斯·安德森风格", "王家卫《花样年华》"]
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "文艺片诗意3×3",
        "shots": [
            {"index": 1, "name": "静谧空间", "shot_type": "远景", "prompt": "Serene landscape, minimal composition, natural lighting, contemplative atmosphere, long take style"},
            {"index": 2, "name": "人物剪影", "shot_type": "全景", "prompt": "Figure in environment, silhouette, poetic framing, golden hour lighting, artistic composition"},
            {"index": 3, "name": "日常瞬间", "shot_type": "中全景", "prompt": "Daily life moment, mundane beauty, naturalistic acting, soft focus, intimate distance"},
            {"index": 4, "name": "情绪流动", "shot_type": "中景", "prompt": "Emotional subtlety, restrained performance, ambient light, shallow depth, contemplative mood"},
            {"index": 5, "name": "内心独白", "shot_type": "中近景", "prompt": "Internal monologue moment, pensive expression, window light, quiet intensity, character study"},
            {"index": 6, "name": "细节诗意", "shot_type": "近景", "prompt": "Poetic detail, tactile texture, intimate object, soft lighting, metaphorical imagery"},
            {"index": 7, "name": "时光痕迹", "shot_type": "特写A", "prompt": "Time passage symbol, worn texture, nostalgic object, warm tones, memory trigger"},
            {"index": 8, "name": "眼神深处", "shot_type": "特写B", "prompt": "Soulful eyes, unspoken emotion, window to inner world, soft focus, profound gaze"},
            {"index": 9, "name": "余韵悠长", "shot_type": "远景/空镜", "prompt": "Lingering emptiness, open ending, atmospheric wide shot, ambiguous mood, poetic closure"},
        ]
    }


# 悬疑/惊悚片知识库
class ThrillerFilmKnowledge:
    """悬疑惊悚片知识库"""
    
    CHARACTERISTICS = {
        "name": "悬疑/惊悚片",
        "description": "制造悬念、心理紧张和意外反转",
        "key_elements": ["悬念递进", "心理镜头", "视觉误导", "节奏控制", "意外结局"],
        "typical_duration": "90-130分钟",
        "typical_shot_count": "600-1200个镜头",
        "pacing": "快慢交替，张弛有度"
    }
    
    SHOT_TECHNIQUES = {
        "suspense": {
            "description": "悬念营造",
            "techniques": ["窥视视角", "受限视角", "信息延迟", "交叉剪辑"],
            "examples": ["希区柯克《惊魂记》", "《后窗》"]
        },
        "psychological": {
            "description": "心理镜头",
            "techniques": [" Dutch angle", "扭曲透视", "闪回剪辑", "主观幻觉"],
            "examples": ["《黑天鹅》", "《搏击俱乐部》"]
        }
    }
    
    STORYBOARD_3X3 = {
        "template_name": "悬疑片紧张3×3",
        "shots": [
            {"index": 1, "name": "神秘环境", "shot_type": "大远景", "prompt": "Mysterious location, foggy atmosphere, ominous lighting, establishing unease, desaturated colors"},
            {"index": 2, "name": "异常迹象", "shot_type": "全景", "prompt": "Something is wrong, subtle anomaly, observational camera, building tension, naturalistic style"},
            {"index": 3, "name": "怀疑产生", "shot_type": "中全景", "prompt": "Suspicion forming, character uncertainty, over-shoulder shot, psychological distance, cool tones"},
            {"index": 4, "name": "紧张升级", "shot_type": "中景", "prompt": "Rising tension, quickened pace, handheld camera, breathing room closing, anxiety building"},
            {"index": 5, "name": "危机临近", "shot_type": "中近景", "prompt": "Impending danger, character realization, close observation, dramatic lighting, fear emerging"},
            {"index": 6, "name": "真相逼近", "shot_type": "近景", "prompt": "Truth approaching, discovery moment, intense focus, revelation lighting, pivotal detail"},
            {"index": 7, "name": "关键证据", "shot_type": "特写A", "prompt": "Crucial clue extreme close-up, telling detail, forensic examination, sharp focus, game changer"},
            {"index": 8, "name": "心理冲击", "shot_type": "特写B", "prompt": "Psychological shock, dawning horror, facial extreme close-up, distorted reality, mind breaking"},
            {"index": 9, "name": "悬念延续", "shot_type": "远景", "prompt": "Unanswered questions, lingering mystery, open composition, ambiguous ending, unsettling peace"},
        ]
    }


# 动作片知识库
class ActionFilmKnowledge:
    """动作片知识库"""
    
    CHARACTERISTICS = {
        "name": "动作片",
        "description": "强调视觉冲击、连贯动作和紧张节奏",
        "key_elements": ["快速剪辑", "连贯动作", "视觉冲击", "特技效果", "英雄主义"],
        "typical_duration": "90-140分钟",
        "typical_shot_count": "1000-2500个镜头",
        "pacing": "快节奏，高能量"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "动作片高能3×3",
        "shots": [
            {"index": 1, "name": "场景建立", "shot_type": "远景", "prompt": "Action location wide shot, urban or exotic setting, dramatic lighting, establishing energy, cinematic scope"},
            {"index": 2, "name": "英雄登场", "shot_type": "全景", "prompt": "Hero entrance, dynamic pose, confident stance, heroic lighting, iconic framing"},
            {"index": 3, "name": "对峙形成", "shot_type": "中全景", "prompt": "Confrontation setup, opposing forces, tension building, standoff composition, dramatic angle"},
            {"index": 4, "name": "动作爆发", "shot_type": "中景", "prompt": "Action explosion, combat initiation, dynamic movement, fast-paced editing, impact moment"},
            {"index": 5, "name": "关键打击", "shot_type": "中近景", "prompt": "Critical hit moment, impact frame, dramatic timing, slow motion potential, decisive action"},
            {"index": 6, "name": "武器/道具", "shot_type": "近景", "prompt": "Weapon detail, tool of action, mechanical beauty, functional close-up, gear porn"},
            {"index": 7, "name": "伤害特写", "shot_type": "特写A", "prompt": "Damage extreme close-up, wound or impact, gritty detail, practical effects, visceral reality"},
            {"index": 8, "name": "决心眼神", "shot_type": "特写B", "prompt": "Determined eyes, unwavering resolve, intense focus, heroic close-up, willpower display"},
            {"index": 9, "name": "胜利姿态", "shot_type": "远景", "prompt": "Victory stance, aftermath wide shot, triumphant composition, atmospheric lighting, heroic silhouette"},
        ]
    }


# 爱情片知识库
class RomanceFilmKnowledge:
    """爱情片知识库"""
    
    CHARACTERISTICS = {
        "name": "爱情片",
        "description": "展现爱情的美好、挣扎与成长",
        "key_elements": ["情绪递进", "眼神交流", "浪漫构图", "柔和光线", "情感共鸣"],
        "typical_duration": "90-130分钟",
        "typical_shot_count": "400-800个镜头",
        "pacing": "温柔流畅，情绪起伏"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "爱情片浪漫3×3",
        "shots": [
            {"index": 1, "name": "浪漫场景", "shot_type": "远景", "prompt": "Romantic location wide shot, beautiful scenery, golden hour, dreamy atmosphere, love story setting"},
            {"index": 2, "name": "初次相遇", "shot_type": "全景", "prompt": "First meeting moment, fateful encounter, wide framing, chemistry building, romantic potential"},
            {"index": 3, "name": "关系萌芽", "shot_type": "中全景", "prompt": "Budding relationship, growing connection, two-shot composition, comfortable distance, sweet interaction"},
            {"index": 4, "name": "情感交流", "shot_type": "中景", "prompt": "Emotional exchange, meaningful conversation, over-shoulder shots, intimate space, growing bond"},
            {"index": 5, "name": "心动瞬间", "shot_type": "中近景", "prompt": "Heart flutter moment, romantic realization, soft focus, tender lighting, emotional peak"},
            {"index": 6, "name": "亲密细节", "shot_type": "近景", "prompt": "Intimate detail, touching hands, loving gesture, soft lighting, tactile romance"},
            {"index": 7, "name": "定情信物", "shot_type": "特写A", "prompt": "Love token extreme close-up, symbolic object, sentimental value, warm tones, love symbol"},
            {"index": 8, "name": "深情凝视", "shot_type": "特写B", "prompt": "Loving gaze, eyes full of emotion, romantic close-up, soft focus, deep connection"},
            {"index": 9, "name": "幸福结局", "shot_type": "远景", "prompt": "Happy ending wide shot, couple together, romantic sunset, hopeful future, love triumphs"},
        ]
    }


# 导出所有知识库
FILM_KNOWLEDGE_BASES = {
    "war": WarFilmKnowledge,
    "art": ArtFilmKnowledge,
    "thriller": ThrillerFilmKnowledge,
    "action": ActionFilmKnowledge,
    "romance": RomanceFilmKnowledge,
}


def get_film_knowledge(film_type: str):
    """获取指定类型的电影知识库"""
    return FILM_KNOWLEDGE_BASES.get(film_type)


def get_film_storyboard(film_type: str, board_type: str = "3x3"):
    """获取指定类型的分镜模板"""
    knowledge = get_film_knowledge(film_type)
    if knowledge:
        return knowledge.STORYBOARD_3X3 if board_type == "3x3" else getattr(knowledge, 'STORYBOARD_4X3', knowledge.STORYBOARD_3X3)
    return None


def list_film_types():
    """列出所有可用的电影类型"""
    return list(FILM_KNOWLEDGE_BASES.keys())


__all__ = [
    'WarFilmKnowledge',
    'ArtFilmKnowledge', 
    'ThrillerFilmKnowledge',
    'ActionFilmKnowledge',
    'RomanceFilmKnowledge',
    'get_film_knowledge',
    'get_film_storyboard',
    'list_film_types',
]
