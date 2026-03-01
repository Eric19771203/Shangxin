"""
现代新晋导演风格库
包含：丹尼斯·维伦纽瓦、乔丹·皮尔、阿里·艾斯特、罗伯特·艾格斯、赵婷
特点：强烈的个人风格、现代美学、新科幻/恐怖风格、高标识度IP
"""


class VilleneuveStyle:
    """丹尼斯·维伦纽瓦风格 - 科幻史诗的庄严美学"""
    
    INFO = {
        "name": "丹尼斯·维伦纽瓦",
        "name_en": "Denis Villeneuve",
        "nationality": "加拿大",
        "active_period": "1990年代至今",
        "genre": "科幻片/剧情片/惊悚片",
        "style_keywords": ["巨物美学", "沙漠美学", "极简构图", "庄严氛围", "存在主义", "IMAX视觉"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "massive_scale": {
            "name": "巨物美学",
            "description": "人物在巨大建筑/自然面前的渺小感，强调存在主义主题",
            "example": "《沙丘》中人物与沙虫、飞船的对比",
            "application": "科幻场景、史诗建立"
        },
        "desert_aesthetic": {
            "name": "沙漠美学",
            "description": "橙色调沙漠、热浪扭曲、沙尘暴的视觉呈现",
            "example": "《沙丘》《降临》中的沙漠场景",
            "application": "外星环境、荒凉场景"
        },
        "minimalist_composition": {
            "name": "极简构图",
            "description": "简洁的几何构图，大量留白，建筑感",
            "example": "《降临》中的飞船着陆场景",
            "application": "科幻建筑、神秘物体"
        },
        "haze_atmosphere": {
            "name": "雾霾氛围",
            "description": "沙尘、雾气、烟雾营造的神秘氛围",
            "example": "《银翼杀手2049》的拉斯维加斯废墟",
            "application": "末日场景、神秘氛围"
        },
        "slow_reveal": {
            "name": "缓慢揭示",
            "description": "通过摄影机运动缓慢揭示场景全貌",
            "example": "《沙丘》中沙虫的首次完整 reveal",
            "application": "悬念建立、奇观展示"
        },
        "orange_teal_grading": {
            "name": "橙青色调",
            "description": "强烈的橙/青对比，现代科幻色彩",
            "example": "《沙丘》《银翼杀手2049》的整体色调",
            "application": "科幻场景、未来感"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "dune": {
            "title": "沙丘",
            "year": 2021,
            "visual_traits": ["沙漠巨物", "橙色调", "IMAX画幅", "庄严配乐"],
            "key_shots": ["沙虫 reveal", "香料收割机", "弗雷曼人剪影", "皇帝飞船"]
        },
        "blade_runner_2049": {
            "title": "银翼杀手2049",
            "year": 2017,
            "visual_traits": ["霓虹赛博朋克", "橙色废墟", "全息投影", "极简建筑"],
            "key_shots": ["拉斯维加斯废墟", " Joi 全息", "复制人诞生", "K的公寓"]
        },
        "arrival": {
            "title": "降临",
            "year": 2016,
            "visual_traits": ["极简飞船", "雾气氛围", "圆形构图", "自然光"],
            "key_shots": ["飞船着陆", "第一次进入", "时间闪回", "语言符号"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["沙漠橙", "深青", "灰蓝", "暖金", "暗褐"],
        "lighting_style": "自然光为主，戏剧化逆光，沙尘散射",
        "composition": "极简几何，人物渺小，建筑感强",
        "camera_movement": "缓慢沉稳，史诗感横移，垂直升降",
        "editing_rhythm": "缓慢节奏，长镜头，情绪积累"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["大远景", "极简中景", "剪影"],
        "frame_rate": "IMAX规格，流畅",
        "color_grading": "橙青分离，高对比，去饱和",
        "typical_mood": "庄严、神秘、存在主义、史诗"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "维伦纽瓦风格3×3",
        "description": "科幻史诗的庄严巨物美学",
        "shots": [
            {
                "index": 1,
                "name": "巨物建立",
                "shot_type": "大远景",
                "technique": "人物与巨物对比",
                "prompt": "Epic wide shot, tiny human figure against massive structure or landscape, Denis Villeneuve style, orange and teal color grading, atmospheric haze, sense of scale, IMAX composition"
            },
            {
                "index": 2,
                "name": "沙漠美学",
                "shot_type": "全景",
                "technique": "热浪扭曲+沙尘",
                "prompt": "Desert landscape with heat distortion, sand dunes, orange monochromatic palette, Denis Villeneuve Dune aesthetic, atmospheric depth, epic scale"
            },
            {
                "index": 3,
                "name": "极简建筑",
                "shot_type": "中景",
                "technique": "几何构图",
                "prompt": "Minimalist architecture shot, geometric composition, clean lines, Denis Villeneuve sci-fi style, mysterious structure, soft natural lighting"
            },
            {
                "index": 4,
                "name": "雾霾氛围",
                "shot_type": "远景",
                "technique": "大气透视",
                "prompt": "Hazy atmosphere shot, distant structure through fog or dust, Denis Villeneuve mysterious ambiance, muted colors, sense of unknown"
            },
            {
                "index": 5,
                "name": "缓慢揭示",
                "shot_type": "运动长镜",
                "technique": "摄影机运动 reveal",
                "prompt": "Slow camera movement revealing massive object, Denis Villeneuve reveal technique, building anticipation, dramatic lighting, sci-fi wonder"
            },
            {
                "index": 6,
                "name": "人物剪影",
                "shot_type": "剪影",
                "technique": "逆光剪影",
                "prompt": "Silhouette against bright background, lone figure, Denis Villeneuve iconic composition, sense of isolation, epic backdrop"
            },
            {
                "index": 7,
                "name": "赛博废墟",
                "shot_type": "全景",
                "technique": "橙色调废墟",
                "prompt": "Post-apocalyptic ruins, orange color grading, Las Vegas aesthetic, Denis Villeneuve Blade Runner style, holographic elements, decayed grandeur"
            },
            {
                "index": 8,
                "name": "存在主义特写",
                "shot_type": "特写",
                "technique": "情绪凝视",
                "prompt": "Close-up of contemplative face, shallow depth of field, Denis Villeneuve intimate moment, emotional weight, soft lighting"
            },
            {
                "index": 9,
                "name": "史诗结局",
                "shot_type": "大远景",
                "technique": "庄严定格",
                "prompt": "Epic final shot, vast landscape, lone figure or massive structure, Denis Villeneuve conclusion, Hans Zimmer music visualized, transcendent atmosphere"
            }
        ]
    }


class PeeleStyle:
    """乔丹·皮尔风格 - 社会惊悚的符号美学"""
    
    INFO = {
        "name": "乔丹·皮尔",
        "name_en": "Jordan Peele",
        "nationality": "美国",
        "active_period": "2010年代至今",
        "genre": "恐怖片/惊悚片/社会讽刺片",
        "style_keywords": ["社会隐喻", "符号学", "种族议题", "心理恐怖", "视觉双关"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "social_horror": {
            "name": "社会恐怖",
            "description": "将社会议题（种族、阶级）包装为恐怖元素",
            "example": "《逃出绝命镇》的种族隐喻",
            "application": "主题表达、深层含义"
        },
        "visual_symbolism": {
            "name": "视觉符号",
            "description": "大量使用象征性视觉元素",
            "example": "《我们》中的剪刀、兔子、隧道",
            "application": "视觉叙事、主题暗示"
        },
        "sunken_place": {
            "name": "下沉空间",
            "description": "人物陷入黑暗虚空的主观视觉",
            "example": "《逃出绝命镇》中的下沉空间",
            "application": "心理恐怖、失去控制"
        },
        "mirror_reflection": {
            "name": "镜像恐怖",
            "description": "利用镜子和反射创造恐怖",
            "example": "《我们》中的镜像家庭",
            "application": "身份恐怖、双重性"
        },
        "daylight_horror": {
            "name": "日光恐怖",
            "description": "在明亮日光下制造恐怖，颠覆传统",
            "example": "《不》中的白天场景",
            "application": "颠覆预期、日常恐怖"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "get_out": {
            "title": "逃出绝命镇",
            "year": 2017,
            "visual_traits": ["下沉空间", "茶杯催眠", "鹿的意象", "郊区恐怖"],
            "key_shots": ["下沉空间", "茶杯特写", "鹿撞车", "最终反抗"]
        },
        "us": {
            "title": "我们",
            "year": 2019,
            "visual_traits": ["红色服装", "剪刀", "隧道", "镜像家庭"],
            "key_shots": ["走廊牵手", "剪刀特写", "地下世界", "最终 reveal"]
        },
        "nope": {
            "title": "不",
            "year": 2022,
            "visual_traits": ["天空恐怖", "云朵", "马", "IMAX自然光"],
            "key_shots": ["云的形状", "马场", "最终对抗", "Gordy场景"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["血红", "深黑", "苍白", "暗绿", "暖黄"],
        "lighting_style": "日常光线中的不安，突然的阴影",
        "composition": "对称与不对称的对比，中心构图",
        "camera_movement": "稳定与突然运动的对比",
        "editing_rhythm": "正常节奏突然打破，跳跃惊吓"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["对称构图", "特写", "主观视角"],
        "frame_rate": "正常",
        "color_grading": "自然色调中的突兀红色",
        "typical_mood": "不安、讽刺、社会批判、心理压迫"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "乔丹·皮尔风格3×3",
        "description": "社会惊悚与视觉符号的恐怖美学",
        "shots": [
            {
                "index": 1,
                "name": "郊区建立",
                "shot_type": "全景",
                "technique": "表面平静",
                "prompt": "Suburban neighborhood shot, seemingly peaceful but ominous, Jordan Peele style, bright daylight with underlying dread, symmetrical composition"
            },
            {
                "index": 2,
                "name": "符号特写",
                "shot_type": "特写",
                "technique": "象征物件",
                "prompt": "Close-up of symbolic object, scissors or teacup, Jordan Peele visual symbolism, shallow depth of field, ominous lighting"
            },
            {
                "index": 3,
                "name": "下沉空间",
                "shot_type": "主观视角",
                "technique": "坠落效果",
                "prompt": "Sunken place visualization, falling through dark void, Jordan Peele psychological horror, disorienting, helplessness"
            },
            {
                "index": 4,
                "name": "镜像恐怖",
                "shot_type": "镜像构图",
                "technique": "反射恐怖",
                "prompt": "Mirror reflection shot, doppelganger appearing, Jordan Peele identity horror, symmetrical framing, uncanny valley"
            },
            {
                "index": 5,
                "name": "社会场景",
                "shot_type": "群像",
                "technique": "社交不适",
                "prompt": "Social gathering with underlying tension, all white clothing, Jordan Peele social horror, smiling faces with menacing undertones"
            },
            {
                "index": 6,
                "name": "日光恐怖",
                "shot_type": "全景",
                "technique": "明亮恐怖",
                "prompt": "Bright daylight horror scene, cloud formation, Jordan Peele Nope aesthetic, natural lighting with supernatural element"
            },
            {
                "index": 7,
                "name": "隧道纵深",
                "shot_type": "纵深",
                "technique": "黑暗通道",
                "prompt": "Tunnel or corridor shot, darkness at end, Jordan Peele underground aesthetic, red lighting, approaching threat"
            },
            {
                "index": 8,
                "name": "眼神恐惧",
                "shot_type": "极端特写",
                "technique": "情绪放大",
                "prompt": "Extreme close-up of terrified eyes, Jordan Peele emotional horror, wide pupils, reflection of horror"
            },
            {
                "index": 9,
                "name": "最终揭示",
                "shot_type": "全景",
                "technique": "真相揭露",
                "prompt": "Wide shot of revelation, social commentary visualized, Jordan Peele conclusion, disturbing imagery with deeper meaning"
            }
        ]
    }


class AsterStyle:
    """阿里·艾斯特风格 - 民俗恐怖的仪式美学"""
    
    INFO = {
        "name": "阿里·艾斯特",
        "name_en": "Ari Aster",
        "nationality": "美国",
        "active_period": "2010年代至今",
        "genre": "恐怖片/心理惊悚片",
        "style_keywords": ["家庭创伤", "民俗恐怖", "仪式感", "心理崩溃", "明亮恐怖", "长镜头"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "family_trauma": {
            "name": "家庭创伤",
            "description": "以家庭关系破裂为恐怖核心",
            "example": "《遗传厄运》中的家庭崩溃",
            "application": "情感基础、心理恐怖"
        },
        "folk_horror": {
            "name": "民俗恐怖",
            "description": "利用民俗传统和异教仪式制造恐怖",
            "example": "《仲夏夜惊魂》的瑞典异教",
            "application": "文化恐怖、仪式感"
        },
        "daylight_dread": {
            "name": "白昼恐惧",
            "description": "在明亮日光下制造持续不安",
            "example": "《仲夏夜惊魂》的永昼",
            "application": "颠覆传统、持续紧张"
        },
        "long_take_breakdown": {
            "name": "长镜头崩溃",
            "description": "长镜头跟随角色心理崩溃过程",
            "example": "《遗传厄运》中的 dinner scene",
            "application": "心理真实、情绪积累"
        },
        "miniature_models": {
            "name": "微缩模型",
            "description": "使用微缩模型暗示命运",
            "example": "《遗传厄运》中的房屋模型",
            "application": "命运隐喻、视觉符号"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "hereditary": {
            "title": "遗传厄运",
            "year": 2018,
            "visual_traits": ["微缩模型", "家庭住宅", "仪式符号", "心理崩溃"],
            "key_shots": ["车祸", "dinner scene", "天花板爬行", "最终仪式"]
        },
        "midsommar": {
            "title": "仲夏夜惊魂",
            "year": 2019,
            "visual_traits": ["永昼", "鲜花", "瑞典乡村", "集体仪式"],
            "key_shots": ["抵达村庄", "悬崖仪式", "五月柱", "最终融入"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["阳光黄", "鲜花色", "苍白", "深红", "自然绿"],
        "lighting_style": "自然日光，过度曝光，明亮但不安",
        "composition": "对称仪式构图，中心焦点",
        "camera_movement": "长镜头，缓慢推进，环绕",
        "editing_rhythm": "长镜头为主，突然剪切"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["长镜头", "对称构图", "特写"],
        "frame_rate": "正常",
        "color_grading": "明亮过曝，鲜花色彩",
        "typical_mood": "不安、仪式、家庭悲剧、民俗恐怖"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "阿里·艾斯特风格3×3",
        "description": "民俗仪式与家庭创伤的光明恐怖",
        "shots": [
            {
                "index": 1,
                "name": "家庭住宅",
                "shot_type": "全景",
                "technique": "微缩模型暗示",
                "prompt": "Family house shot, dollhouse aesthetic, Ari Aster style, miniature model feel, ominous domesticity, detailed production design"
            },
            {
                "index": 2,
                "name": "仪式准备",
                "shot_type": "中景",
                "technique": "对称构图",
                "prompt": "Ritual preparation, symmetrical composition, Ari Aster folk horror, bright lighting, ceremonial objects, unsettling order"
            },
            {
                "index": 3,
                "name": "心理崩溃",
                "shot_type": "特写",
                "technique": "长镜头跟随",
                "prompt": "Psychological breakdown close-up, grief and horror, Ari Aster emotional intensity, naturalistic performance, uncomfortable intimacy"
            },
            {
                "index": 4,
                "name": "民俗场景",
                "shot_type": "全景",
                "technique": "明亮日光",
                "prompt": "Folk ritual in bright daylight, flowers and white dresses, Ari Aster Midsommar aesthetic, seemingly beautiful but disturbing"
            },
            {
                "index": 5,
                "name": "晚餐场景",
                "shot_type": "长镜头",
                "technique": "持续紧张",
                "prompt": "Long take dinner scene, family tension building, Ari Aster signature shot, static camera, unbearable silence"
            },
            {
                "index": 6,
                "name": "仪式中心",
                "shot_type": "俯拍",
                "technique": "几何图案",
                "prompt": "Overhead ritual shot, geometric pattern, Ari Aster ceremonial aesthetic, human figures arranged symbolically, disturbing beauty"
            },
            {
                "index": 7,
                "name": "创伤瞬间",
                "shot_type": "极端特写",
                "technique": "情绪爆发",
                "prompt": "Extreme close-up of trauma, screaming or shock, Ari Aster horror moment, raw emotion, invasive camera"
            },
            {
                "index": 8,
                "name": "自然恐怖",
                "shot_type": "远景",
                "technique": "环境恐怖",
                "prompt": "Nature as horror, beautiful landscape with hidden threat, Ari Aster environmental dread, bright colors, wrongness"
            },
            {
                "index": 9,
                "name": "最终仪式",
                "shot_type": "全景",
                "technique": "集体参与",
                "prompt": "Final ritual scene, community participation, Ari Aster conclusion, flames or sacrifice, disturbing catharsis"
            }
        ]
    }


class EggersStyle:
    """罗伯特·艾格斯风格 - 历史真实主义的哥特恐怖"""
    
    INFO = {
        "name": "罗伯特·艾格斯",
        "name_en": "Robert Eggers",
        "nationality": "美国",
        "active_period": "2010年代至今",
        "genre": "恐怖片/历史片/剧情片",
        "style_keywords": ["历史真实", "方言对白", "自然光", "1.19:1画幅", "手工质感", "民俗研究"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "historical_accuracy": {
            "name": "历史考据",
            "description": "极致的历史细节还原，包括服装、道具、语言",
            "example": "《女巫》的17世纪新英格兰",
            "application": "时代感、沉浸感"
        },
        "natural_light_only": {
            "name": "纯自然光",
            "description": "仅使用蜡烛、油灯等时代光源",
            "example": "《灯塔》的黑白摄影",
            "application": "真实感、历史氛围"
        },
        "academy_ratio": {
            "name": "学院比例",
            "description": "使用1.19:1或1.33:1的复古画幅",
            "example": "《灯塔》的1.19:1黑白",
            "application": "复古感、幽闭感"
        },
        "dialect_performance": {
            "name": "方言表演",
            "description": "使用历史方言和古老语言",
            "example": "《女巫》的古英语",
            "application": "历史真实、异化感"
        },
        "folklore_research": {
            "name": "民俗研究",
            "description": "深入研究民间传说和迷信",
            "example": "《女巫》的民间女巫形象",
            "application": "文化深度、恐怖根源"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "the_witch": {
            "title": "女巫",
            "year": 2015,
            "visual_traits": ["自然光", "森林", "1.66:1画幅", "灰色调"],
            "key_shots": ["森林边缘", "玉米地", "黑山羊", "最终飞行"]
        },
        "the_lighthouse": {
            "title": "灯塔",
            "year": 2019,
            "visual_traits": ["1.19:1黑白", "高对比", "海洋", "疯狂"],
            "key_shots": ["灯塔建立", " mermaid", "章鱼", "最终疯狂"]
        },
        "the_northman": {
            "title": "北欧人",
            "year": 2022,
            "visual_traits": ["维京时代", "自然光", "史诗", "神话"],
            "key_shots": ["村庄袭击", "火山", "复仇", "瓦尔哈拉"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["黑白", "灰褐", "暗绿", "泥土色", "暗金"],
        "lighting_style": "纯自然光，烛光，高对比",
        "composition": "复古画幅，垂直构图",
        "camera_movement": "缓慢，稳定，尊重历史",
        "editing_rhythm": "古典节奏，长镜头"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["复古画幅", "自然光", "历史场景"],
        "frame_rate": "正常",
        "color_grading": "去饱和，或黑白",
        "typical_mood": "历史沉重、民俗恐怖、疯狂、真实"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "罗伯特·艾格斯风格3×3",
        "description": "历史真实主义的哥特民俗恐怖",
        "shots": [
            {
                "index": 1,
                "name": "历史建立",
                "shot_type": "全景",
                "technique": "时代细节",
                "prompt": "Historical establishing shot, period accurate details, Robert Eggers style, natural lighting, authentic costumes and sets, desaturated colors"
            },
            {
                "index": 2,
                "name": "烛光场景",
                "shot_type": "中景",
                "technique": "单一光源",
                "prompt": "Candlelit interior, single light source, Robert Eggers natural lighting, chiaroscuro, historical accuracy, warm flame glow"
            },
            {
                "index": 3,
                "name": "森林恐惧",
                "shot_type": "远景",
                "technique": "自然光",
                "prompt": "Forest edge shot, natural daylight, Robert Eggers The Witch aesthetic, ominous woods, period atmosphere, desaturated greens"
            },
            {
                "index": 4,
                "name": "疯狂特写",
                "shot_type": "特写",
                "technique": "高对比",
                "prompt": "Close-up of madness, high contrast lighting, Robert Eggers psychological horror, intense expression, claustrophobic framing"
            },
            {
                "index": 5,
                "name": "海洋风暴",
                "shot_type": "全景",
                "technique": "黑白/高对比",
                "prompt": "Stormy ocean shot, black and white or desaturated, Robert Eggers The Lighthouse style, violent waves, isolation"
            },
            {
                "index": 6,
                "name": "民俗仪式",
                "shot_type": "中景",
                "technique": "历史准确",
                "prompt": "Folk ritual scene, historically accurate, Robert Eggers research-based, authentic costumes, serious tone, atmospheric"
            },
            {
                "index": 7,
                "name": "神话意象",
                "shot_type": "特写",
                "technique": "象征物件",
                "prompt": "Mythological imagery close-up, symbolic object, Robert Eggers folklore aesthetic, tactile texture, ancient symbolism"
            },
            {
                "index": 8,
                "name": "复古画幅",
                "shot_type": "全景",
                "technique": "1.19:1或1.33:1",
                "prompt": "Academy ratio composition, vertical emphasis, Robert Eggers framing, claustrophobic, historical film aesthetic"
            },
            {
                "index": 9,
                "name": "悲剧结局",
                "shot_type": "远景",
                "technique": "命运感",
                "prompt": "Tragic ending shot, fate visualized, Robert Eggers conclusion, historical doom, natural setting, haunting atmosphere"
            }
        ]
    }


class ZhaoStyle:
    """赵婷风格 - 自然主义诗电影"""
    
    INFO = {
        "name": "赵婷",
        "name_en": "Chloé Zhao",
        "nationality": "中国/美国",
        "active_period": "2010年代至今",
        "genre": "剧情片/西部片/超级英雄片",
        "style_keywords": ["自然主义", "非职业演员", "黄金时刻", "广阔风景", "诗意叙事", "边缘人群"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "naturalistic_performance": {
            "name": "自然主义表演",
            "description": "使用非职业演员，真实感表演",
            "example": "《无依之地》中的真实游牧民",
            "application": "真实感、纪录片风格"
        },
        "magic_hour": {
            "name": "黄金时刻",
            "description": "大量使用日出日落时分的自然光",
            "example": "《骑士》中的黄昏场景",
            "application": "诗意、温暖、怀旧"
        },
        "vast_landscape": {
            "name": "广阔风景",
            "description": "人物在自然风景中的渺小",
            "example": "《无依之地》的美国西部",
            "application": "存在主义、自由"
        },
        "documentary_style": {
            "name": "纪录片风格",
            "description": "模糊的剧情片与纪录片界限",
            "example": "《哥哥教我唱的歌》",
            "application": "真实感、沉浸感"
        },
        "marginalized_communities": {
            "name": "边缘群体",
            "description": "关注社会边缘人群的故事",
            "example": "《无依之地》的游牧老人",
            "application": "人文关怀、社会议题"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "nomadland": {
            "title": "无依之地",
            "year": 2020,
            "visual_traits": ["黄金时刻", "真实游牧民", "房车", "美国西部"],
            "key_shots": ["公路旅行", "营地生活", "自然景观", "弗恩的旅程"]
        },
        "the_rider": {
            "title": "骑士",
            "year": 2017,
            "visual_traits": ["草原", "马", "牛仔", "自然光"],
            "key_shots": ["骑马", "受伤", "日落", "身份认同"]
        },
        "eternals": {
            "title": "永恒族",
            "year": 2021,
            "visual_traits": ["自然光", "史诗风景", "IMAX", "神话"],
            "key_shots": ["巴比伦", "亚马逊", "现代城市", "宇宙"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["黄金", "大地色", "天空蓝", "暖橙", "自然绿"],
        "lighting_style": "黄金时刻自然光，柔和温暖",
        "composition": "人物在自然中，大量留白",
        "camera_movement": "稳定器跟随，环绕人物",
        "editing_rhythm": "舒缓，尊重时间"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["黄金时刻远景", "自然中景", "环境人像"],
        "frame_rate": "正常",
        "color_grading": "温暖自然，黄金色调",
        "typical_mood": "诗意、自由、怀旧、人文关怀"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "赵婷风格3×3",
        "description": "自然主义诗电影与边缘人群的人文关怀",
        "shots": [
            {
                "index": 1,
                "name": "黄金时刻风景",
                "shot_type": "大远景",
                "technique": "黄金时刻",
                "prompt": "Magic hour landscape, golden sunlight, vast American West, Chloé Zhao style, tiny figure in nature, warm tones, sense of freedom"
            },
            {
                "index": 2,
                "name": "人物与环境",
                "shot_type": "全景",
                "technique": "自然融合",
                "prompt": "Figure in environment, natural integration, Chloé Zhao composition, non-professional actor, documentary feel, golden hour"
            },
            {
                "index": 3,
                "name": "日常生活",
                "shot_type": "中景",
                "technique": "真实瞬间",
                "prompt": "Daily life moment, authentic performance, Chloé Zhao naturalism, available light, real location, unscripted feel"
            },
            {
                "index": 4,
                "name": "房车/移动",
                "shot_type": "运动镜头",
                "technique": "跟随",
                "prompt": "RV or vehicle on road, traveling shot, Chloé Zhao Nomadland aesthetic, landscape passing, freedom of movement"
            },
            {
                "index": 5,
                "name": "人物肖像",
                "shot_type": "近景",
                "technique": "自然光肖像",
                "prompt": "Environmental portrait, natural light on face, Chloé Zhao intimate style, weathered features, character study"
            },
            {
                "index": 6,
                "name": "营地/社群",
                "shot_type": "全景",
                "technique": "群体场景",
                "prompt": "Camp or community gathering, real people, Chloé Zhao social realism, firelight or sunset, authentic interactions"
            },
            {
                "index": 7,
                "name": "自然细节",
                "shot_type": "特写",
                "technique": "诗意细节",
                "prompt": "Nature detail close-up, tactile texture, Chloé Zhao poetic realism, wind, grass, or rock, contemplative"
            },
            {
                "index": 8,
                "name": "黄昏时刻",
                "shot_type": "远景",
                "technique": "日落",
                "prompt": "Sunset silhouette, end of day, Chloé Zhao melancholy beauty, warm colors fading, reflective mood"
            },
            {
                "index": 9,
                "name": "旅程继续",
                "shot_type": "远景",
                "technique": "开放结局",
                "prompt": "Journey continues, road ahead, Chloé Zhao open ending, dawn or dusk, hope and uncertainty, vast horizon"
            }
        ]
    }


# 导出
MODERN_DIRECTORS = {
    "villeneuve": VilleneuveStyle,
    "peele": PeeleStyle,
    "aster": AsterStyle,
    "eggers": EggersStyle,
    "zhao": ZhaoStyle
}


def get_modern_director_style(director_name: str):
    """获取现代导演风格"""
    return MODERN_DIRECTORS.get(director_name)


def list_modern_directors():
    """列出所有现代导演"""
    return list(MODERN_DIRECTORS.keys())
