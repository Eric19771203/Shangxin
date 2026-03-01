"""
电影分类知识库 - 战争片
包含战争片的叙事特点、分镜技巧、经典参考等
"""

from typing import List, Dict, Any


class WarFilmKnowledge:
    """战争片知识库"""
    
    # 类型特点
    CHARACTERISTICS = {
        "name": "战争片",
        "description": "以战争为背景，展现人性、英雄主义与悲剧",
        "key_elements": [
            "大规模场面调度",
            "多线叙事结构",
            "紧张的节奏控制",
            "真实感与沉浸感",
            "人性深度挖掘"
        ],
        "typical_duration": "90-180分钟",
        "typical_shot_count": "800-2000+个镜头",
        "pacing": "快慢交替，张弛有度"
    }
    
    # 分镜要点
    SHOT_TECHNIQUES = {
        "establishing_shots": {
            "description": "战场环境建立",
            "techniques": [
                "大远景展现战场规模",
                "航拍展示战略布局",
                "烟雾/火光增强氛围",
                "广角镜头增强空间感"
            ],
            "equipment": ["无人机", "广角镜头(16-24mm)", "稳定器"],
            "examples": ["《敦刻尔克》海滩全景", "《拯救大兵瑞恩》诺曼底登陆开场"]
        },
        "action_sequences": {
            "description": "战斗场面",
            "techniques": [
                "手持镜头增强真实感",
                "快速剪辑（1-3秒/镜）",
                "多机位覆盖",
                "主观镜头增强沉浸",
                "爆炸/冲击特写"
            ],
            "equipment": ["手持云台", "高速摄影机", "多机位同步"],
            "examples": ["《血战钢锯岭》冲锋场面", "《1917》一镜到底"]
        },
        "character_moments": {
            "description": "人物刻画",
            "techniques": [
                "特写捕捉微表情",
                "过肩镜头建立关系",
                "眼神特写传达恐惧/决心",
                "慢动作强调关键时刻"
            ],
            "equipment": ["长焦镜头(85-135mm)", "高速摄影"],
            "examples": ["《敦刻尔克》飞行员特写", "《钢琴家》饥饿眼神"]
        },
        "tension_building": {
            "description": "紧张感营造",
            "techniques": [
                "低角度仰拍增强压迫感",
                "阴影与剪影",
                "环境音铺垫",
                "静默后突然爆发"
            ],
            "equipment": ["低角度支架", "遮光板"],
            "examples": ["《猎杀U-571》潜艇内部", "《拆弹部队》排弹场景"]
        }
    }
    
    # 经典参考
    REFERENCES = {
        "saving_private_yan": {
            "title": "拯救大兵瑞恩",
            "director": "史蒂文·斯皮尔伯格",
            "year": 1998,
            "techniques": [
                "手持摄影增强真实感",
                " desaturated色调",
                "快速剪辑",
                "主观视角"
            ],
            "notable_scenes": [
                "诺曼底登陆开场（27分钟）",
                "狙击手对决",
                "最后的桥战"
            ],
            "shot_count": "约1200个镜头"
        },
        "dunkirk": {
            "title": "敦刻尔克",
            "director": "克里斯托弗·诺兰",
            "year": 2017,
            "techniques": [
                "三线叙事（海/陆/空时间维度交错）",
                "IMAX胶片拍摄",
                "实景特效",
                "极简对白"
            ],
            "notable_scenes": [
                "海滩撤退全景",
                "空中狗斗",
                "民用船救援"
            ],
            "shot_count": "约800个镜头"
        },
        "1917": {
            "title": "1917",
            "director": "萨姆·门德斯",
            "year": 2019,
            "techniques": [
                "一镜到底（伪长镜头）",
                "实时叙事",
                "精确的舞台调度",
                "沉浸式体验"
            ],
            "notable_scenes": [
                "穿越无人区",
                "燃烧的教堂",
                "河流漂流"
            ],
            "shot_count": "约50个长镜头（剪辑后）"
        },
        "come_and_see": {
            "title": "自己去看",
            "director": "依莱姆·克里莫夫",
            "year": 1985,
            "techniques": [
                "极端特写",
                "自然光运用",
                "主观视角",
                "心理写实"
            ],
            "notable_scenes": [
                "村庄屠杀",
                "森林逃亡",
                "最终崩溃"
            ],
            "shot_count": "约600个镜头"
        }
    }
    
    # 叙事结构模板
    NARRATIVE_TEMPLATES = {
        "classic_war": {
            "name": "经典战争叙事",
            "description": "任务驱动型叙事",
            "structure": [
                {"act": "第一幕", "content": "建立任务/征召", "shots": "远景-全景-中景"},
                {"act": "第二幕A", "content": "执行任务，遭遇阻碍", "shots": "中景-近景-特写"},
                {"act": "第二幕B", "content": "最大危机，同伴牺牲", "shots": "特写-慢动作-全景"},
                {"act": "第三幕", "content": "最终战斗，代价与反思", "shots": "全景-特写-远景"}
            ]
        },
        "ensemble_war": {
            "name": "群像战争叙事",
            "description": "多人物视角展现战争全貌",
            "structure": [
                {"act": "第一幕", "content": "多线人物建立", "shots": "平行剪辑"},
                {"act": "第二幕", "content": "命运交织，战场相遇", "shots": "交叉剪辑"},
                {"act": "第三幕", "content": "共同面对，各自结局", "shots": "汇聚与分离"}
            ]
        },
        "survival_war": {
            "name": "生存战争叙事",
            "description": "聚焦个体生存体验",
            "structure": [
                {"act": "第一幕", "content": "平静生活被打破", "shots": "从静到动"},
                {"act": "第二幕", "content": "逃亡与求生", "shots": "紧张跟随"},
                {"act": "第三幕", "content": "失去与幸存", "shots": "从动到静"}
            ]
        }
    }
    
    # 3×3分镜模板
    STORYBOARD_3X3 = {
        "template_name": "战争片标准3×3",
        "shots": [
            # 第一行：战场建立
            {
                "index": 1,
                "name": "战场全景",
                "shot_type": "大远景(ELS)",
                "angle": "俯视或平视",
                "movement": "缓慢横移或固定",
                "description": "展现战场规模，烟雾弥漫，远处火光",
                "sound": "环境音：炮火轰鸣，飞机轰鸣",
                "color": "desaturated，偏灰蓝或土黄",
                "prompt": "Epic war scene, vast battlefield, smoke and fire in distance, desaturated colors, cinematic wide shot, IMAX quality, atmospheric haze"
            },
            {
                "index": 2,
                "name": "士兵入场",
                "shot_type": "全景(FS)",
                "angle": "平视或略低角度",
                "movement": "跟随士兵移动",
                "description": "士兵们列队或行进，装备齐全",
                "sound": "脚步声，装备碰撞声，低声交谈",
                "color": "军装色调，泥土色",
                "prompt": "Soldiers in formation, full body shot, military uniforms, equipment details, gritty texture, natural lighting, documentary style"
            },
            {
                "index": 3,
                "name": "战友情谊",
                "shot_type": "中全景(MLS)",
                "angle": "平视",
                "movement": "轻微横移",
                "description": "士兵之间互动，检查装备，眼神交流",
                "sound": "对话，装备检查声",
                "color": "温暖色调，人性化光线",
                "prompt": "Soldiers interacting, checking equipment, camaraderie moment, medium wide shot, warm lighting, human connection"
            },
            # 第二行：战斗爆发
            {
                "index": 4,
                "name": "战斗开始",
                "shot_type": "中景(MS)",
                "angle": "动态角度",
                "movement": "手持跟拍",
                "description": "冲锋或躲避，动作开始",
                "sound": "枪声，爆炸声，喊叫声",
                "color": "高对比度，烟雾影响",
                "prompt": "Combat action, soldiers running, handheld camera, dynamic movement, dust and smoke, intense action, shaky cam"
            },
            {
                "index": 5,
                "name": "生死瞬间",
                "shot_type": "中近景(MCU)",
                "angle": "特写角度",
                "movement": "快速推拉",
                "description": "士兵表情特写，恐惧与决心",
                "sound": "心跳声，呼吸声，慢动作音效",
                "color": "面部特写，汗水与泥土",
                "prompt": "Soldier's face close-up, intense emotion, fear and determination, sweat and dirt, shallow depth of field, dramatic lighting"
            },
            {
                "index": 6,
                "name": "武器特写",
                "shot_type": "近景(CU)",
                "angle": "细节角度",
                "movement": "固定或微动",
                "description": "武器操作，弹药装填，细节动作",
                "sound": "机械声，金属碰撞",
                "color": "金属质感，磨损痕迹",
                "prompt": "Weapon detail close-up, loading ammunition, mechanical parts, worn metal texture, macro shot, tactile details"
            },
            # 第三行：战争反思
            {
                "index": 7,
                "name": "象征物品",
                "shot_type": "特写A(ECU)",
                "angle": "细节特写",
                "movement": "缓慢推进",
                "description": "信件、照片、护身符等象征物",
                "sound": "静默或微弱环境音",
                "color": "温暖色调，怀旧感",
                "prompt": "Symbolic object extreme close-up, letter or photograph, worn edges, emotional weight, soft focus background, sentimental lighting"
            },
            {
                "index": 8,
                "name": "眼神空洞",
                "shot_type": "特写B(ECU)",
                "angle": "眼睛特写",
                "movement": "固定",
                "description": "战后创伤，空洞眼神",
                "sound": "耳鸣声，静默",
                "color": "冷色调，眼神反光",
                "prompt": "Eyes extreme close-up, thousand-yard stare, PTSD expression, reflection in eyes, cold color grading, haunting gaze"
            },
            {
                "index": 9,
                "name": "战后废墟",
                "shot_type": "远景(LS)",
                "angle": "高角度或平视",
                "movement": "缓慢横移或固定",
                "description": "战场废墟，尸体，幸存者",
                "sound": "寂静，风声，远处呻吟",
                "color": "desaturated，灰色调",
                "prompt": "Post-battle landscape, ruins and devastation, survivors among wreckage, wide shot, desaturated colors, somber atmosphere, overcast sky"
            }
        ]
    }
    
    # 4×3分镜模板（史诗节奏）
    STORYBOARD_4X3 = {
        "template_name": "战争片史诗4×3",
        "description": "适用于宏大战争史诗的12格结构",
        "rows": [
            {
                "name": "战争机器",
                "shots": [
                    {
                        "index": 1,
                        "name": "世界全景",
                        "shot_type": "大远景",
                        "prompt": "World war panorama, multiple battlefronts, strategic overview, map-like perspective, epic scale"
                    },
                    {
                        "index": 2,
                        "name": "军队集结",
                        "shot_type": "远景",
                        "prompt": "Army mobilization, thousands of soldiers, military vehicles, organized chaos, aerial view"
                    },
                    {
                        "index": 3,
                        "name": "战前准备",
                        "shot_type": "远景/全景",
                        "prompt": "Pre-battle preparation, trenches, equipment check, tense atmosphere, dawn lighting"
                    },
                    {
                        "index": 4,
                        "name": "指挥所",
                        "shot_type": "全景",
                        "prompt": "Command center, maps and radios, officers planning, strategic atmosphere, interior lighting"
                    }
                ]
            },
            {
                "name": "前线士兵",
                "shots": [
                    {
                        "index": 5,
                        "name": "士兵群像",
                        "shot_type": "全景",
                        "prompt": "Soldiers in trenches, diverse faces, waiting for orders, documentary style, natural light"
                    },
                    {
                        "index": 6,
                        "name": "小队互动",
                        "shot_type": "中全景",
                        "prompt": "Squad camaraderie, sharing rations, nervous laughter, medium wide, warm tones"
                    },
                    {
                        "index": 7,
                        "name": "命令下达",
                        "shot_type": "中景",
                        "prompt": "Officer giving orders, soldiers listening, tension building, over-shoulder shots"
                    },
                    {
                        "index": 8,
                        "name": "冲锋时刻",
                        "shot_type": "中近景",
                        "prompt": "Going over the top, charging forward, intense action, handheld camera, dust and smoke"
                    }
                ]
            },
            {
                "name": "战争创伤",
                "shots": [
                    {
                        "index": 9,
                        "name": "战场医疗",
                        "shot_type": "近景",
                        "prompt": "Field hospital, medic treating wound, blood and bandages, intense close-up"
                    },
                    {
                        "index": 10,
                        "name": "死亡特写",
                        "shot_type": "特写",
                        "prompt": "Death moment, life leaving eyes, extreme close-up, slow motion, haunting"
                    },
                    {
                        "index": 11,
                        "name": "幸存者",
                        "shot_type": "大特写",
                        "prompt": "Survivor's face, thousand-yard stare, PTSD, extreme close-up, hollow eyes"
                    },
                    {
                        "index": 12,
                        "name": "无尽战争",
                        "shot_type": "远景/空镜",
                        "prompt": "Empty battlefield, smoke clearing, sunset or dawn, poetic wide shot, melancholic beauty"
                    }
                ]
            }
        ]
    }
    
    @classmethod
    def get_all_techniques(cls) -> Dict:
        """获取所有技巧"""
        return cls.SHOT_TECHNIQUES
    
    @classmethod
    def get_references(cls) -> Dict:
        """获取经典参考"""
        return cls.REFERENCES
    
    @classmethod
    def get_storyboard_template(cls, board_type: str = "3x3") -> Dict:
        """获取分镜模板"""
        if board_type == "3x3":
            return cls.STORYBOARD_3X3
        elif board_type == "4x3":
            return cls.STORYBOARD_4X3
        return cls.STORYBOARD_3X3


# 便捷函数
def get_war_film_info() -> Dict:
    """获取战争片基本信息"""
    return WarFilmKnowledge.CHARACTERISTICS


def get_war_techniques() -> Dict:
    """获取战争片拍摄技巧"""
    return WarFilmKnowledge.get_all_techniques()


def get_war_references() -> Dict:
    """获取经典战争片参考"""
    return WarFilmKnowledge.get_references()


def get_war_storyboard(board_type: str = "3x3") -> Dict:
    """获取战争片分镜模板"""
    return WarFilmKnowledge.get_storyboard_template(board_type)


if __name__ == "__main__":
    print("=== 战争片知识库 ===")
    info = get_war_film_info()
    print(f"类型: {info['name']}")
    print(f"描述: {info['description']}")
    print(f"关键元素: {', '.join(info['key_elements'])}")
    
    print("\n=== 经典参考 ===")
    refs = get_war_references()
    for key, ref in refs.items():
        print(f"《{ref['title']}》({ref['year']}) - {ref['director']}")
