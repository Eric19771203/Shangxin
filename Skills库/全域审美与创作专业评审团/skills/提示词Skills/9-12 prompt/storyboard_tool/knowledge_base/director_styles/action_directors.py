"""
动作片导演风格库
包含：昆汀·塔伦蒂诺
"""


class TarantinoStyle:
    """昆汀·塔伦蒂诺风格 - 暴力美学的电影极客"""
    
    INFO = {
        "name": "昆汀·塔伦蒂诺",
        "name_en": "Quentin Tarantino",
        "nationality": "美国",
        "active_period": "1990年代至今",
        "genre": "动作片/犯罪片/西部片",
        "style_keywords": ["非线性叙事", "暴力美学", "对话驱动", "迷影致敬", "黑色幽默"]
    }
    
    SIGNATURE_TECHNIQUES = {
        "non_linear_narrative": {
            "name": "非线性叙事",
            "description": "打乱时间顺序，章节式结构",
            "example": "《低俗小说》的时间跳跃",
            "application": "整体叙事结构"
        },
        "trunk_shot": {
            "name": "后备箱视角",
            "description": "从汽车后备箱内向上拍摄",
            "example": "《落水狗》《低俗小说》《杀死比尔》",
            "application": "紧张场景、绑架场景"
        },
        "long_take_dialogue": {
            "name": "长镜头对话",
            "description": "超长对话场景， often over mundane topics",
            "example": "《落水狗》的开场餐厅对话",
            "application": "角色塑造、张力建立"
        },
        "mexican_standoff": {
            "name": "墨西哥对峙",
            "description": "多方持枪互相瞄准的紧张对峙",
            "example": "《落水狗》《无耻混蛋》",
            "application": "高潮场景、紧张顶点"
        },
        "extreme_violence": {
            "name": "极端暴力",
            "description": "突然的极端暴力场面， often 与平静形成对比",
            "example": "《杀死比尔》的暴力场面",
            "application": "动作高潮、视觉冲击"
        },
        "pop_culture_dialogue": {
            "name": "流行文化对话",
            "description": "角色讨论电影、音乐等流行文化",
            "example": "《低俗小说》的足疗讨论",
            "application": "角色塑造、真实感"
        },
        "anachronistic_soundtrack": {
            "name": "时代错置配乐",
            "description": "使用与时代不符的音乐",
            "example": "《被解救的姜戈》的现代音乐",
            "application": "情绪调节、风格化"
        }
    }
    
    REPRESENTATIVE_WORKS = {
        "pulp_fiction": {
            "title": "低俗小说",
            "year": 1994,
            "visual_traits": ["非线性叙事", "黑色幽默", "对话驱动", "流行文化"],
            "key_shots": ["开场餐厅", "肾上腺素注射", "舞蹈场景", "后备箱视角"]
        },
        "kill_bill": {
            "title": "杀死比尔",
            "year": 2003,
            "visual_traits": ["武侠致敬", "动漫风格", "血浆暴力", "日本美学"],
            "key_shots": ["青叶屋大战", "雪地决斗", "动画段落", "五人组介绍"]
        },
        "reservoir_dogs": {
            "title": "落水狗",
            "year": 1992,
            "visual_traits": ["单一场景", "时间跳跃", "血腥", "西装美学"],
            "key_shots": ["开场对话", "仓库折磨", "慢动作出场", "血泊中的白先生"]
        },
        "inglourious_basterds": {
            "title": "无耻混蛋",
            "year": 2009,
            "visual_traits": ["历史改写", "多语言", "紧张对话", "暴力释放"],
            "key_shots": ["开场农场", "地下室酒吧", "电影院结局", "犹太熊"]
        }
    }
    
    VISUAL_CHARACTERISTICS = {
        "color_palette": ["血红色", "霓虹色", "复古黄", "高饱和", "黑白"],
        "lighting_style": "戏剧化照明， often 使用彩色光源",
        "composition": "宽银幕构图，中心人物，复古美学",
        "camera_movement": "流畅运动，突然静止，荷兰角",
        "editing_rhythm": "非线性，章节标题，音乐驱动剪辑"
    }
    
    STORYBOARD_CHARACTERISTICS = {
        "shot_types": ["中景", "特写", "荷兰角"],
        "frame_rate": "正常，偶尔慢动作",
        "color_grading": "高饱和，复古感，或黑白",
        "typical_mood": "酷、暴力、幽默、怀旧"
    }
    
    STORYBOARD_3X3 = {
        "template_name": "昆汀·塔伦蒂诺风格3×3",
        "description": "暴力美学与流行文化的电影致敬",
        "shots": [
            {
                "index": 1,
                "name": "慢动作出场",
                "shot_type": "全景",
                "technique": "慢动作+配乐",
                "prompt": "Slow motion group walk, cool characters in formation, anachronistic soundtrack, Tarantino style intro, confident swagger, cinematic wide shot"
            },
            {
                "index": 2,
                "name": "后备箱视角",
                "shot_type": "低角度",
                "technique": "POV from trunk",
                "prompt": "Trunk shot looking up, characters looking down into trunk, low angle, dramatic lighting, Tarantino signature shot, tense moment"
            },
            {
                "index": 3,
                "name": "对话场景",
                "shot_type": "双人",
                "technique": "长镜头对话",
                "prompt": "Two shot dialogue scene, characters discussing pop culture, diner or bar setting, Tarantino conversational style, naturalistic but stylized"
            },
            {
                "index": 4,
                "name": "暴力瞬间",
                "shot_type": "特写",
                "technique": "突然暴力",
                "prompt": "Extreme close-up of violent action, blood spray, sudden shift from calm, Tarantino shock moment, high impact"
            },
            {
                "index": 5,
                "name": "墨西哥对峙",
                "shot_type": "全景",
                "technique": "多方对峙",
                "prompt": "Wide shot Mexican standoff, multiple characters with guns aimed, circular composition, Tarantino tension moment, dramatic lighting"
            },
            {
                "index": 6,
                "name": "荷兰角紧张",
                "shot_type": "中景",
                "technique": "荷兰角",
                "prompt": "Dutch angle medium shot, psychological tension, disorienting composition, Tarantino stylistic choice, impending violence"
            },
            {
                "index": 7,
                "name": "章节标题",
                "shot_type": "文字卡",
                "technique": "标题卡",
                "prompt": "Chapter title card, bold typography, retro design, Tarantino chapter marker, film grain texture"
            },
            {
                "index": 8,
                "name": "复古特写",
                "shot_type": "特写",
                "technique": "复古滤镜",
                "prompt": "Close-up with retro color grading, saturated colors, film grain, Tarantino vintage aesthetic, character detail"
            },
            {
                "index": 9,
                "name": "血腥结局",
                "shot_type": "俯拍",
                "technique": "血浆美学",
                "prompt": "Overhead shot of aftermath, bodies and blood, artistic composition of violence, Tarantino blood opera, dramatic lighting"
            }
        ]
    }


# 导出
ACTION_DIRECTORS = {
    "tarantino": TarantinoStyle
}


def get_action_director_style(director_name: str):
    """获取动作片导演风格"""
    return ACTION_DIRECTORS.get(director_name)


def list_action_directors():
    """列出所有动作片导演"""
    return list(ACTION_DIRECTORS.keys())
