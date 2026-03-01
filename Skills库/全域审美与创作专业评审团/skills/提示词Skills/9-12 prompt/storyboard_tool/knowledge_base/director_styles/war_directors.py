"""
战争片导演风格知识库
包含斯皮尔伯格、诺兰、雷德利·斯科特等导演的风格特点
"""

from typing import Dict, List, Any


class SpielbergStyle:
    """史蒂文·斯皮尔伯格导演风格"""
    
    INFO = {
        "name": "史蒂文·斯皮尔伯格",
        "name_en": "Steven Spielberg",
        "nationality": "美国",
        "active_period": "1970年代至今",
        "genre": "战争片/科幻片/剧情片",
        "style_keywords": ["写实性叙事", "人文关怀", "视觉奇观", "情感驱动", "主流叙事"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "diagonal_tracking": {
            "name": "斜向跟踪拍摄",
            "description": "侧面跟拍人物移动，前景增加遮挡物增强层次感",
            "example": "《拯救大兵瑞恩》中士兵穿越战场的镜头",
            "application": "动作场景、人物移动"
        },
        "character_intro": {
            "name": "主角介绍手法",
            "description": "通过动作或身体局部特写介绍主角，而非直接面部特写",
            "example": "《夺宝奇兵》印第安纳·琼斯的经典登场",
            "application": "人物首次登场"
        },
        "emotional_long_take": {
            "name": "情感长镜头",
            "description": "不规则的情感驱动长镜头，而非技术性展示",
            "example": "《辛德勒的名单》中的大屠杀场景",
            "application": "情感高潮、重要转折"
        },
        "over_shoulder_claustrophobia": {
            "name": "幽闭过肩镜头",
            "description": "广角镜头拍摄过肩镜头，创造幽闭恐惧感",
            "example": "《大白鲨》中的对话场景",
            "application": "紧张对话、心理压迫"
        },
        "picture_in_picture": {
            "name": "画中画效果",
            "description": "利用镜子、窗户、门、电线分割画面",
            "example": "《人工智能》中的多个场景",
            "application": "复杂构图、多重信息"
        }
    }
    
    REPRESENTATIVE_WORKS = [
        {
            "title": "拯救大兵瑞恩",
            "year": 1998,
            "techniques": ["手持摄影", "desaturated色调", "快速剪辑", "写实风格"],
            "notable_scenes": ["诺曼底登陆开场", "狙击手对决", "最后的桥战"]
        },
        {
            "title": "辛德勒的名单",
            "year": 1993,
            "techniques": ["黑白摄影", "红衣女孩", "长镜头", "纪实风格"],
            "notable_scenes": ["大屠杀清洗", "名单宣读", "告别场景"]
        },
        {
            "title": "夺宝奇兵",
            "year": 1981,
            "techniques": ["经典冒险叙事", "动作喜剧", "视觉奇观"],
            "notable_scenes": ["巨石追逐", "开场的黄金雕像"]
        }
    ]
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": "desaturated色调，高对比度，纪实感",
        "lighting": "自然光与戏剧光结合，强调真实感",
        "composition": "经典好莱坞构图，重视画面层次",
        "camera_movement": "流畅的摄影机运动，情感驱动的运镜",
        "lens_preference": "标准镜头到长焦，根据场景灵活选择"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "style": "精细的手绘分镜，几乎每个镜头都预先设计",
        "detail_level": "高度详细，包含具体机位和运镜",
        "color_usage": "有时使用颜色标注情绪和光线",
        "annotation": "详细的动作和情绪说明"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "斯皮尔伯格风格3×3",
        "description": "写实主义与人文关怀并重的叙事风格",
        "shots": [
            {
                "index": 1,
                "name": "史诗建立",
                "shot_type": "大远景",
                "technique": "斜向跟踪+前景遮挡",
                "prompt": "Epic establishing shot with diagonal tracking, foreground elements creating depth, desaturated colors, documentary feel, Spielberg style, cinematic wide shot"
            },
            {
                "index": 2,
                "name": "主角登场",
                "shot_type": "全景",
                "technique": "动作或局部特写介绍",
                "prompt": "Character introduction through action, partial body shot, heroic lighting, iconic framing, Spielberg character entrance, dramatic composition"
            },
            {
                "index": 3,
                "name": "关系建立",
                "shot_type": "中全景",
                "technique": "过肩镜头",
                "prompt": "Over-shoulder two-shot, relationship dynamics, natural lighting, human connection, Spielberg dialogue framing, warm tones"
            },
            {
                "index": 4,
                "name": "动作场景",
                "shot_type": "中景",
                "technique": "手持摄影+流畅切换",
                "prompt": "Action sequence, handheld camera with smooth transitions, realistic movement, desaturated colors, gritty texture, Spielberg war scene"
            },
            {
                "index": 5,
                "name": "情感高潮",
                "shot_type": "中近景",
                "technique": "情感长镜头",
                "prompt": "Emotional close-up, long take, intense feeling, dramatic lighting, shallow depth of field, Spielberg emotional peak, humanistic focus"
            },
            {
                "index": 6,
                "name": "细节特写",
                "shot_type": "近景",
                "technique": "重要道具或动作",
                "prompt": "Important detail close-up, symbolic object, soft focus background, emotional weight, Spielberg detail shot, tactile texture"
            },
            {
                "index": 7,
                "name": "象征元素",
                "shot_type": "特写A",
                "technique": "画中画构图",
                "prompt": "Symbolic element, picture-in-picture composition, mirror or window frame, emotional resonance, Spielberg symbolism, layered framing"
            },
            {
                "index": 8,
                "name": "眼神特写",
                "shot_type": "特写B",
                "technique": "情感眼神",
                "prompt": "Emotional eyes extreme close-up, soulful gaze, dramatic lighting, reflection visible, Spielberg eye close-up, profound emotion"
            },
            {
                "index": 9,
                "name": "史诗收尾",
                "shot_type": "远景",
                "technique": "情感升华",
                "prompt": "Epic conclusion wide shot, emotional elevation, atmospheric lighting, lasting impression, Spielberg ending, hopeful yet somber"
            }
        ]
    }


class NolanStyle:
    """克里斯托弗·诺兰导演风格"""
    
    INFO = {
        "name": "克里斯托弗·诺兰",
        "name_en": "Christopher Nolan",
        "nationality": "英国/美国",
        "active_period": "1990年代至今",
        "genre": "科幻/悬疑/战争",
        "style_keywords": ["非线性叙事", "时间解构", "现实主义", "IMAX实拍", "极简对白"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "nonlinear_narrative": {
            "name": "非线性叙事",
            "description": "碎片化叙事，打破时间顺序",
            "example": "《记忆碎片》的倒叙结构",
            "application": "悬疑、心理题材"
        },
        "parallel_timelines": {
            "name": "平行时间线",
            "description": "多条时间线并行，最终交汇",
            "example": "《敦刻尔克》海陆空三线叙事",
            "application": "史诗、多视角叙事"
        },
        "imax_film": {
            "name": "IMAX胶片实拍",
            "description": "坚持使用IMAX胶片摄影机，追求真实质感",
            "example": "《星际穿越》《敦刻尔克》",
            "application": "视觉奇观场景"
        },
        "minimal_dialogue": {
            "name": "极简对白",
            "description": "用视觉而非对白推动叙事",
            "example": "《敦刻尔克》大量无对白场景",
            "application": "紧张、沉浸式场景"
        },
        "practical_effects": {
            "name": "实景特效",
            "description": "尽可能使用实景拍摄而非CGI",
            "example": "《盗梦空间》的旋转走廊",
            "application": "动作、科幻场景"
        }
    }
    
    REPRESENTATIVE_WORKS = [
        {
            "title": "记忆碎片",
            "year": 2000,
            "techniques": ["倒叙结构", "黑白彩色交替", "碎片化叙事"],
            "notable_scenes": ["开场倒放", "纹身场景", "真相揭示"]
        },
        {
            "title": "盗梦空间",
            "year": 2010,
            "techniques": ["多层梦境", "时间膨胀", "旋转走廊实拍"],
            "notable_scenes": ["巴黎折叠", "旋转走廊打斗", "梦境坠落"]
        },
        {
            "title": "敦刻尔克",
            "year": 2017,
            "techniques": ["三线叙事", "IMAX实拍", "极简对白", "时间错位"],
            "notable_scenes": ["海滩全景", "空中狗斗", "沉船场景"]
        }
    ]
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": "冷色调，高对比，胶片质感",
        "lighting": "高对比度照明，强调戏剧性",
        "composition": "宏大构图，IMAX画幅优势",
        "camera_movement": "实拍感强的摄影机运动",
        "lens_preference": "IMAX胶片，大画幅"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "style": "复杂的时间线分镜表，多线并行",
        "detail_level": "精确的时间计算和同步",
        "color_usage": "用颜色区分不同时间线",
        "annotation": "详细的时间标记和逻辑说明"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "诺兰风格3×3",
        "description": "非线性叙事与时间解构的视觉迷宫",
        "shots": [
            {
                "index": 1,
                "name": "时间建立",
                "shot_type": "大远景",
                "technique": "宏大场景+时间标记",
                "prompt": "Epic wide shot with temporal markers, IMAX quality, desaturated colors, Nolan style, time-space establishment, cinematic scope"
            },
            {
                "index": 2,
                "name": "主角状态",
                "shot_type": "全景",
                "technique": "孤立感构图",
                "prompt": "Protagonist full shot, isolated composition, dramatic lighting, high contrast, Nolan character introduction, mysterious atmosphere"
            },
            {
                "index": 3,
                "name": "线索呈现",
                "shot_type": "中全景",
                "technique": "信息密度高",
                "prompt": "Clue presentation shot, high information density, sharp focus, Nolan puzzle element, precise composition"
            },
            {
                "index": 4,
                "name": "时间跳跃",
                "shot_type": "中景",
                "technique": "视觉转场",
                "prompt": "Time jump transition, visual continuity, match cut, Nolan temporal shift, disorienting yet logical"
            },
            {
                "index": 5,
                "name": "真相逼近",
                "shot_type": "中近景",
                "technique": "情绪积累",
                "prompt": "Truth approaching close-up, intense focus, dramatic revelation lighting, Nolan climax moment, psychological depth"
            },
            {
                "index": 6,
                "name": "关键道具",
                "shot_type": "近景",
                "technique": "象征物特写",
                "prompt": "Key object close-up, symbolic meaning, sharp detail, Nolan MacGuffin, practical prop"
            },
            {
                "index": 7,
                "name": "时间线索",
                "shot_type": "特写A",
                "technique": "时间标记特写",
                "prompt": "Time marker extreme close-up, watch or clock, ticking sound implied, Nolan time obsession, precise detail"
            },
            {
                "index": 8,
                "name": "顿悟瞬间",
                "shot_type": "特写B",
                "technique": "眼神变化",
                "prompt": "Realization moment, eyes extreme close-up, dawning comprehension, Nolan revelation, dramatic lighting"
            },
            {
                "index": 9,
                "name": "时间收束",
                "shot_type": "远景",
                "technique": "多线交汇",
                "prompt": "Convergence wide shot, multiple timelines meeting, epic composition, Nolan ending, time-space resolution"
            }
        ]
    }


class RidleyScottStyle:
    """雷德利·斯科特导演风格"""
    
    INFO = {
        "name": "雷德利·斯科特",
        "name_en": "Ridley Scott",
        "nationality": "英国",
        "active_period": "1970年代至今",
        "genre": "科幻/史诗/惊悚",
        "style_keywords": ["科幻美学", "宏大场面", "细节丰富", "未来主义", "视觉奇观"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "claustrophobic_space": {
            "name": "封闭空间氛围",
            "description": "在封闭空间营造压抑氛围",
            "example": "《异形》的太空船场景",
            "application": "科幻恐怖"
        },
        "ensemble_blocking": {
            "name": "群戏调度",
            "description": "复杂的群戏场面调度",
            "example": "《角斗士》的竞技场场景",
            "application": "史诗场面"
        },
        "futuristic_design": {
            "name": "未来主义设计",
            "description": "独特的科幻视觉设计",
            "example": "《银翼杀手》的赛博朋克城市",
            "application": "科幻场景"
        },
        "visual_world_building": {
            "name": "视觉世界构建",
            "description": "通过细节构建完整的世界观",
            "example": "《普罗米修斯》的外星世界",
            "application": "科幻、史诗"
        }
    }
    
    REPRESENTATIVE_WORKS = [
        {
            "title": "异形",
            "year": 1979,
            "techniques": ["封闭空间", "生物机械设计", "缓慢积累恐惧"],
            "notable_scenes": ["破胸场景", "通风管道", "太空船走廊"]
        },
        {
            "title": "银翼杀手",
            "year": 1982,
            "techniques": ["赛博朋克美学", "霓虹灯光", "未来城市"],
            "notable_scenes": ["开场城市", "泰瑞公司", "雨中独白"]
        },
        {
            "title": "角斗士",
            "year": 2000,
            "techniques": ["史诗场面", "古罗马重现", "动作设计"],
            "notable_scenes": ["开场战役", "竞技场战斗", "麦田结尾"]
        }
    ]
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": "冷峻、金属质感、未来感",
        "lighting": "戏剧化照明，强调质感",
        "composition": "宏大构图，细节丰富",
        "camera_movement": "稳定而流畅的运镜",
        "lens_preference": "广角到标准镜头"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "style": "详细的场景设计，重视美术",
        "detail_level": "丰富的环境细节",
        "color_usage": "概念艺术风格",
        "annotation": "大量美术指导说明"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "雷德利·斯科特风格3×3",
        "description": "科幻美学与宏大场面的视觉盛宴",
        "shots": [
            {
                "index": 1,
                "name": "世界建立",
                "shot_type": "大远景",
                "technique": "宏大世界观",
                "prompt": "Epic world-building wide shot, futuristic or ancient setting, atmospheric haze, Ridley Scott style, detailed environment, cinematic scope"
            },
            {
                "index": 2,
                "name": "环境细节",
                "shot_type": "全景",
                "technique": "丰富细节",
                "prompt": "Environment detail shot, rich textures, production design excellence, Ridley Scott production value, immersive setting"
            },
            {
                "index": 3,
                "name": "人物融入",
                "shot_type": "中全景",
                "technique": "人物与环境关系",
                "prompt": "Character in environment, scale relationship, atmospheric lighting, Ridley Scott composition, sci-fi or epic costume"
            },
            {
                "index": 4,
                "name": "紧张场景",
                "shot_type": "中景",
                "technique": "封闭空间",
                "prompt": "Tense scene, confined space, atmospheric lighting, Ridley Scott tension, detailed production design, claustrophobic feel"
            },
            {
                "index": 5,
                "name": "关键揭示",
                "shot_type": "中近景",
                "technique": "戏剧化照明",
                "prompt": "Key revelation close-up, dramatic lighting, high contrast, Ridley Scott dramatic moment, intense expression"
            },
            {
                "index": 6,
                "name": "技术细节",
                "shot_type": "近景",
                "technique": "未来科技或古代工艺",
                "prompt": "Technology or craft detail, futuristic or ancient, intricate design, Ridley Scott detail shot, tactile quality"
            },
            {
                "index": 7,
                "name": "威胁元素",
                "shot_type": "特写A",
                "technique": "恐怖或威胁特写",
                "prompt": "Threat element extreme close-up, alien or danger, sharp detail, Ridley Scott horror, visceral impact"
            },
            {
                "index": 8,
                "name": "决心眼神",
                "shot_type": "特写B",
                "technique": "人物决心",
                "prompt": "Determined eyes close-up, survival instinct, dramatic lighting, Ridley Scott protagonist, intense gaze"
            },
            {
                "index": 9,
                "name": "史诗收尾",
                "shot_type": "远景",
                "technique": "宏大结局",
                "prompt": "Epic conclusion wide shot, vast landscape, atmospheric ending, Ridley Scott finale, haunting beauty"
            }
        ]
    }


# 导出所有战争片导演风格
WAR_DIRECTORS = {
    "spielberg": SpielbergStyle,
    "nolan": NolanStyle,
    "ridley_scott": RidleyScottStyle
}


def get_war_director_style(director_name: str):
    """获取战争片导演风格"""
    return WAR_DIRECTORS.get(director_name)


def list_war_directors():
    """列出所有战争片导演"""
    return list(WAR_DIRECTORS.keys())


if __name__ == "__main__":
    print("=== 战争片导演风格 ===")
    for key, director in WAR_DIRECTORS.items():
        print(f"\n{director.INFO['name']} ({director.INFO['name_en']})")
        print(f"  风格关键词: {', '.join(director.INFO['style_keywords'])}")
