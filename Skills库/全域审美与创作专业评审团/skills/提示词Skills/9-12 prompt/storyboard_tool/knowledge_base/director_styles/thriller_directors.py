"""
悬疑片导演风格库
包含：希区柯克、大卫·芬奇、奉俊昊
"""


class HitchcockStyle:
    """希区柯克风格 - 悬疑大师的心理游戏"""
    
    INFO = {
        "name": "阿尔弗雷德·希区柯克",
        "name_en": "Alfred Hitchcock",
        "nationality": "英国/美国",
        "active_period": "1922-1976",
        "genre": "悬疑片/惊悚片/剧情片",
        "style_keywords": ["麦格芬", "悬念", "心理恐惧", "视觉隐喻", "控制狂美学"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "macguffin": {
            "name": "麦格芬手法",
            "description": "推动剧情发展的神秘物件或目标，本身并不重要",
            "example": "《西北偏北》中的微缩胶卷",
            "application": "剧情驱动、悬念设置"
        },
        "suspense_vs_surprise": {
            "name": "悬念vs惊吓",
            "description": "让观众知道危险而角色不知道，制造紧张感",
            "example": "《夺魂索》中的尸体藏在餐桌",
            "application": "惊悚场景、观众操控"
        },
        "point_of_view": {
            "name": "主观视角",
            "description": "通过角色的眼睛看世界，增强代入感",
            "example": "《后窗》中透过窗户的观察",
            "application": "偷窥场景、心理描写"
        },
        "dolly_zoom": {
            "name": "推拉变焦",
            "description": "镜头推进同时变焦拉出，背景变形而主体不变",
            "example": "《迷魂记》中的眩晕镜头",
            "application": "心理震撼、眩晕感"
        },
        "cameo_appearance": {
            "name": "导演客串",
            "description": "在每部电影中客串小角色",
            "example": "几乎所有希区柯克电影",
            "application": "导演签名、彩蛋"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "psycho": {
            "title": "惊魂记",
            "year": 1960,
            "visual_traits": ["黑白摄影", "淋浴场景", "心理惊悚", "哥特式阴影"],
            "key_shots": ["淋浴谋杀", "贝茨旅馆", "骷髅 reveal", "楼梯场景"]
        },
        "vertigo": {
            "title": "迷魂记",
            "year": 1958,
            "visual_traits": ["推拉变焦", "螺旋意象", "迷幻色彩", "绿色调"],
            "key_shots": ["钟楼坠落", "螺旋动画", "变身场景", "追逐戏"]
        },
        "rear_window": {
            "title": "后窗",
            "year": 1954,
            "visual_traits": ["单一场景", "主观视角", "窥视主题", "暖色调"],
            "key_shots": ["窗口观察", "对面公寓", "黑暗中的手", "闪光灯结局"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["黑白", "深红", "墨绿", "金色", "暗棕"],
        "lighting_style": "高对比度黑白，强烈的明暗对比",
        "composition": "几何构图，螺旋元素，对称与不对称的对比",
        "camera_movement": "精确控制，流畅移动，主观视角",
        "editing_rhythm": "蒙太奇剪辑，交叉剪辑，节奏控制"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["特写", "主观视角", "俯拍"],
        "frame_rate": "正常",
        "color_grading": "高对比黑白，或高饱和色彩",
        "typical_mood": "紧张、不安、悬疑、心理压迫"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "希区柯克风格3×3",
        "description": "心理悬疑与视觉控制的经典范式",
        "shots": [
            {
                "index": 1,
                "name": "悬念建立",
                "shot_type": "全景",
                "technique": "信息展示",
                "prompt": "Wide establishing shot revealing important information, dramatic shadows, suspenseful atmosphere, Hitchcock style, high contrast lighting, ominous mood"
            },
            {
                "index": 2,
                "name": "主观视角",
                "shot_type": "POV",
                "technique": "角色视角",
                "prompt": "Point of view shot through window or doorway, voyeuristic framing, shallow depth of field, Hitchcock subjective camera, mysterious atmosphere"
            },
            {
                "index": 3,
                "name": "心理特写",
                "shot_type": "极端特写",
                "technique": "情绪放大",
                "prompt": "Extreme close-up of eyes or hands, psychological tension, dramatic lighting, Hitchcock intense moment, fear and anxiety"
            },
            {
                "index": 4,
                "name": "楼梯悬疑",
                "shot_type": "俯拍/仰拍",
                "technique": "角度压迫",
                "prompt": "Staircase shot from above or below, dramatic angle, spiral composition, Hitchcock geometric framing, impending danger"
            },
            {
                "index": 5,
                "name": "推拉变焦",
                "shot_type": "变焦特写",
                "technique": "dolly zoom",
                "prompt": "Dolly zoom effect, background stretching while subject stays same size, psychological disorientation, Hitchcock vertigo shot, dramatic moment"
            },
            {
                "index": 6,
                "name": "阴影威胁",
                "shot_type": "剪影",
                "technique": "光影对比",
                "prompt": "Silhouette against wall or door, dramatic shadow, threatening presence, Hitchcock noir lighting, suspense building"
            },
            {
                "index": 7,
                "name": "镜像分裂",
                "shot_type": "镜像构图",
                "technique": "反射心理",
                "prompt": "Mirror reflection shot, character and reflection showing different emotions, psychological split, Hitchcock doppelganger theme"
            },
            {
                "index": 8,
                "name": "麦格芬揭示",
                "shot_type": "特写",
                "technique": "物件聚焦",
                "prompt": "Close-up of mysterious object, shallow depth of field, dramatic lighting on MacGuffin, Hitchcock plot device, intrigue and mystery"
            },
            {
                "index": 9,
                "name": "悬念高潮",
                "shot_type": "快速剪辑",
                "technique": "蒙太奇",
                "prompt": "Rapid montage of faces, objects, and actions, cross-cutting between danger and victim, Hitchcock climax editing, maximum tension"
            }
        ]
    }


class FincherStyle:
    """大卫·芬奇风格 - 黑暗美学的完美主义者"""
    
    INFO = {
        "name": "大卫·芬奇",
        "name_en": "David Fincher",
        "nationality": "美国",
        "active_period": "1980年代至今",
        "genre": "悬疑片/惊悚片/犯罪片",
        "style_keywords": ["黑暗色调", "完美主义", "社会批判", "技术控", "心理深度"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "low_key_lighting": {
            "name": "低键照明",
            "description": "大量使用阴影和暗部，低照度场景",
            "example": "《七宗罪》的几乎所有场景",
            "application": "犯罪场景、心理描写"
        },
        "fluid_camera": {
            "name": "流畅摄影机运动",
            "description": "精确的摄影机运动，常使用Motion Control",
            "example": "《搏击俱乐部》的开场大脑之旅",
            "application": "片头、转场、心理场景"
        },
        "desaturated_palette": {
            "name": "去饱和色调",
            "description": "降低饱和度，偏向青绿色和黄色",
            "example": "《社交网络》的色调处理",
            "application": "整体视觉风格"
        },
        "invisible_editing": {
            "name": "隐形剪辑",
            "description": "流畅的剪辑让观众意识不到剪辑点",
            "example": "《本杰明·巴顿奇事》的衰老过程",
            "application": "时间流逝、连续场景"
        },
        "toxic_masculinity": {
            "name": "有毒男性气质",
            "description": "探讨男性身份危机和暴力",
            "example": "《搏击俱乐部》《消失的爱人》",
            "application": "主题表达、角色塑造"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "seven": {
            "title": "七宗罪",
            "year": 1995,
            "visual_traits": ["雨景", "黑暗", "潮湿", "城市地狱", "低键照明"],
            "key_shots": ["开场字幕", "犯罪现场", "图书馆", "沙漠结局"]
        },
        "fight_club": {
            "title": "搏击俱乐部",
            "year": 1999,
            "visual_traits": ["肮脏美学", "绿色调", "快速剪辑", "心理分裂"],
            "key_shots": ["大脑之旅开场", "搏击场景", " IKEA 公寓", "爆炸结局"]
        },
        "gone_girl": {
            "title": "消失的爱人",
            "year": 2014,
            "visual_traits": ["冷色调", "媒体批判", "双重叙事", "郊区恐怖"],
            "key_shots": ["日记闪回", "媒体发布会", "厨房场景", "回归场景"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["青绿色", "琥珀黄", "深灰", "黑色", "暗棕"],
        "lighting_style": "低键照明，高对比，偏向暗部",
        "composition": "精确构图，几何线条，中心对称",
        "camera_movement": "流畅精确，Motion Control，复杂运动",
        "editing_rhythm": "隐形剪辑，节奏控制，心理时间"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["特写", "低角度", "俯拍"],
        "frame_rate": "正常，偶尔变速",
        "color_grading": "去饱和，青绿/琥珀分离",
        "typical_mood": "黑暗、压抑、不安、精密"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "大卫·芬奇风格3×3",
        "description": "黑暗色调与完美主义的技术美学",
        "shots": [
            {
                "index": 1,
                "name": "雨夜城市",
                "shot_type": "大远景",
                "technique": "低键照明",
                "prompt": "Rainy cityscape at night, low-key lighting, desaturated teal and amber, wet streets reflecting neon, David Fincher atmospheric opening, cinematic wide shot"
            },
            {
                "index": 2,
                "name": "犯罪现场",
                "shot_type": "俯拍",
                "technique": "精确构图",
                "prompt": "Overhead shot of crime scene, geometric composition, desaturated colors, forensic detail, David Fincher precise framing, dark and moody"
            },
            {
                "index": 3,
                "name": "心理特写",
                "shot_type": "极端特写",
                "technique": "暗部细节",
                "prompt": "Extreme close-up in near darkness, half face illuminated, desaturated skin tones, psychological intensity, David Fincher intimate moment, high contrast"
            },
            {
                "index": 4,
                "name": "流畅运动",
                "shot_type": "运动长镜",
                "technique": "Motion Control",
                "prompt": "Fluid camera movement through space, motion control precision, complex path, David Fincher technical shot, seamless transition"
            },
            {
                "index": 5,
                "name": "低角度威胁",
                "shot_type": "低角度",
                "technique": "角度压迫",
                "prompt": "Low angle shot looking up at figure, imposing presence, dark silhouette against dim light, David Fincher power dynamic, threatening atmosphere"
            },
            {
                "index": 6,
                "name": "办公室夜景",
                "shot_type": "内景",
                "technique": "百叶窗光影",
                "prompt": "Office interior at night, venetian blind shadows, computer screen glow, desaturated palette, David Fincher workplace scene, isolated atmosphere"
            },
            {
                "index": 7,
                "name": "发现瞬间",
                "shot_type": "反应特写",
                "technique": "情绪控制",
                "prompt": "Close-up of discovery moment, controlled emotional reaction, subtle lighting change, David Fincher revelation scene, restrained performance"
            },
            {
                "index": 8,
                "name": "走廊纵深",
                "shot_type": "纵深构图",
                "technique": "单点透视",
                "prompt": "Corridor with single point perspective, figure at far end, fluorescent lighting, David Fincher architectural shot, institutional atmosphere"
            },
            {
                "index": 9,
                "name": "结局定格",
                "shot_type": "定格",
                "technique": "开放式",
                "prompt": "Final shot holding on ambiguous expression, slow fade, desaturated colors, David Fincher ending, unresolved tension, lingering question"
            }
        ]
    }


class BongJoonHoStyle:
    """奉俊昊风格 - 类型融合的社会寓言"""
    
    INFO = {
        "name": "奉俊昊",
        "name_en": "Bong Joon-ho",
        "nationality": "韩国",
        "active_period": "1990年代至今",
        "genre": "悬疑片/惊悚片/社会讽刺片",
        "style_keywords": ["类型融合", "社会阶级", "黑色幽默", "完美主义", "道德模糊"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "genre_mixing": {
            "name": "类型融合",
            "description": "将多种类型元素无缝融合",
            "example": "《寄生虫》融合喜剧、惊悚、悲剧",
            "application": "整体叙事策略"
        },
        "vertical_composition": {
            "name": "垂直构图",
            "description": "利用上下空间表现阶级差异",
            "example": "《寄生虫》的半地下室vs豪宅",
            "application": "阶级主题、空间隐喻"
        },
        "tone_shift": {
            "name": "情绪急转",
            "description": "从喜剧突然转为恐怖或悲剧",
            "example": "《寄生虫》的生日派对场景",
            "application": "戏剧转折、观众操控"
        },
        "precise_storyboarding": {
            "name": "精确分镜",
            "description": "每个镜头都精确绘制，极少即兴",
            "example": "《杀人回忆》的田野场景",
            "application": "所有场景"
        },
        "social_commentary": {
            "name": "社会批判",
            "description": "通过类型片包装社会议题",
            "example": "《雪国列车》的阶级寓言",
            "application": "主题表达"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "parasite": {
            "title": "寄生虫",
            "year": 2019,
            "visual_traits": ["垂直空间", "现代建筑", "暴雨", "阶级对比"],
            "key_shots": ["半地下室", "豪宅全景", "楼梯上下", "草坪派对", "地下室 reveal"]
        },
        "memories_of_murder": {
            "title": "杀人回忆",
            "year": 2003,
            "visual_traits": ["田野", "雨夜", "1980年代", "压抑色调"],
            "key_shots": ["隧道场景", "田野搜索", "火车经过", "最后凝视"]
        },
        "mother": {
            "title": "母亲",
            "year": 2009,
            "visual_traits": ["小城镇", "草药", "舞蹈", "心理扭曲"],
            "key_shots": ["田野舞蹈", "针灸场景", "阁楼发现", "公交车舞蹈"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["大地色", "深绿", "暗褐", "灰蓝", "雨色"],
        "lighting_style": "自然主义，根据场景需要变化",
        "composition": "精确构图，垂直线条，空间分层",
        "camera_movement": "流畅运动，根据情绪调整",
        "editing_rhythm": "类型决定节奏，喜剧快，惊悚慢"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["全景", "垂直构图", "群像"],
        "frame_rate": "正常",
        "color_grading": "根据类型变化，从暖到冷",
        "typical_mood": "讽刺、紧张、荒诞、悲剧"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "奉俊昊风格3×3",
        "description": "类型融合与社会批判的精准叙事",
        "shots": [
            {
                "index": 1,
                "name": "空间对比",
                "shot_type": "分屏/对比",
                "technique": "上下空间",
                "prompt": "Split composition showing upper and lower spaces, vertical class divide, modern architecture vs cramped space, Bong Joon-ho social commentary, sharp contrast"
            },
            {
                "index": 2,
                "name": "家庭群像",
                "shot_type": "全景",
                "technique": "精确调度",
                "prompt": "Wide shot of family in interior, precise blocking, domestic setting, Bong Joon-ho ensemble composition, subtle tension beneath surface"
            },
            {
                "index": 3,
                "name": "楼梯隐喻",
                "shot_type": "纵深",
                "technique": "垂直运动",
                "prompt": "Staircase shot connecting different levels, characters moving between classes, Bong Joon-ho vertical metaphor, architectural storytelling"
            },
            {
                "index": 4,
                "name": "喜剧时刻",
                "shot_type": "中景",
                "technique": "幽默调度",
                "prompt": "Medium shot with comedic timing, characters in absurd situation, natural lighting, Bong Joon-ho dark humor, everyday setting"
            },
            {
                "index": 5,
                "name": "情绪急转",
                "shot_type": "特写",
                "technique": "瞬间转变",
                "prompt": "Close-up capturing sudden tone shift, expression changing from comedy to horror, Bong Joon-ho genre transition, dramatic lighting change"
            },
            {
                "index": 6,
                "name": "雨夜戏剧",
                "shot_type": "夜景",
                "technique": "暴雨氛围",
                "prompt": "Night scene with heavy rain, dramatic weather, characters in crisis, Bong Joon-ho atmospheric moment, water and reflection"
            },
            {
                "index": 7,
                "name": "发现场景",
                "shot_type": "揭示镜头",
                "technique": "信息揭露",
                "prompt": "Revelation shot discovering hidden truth, camera movement revealing secret, Bong Joon-ho plot twist, precise framing"
            },
            {
                "index": 8,
                "name": "社会全景",
                "shot_type": "大远景",
                "technique": "环境人物",
                "prompt": "Wide environmental shot showing society, tiny figures in landscape, Bong Joon-ho social observation, natural setting with human presence"
            },
            {
                "index": 9,
                "name": "道德困境",
                "shot_type": "双人",
                "technique": "对峙构图",
                "prompt": "Two shot with moral confrontation, ambiguous lighting, unresolved tension, Bong Joon-ho ethical dilemma, open ending composition"
            }
        ]
    }


# 导出
THRILLER_DIRECTORS = {
    "hitchcock": HitchcockStyle,
    "fincher": FincherStyle,
    "bong_joon_ho": BongJoonHoStyle
}


def get_thriller_director_style(director_name: str):
    """获取悬疑片导演风格"""
    return THRILLER_DIRECTORS.get(director_name)


def list_thriller_directors():
    """列出所有悬疑片导演"""
    return list(THRILLER_DIRECTORS.keys())
