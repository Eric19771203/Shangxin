"""
视觉术语词典
用于统一分镜创作中的视觉语言，确保术语使用的准确性和一致性
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum


class TermCategory(Enum):
    """术语分类"""
    COMPOSITION = "构图"
    CAMERA = "摄影机"
    LIGHTING = "灯光"
    COLOR = "色彩"
    MOVEMENT = "运动"
    PERSPECTIVE = "视角"
    DEPTH = "景深"
    FRAMING = "景别"
    ANGLE = "角度"
    TRANSITION = "转场"
    EFFECT = "特效"
    STAGING = "场面调度"


@dataclass
class VisualTerm:
    """视觉术语定义"""
    term: str                          # 术语名称
    english: str                       # 英文名称
    category: TermCategory             # 分类
    definition: str                    # 定义
    visual_description: str            # 视觉描述
    usage_scenarios: List[str]         # 使用场景
    related_terms: List[str]           # 相关术语
    examples: List[str]                # 示例影片
    technical_notes: str = ""          # 技术要点
    common_mistakes: List[str] = field(default_factory=list)  # 常见误区
    ai_prompt_keywords: List[str] = field(default_factory=list)  # AI提示词关键词


# ==================== 构图术语 ====================
COMPOSITION_TERMS: Dict[str, VisualTerm] = {
    "三分法": VisualTerm(
        term="三分法",
        english="Rule of Thirds",
        category=TermCategory.COMPOSITION,
        definition="将画面横竖各分为三等份，将主体放置在交叉点或线上，创造平衡且富有动感的构图",
        visual_description="画面被两条水平线和两条垂直线均分为九宫格，视觉焦点位于线条交点",
        usage_scenarios=[
            "人物访谈画面",
            "风景摄影",
            "对话场景",
            "建立镜头"
        ],
        related_terms=["黄金分割", "九宫格", "视觉重心"],
        examples=["《美国丽人》", "《布达佩斯大饭店》", "《教父》"],
        technical_notes="避免将主体完全居中，除非追求对称或正式感",
        common_mistakes=["过度机械使用", "忽视背景元素", "不考虑运动方向"],
        ai_prompt_keywords=["rule of thirds composition", "off-center framing", "balanced asymmetry"]
    ),
    
    "黄金分割": VisualTerm(
        term="黄金分割",
        english="Golden Ratio / Golden Section",
        category=TermCategory.COMPOSITION,
        definition="按照1:1.618的比例分割画面，被认为是最具美感的构图比例",
        visual_description="螺旋线或矩形网格引导视线从画面一角自然流动到主体",
        usage_scenarios=[
            "艺术电影",
            "海报设计",
            "开场画面",
            "关键情感时刻"
        ],
        related_terms=["三分法", "斐波那契螺旋", "动态对称"],
        examples=["《达芬奇密码》", "《2001太空漫游》", "《黑天鹅》"],
        technical_notes="可以使用黄金螺旋或黄金矩形两种形式",
        ai_prompt_keywords=["golden ratio composition", "fibonacci spiral", "divine proportion"]
    ),
    
    "对称构图": VisualTerm(
        term="对称构图",
        english="Symmetrical Composition",
        category=TermCategory.COMPOSITION,
        definition="画面左右或上下完全对称，营造秩序感、稳定感或超现实感",
        visual_description="画面中心轴线两侧元素镜像对称，强调几何秩序",
        usage_scenarios=[
            "韦斯·安德森风格",
            "建筑展示",
            "仪式场景",
            "心理惊悚暗示"
        ],
        related_terms=["中心构图", "轴线", "平衡"],
        examples=["《布达佩斯大饭店》", "《闪灵》", "《黑天鹅》"],
        technical_notes="严格对称可能显得呆板，可通过细微差异增加趣味",
        ai_prompt_keywords=["symmetrical framing", "centered composition", "mirror image"]
    ),
    
    "引导线": VisualTerm(
        term="引导线",
        english="Leading Lines",
        category=TermCategory.COMPOSITION,
        definition="利用画面中的线条元素引导观众视线指向主体或画面深处",
        visual_description="道路、栏杆、建筑线条等形成视觉路径，指向画面焦点",
        usage_scenarios=[
            "建立镜头",
            "追踪场景",
            "揭示画面",
            "创造纵深感"
        ],
        related_terms=["纵深", "透视", "视觉动线"],
        examples=["《美国丽人》玫瑰场景", "《盗梦空间》", "《银翼杀手2049》"],
        ai_prompt_keywords=["leading lines", "converging lines", "visual pathway"]
    ),
    
    "框架式构图": VisualTerm(
        term="框架式构图",
        english="Frame within Frame",
        category=TermCategory.COMPOSITION,
        definition="利用前景元素形成框架，将主体框在其中，增加层次感和聚焦效果",
        visual_description="门窗、拱门、树枝等自然或人工元素形成画框",
        usage_scenarios=[
            "偷窥视角",
            "限制感表达",
            "增加景深",
            "强调主体"
        ],
        related_terms=["前景", "层次", "画中画"],
        examples=["《教父》", "《肖申克的救赎》", "《布达佩斯大饭店》"],
        ai_prompt_keywords=["frame within frame", "natural framing", "layered composition"]
    ),
    
    "负空间": VisualTerm(
        term="负空间",
        english="Negative Space",
        category=TermCategory.COMPOSITION,
        definition="主体周围或之间的空白区域，用于强调主体、创造氛围或表达孤独感",
        visual_description="主体占据画面较小部分，大面积留白营造极简主义美学",
        usage_scenarios=[
            "孤独感表达",
            "极简主义风格",
            "强调主体重要性",
            "呼吸感画面"
        ],
        related_terms=["留白", "极简", "空间感"],
        examples=["《荒野猎人》", "《地心引力》", "《花样年华》"],
        ai_prompt_keywords=["negative space", "minimalist composition", "isolated subject"]
    ),
}


# ==================== 景别术语 ====================
FRAMING_TERMS: Dict[str, VisualTerm] = {
    "大远景": VisualTerm(
        term="大远景",
        english="Extreme Long Shot / ELS",
        category=TermCategory.FRAMING,
        definition="人物在画面中占比极小，主要用于展示环境、规模和氛围",
        visual_description="人物可能仅占画面高度的1/4以下，环境成为绝对主角",
        usage_scenarios=[
            "史诗片开场",
            "展示地理环境",
            "强调人物渺小",
            "建立时空背景"
        ],
        related_terms=["建立镜头", "环境", "规模"],
        examples=["《阿拉伯的劳伦斯》", "《疯狂的麦克斯：狂暴之路》", "《沙丘》"],
        technical_notes="通常配合航拍或广角镜头使用",
        ai_prompt_keywords=["extreme wide shot", "vast landscape", "tiny figure in environment"]
    ),
    
    "全景": VisualTerm(
        term="全景",
        english="Long Shot / Full Shot",
        category=TermCategory.FRAMING,
        definition="人物全身完整呈现，头部和脚部都在画面内，展示人物与环境关系",
        visual_description="人物占据画面主体，但仍有足够环境信息",
        usage_scenarios=[
            "动作场景",
            "舞蹈场面",
            "展示服装",
            "人物入场"
        ],
        related_terms=["全身镜头", "环境人像"],
        examples=["《爱乐之城》", "《杀死比尔》", "《布达佩斯大饭店》"],
        ai_prompt_keywords=["full shot", "full body", "character in environment"]
    ),
    
    "中景": VisualTerm(
        term="中景",
        english="Medium Shot",
        category=TermCategory.FRAMING,
        definition="人物膝盖以上入画，兼顾表情和肢体语言，是最常用的叙事景别",
        visual_description="人物占据画面2/3左右，既能看清表情又有身体语言",
        usage_scenarios=[
            "对话场景",
            "双人互动",
            "日常叙事",
            "新闻采访"
        ],
        related_terms=["牛仔镜头", "美式中景"],
        examples=["几乎所有电影", "《低俗小说》对话", "《社交网络》"],
        technical_notes="最安全通用的景别，但过度使用会显得单调",
        ai_prompt_keywords=["medium shot", "knee shot", "conversational framing"]
    ),
    
    "特写": VisualTerm(
        term="特写",
        english="Close-Up / CU",
        category=TermCategory.FRAMING,
        definition="人物肩部以上或物体局部，强调情感细节或重要物品",
        visual_description="面部占据画面主要部分，背景虚化或不可见",
        usage_scenarios=[
            "情感高潮",
            "揭示关键信息",
            "强调反应",
            "物品展示"
        ],
        related_terms=["表情", "细节", "情感"],
        examples=["《教父》", "《黑天鹅》", "《闪灵》"],
        technical_notes="需要精确对焦，浅景深常用",
        ai_prompt_keywords=["close-up", "intimate framing", "facial detail"]
    ),
    
    "大特写": VisualTerm(
        term="大特写",
        english="Extreme Close-Up / ECU",
        category=TermCategory.FRAMING,
        definition="仅展示眼睛、嘴唇或物体的极小部分，创造强烈视觉冲击",
        visual_description="画面被单一细节填满，如一只眼睛、一滴水珠",
        usage_scenarios=[
            "强烈情感",
            "悬疑揭示",
            "抽象表现",
            "视觉冲击"
        ],
        related_terms=["微距", "细节", "抽象"],
        examples=["《2001太空漫游》黑石", "《黑天鹅》", "《母亲！》"],
        technical_notes="需要微距镜头或后期放大，注意细节质感",
        ai_prompt_keywords=["extreme close-up", "macro detail", "abstract texture"]
    ),
}


# ==================== 角度术语 ====================
ANGLE_TERMS: Dict[str, VisualTerm] = {
    "平视": VisualTerm(
        term="平视",
        english="Eye Level",
        category=TermCategory.ANGLE,
        definition="摄影机与被摄主体视线平齐，创造客观中立的观看体验",
        visual_description="画面水平线平稳，人物比例正常，最自然的观看角度",
        usage_scenarios=[
            "标准叙事",
            "对话场景",
            "建立客观感",
            "让观众代入"
        ],
        related_terms=["中性角度", "标准视角"],
        examples=["大多数电影的标准角度", "《十二怒汉》"],
        ai_prompt_keywords=["eye level shot", "neutral angle", "standard perspective"]
    ),
    
    "仰拍": VisualTerm(
        term="仰拍",
        english="Low Angle",
        category=TermCategory.ANGLE,
        definition="摄影机低于被摄主体向上拍摄，使主体显得高大、威严或威胁",
        visual_description="从下往上看，人物显得高大，背景常为天空或天花板",
        usage_scenarios=[[
            "英雄登场",
            "表现权威",
            "制造威胁感",
            "强调建筑高度"
        ]],
        related_terms=["低角度", "仰视", "英雄镜头"],
        examples=["《公民凯恩》", "《蝙蝠侠》系列", "《2001太空漫游》"],
        ai_prompt_keywords=["low angle shot", "hero shot", "looking up", "imposing figure"]
    ),
    
    "俯拍": VisualTerm(
        term="俯拍",
        english="High Angle",
        category=TermCategory.ANGLE,
        definition="摄影机高于被摄主体向下拍摄，使主体显得渺小、弱势或脆弱",
        visual_description="从上往下看，人物显得渺小，展现地面或地板",
        usage_scenarios=[
            "表现无助",
            "上帝视角",
            "展示环境布局",
            "死亡暗示"
        ],
        related_terms=["高角度", "俯视", "上帝视角"],
        examples=["《惊魂记》淋浴场景", "《美国丽人》", "《闪灵》"],
        ai_prompt_keywords=["high angle shot", "overhead view", "god's eye view", "vulnerable"]
    ),
    
    "荷兰角": VisualTerm(
        term="荷兰角",
        english="Dutch Angle / Canted Angle",
        category=TermCategory.ANGLE,
        definition="摄影机倾斜，地平线不再水平，创造不安、混乱或超现实感",
        visual_description="画面倾斜，垂直线不再垂直，视觉平衡被打破",
        usage_scenarios=[
            "心理不安",
            "梦境场景",
            "动作紧张",
            "反派登场"
        ],
        related_terms=["倾斜镜头", "德国表现主义", "不平衡"],
        examples=["《蝙蝠侠》", "《盗梦空间》", "《第三人》"],
        technical_notes="倾斜角度通常15-45度，过度使用会分散注意力",
        ai_prompt_keywords=["dutch angle", "tilted frame", "canted angle", "disorienting"]
    ),
}


# ==================== 摄影机运动术语 ====================
MOVEMENT_TERMS: Dict[str, VisualTerm] = {
    "推轨": VisualTerm(
        term="推轨",
        english="Dolly / Track",
        category=TermCategory.MOVEMENT,
        definition="摄影机沿轨道前后或左右移动，平滑稳定地接近或远离主体",
        visual_description="画面平稳推进或拉远，透视关系缓慢变化",
        usage_scenarios=[
            "强调情感",
            "揭示场景",
            "跟随人物",
            "建立关系"
        ],
        related_terms=["轨道", "移动", "推拉"],
        examples=["《好家伙》", "《闪灵》", "《鸟人》"],
        technical_notes="需要轨道车或稳定器，保持速度均匀",
        ai_prompt_keywords=["dolly shot", "smooth tracking", "push in", "pull back"]
    ),
    
    "手持": VisualTerm(
        term="手持",
        english="Handheld",
        category=TermCategory.MOVEMENT,
        definition="摄影师手持摄影机拍摄，画面带有自然的晃动和呼吸感",
        visual_description="轻微不规则晃动，模拟人眼观察的真实感",
        usage_scenarios=[
            "纪录片风格",
            "动作场景",
            "紧张氛围",
            "真实感追求"
        ],
        related_terms=["肩扛", "纪实风格", "晃动"],
        examples=["《拯救大兵瑞恩》", "《谍影重重》", "《切尔诺贝利》"],
        technical_notes="晃动要有节制，过度会令人不适",
        ai_prompt_keywords=["handheld camera", "shaky cam", "documentary style", "raw footage"]
    ),
    
    "斯坦尼康": VisualTerm(
        term="斯坦尼康",
        english="Steadicam",
        category=TermCategory.MOVEMENT,
        definition="使用斯坦尼康稳定器拍摄，获得流畅移动同时保持自然感",
        visual_description="如幽灵般平滑流畅的移动，仿佛观众亲身在场",
        usage_scenarios=[
            "长镜头",
            "跟随镜头",
            "复杂调度",
            "梦境场景"
        ],
        related_terms=["稳定器", "长镜头", "流畅"],
        examples=["《闪灵》", "《好家伙》", "《俄罗斯方舟》"],
        ai_prompt_keywords=["steadicam shot", "smooth floating movement", "continuous shot"]
    ),
    
    "摇臂": VisualTerm(
        term="摇臂",
        english="Crane / Jib",
        category=TermCategory.MOVEMENT,
        definition="使用摇臂实现大幅度的垂直或弧形运动，创造壮观视觉效果",
        visual_description="从高处俯瞰到近景，或从地面升至空中的流畅运动",
        usage_scenarios=[
            "开场/结尾",
            "壮观场面",
            "场景转换",
            "情感升华"
        ],
        related_terms=["升降", "吊臂", "大场面"],
        examples=["《乱世佳人》", "《指环王》", "《爱乐之城》"],
        ai_prompt_keywords=["crane shot", "sweeping movement", "majestic reveal"]
    ),
    
    "变焦": VisualTerm(
        term="变焦",
        english="Zoom",
        category=TermCategory.MOVEMENT,
        definition="通过改变镜头焦距实现画面放大或缩小，不同于物理移动",
        visual_description="画面内容快速放大或压缩，透视关系不变",
        usage_scenarios=[
            "复古风格",
            "突然聚焦",
            "紧张揭示",
            "70年代美学"
        ],
        related_terms=["推焦", "拉焦", "冲击变焦"],
        examples=["《大白鲨》", "《杀死比尔》", "《好家伙》"],
        technical_notes="变焦与推轨的区别在于透视关系是否改变",
        ai_prompt_keywords=["zoom shot", "snap zoom", "retro zoom", "whip zoom"]
    ),
}


# ==================== 灯光术语 ====================
LIGHTING_TERMS: Dict[str, VisualTerm] = {
    "三点布光": VisualTerm(
        term="三点布光",
        english="Three-Point Lighting",
        category=TermCategory.LIGHTING,
        definition="使用主光、辅光、轮廓光三个光源塑造立体感的人物照明方案",
        visual_description="人物面部有明暗层次，边缘有轮廓分离背景",
        usage_scenarios=[
            "标准人像",
            "访谈节目",
            "经典好莱坞风格",
            "美容广告"
        ],
        related_terms=["主光", "辅光", "轮廓光", "好莱坞式"],
        examples=["经典好莱坞电影", "《卡萨布兰卡》", "电视新闻"],
        ai_prompt_keywords=["three-point lighting", "classic Hollywood lighting", "glamour lighting"]
    ),
    
    "自然光": VisualTerm(
        term="自然光",
        english="Natural Light / Available Light",
        category=TermCategory.LIGHTING,
        definition="利用日光、月光或现场环境光拍摄，追求真实自然效果",
        visual_description="光线柔和有层次，阴影自然，色温随时间变化",
        usage_scenarios=[
            "纪实风格",
            "现实主义",
            "外景拍摄",
            "节省预算"
        ],
        related_terms=["日光", "实景", "真实感"],
        examples=["《罗马》", "《月光男孩》", "《游牧之地》"],
        ai_prompt_keywords=["natural lighting", "available light", "golden hour", "soft daylight"]
    ),
    
    "明暗对比": VisualTerm(
        term="明暗对比",
        english="Chiaroscuro",
        category=TermCategory.LIGHTING,
        definition="强烈的明暗对比，深黑阴影与明亮高光并存，创造戏剧性效果",
        visual_description="大面积阴影中透出的光束，神秘而戏剧化",
        usage_scenarios=[
            "黑色电影",
            "恐怖片",
            "戏剧性场景",
            "表现主义"
        ],
        related_terms=["伦勃朗光", "黑色电影", "戏剧性"],
        examples=["《公民凯恩》", "《教父》", "《银翼杀手》"],
        ai_prompt_keywords=["chiaroscuro", "dramatic lighting", "high contrast", "film noir lighting"]
    ),
    
    "剪影": VisualTerm(
        term="剪影",
        english="Silhouette",
        category=TermCategory.LIGHTING,
        definition="主体背光，呈现为黑色轮廓，背景明亮，强调形状和姿态",
        visual_description="黑色人影或物体轮廓，背景是明亮的天空或光源",
        usage_scenarios=[
            "神秘感",
            "英雄登场",
            "情感疏离",
            "唯美画面"
        ],
        related_terms=["逆光", "轮廓", "背光"],
        examples=["《黄金三镖客》", "《星球大战》", "《狮子王》"],
        ai_prompt_keywords=["silhouette", "backlit", "rim lighting", "dramatic outline"]
    ),
}


# ==================== 色彩术语 ====================
COLOR_TERMS: Dict[str, VisualTerm] = {
    "冷暖对比": VisualTerm(
        term="冷暖对比",
        english="Warm-Cool Contrast",
        category=TermCategory.COLOR,
        definition="在画面中同时使用暖色调(橙黄红)和冷色调(蓝青紫)创造视觉张力",
        visual_description="画面一部分温暖橙黄，另一部分冷蓝青，形成鲜明对比",
        usage_scenarios=[
            "科幻片",
            "动作片",
            "情感对比",
            "日夜交替"
        ],
        related_terms=["色温", "互补色", "橙青色调"],
        examples=["《疯狂的麦克斯：狂暴之路》", "《银翼杀手2049》", "《变形金刚》"],
        ai_prompt_keywords=["teal and orange", "warm cool contrast", "color grading", "cinematic color"]
    ),
    
    "单色调": VisualTerm(
        term="单色调",
        english="Monochromatic",
        category=TermCategory.COLOR,
        definition="使用单一色相的不同明度和饱和度，创造统一和谐的视觉效果",
        visual_description="画面以单一颜色为主，如全蓝调或全金色调",
        usage_scenarios=[
            "风格化表达",
            "特定年代",
            "情感统一",
            "艺术电影"
        ],
        related_terms=["色调", "统一", "风格化"],
        examples=["《罪恶之城》", "《她》", "《布达佩斯大饭店》"],
        ai_prompt_keywords=["monochromatic", "single color palette", "tonal harmony"]
    ),
    
    "去饱和": VisualTerm(
        term="去饱和",
        english="Desaturation",
        category=TermCategory.COLOR,
        definition="降低画面色彩饱和度，创造灰暗、怀旧或压抑的视觉效果",
        visual_description="画面呈现灰蒙蒙或接近黑白的效果，仅有微弱色彩",
        usage_scenarios=[
            "战争片",
            "回忆场景",
            "末日题材",
            "压抑氛围"
        ],
        related_terms=["饱和度", "黑白", "褪色"],
        examples=["《拯救大兵瑞恩》", "《疯狂的麦克斯：狂暴之路》", "《1917》"],
        ai_prompt_keywords=["desaturated", "muted colors", "bleached look", "post-apocalyptic color"]
    ),
}


# ==================== 转场术语 ====================
TRANSITION_TERMS: Dict[str, VisualTerm] = {
    "匹配剪辑": VisualTerm(
        term="匹配剪辑",
        english="Match Cut",
        category=TermCategory.TRANSITION,
        definition="利用形状、颜色、动作等视觉相似性连接两个不同时空的镜头",
        visual_description="画面元素在剪辑点完美衔接，创造流畅时空跳跃",
        usage_scenarios=[
            "时空转换",
            "蒙太奇",
            "诗意表达",
            "视觉冲击"
        ],
        related_terms=["图形匹配", "动作匹配", "跳切"],
        examples=["《2001太空漫游》骨头变飞船", "《教父》", "《鸟人》"],
        ai_prompt_keywords=["match cut", "graphic match", "seamless transition"]
    ),
    
    "跳切": VisualTerm(
        term="跳切",
        english="Jump Cut",
        category=TermCategory.TRANSITION,
        definition="在同一镜头内剪辑，时间跳跃但空间不变，创造急促或断裂感",
        visual_description="人物或物体突然改变位置，时间被压缩",
        usage_scenarios=[
            "戈达尔风格",
            "时间压缩",
            "紧张感",
            "新浪潮"
        ],
        related_terms=["断裂剪辑", "法国新浪潮", "时间跳跃"],
        examples=["《筋疲力尽》", "《无间道风云》", "《社交网络》"],
        ai_prompt_keywords=["jump cut", "time lapse", "discontinuous editing"]
    ),
    
    "溶解": VisualTerm(
        term="溶解",
        english="Dissolve",
        category=TermCategory.TRANSITION,
        definition="一个画面渐隐同时另一个画面渐显，表示时间流逝或场景转换",
        visual_description="两个画面短暂重叠，柔和过渡",
        usage_scenarios=[
            "时间流逝",
            "回忆场景",
            "梦境转换",
            "诗意蒙太奇"
        ],
        related_terms=["叠化", "淡入淡出", "时间过渡"],
        examples=["《公民凯恩》", "《教父2》", "经典好莱坞电影"],
        ai_prompt_keywords=["dissolve", "crossfade", "gentle transition"]
    ),
    
    "划接": VisualTerm(
        term="划接",
        english="Wipe",
        category=TermCategory.TRANSITION,
        definition="一个画面以某种形状或方向滑出，同时揭示下一个画面",
        visual_description="线条划过画面，新画面从边缘推进",
        usage_scenarios=[
            "复古风格",
            "场景转换",
            "喜剧效果",
            "星球大战风格"
        ],
        related_terms=["擦除", "滑动", "老式转场"],
        examples=["《星球大战》", "《疯狂的麦克斯》", "早期电影"],
        ai_prompt_keywords=["wipe transition", "star wars transition", "retro wipe"]
    ),
}


# ==================== 合并所有术语 ====================
VISUAL_GLOSSARY: Dict[str, VisualTerm] = {
    **COMPOSITION_TERMS,
    **FRAMING_TERMS,
    **ANGLE_TERMS,
    **MOVEMENT_TERMS,
    **LIGHTING_TERMS,
    **COLOR_TERMS,
    **TRANSITION_TERMS,
}


# ==================== 工具函数 ====================
def get_term(term_name: str) -> Optional[VisualTerm]:
    """获取术语定义"""
    return VISUAL_GLOSSARY.get(term_name)


def search_terms(keyword: str) -> List[VisualTerm]:
    """搜索术语"""
    results = []
    keyword_lower = keyword.lower()
    
    for term in VISUAL_GLOSSARY.values():
        if (keyword_lower in term.term.lower() or 
            keyword_lower in term.english.lower() or
            keyword_lower in term.definition.lower() or
            any(keyword_lower in t.lower() for t in term.related_terms)):
            results.append(term)
    
    return results


def get_terms_by_category(category: TermCategory) -> List[VisualTerm]:
    """按分类获取术语"""
    return [term for term in VISUAL_GLOSSARY.values() if term.category == category]


def get_ai_keywords(term_names: List[str]) -> List[str]:
    """获取术语对应的AI提示词关键词"""
    keywords = []
    for name in term_names:
        term = VISUAL_GLOSSARY.get(name)
        if term:
            keywords.extend(term.ai_prompt_keywords)
    return keywords


def get_terms_for_scene_type(scene_type: str) -> List[VisualTerm]:
    """根据场景类型推荐术语"""
    scene_term_mapping = {
        "对话": ["中景", "平视", "过肩镜头", "正反打"],
        "动作": ["手持", "全景", "快速剪辑", "斯坦尼康"],
        "情感": ["特写", "大特写", "推轨", "冷暖对比"],
        "悬疑": ["明暗对比", "荷兰角", "剪影", "低角度"],
        "史诗": ["大远景", "摇臂", "冷暖对比", "三分法"],
        "恐怖": ["低角度", "明暗对比", "剪影", "手持"],
        "浪漫": ["特写", "推轨", "暖色调", "柔光"],
        "科幻": ["冷暖对比", "对称构图", "负空间", "推轨"],
    }
    
    recommended = scene_term_mapping.get(scene_type, [])
    return [VISUAL_GLOSSARY.get(term) for term in recommended if term in VISUAL_GLOSSARY]


def explain_term_for_ai(term_name: str) -> str:
    """为AI生成解释术语的提示词"""
    term = VISUAL_GLOSSARY.get(term_name)
    if not term:
        return f"术语 '{term_name}' 未找到"
    
    return f"""
术语: {term.term} ({term.english})
定义: {term.definition}
视觉特征: {term.visual_description}
使用场景: {', '.join(term.usage_scenarios)}
相关术语: {', '.join(term.related_terms)}
示例影片: {', '.join(term.examples)}
AI提示词: {', '.join(term.ai_prompt_keywords)}
"""


# 分类映射（中文）
CATEGORY_NAMES = {
    TermCategory.COMPOSITION: "构图",
    TermCategory.CAMERA: "摄影机",
    TermCategory.LIGHTING: "灯光",
    TermCategory.COLOR: "色彩",
    TermCategory.MOVEMENT: "运动",
    TermCategory.PERSPECTIVE: "视角",
    TermCategory.DEPTH: "景深",
    TermCategory.FRAMING: "景别",
    TermCategory.ANGLE: "角度",
    TermCategory.TRANSITION: "转场",
    TermCategory.EFFECT: "特效",
    TermCategory.STAGING: "场面调度",
}


if __name__ == "__main__":
    # 测试
    print("=" * 60)
    print("视觉术语词典测试")
    print("=" * 60)
    
    print(f"\n共收录 {len(VISUAL_GLOSSARY)} 个术语\n")
    
    # 测试查询
    term = get_term("三分法")
    if term:
        print(f"术语: {term.term}")
        print(f"定义: {term.definition}")
        print(f"AI关键词: {term.ai_prompt_keywords}")
    
    # 测试分类查询
    print("\n\n构图类术语:")
    comp_terms = get_terms_by_category(TermCategory.COMPOSITION)
    for t in comp_terms[:3]:
        print(f"  - {t.term}: {t.definition[:30]}...")
