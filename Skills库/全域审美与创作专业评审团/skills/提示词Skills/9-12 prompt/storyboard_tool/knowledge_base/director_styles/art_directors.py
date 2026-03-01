"""
文艺片导演风格库
包含：王家卫、韦斯·安德森、侯孝贤
"""


class WongKarWaiStyle:
    """王家卫风格 - 迷离都市的诗意"""
    
    INFO = {
        "name": "王家卫",
        "name_en": "Wong Kar-wai",
        "nationality": "中国香港",
        "active_period": "1988年至今",
        "genre": "文艺片/爱情片/剧情片",
        "style_keywords": ["时间流逝感", "疏离感", "色彩情绪", "碎片化叙事", "都市孤独"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "step_printing": {
            "name": "抽帧/拖影效果",
            "description": "通过改变快门速度创造动态模糊和抽帧效果，表现时间流逝",
            "example": "《重庆森林》中林青霞奔跑的拖影镜头",
            "application": "动作场景、表现时间感"
        },
        "slow_motion_emotion": {
            "name": "慢动作情绪渲染",
            "description": "慢动作配合特写捕捉细微情感变化",
            "example": "《花样年华》中张曼玉的慢动作回眸",
            "application": "情感高潮、人物特写"
        },
        "mirror_reflection": {
            "name": "镜像反射构图",
            "description": "利用镜子、玻璃等反射面创造双重空间",
            "example": "《花样年华》中多次出现的镜子反射",
            "application": "人物关系、自我审视"
        },
        "neon_lighting": {
            "name": "霓虹灯光影",
            "description": "高饱和度的霓虹色彩营造都市迷离感",
            "example": "《重庆森林》的霓虹街道",
            "application": "夜景、都市氛围"
        },
        "repetitive_action": {
            "name": "重复性动作蒙太奇",
            "description": "重复的动作片段表现时间循环和等待",
            "example": "《重庆森林》中反复出现的买凤梨罐头",
            "application": "时间流逝、情感累积"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "in_the_mood_for_love": {
            "title": "花样年华",
            "year": 2000,
            "visual_traits": ["红色调", "旗袍美学", "狭窄空间构图", "含蓄情感"],
            "key_shots": ["楼梯间相遇", "云吞面摊", "吴哥窟结局"]
        },
        "chungking_express": {
            "title": "重庆森林",
            "year": 1994,
            "visual_traits": ["手持摄影", "抽帧效果", "霓虹色彩", "快节奏剪辑"],
            "key_shots": ["林青霞奔跑", "加州酒吧", "空姐制服"]
        },
        "ashes_of_time": {
            "title": "东邪西毒",
            "year": 1994,
            "visual_traits": ["沙漠意象", "极端特写", "独白叙事", "时间错位"],
            "key_shots": ["鸟笼", "沙漠剪影", "水中倒影"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["霓虹红", "翡翠绿", "琥珀黄", "午夜蓝", "深紫"],
        "lighting_style": "高对比霓虹光，强烈的色彩分离",
        "composition": "不对称构图，大量前景遮挡，浅景深",
        "camera_movement": "手持晃动，慢速横移，抽帧效果",
        "editing_rhythm": "碎片化剪辑，跳切，重复蒙太奇"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["特写", "近景", "反射构图"],
        "frame_rate": "可变帧率，常使用抽帧",
        "color_grading": "高饱和，强对比，色彩象征",
        "typical_mood": "迷离、孤独、怀旧、暧昧"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "王家卫风格3×3",
        "description": "都市孤独与情感疏离的诗意表达",
        "shots": [
            {
                "index": 1,
                "name": "霓虹都市",
                "shot_type": "全景/夜景",
                "technique": "霓虹灯光+手持晃动",
                "prompt": "Night cityscape with neon lights, handheld camera shake, vibrant red and green colors, motion blur, Wong Kar-wai style, urban loneliness, cinematic"
            },
            {
                "index": 2,
                "name": "抽帧相遇",
                "shot_type": "中景",
                "technique": "抽帧效果+慢动作",
                "prompt": "Medium shot with step printing effect, slow motion, two figures passing by, motion blur, saturated colors, emotional distance, Wong Kar-wai aesthetic"
            },
            {
                "index": 3,
                "name": "镜像自我",
                "shot_type": "特写",
                "technique": "镜面反射构图",
                "prompt": "Close-up with mirror reflection, dual image composition, neon lighting, contemplative mood, shallow depth of field, Wong Kar-wai style"
            },
            {
                "index": 4,
                "name": "走廊等待",
                "shot_type": "长镜头",
                "technique": "慢速横移+重复",
                "prompt": "Long corridor shot, slow horizontal tracking, repetitive action, warm tungsten lighting, waiting mood, Wong Kar-wai visual style"
            },
            {
                "index": 5,
                "name": "情感特写",
                "shot_type": "极端特写",
                "technique": "慢动作+浅景深",
                "prompt": "Extreme close-up, slow motion, shallow depth of field, emotional detail, soft focus, saturated color, Wong Kar-wai intimate moment"
            },
            {
                "index": 6,
                "name": "都市剪影",
                "shot_type": "逆光剪影",
                "technique": "逆光+霓虹背景",
                "prompt": "Silhouette against neon lights, backlit, urban night, vibrant background colors, mysterious atmosphere, Wong Kar-wai cinematic"
            },
            {
                "index": 7,
                "name": "窗框构图",
                "shot_type": "框架内构图",
                "technique": "窗框前景+浅景深",
                "prompt": "Frame within frame through window, shallow depth of field, rain drops on glass, blurred city lights, melancholic mood, Wong Kar-wai style"
            },
            {
                "index": 8,
                "name": "时间流逝",
                "shot_type": "延时/抽帧",
                "technique": "抽帧蒙太奇",
                "prompt": "Time-lapse with step printing, passing time, repetitive elements, motion blur, saturated colors, Wong Kar-wai temporal feeling"
            },
            {
                "index": 9,
                "name": "离别时刻",
                "shot_type": "远景/背影",
                "technique": "慢动作+长焦压缩",
                "prompt": "Wide shot from behind, slow motion, figure walking away, compressed space with telephoto lens, emotional departure, Wong Kar-wai ending shot"
            }
        ]
    }


class WesAndersonStyle:
    """韦斯·安德森风格 - 对称美学的童话世界"""
    
    INFO = {
        "name": "韦斯·安德森",
        "name_en": "Wes Anderson",
        "nationality": "美国",
        "active_period": "1996年至今",
        "genre": "喜剧/剧情片/冒险片",
        "style_keywords": ["对称构图", "糖果色调", "平面化", "童话质感", "强迫症美学"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "symmetrical_composition": {
            "name": "中心对称构图",
            "description": "严格的中心对称，人物居中，几何平衡",
            "example": "《布达佩斯大饭店》中几乎所有镜头",
            "application": "人物介绍、场景展示"
        },
        "flat_staging": {
            "name": "平面化调度",
            "description": "人物横向移动，缺乏纵深，像舞台剧",
            "example": "《月升王国》中的追逐场景",
            "application": "动作场景、群体场面"
        },
        "whip_pan": {
            "name": "快速摇镜",
            "description": "快速水平摇镜连接不同场景或人物",
            "example": "《天才一族》中的场景转换",
            "application": "场景切换、喜剧效果"
        },
        "color_coding": {
            "name": "色彩编码",
            "description": "特定的色彩主题区分场景和情绪",
            "example": "《布达佩斯大饭店》的粉色、紫色主题",
            "application": "场景区分、情绪暗示"
        },
        "miniature_effect": {
            "name": "微缩模型效果",
            "description": "使用微缩模型创造童话般的场景",
            "example": "《布达佩斯大饭店》的山景和建筑",
            "application": " establishing shot、转场"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "grand_budapest_hotel": {
            "title": "布达佩斯大饭店",
            "year": 2014,
            "visual_traits": ["粉色与紫色", "多层画幅", "微缩模型", "章节结构"],
            "key_shots": ["饭店外观", "电梯场景", "雪山追逐", "大堂对称构图"]
        },
        "moonrise_kingdom": {
            "title": "月升王国",
            "year": 2012,
            "visual_traits": ["黄绿色调", "自然光", "平面构图", "儿童视角"],
            "key_shots": ["帐篷场景", "灯塔", "地图动画", "逃跑路线"]
        },
        "royal_tenenbaums": {
            "title": "天才一族",
            "year": 2001,
            "visual_traits": ["红色主题", "书籍封面式构图", "章节标题", "暖色调"],
            "key_shots": ["家庭合影", "网球场", "衣柜场景", " introduction montage"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["千禧粉", "薄荷绿", "奶油黄", "天蓝色", "暖橙色"],
        "lighting_style": "均匀柔和，缺乏强烈阴影",
        "composition": "严格中心对称，几何图形构图",
        "camera_movement": "水平/垂直直线运动，快速摇镜",
        "editing_rhythm": "章节式结构，标题卡，定格画面"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["全景", "中景", "对称构图"],
        "frame_rate": "正常，偶尔慢动作",
        "color_grading": "糖果色调，高饱和，去对比度",
        "typical_mood": " whimsical、怀旧、幽默、精致"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "韦斯·安德森风格3×3",
        "description": "对称强迫症与糖果色调的童话世界",
        "shots": [
            {
                "index": 1,
                "name": "对称建筑",
                "shot_type": "大远景",
                "technique": "中心对称+微缩感",
                "prompt": "Symmetrical establishing shot, centered composition, pastel colors, miniature-like building, Wes Anderson style, flat lighting, whimsical"
            },
            {
                "index": 2,
                "name": "人物居中",
                "shot_type": "中景",
                "technique": "严格中心对称",
                "prompt": "Centered medium shot, perfect symmetry, character facing camera, pastel wardrobe, flat background, Wes Anderson portrait style"
            },
            {
                "index": 3,
                "name": "平面横移",
                "shot_type": "全景",
                "technique": "平面化调度+横向移动",
                "prompt": "Wide shot with flat staging, characters moving horizontally, side view, colorful set design, Wes Anderson tracking shot"
            },
            {
                "index": 4,
                "name": "快速摇镜",
                "shot_type": "摇镜",
                "technique": "whip pan转场",
                "prompt": "Whip pan transition, horizontal camera movement, blur effect, connecting two symmetrical compositions, Wes Anderson style"
            },
            {
                "index": 5,
                "name": "群体对称",
                "shot_type": "全景",
                "technique": "多人对称排列",
                "prompt": "Group shot with symmetrical arrangement, characters in geometric pattern, pastel costumes, centered composition, Wes Anderson ensemble"
            },
            {
                "index": 6,
                "name": "室内对称",
                "shot_type": "内景全景",
                "technique": "走廊/房间对称构图",
                "prompt": "Interior wide shot, symmetrical room, centered perspective, vintage decor, warm pastel lighting, Wes Anderson production design"
            },
            {
                "index": 7,
                "name": "交通工具",
                "shot_type": "横截面",
                "technique": "火车/汽车剖面视图",
                "prompt": "Cross-section view of vehicle, characters inside, symmetrical composition, detailed miniature aesthetic, Wes Anderson style"
            },
            {
                "index": 8,
                "name": "地图动画",
                "shot_type": "俯视图",
                "technique": "平面地图+动画",
                "prompt": "Overhead map view, animated path, vintage cartography style, flat colors, Wes Anderson journey sequence"
            },
            {
                "index": 9,
                "name": "章节标题",
                "shot_type": "文字卡",
                "technique": "标题卡+定格",
                "prompt": "Title card with Futura font, chapter heading, centered text, pastel background, book illustration style, Wes Anderson chapter marker"
            }
        ]
    }


class HouHsiaoHsienStyle:
    """侯孝贤风格 - 长镜头中的生活诗学"""
    
    INFO = {
        "name": "侯孝贤",
        "name_en": "Hou Hsiao-hsien",
        "nationality": "中国台湾",
        "active_period": "1980年至今",
        "genre": "文艺片/历史片/剧情片",
        "style_keywords": ["长镜头美学", "固定机位", "自然光", "生活流", "东方意境"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "long_take": {
            "name": "极简长镜头",
            "description": "固定机位长镜头，极少剪辑，观察式记录",
            "example": "《悲情城市》中大量3-5分钟的长镜头",
            "application": "日常场景、情感积累"
        },
        "natural_light": {
            "name": "自然光写实",
            "description": "完全使用自然光，拒绝人工打光",
            "example": "《海上花》的烛光场景",
            "application": "室内场景、夜景"
        },
        "deep_focus": {
            "name": "深焦全景",
            "description": "深景深让前后景都清晰，人物与环境共存",
            "example": "《恋恋风尘》的远景人物",
            "application": "风景、人物与环境关系"
        },
        "off_screen_space": {
            "name": "画外空间",
            "description": "声音和动作来自画面外，扩展空间想象",
            "example": "《悲情城市》中画外的广播声",
            "application": "声音设计、空间暗示"
        },
        "static_observation": {
            "name": "静观美学",
            "description": "摄影机像旁观者一样静静观察，不介入",
            "example": "《咖啡时光》中的街景观察",
            "application": "日常场景、纪录片风格"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "city_of_sadness": {
            "title": "悲情城市",
            "year": 1989,
            "visual_traits": ["自然光", "长镜头", "深焦", "历史厚重感"],
            "key_shots": ["家族聚餐", "医院走廊", "山顶远景", "室内对话"]
        },
        "flowers_of_shanghai": {
            "title": "海上花",
            "year": 1998,
            "visual_traits": ["烛光照明", "室内长镜头", "深色调", "缓慢移动"],
            "key_shots": ["青楼内景", "餐桌场景", "走廊", "房间"]
        },
        "dust_in_the_wind": {
            "title": "恋恋风尘",
            "year": 1986,
            "visual_traits": ["自然风景", "远景人物", "长镜头", "青春记忆"],
            "key_shots": ["山间小路", "火车站", "村庄远景", "矿场景象"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["自然绿", "土黄色", "灰蓝色", "褐色", "暗金色"],
        "lighting_style": "完全自然光，拒绝人工光源",
        "composition": "深焦全景，人物在环境中，大量留白",
        "camera_movement": "极少移动，固定机位为主，偶尔极慢横移",
        "editing_rhythm": "长镜头，极少剪辑，尊重时间流逝"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["远景", "全景", "深焦"],
        "frame_rate": "正常",
        "color_grading": "自然色调，低饱和，去人工感",
        "typical_mood": "沉静、怀旧、诗意、观察"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "侯孝贤风格3×3",
        "description": "长镜头静观中的东方生活诗学",
        "shots": [
            {
                "index": 1,
                "name": "远山远景",
                "shot_type": "大远景",
                "technique": "深焦+固定机位",
                "prompt": "Extreme wide shot, deep focus, fixed camera, natural landscape, tiny figures in vast environment, natural lighting, Hou Hsiao-hsien contemplative style"
            },
            {
                "index": 2,
                "name": "日常长镜",
                "shot_type": "全景",
                "technique": "固定长镜头+自然光",
                "prompt": "Wide shot long take, static camera, daily life scene, natural window light, deep focus, characters in environment, Hou Hsiao-hsien observational style"
            },
            {
                "index": 3,
                "name": "室内深焦",
                "shot_type": "内景全景",
                "technique": "深焦+自然光",
                "prompt": "Interior wide shot, deep focus, natural lighting from windows, multiple planes of action, warm tungsten feel, Hou Hsiao-hsien domestic scene"
            },
            {
                "index": 4,
                "name": "走廊纵深",
                "shot_type": "纵深构图",
                "technique": "长镜头+纵深调度",
                "prompt": "Corridor shot with deep perspective, long take, figures moving through space, natural light from end, Hou Hsiao-hsien spatial composition"
            },
            {
                "index": 5,
                "name": "窗光人物",
                "shot_type": "中景",
                "technique": "侧窗自然光",
                "prompt": "Medium shot by window, side natural light, contemplative figure, soft shadows, interior detail, Hou Hsiao-hsien intimate moment"
            },
            {
                "index": 6,
                "name": "画外声音",
                "shot_type": "空镜头",
                "technique": "固定机位+声音叙事",
                "prompt": "Empty room shot, static camera, off-screen sounds suggesting action, natural lighting, Hou Hsiao-hsien off-screen space technique"
            },
            {
                "index": 7,
                "name": "黄昏时刻",
                "shot_type": "黄金时刻",
                "technique": "自然暮光",
                "prompt": "Golden hour wide shot, natural sunset light, warm tones, silhouettes possible, rural or urban landscape, Hou Hsiao-hsien temporal mood"
            },
            {
                "index": 8,
                "name": "慢速横移",
                "shot_type": "横移长镜",
                "technique": "极慢横移",
                "prompt": "Extremely slow horizontal tracking, panoramic view, natural landscape or street, observational mood, Hou Hsiao-hsien contemplative movement"
            },
            {
                "index": 9,
                "name": "离别远景",
                "shot_type": "远景",
                "technique": "固定长镜头",
                "prompt": "Distant wide shot, fixed camera, figure walking away or waiting, vast environment, natural light, Hou Hsiao-hsien farewell moment, poetic ending"
            }
        ]
    }


# 导出
ART_DIRECTORS = {
    "wong_kar_wai": WongKarWaiStyle,
    "wes_anderson": WesAndersonStyle,
    "hou_hsiao_hsien": HouHsiaoHsienStyle
}


def get_art_director_style(director_name: str):
    """获取文艺片导演风格"""
    return ART_DIRECTORS.get(director_name)


def list_art_directors():
    """列出所有文艺片导演"""
    return list(ART_DIRECTORS.keys())
