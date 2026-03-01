"""
分镜理论知识库
==============
按主题组织的分镜理论知识体系

知识分类：
1. 构图原理 - 画面布局、平衡、视觉引导
2. 镜头语言 - 景别、角度、运动的叙事功能
3. 剪辑理论 - 连续性、节奏、转场
4. 空间设计 - 轴线、180度规则、视线匹配
5. 时间控制 - 节奏、时间压缩/延展
6. 情感表达 - 视觉情感、色彩心理学
"""

from typing import Dict, List, Optional, Any


# 知识库主结构
KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    "构图原理": {
        "description": "画面布局的基本原理和视觉组织方法",
        "principles": {
            "三分法则": {
                "definition": "将画面分为九宫格，重要元素放在交点或线上",
                "application": "人物位置、地平线放置、视觉焦点",
                "examples": ["人物眼睛位于上三分线", "地平线位于下三分线"],
                "books": ["block_visual_story", "zeng_storyboard"]
            },
            "黄金分割": {
                "definition": "1:1.618的比例关系，自然界最美的比例",
                "application": "画面分割、螺旋构图、斐波那契数列",
                "examples": ["螺旋线引导视线", "黄金矩形构图"],
                "books": ["block_visual_story"]
            },
            "对称与平衡": {
                "definition": "画面的视觉重量分布",
                "application": "正式/非正式平衡、对称构图、动态平衡",
                "examples": ["对称构图表现稳定", "非对称平衡创造动感"],
                "books": ["block_visual_story", "katz_film_directing"]
            },
            "视觉引导线": {
                "definition": "利用线条引导观众视线",
                "application": "道路、栏杆、视线方向、光影线条",
                "examples": ["S型曲线引导", "汇聚线创造深度"],
                "books": ["block_visual_story"]
            },
            "框架内框架": {
                "definition": "利用前景元素创造画中画效果",
                "application": "门窗、拱门、树枝、阴影",
                "examples": ["透过窗户拍摄", "镜子反射构图"],
                "books": ["katz_film_directing"]
            }
        }
    },
    
    "镜头语言": {
        "description": "不同镜头类型的叙事功能和情感表达",
        "principles": {
            "景别叙事": {
                "definition": "不同景别的情感距离和信息披露",
                "application": "大远景-环境，特写-情感，中景-关系",
                "examples": ["特写表现内心", "远景强调孤独"],
                "books": ["katz_film_directing", "bordwell_film_art"]
            },
            "角度心理": {
                "definition": "摄影机角度的权力和情感暗示",
                "application": "仰拍-力量，俯拍-弱小，平视-平等",
                "examples": ["仰拍反派增强威胁", "俯拍受害者表现无助"],
                "books": ["katz_film_directing"]
            },
            "运动功能": {
                "definition": "摄影机运动的叙事目的",
                "application": "推-强调，拉-环境，摇-空间，移-跟随",
                "examples": ["推镜强调情感", "横移展现场景"],
                "books": ["katz_film_directing", "lumet_directing"]
            },
            "景深叙事": {
                "definition": "利用景深控制信息层次",
                "application": "深焦-关系，浅焦-隔离，变焦-注意",
                "examples": ["深焦表现人物关系", "浅焦突出主体"],
                "books": ["brown_cinematography"]
            }
        }
    },
    
    "剪辑理论": {
        "description": "镜头组接的原理和技巧",
        "principles": {
            "连续性剪辑": {
                "definition": "保持时间、空间、动作连贯的剪辑方式",
                "application": "动作匹配、视线匹配、轴线规则",
                "examples": ["开门动作的连续性", "对话的视线匹配"],
                "books": ["murch_in_blink", "bordwell_film_art"]
            },
            "剪辑六原则": {
                "definition": "Walter Murch提出的剪辑决策标准",
                "application": "情感51%，故事23%，节奏10%，视线7%，二维特性5%，三维连贯4%",
                "examples": ["情感优先原则", "眨眼理论应用"],
                "books": ["murch_in_blink"]
            },
            "节奏控制": {
                "definition": "通过剪辑控制时间感和情绪节奏",
                "application": "长镜头-沉思，短切-紧张，渐快-高潮",
                "examples": ["追逐戏的加速剪辑", "对话戏的舒缓节奏"],
                "books": ["murch_in_blink", "block_visual_story"]
            },
            "转场技巧": {
                "definition": "镜头之间过渡的方式",
                "application": "切-标准，叠-时间，划-风格，淡-情绪",
                "examples": ["匹配剪辑", "跳切表现时间流逝"],
                "books": ["murch_in_blink"]
            }
        }
    },
    
    "空间设计": {
        "description": "三维空间在二维画面中的呈现",
        "principles": {
            "180度规则": {
                "definition": "对话场景中保持空间一致性的轴线规则",
                "application": "对话场景、动作场景、关系场景",
                "examples": ["双人对话的轴线", "越轴的特殊效果"],
                "books": ["katz_film_directing", "bordwell_film_art"]
            },
            "视线匹配": {
                "definition": "保持角色视线方向一致性的原则",
                "application": "对话剪辑、反应镜头、视线引导",
                "examples": ["A看右，B看左", "视线方向与画面位置"],
                "books": ["katz_film_directing", "murch_in_blink"]
            },
            "动作轴线": {
                "definition": "保持运动方向一致性的轴线",
                "application": "追逐戏、运动场景、车辆移动",
                "examples": ["从左到右的运动", "越轴表现方向改变"],
                "books": ["katz_film_directing"]
            },
            "三角原则": {
                "definition": "三人对话场景的摄影机位置原则",
                "application": "三人对话、群体场景",
                "examples": ["内反拍", "外反拍", "平行机位"],
                "books": ["katz_film_directing"]
            }
        }
    },
    
    "时间控制": {
        "description": "电影时间的压缩、延展和操控",
        "principles": {
            "时间压缩": {
                "definition": "通过剪辑缩短实际时间",
                "application": "旅行蒙太奇、时间流逝、过程简化",
                "examples": ["四季变化的蒙太奇", "城市到乡村的旅程"],
                "books": ["bordwell_film_art"]
            },
            "时间延展": {
                "definition": "通过剪辑延长实际时间",
                "application": "慢动作、多角度重复、内心时间",
                "examples": ["子弹时间的多角度", "关键时刻的慢动作"],
                "books": ["bordwell_film_art"]
            },
            "交叉剪辑": {
                "definition": "交替展示两个或多个同时发生的事件",
                "application": "最后一分钟营救、平行叙事、对比",
                "examples": ["格里菲斯式营救", "婚礼与葬礼的对比"],
                "books": ["bordwell_film_art"]
            },
            "节奏模式": {
                "definition": "建立和打破节奏预期的技巧",
                "application": "渐强、突停、对比、重复",
                "examples": ["追逐戏的加速", "爆炸后的静默"],
                "books": ["block_visual_story"]
            }
        }
    },
    
    "情感表达": {
        "description": "通过视觉元素传达情感",
        "principles": {
            "色彩心理学": {
                "definition": "不同色彩的情感和文化含义",
                "application": "红色-激情/危险，蓝色-冷静/忧郁，黄色-快乐/警示",
                "examples": ["《辛德勒的名单》红衣女孩", "《美国丽人》红色玫瑰"],
                "books": ["block_visual_story", "brown_cinematography"]
            },
            "光影情感": {
                "definition": "光线质量和方向的情感暗示",
                "application": "高调-喜剧/希望，低调-惊悚/神秘，侧光-戏剧",
                "examples": ["黑色电影的高对比", "恐怖片的底光"],
                "books": ["brown_cinematography"]
            },
            "空间情感": {
                "definition": "空间大小和封闭性的情感",
                "application": "开放空间-自由，封闭空间-压抑，狭窄空间-紧张",
                "examples": ["《闪灵》的广阔酒店", "《活埋》的封闭棺材"],
                "books": ["block_visual_story"]
            },
            "视觉隐喻": {
                "definition": "通过视觉元素暗示抽象概念",
                "application": "镜子-自我，窗户-窥视，门-机会/危险",
                "examples": ["《黑天鹅》的镜子", "《后窗》的窗户"],
                "books": ["bordwell_film_art"]
            }
        }
    },
    
    "场面调度": {
        "description": "演员、摄影机、场景的综合安排",
        "principles": {
            "演员走位": {
                "definition": "演员在场景中的移动设计",
                "application": "揭示关系、创造张力、引导视线",
                "examples": ["从远到近的接近", "围绕的压迫感"],
                "books": ["katz_film_directing", "lumet_directing"]
            },
            "摄影机调度": {
                "definition": "摄影机与演员的相对运动",
                "application": "跟随、阻挡、揭示、强调",
                "examples": ["环绕拍摄", "后退揭示环境"],
                "books": ["katz_film_directing"]
            },
            "场景设计": {
                "definition": "布景和道具的叙事功能",
                "application": "时代背景、人物性格、情节暗示",
                "examples": ["《教父》的昏暗办公室", "《布达佩斯大饭店》的对称布景"],
                "books": ["lumet_directing"]
            }
        }
    }
}


def get_theory_by_topic(topic: str) -> Optional[Dict[str, Any]]:
    """获取特定主题的理论知识"""
    return KNOWLEDGE_BASE.get(topic)


def search_knowledge(keyword: str) -> List[Dict[str, Any]]:
    """
    搜索知识库
    
    Args:
        keyword: 搜索关键词
        
    Returns:
        匹配的知识条目列表
    """
    results = []
    keyword_lower = keyword.lower()
    
    for topic, data in KNOWLEDGE_BASE.items():
        # 搜索主题名
        if keyword_lower in topic.lower():
            results.append({
                "type": "topic",
                "name": topic,
                "description": data["description"],
                "data": data
            })
            continue
        
        # 搜索原理
        for principle_name, principle_data in data.get("principles", {}).items():
            if keyword_lower in principle_name.lower():
                results.append({
                    "type": "principle",
                    "topic": topic,
                    "name": principle_name,
                    "data": principle_data
                })
                continue
            
            # 搜索定义
            if keyword_lower in principle_data.get("definition", "").lower():
                results.append({
                    "type": "principle",
                    "topic": topic,
                    "name": principle_name,
                    "data": principle_data
                })
                continue
            
            # 搜索应用
            if any(keyword_lower in app.lower() for app in principle_data.get("application", "")):
                results.append({
                    "type": "principle",
                    "topic": topic,
                    "name": principle_name,
                    "data": principle_data
                })
    
    return results


def get_principle_detail(topic: str, principle: str) -> Optional[Dict[str, Any]]:
    """获取特定原理的详细信息"""
    topic_data = KNOWLEDGE_BASE.get(topic)
    if topic_data:
        return topic_data.get("principles", {}).get(principle)
    return None


def list_all_topics() -> List[str]:
    """列出所有知识主题"""
    return list(KNOWLEDGE_BASE.keys())


def get_related_books(topic: str, principle: Optional[str] = None) -> List[str]:
    """获取相关的参考书籍ID"""
    if principle:
        detail = get_principle_detail(topic, principle)
        if detail:
            return detail.get("books", [])
    
    topic_data = KNOWLEDGE_BASE.get(topic)
    if topic_data:
        books = set()
        for p_data in topic_data.get("principles", {}).values():
            books.update(p_data.get("books", []))
        return list(books)
    
    return []


def apply_theory_to_storyboard(theory_topic: str, 
                                theory_principle: str,
                                context: Dict[str, Any]) -> Dict[str, Any]:
    """
    将理论应用到分镜创作
    
    Args:
        theory_topic: 理论主题
        theory_principle: 具体原理
        context: 创作上下文 {scene_type, emotion, characters, etc.}
        
    Returns:
        应用建议和示例
    """
    principle_data = get_principle_detail(theory_topic, theory_principle)
    if not principle_data:
        return {"error": "未找到指定理论"}
    
    return {
        "theory": f"{theory_topic} - {theory_principle}",
        "definition": principle_data.get("definition"),
        "application": principle_data.get("application"),
        "examples": principle_data.get("examples", []),
        "suggestions": generate_application_suggestions(
            theory_topic, theory_principle, context
        ),
        "reference_books": principle_data.get("books", [])
    }


def generate_application_suggestions(topic: str, 
                                     principle: str, 
                                     context: Dict[str, Any]) -> List[str]:
    """生成应用建议"""
    suggestions = []
    scene_type = context.get("scene_type", "")
    emotion = context.get("emotion", "")
    
    # 根据主题生成建议
    if topic == "构图原理":
        if principle == "三分法则":
            suggestions.append("将主要人物放在画面左侧或右侧三分线上")
            suggestions.append("地平线避免放在画面正中，选择上下三分线")
        elif principle == "视觉引导线":
            suggestions.append("利用场景中的道路、栏杆引导观众视线到主体")
    
    elif topic == "镜头语言":
        if principle == "景别叙事":
            if emotion == "亲密":
                suggestions.append("使用特写或极特写表现情感")
            elif emotion == "孤独":
                suggestions.append("使用大远景强调人物的渺小")
        elif principle == "角度心理":
            if context.get("power_dynamic") == "强势":
                suggestions.append("使用仰拍增强人物的权威感")
    
    elif topic == "剪辑理论":
        if principle == "节奏控制":
            if emotion == "紧张":
                suggestions.append("使用短镜头快速剪辑")
                suggestions.append("逐渐加快剪辑速度推向高潮")
    
    elif topic == "空间设计":
        if principle == "180度规则":
            suggestions.append("在对话场景中保持摄影机在同一侧")
            suggestions.append("如需越轴，使用特写或中性镜头过渡")
    
    elif topic == "情感表达":
        if principle == "色彩心理学":
            if emotion == "激情":
                suggestions.append("使用红色或暖色调增强情感")
            elif emotion == "忧郁":
                suggestions.append("使用蓝色或冷色调营造氛围")
    
    return suggestions if suggestions else ["参考示例和书籍获取更具体的应用方法"]


# 快速参考表
QUICK_REFERENCE = {
    "对话场景": {
        "构图": ["过肩镜头", "单人镜头", "双人镜头"],
        "规则": ["180度规则", "视线匹配", "三角原则"],
        "技巧": ["反应镜头", "插入镜头", "切出镜头"]
    },
    "动作场景": {
        "构图": ["动态构图", "留白", "运动方向"],
        "规则": ["动作轴线", "连续性"],
        "技巧": ["跟随拍摄", "多角度覆盖", "慢动作强调"]
    },
    "情感场景": {
        "构图": ["特写", "浅景深", "框架构图"],
        "规则": ["情感优先", "节奏控制"],
        "技巧": ["推镜强调", "眼神光", "色彩情绪"]
    },
    "转场": {
        "类型": ["切", "叠化", "划", "淡入淡出"],
        "技巧": ["匹配剪辑", "声音桥", "相似性转场"],
        "创意": ["物体匹配", "颜色匹配", "动作匹配"]
    }
}


def get_quick_reference(scene_type: str) -> Optional[Dict[str, List[str]]]:
    """获取快速参考"""
    return QUICK_REFERENCE.get(scene_type)
