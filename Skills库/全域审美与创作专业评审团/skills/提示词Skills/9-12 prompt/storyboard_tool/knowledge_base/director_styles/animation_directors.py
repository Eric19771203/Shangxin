"""
动画导演风格库
包含：宫崎骏、新海诚、蒂姆·伯顿
"""


class MiyazakiStyle:
    """宫崎骏风格 - 手绘自然的诗意幻想"""
    
    INFO = {
        "name": "宫崎骏",
        "name_en": "Hayao Miyazaki",
        "nationality": "日本",
        "active_period": "1963年至今",
        "genre": "动画/奇幻/冒险",
        "style_keywords": ["手绘自然", "飞行主题", "环保意识", "少女成长", "无明确反派"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "hand_drawn_nature": {
            "name": "手绘自然",
            "description": "精细手绘的自然景观，强调有机质感",
            "example": "《龙猫》中的森林和农田",
            "application": "环境描绘、氛围营造"
        },
        "flying_sequences": {
            "name": "飞行场景",
            "description": "角色飞行或漂浮，象征自由与梦想",
            "example": "《天空之城》《千与千寻》中的飞行",
            "application": "情感高潮、幻想场景"
        },
        "food_animation": {
            "name": "食物描绘",
            "description": "详细描绘食物的制作和享用过程",
            "example": "《千与千寻》中的食物场景",
            "application": "生活细节、文化展示"
        },
        "ma": {
            "name": "间（留白）",
            "description": "日本美学中的留白和静谧时刻",
            "example": "《龙猫》中等待猫巴士的场景",
            "application": "节奏控制、情感沉淀"
        },
        "no_clear_villain": {
            "name": "无明确反派",
            "description": "冲突来自情境而非邪恶角色",
            "example": "《幽灵公主》中的多方立场",
            "application": "主题深度、道德复杂性"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "spirited_away": {
            "title": "千与千寻",
            "year": 2001,
            "visual_traits": ["神怪世界", "浴场场景", "食物细节", "水彩质感"],
            "key_shots": ["隧道入口", "无脸男", "海上列车", "猪父母"]
        },
        "my_neighbor_totoro": {
            "title": "龙猫",
            "year": 1988,
            "visual_traits": ["乡村风景", "雨景", "自然细节", "温暖色调"],
            "key_shots": ["雨中等车", "猫巴士", "橡果子", "农田全景"]
        },
        "princess_mononoke": {
            "title": "幽灵公主",
            "year": 1997,
            "visual_traits": ["森林神怪", "古代日本", "战争场面", "生态主题"],
            "key_shots": ["麒麟兽", "铁工厂", "森林全景", "最终和解"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["自然绿", "天空蓝", "温暖黄", "大地棕", "水彩质感"],
        "lighting_style": "自然光，柔和阴影，水彩效果",
        "composition": "开阔空间，自然元素，有机线条",
        "camera_movement": "流畅飞行感，缓慢横移，跟随角色",
        "editing_rhythm": "舒缓节奏，留白时刻，情感停顿"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["全景", "飞行镜头", "自然细节"],
        "frame_rate": "传统手绘动画",
        "color_grading": "水彩质感，自然色调",
        "typical_mood": "温暖、梦幻、怀旧、治愈"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "宫崎骏风格3×3",
        "description": "手绘自然与飞行梦想的温暖幻想",
        "shots": [
            {
                "index": 1,
                "name": "自然全景",
                "shot_type": "大远景",
                "technique": "手绘风景",
                "prompt": "Hand-painted landscape, lush green nature, soft watercolor style, Studio Ghibli aesthetic, peaceful rural scene, Miyazaki nature worship, detailed vegetation"
            },
            {
                "index": 2,
                "name": "飞行场景",
                "shot_type": "动态镜头",
                "technique": "飞行跟随",
                "prompt": "Flying sequence through clouds, sense of freedom and wonder, hand-drawn animation style, Studio Ghibli flight scene, Miyazaki soaring moment, magical atmosphere"
            },
            {
                "index": 3,
                "name": "食物细节",
                "shot_type": "特写",
                "technique": "美食描绘",
                "prompt": "Close-up of food, detailed hand-drawn texture, steam rising, Studio Ghibli food scene, Miyazaki culinary moment, warm lighting, appetizing detail"
            },
            {
                "index": 4,
                "name": "雨景氛围",
                "shot_type": "全景",
                "technique": "雨动画",
                "prompt": "Rain scene with hand-drawn raindrops, puddle reflections, waiting at bus stop, Studio Ghibli atmosphere, Miyazaki rainy day, peaceful melancholy"
            },
            {
                "index": 5,
                "name": "神怪出现",
                "shot_type": "中景",
                "technique": "神秘 reveal",
                "prompt": "Spirit creature appearing, magical transformation, hand-drawn effects, Studio Ghibli spirit world, Miyazaki wonder moment, soft glowing light"
            },
            {
                "index": 6,
                "name": "乡村日常",
                "shot_type": "全景",
                "technique": "生活细节",
                "prompt": "Rural daily life scene, traditional Japanese house, garden and fields, Studio Ghibli domestic scene, Miyazaki slice of life, warm afternoon light"
            },
            {
                "index": 7,
                "name": "留白时刻",
                "shot_type": "空镜头",
                "technique": "间（ma）",
                "prompt": "Empty landscape shot, wind through grass, clouds moving slowly, Studio Ghibli quiet moment, Miyazaki ma concept, contemplative atmosphere"
            },
            {
                "index": 8,
                "name": "冒险启程",
                "shot_type": "远景",
                "technique": "旅程开始",
                "prompt": "Journey beginning, path through nature, character small in landscape, Studio Ghibli adventure start, Miyazaki quest opening, hopeful atmosphere"
            },
            {
                "index": 9,
                "name": "温暖结局",
                "shot_type": "全景",
                "technique": "团圆场景",
                "prompt": "Warm ending scene, family or friends together, sunset lighting, Studio Ghibli conclusion, Miyazaki emotional resolution, healing atmosphere"
            }
        ]
    }


class ShinkaiStyle:
    """新海诚风格 - 光影交织的现实幻想"""
    
    INFO = {
        "name": "新海诚",
        "name_en": "Makoto Shinkai",
        "nationality": "日本",
        "active_period": "1990年代至今",
        "genre": "动画/爱情/科幻",
        "style_keywords": ["超写实背景", "光影效果", "远距离恋爱", "天空描绘", "情感细腻"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "photorealistic_backgrounds": {
            "name": "超写实背景",
            "description": "照片级的背景绘制，细节丰富",
            "example": "《你的名字》中的城市景观",
            "application": "环境描绘、视觉冲击"
        },
        "light_effects": {
            "name": "光影特效",
            "description": "精细的光照、反射、镜头光晕",
            "example": "《言叶之庭》中的雨滴和光线",
            "application": "氛围营造、情感表达"
        },
        "sky_obsession": {
            "name": "天空痴迷",
            "description": "对天空、云彩、光线的极致描绘",
            "example": "《天气之子》中的各种天空",
            "application": "情绪暗示、视觉标志"
        },
        "long_distance_relationship": {
            "name": "远距离恋爱",
            "description": "分隔两地的恋人主题",
            "example": "《秒速5厘米》《你的名字》",
            "application": "核心主题、情感驱动"
        },
        "montage_sequences": {
            "name": "蒙太奇序列",
            "description": "快速剪辑展示时间流逝",
            "example": "《秒速5厘米》的樱花飘落",
            "application": "时间流逝、情感累积"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "your_name": {
            "title": "你的名字",
            "year": 2016,
            "visual_traits": ["彗星", "身体交换", "城市与乡村", "黄昏时刻"],
            "key_shots": ["彗星坠落", "身体交换 montage", "黄昏相遇", "楼梯重逢"]
        },
        "weathering_with_you": {
            "title": "天气之子",
            "year": 2019,
            "visual_traits": ["雨景", "晴天巫女", "东京全景", "天空变化"],
            "key_shots": ["鸟居之上", "东京水淹", "阳光穿透", "最终选择"]
        },
        "garden_of_words": {
            "title": "言叶之庭",
            "year": 2013,
            "visual_traits": ["雨景", "庭园", "足袋", "细腻光影"],
            "key_shots": ["雨中庭园", "足袋特写", "楼梯告白", "雨过天晴"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["天空蓝", "樱花粉", "阳光金", "雨灰", "霓虹色"],
        "lighting_style": "强烈光影，镜头光晕，反射效果",
        "composition": "超写实背景，人物与环境的对比",
        "camera_movement": "流畅3D，复杂运动，天空旋转",
        "editing_rhythm": "蒙太奇，时间跳跃，情感节奏"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["超写实远景", "光影特写", "天空镜头"],
        "frame_rate": "数字动画，流畅60fps",
        "color_grading": "高饱和，强对比，光影分离",
        "typical_mood": "唯美、忧伤、希望、距离感"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "新海诚风格3×3",
        "description": "超写实光影与远距离恋爱的视觉诗",
        "shots": [
            {
                "index": 1,
                "name": "城市全景",
                "shot_type": "超写实远景",
                "technique": "照片级背景",
                "prompt": "Photorealistic cityscape, detailed urban environment, Makoto Shinkai background art, dramatic sky, light rays through buildings, anime aesthetic, high detail"
            },
            {
                "index": 2,
                "name": "天空变幻",
                "shot_type": "天空镜头",
                "technique": "云彩动画",
                "prompt": "Dramatic sky shot, detailed clouds, changing weather, Makoto Shinkai sky obsession, light and shadow play, anime sky, emotional atmosphere"
            },
            {
                "index": 3,
                "name": "光影特写",
                "shot_type": "特写",
                "technique": "光线效果",
                "prompt": "Close-up with dramatic lighting, lens flare, light particles, Makoto Shinkai light effect, detailed texture, emotional moment, anime style"
            },
            {
                "index": 4,
                "name": "雨景氛围",
                "shot_type": "中景",
                "technique": "雨滴效果",
                "prompt": "Rain scene with detailed water effects, reflections on ground, wet surfaces, Makoto Shinkai rain aesthetic, melancholic atmosphere, anime visual"
            },
            {
                "index": 5,
                "name": "黄昏时刻",
                "shot_type": "全景",
                "technique": "黄金光线",
                "prompt": "Magic hour scene, golden light, long shadows, Makoto Shinkai sunset, warm colors transitioning to cool, anime twilight, romantic atmosphere"
            },
            {
                "index": 6,
                "name": "距离构图",
                "shot_type": "远景",
                "technique": "人物与环境",
                "prompt": "Wide shot with tiny figure in vast environment, emphasizing distance, Makoto Shinkai scale contrast, detailed background, lone character, anime composition"
            },
            {
                "index": 7,
                "name": "蒙太奇流逝",
                "shot_type": "蒙太奇",
                "technique": "时间跳跃",
                "prompt": "Montage sequence showing time passing, seasons changing, Makoto Shinkai temporal montage, detailed environmental changes, anime editing"
            },
            {
                "index": 8,
                "name": "相遇瞬间",
                "shot_type": "双人",
                "technique": "情感光线",
                "prompt": "Two shot of meeting moment, dramatic backlighting, emotional lighting, Makoto Shinkai reunion scene, anime character animation, poignant atmosphere"
            },
            {
                "index": 9,
                "name": "离别场景",
                "shot_type": "远景",
                "technique": "距离感",
                "prompt": "Separation scene, characters at distance, dramatic sky background, Makoto Shinkai farewell, emotional anime ending, beautiful but sad"
            }
        ]
    }


class BurtonStyle:
    """蒂姆·伯顿风格 - 哥特童话的黑暗诗意"""
    
    INFO = {
        "name": "蒂姆·伯顿",
        "name_en": "Tim Burton",
        "nationality": "美国",
        "active_period": "1980年代至今",
        "genre": "奇幻/哥特/黑色喜剧",
        "style_keywords": ["哥特美学", "条纹元素", "局外人主题", "德国表现主义", "黑色幽默"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "gothic_aesthetic": {
            "name": "哥特美学",
            "description": "黑暗、扭曲、维多利亚式的视觉风格",
            "example": "《剪刀手爱德华》的城堡",
            "application": "场景设计、整体风格"
        },
        "striped_patterns": {
            "name": "条纹元素",
            "description": "黑白条纹服装和场景元素",
            "example": "《甲壳虫汁》的条纹西装",
            "application": "服装设计、视觉标志"
        },
        "outsider_protagonist": {
            "name": "局外人主角",
            "description": "与社会格格不入的主角",
            "example": "剪刀手爱德华、僵尸新娘",
            "application": "角色塑造、主题表达"
        },
        "german_expressionism": {
            "name": "德国表现主义",
            "description": "扭曲的布景、强烈的阴影、几何形状",
            "example": "《蝙蝠侠》的哥谭市",
            "application": "场景设计、光影"
        },
        "stop_motion": {
            "name": "定格动画",
            "description": "使用定格动画技术",
            "example": "《僵尸新娘》《科学怪狗》",
            "application": "动画技术、独特质感"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "edward_scissorhands": {
            "title": "剪刀手爱德华",
            "year": 1990,
            "visual_traits": ["哥特城堡", "糖果色 suburbia", "剪刀手", "雪"],
            "key_shots": ["城堡山顶", "创造场景", "冰雕时刻", "告别场景"]
        },
        "nightmare_before_christmas": {
            "title": "圣诞夜惊魂",
            "year": 1993,
            "visual_traits": ["定格动画", "万圣节镇", "圣诞镇", "扭曲设计"],
            "key_shots": ["这是什么？", "圣诞镇发现", "圣诞老人绑架", "雪中的莎莉"]
        },
        "corpse_bride": {
            "title": "僵尸新娘",
            "year": 2005,
            "visual_traits": ["生死两界", "蓝色调", "定格动画", "维多利亚时代"],
            "key_shots": ["婚礼练习", "死者之地", "钢琴二重奏", "最终选择"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["黑白", "暗紫", "深蓝", "苍白", "偶尔鲜艳对比"],
        "lighting_style": "高对比，强烈阴影，戏剧性照明",
        "composition": "扭曲透视，几何形状，不对称",
        "camera_movement": "定格动画的顿挫感，或流畅的诡异运动",
        "editing_rhythm": "音乐驱动，定格动画的节奏"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["哥特全景", "特写", "扭曲构图"],
        "frame_rate": "定格动画或正常",
        "color_grading": "去饱和，高对比，偶尔色彩爆发",
        "typical_mood": "诡异、浪漫、忧郁、幽默"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "蒂姆·伯顿风格3×3",
        "description": "哥特童话与局外人的黑暗浪漫",
        "shots": [
            {
                "index": 1,
                "name": "哥特城堡",
                "shot_type": "大远景",
                "technique": "表现主义布景",
                "prompt": "Gothic castle on hill, German expressionist architecture, twisted spires, Tim Burton style, dark fairytale atmosphere, high contrast lighting, ominous sky"
            },
            {
                "index": 2,
                "name": "局外人特写",
                "shot_type": "特写",
                "technique": "角色设计",
                "prompt": "Close-up of outsider character, pale skin, dark eye circles, unique hairstyle, Tim Burton character design, emotional vulnerability, gothic aesthetic"
            },
            {
                "index": 3,
                "name": "条纹元素",
                "shot_type": "中景",
                "technique": "视觉标志",
                "prompt": "Medium shot with striped pattern, black and white stripes, Tim Burton signature visual, costume or set design, gothic whimsy"
            },
            {
                "index": 4,
                "name": "扭曲城镇",
                "shot_type": "全景",
                "technique": "表现主义",
                "prompt": "Twisted townscape, crooked buildings, German expressionist influence, Tim Burton environment design, dark fairytale setting, surreal architecture"
            },
            {
                "index": 5,
                "name": "生死交界",
                "shot_type": "分屏",
                "technique": "双色对比",
                "prompt": "Split between living world and dead world, color vs monochrome, Tim Burton afterlife aesthetic, Corpse Bride style, two contrasting realms"
            },
            {
                "index": 6,
                "name": "定格动画",
                "shot_type": "特写",
                "technique": "定格质感",
                "prompt": "Stop-motion animation close-up, tactile texture, Tim Burton claymation style, detailed puppet, gothic character design, subtle movements"
            },
            {
                "index": 7,
                "name": "雪/花瓣",
                "shot_type": "全景",
                "technique": "诗意元素",
                "prompt": "Wide shot with falling snow or petals, romantic but melancholic, Tim Burton poetic moment, Edward Scissorhands reference, bittersweet atmosphere"
            },
            {
                "index": 8,
                "name": "怪诞群像",
                "shot_type": "群像",
                "technique": "角色设计",
                "prompt": "Group shot of quirky characters, each uniquely designed, Tim Burton ensemble, gothic circus atmosphere, dark whimsy, detailed costumes"
            },
            {
                "index": 9,
                "name": "孤独剪影",
                "shot_type": "剪影",
                "technique": "逆光",
                "prompt": "Silhouette against moon or light, lonely figure, Tim Burton iconic image, gothic romance, bittersweet ending, dramatic backlighting"
            }
        ]
    }


# 导出
ANIMATION_DIRECTORS = {
    "miyazaki": MiyazakiStyle,
    "shinkai": ShinkaiStyle,
    "burton": BurtonStyle
}


def get_animation_director_style(director_name: str):
    """获取动画导演风格"""
    return ANIMATION_DIRECTORS.get(director_name)


def list_animation_directors():
    """列出所有动画导演"""
    return list(ANIMATION_DIRECTORS.keys())
