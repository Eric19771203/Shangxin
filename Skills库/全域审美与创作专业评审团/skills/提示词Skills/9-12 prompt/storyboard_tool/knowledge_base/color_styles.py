#!/usr/bin/env python3
"""
色彩风格派系库
收录全球经典视觉风格与色彩参数
"""

from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass
class ColorStyle:
    """色彩风格定义"""
    name: str
    name_en: str
    description: str
    origin: str
    era: str
    
    # 核心色彩
    primary_colors: List[str]
    secondary_colors: List[str]
    accent_colors: List[str]
    
    # 色彩参数
    saturation: str  # 饱和度: high/medium/low
    brightness: str  # 明度: high/medium/low
    contrast: str    # 对比度: high/medium/low
    
    # 视觉特征
    visual_features: List[str]
    
    # 参考作品
    reference_works: List[str]
    
    # AI提示词关键词
    ai_prompt_keywords: List[str]
    
    # 适用场景
    suitable_scenes: List[str]
    
    # 技术参数
    technical_params: Dict[str, Any]


# ============================================
# 1. 中国宋代古风色调
# ============================================
SONG_DYNASTY = ColorStyle(
    name="宋代古风",
    name_en="Song Dynasty Aesthetic",
    description="以'雅、淡、寂、静'为魂，极简极素的东方美学。色彩克制含蓄，追求天人合一的意境",
    origin="中国宋代",
    era="960-1279年",
    
    primary_colors=["#D4C4B0", "#B8A99A", "#9B8B7A", "#7D6E5D"],  # 米白、驼色、茶色
    secondary_colors=["#A8B5A0", "#8FA090", "#6B7B6A", "#4A5A48"],  # 青绿、竹青
    accent_colors=["#C85A54", "#8B4513", "#D4AF37"],  # 朱砂、赭石、金
    
    saturation="low",
    brightness="medium",
    contrast="low",
    
    visual_features=[
        "低饱和度中间调",
        "灰度色系为主",
        "水墨渲染质感",
        "留白构图",
        "自然光线",
        "含蓄内敛"
    ],
    
    reference_works=[
        "《梦华录》",
        "《知否知否应是绿肥红瘦》",
        "《清平乐》",
        "宋代山水画"
    ],
    
    ai_prompt_keywords=[
        "Song Dynasty aesthetic",
        "muted earth tones",
        "ink wash painting style",
        "minimalist composition",
        "natural lighting",
        "subtle elegance",
        "sepia undertones",
        "zen atmosphere"
    ],
    
    suitable_scenes=[
        "古装历史剧",
        "文人雅士场景",
        "园林建筑",
        "茶道花道",
        "诗词书画"
    ],
    
    technical_params={
        "color_temperature": "warm",
        "gamma": 1.1,
        "shadow_tint": "warm",
        "highlight_tint": "neutral"
    }
)


# ============================================
# 2. 邵氏电影风格
# ============================================
SHAW_BROTHERS = ColorStyle(
    name="邵氏武侠",
    name_en="Shaw Brothers Wuxia",
    description="香港邵氏电影公司经典武侠风格，色彩浓烈饱和，场面宏大华丽，充满东方浪漫主义",
    origin="中国香港",
    era="1958-1985年",
    
    primary_colors=["#8B0000", "#DAA520", "#FFD700", "#FF4500"],  # 深红、金黄、橙红
    secondary_colors=["#2F4F4F", "#556B2F", "#8B4513"],  # 深绿、橄榄、赭石
    accent_colors=["#FFFFFF", "#000000", "#C0C0C0"],  # 黑白对比
    
    saturation="high",
    brightness="high",
    contrast="high",
    
    visual_features=[
        "高饱和度色彩",
        "浓烈的红金配色",
        "戏剧化布光",
        "华丽服装布景",
        "快速剪辑",
        "夸张动作设计"
    ],
    
    reference_works=[
        "《独臂刀》",
        "《五毒》",
        "《金臂童》",
        "《刺马》"
    ],
    
    ai_prompt_keywords=[
        "Shaw Brothers style",
        "wuxia cinema",
        "vibrant saturated colors",
        "golden red palette",
        "dramatic lighting",
        "martial arts epic",
        "1960s Hong Kong cinema",
        "theatrical composition"
    ],
    
    suitable_scenes=[
        "武侠打斗",
        "江湖恩怨",
        "古装动作",
        "门派对决",
        "英雄救美"
    ],
    
    technical_params={
        "color_temperature": "warm",
        "saturation_boost": 1.4,
        "contrast_boost": 1.3,
        "vignette": "medium"
    }
)


# ============================================
# 3. 虚幻5最终幻想风格
# ============================================
UNREAL5_FANTASY = ColorStyle(
    name="虚幻5幻想",
    name_en="Unreal Engine 5 Fantasy",
    description="次世代游戏引擎渲染的奇幻风格，超写实与风格化并存，光影极致细腻，色彩梦幻绚烂",
    origin="数字艺术",
    era="2020年代",
    
    primary_colors=["#4A90E2", "#7B68EE", "#00CED1", "#FF6B9D"],  # 蓝紫、青、粉
    secondary_colors=["#FFD93D", "#6BCB77", "#4D96FF"],  # 金黄、翠绿、天蓝
    accent_colors=["#FFFFFF", "#FF00FF", "#00FFFF"],  # 白、洋红、青
    
    saturation="high",
    brightness="high",
    contrast="medium",
    
    visual_features=[
        "次世代渲染质感",
        "Lumen全局光照",
        "Nanite几何细节",
        "体积雾光效",
        "金属度/粗糙度材质",
        "赛博朋克与奇幻融合"
    ],
    
    reference_works=[
        "《最终幻想16》",
        "《黑神话：悟空》",
        "《巫师3》次世代版",
        "《艾尔登法环》"
    ],
    
    ai_prompt_keywords=[
        "Unreal Engine 5",
        "next-gen graphics",
        "Lumen lighting",
        "fantasy aesthetic",
        "volumetric fog",
        "ray tracing",
        "metallic materials",
        "epic scale",
        "cinematic composition"
    ],
    
    suitable_scenes=[
        "奇幻冒险",
        "史诗战斗",
        "魔法世界",
        "科幻未来",
        "游戏CG"
    ],
    
    technical_params={
        "render_engine": "UE5",
        "lighting": "Lumen",
        "geometry": "Nanite",
        "reflections": "ray_traced"
    }
)


# ============================================
# 4. 赛博朋克风格
# ============================================
CYBERPUNK = ColorStyle(
    name="赛博朋克",
    name_en="Cyberpunk",
    description="高科技低生活的未来都市美学，霓虹灯光与阴暗街道的强烈对比，充满反乌托邦气息",
    origin="科幻文学/电影",
    era="1980年代至今",
    
    primary_colors=["#FF0080", "#00FFFF", "#FF00FF", "#8A2BE2"],  # 洋红、青、紫
    secondary_colors=["#1A1A2E", "#16213E", "#0F3460"],  # 深蓝黑
    accent_colors=["#FFD700", "#FF4500", "#00FF00"],  # 金黄、橙红、绿
    
    saturation="high",
    brightness="low",
    contrast="high",
    
    visual_features=[
        "霓虹灯光效果",
        "高对比度",
        "雨夜反射",
        "全息投影",
        "阴暗街道",
        "未来科技感"
    ],
    
    reference_works=[
        "《银翼杀手》",
        "《银翼杀手2049》",
        "《攻壳机动队》",
        "《赛博朋克2077》"
    ],
    
    ai_prompt_keywords=[
        "cyberpunk aesthetic",
        "neon lights",
        "rainy night",
        "holographic displays",
        "dystopian future",
        "high contrast",
        "magenta cyan palette",
        "urban decay",
        "tech noir"
    ],
    
    suitable_scenes=[
        "未来都市",
        "雨夜追逐",
        "黑客场景",
        "赛博空间",
        "反乌托邦世界"
    ],
    
    technical_params={
        "color_temperature": "cool",
        "neon_glow": "high",
        "bloom": "strong",
        "chromatic_aberration": "subtle"
    }
)


# ============================================
# 5. 韦斯安德森对称美学
# ============================================
WES_ANDERSON = ColorStyle(
    name="韦斯安德森",
    name_en="Wes Anderson Aesthetic",
    description="极致对称构图与糖果色调的童话世界，复古优雅中带着怪诞幽默",
    origin="美国电影",
    era="2000年代至今",
    
    primary_colors=["#F4A460", "#87CEEB", "#FFB6C1", "#F0E68C"],  # 沙色、天蓝、粉、黄
    secondary_colors=["#DDA0DD", "#98FB98", "#F4A460"],  # 紫、绿、橙
    accent_colors=["#FF6347", "#40E0D0", "#FFD700"],  # 番茄红、青绿、金
    
    saturation="medium",
    brightness="medium",
    contrast="medium",
    
    visual_features=[
        "极致对称构图",
        "糖果色调",
        "平面化视觉",
        "复古元素",
        "中心构图",
        "童话质感"
    ],
    
    reference_works=[
        "《布达佩斯大饭店》",
        "《月升王国》",
        "《法兰西特派》",
        "《天才一族》"
    ],
    
    ai_prompt_keywords=[
        "Wes Anderson style",
        "symmetrical composition",
        "pastel color palette",
        "vintage aesthetic",
        "storybook quality",
        "centered framing",
        "whimsical atmosphere",
        "retro design"
    ],
    
    suitable_scenes=[
        "复古场景",
        "酒店宾馆",
        "家庭喜剧",
        "旅行冒险",
        "青春成长"
    ],
    
    technical_params={
        "composition": "symmetrical",
        "aspect_ratio": "4:3_or_16:9",
        "color_palette": "pastel",
        "depth_of_field": "deep"
    }
)


# ============================================
# 6. 莫兰迪色系
# ============================================
MORANDI = ColorStyle(
    name="莫兰迪色系",
    name_en="Morandi Color Palette",
    description="意大利画家乔治·莫兰迪的色彩哲学，低饱和度灰调色彩，温柔高级的视觉体验",
    origin="意大利",
    era="20世纪",
    
    primary_colors=["#B5B5B5", "#C4B9C2", "#B8C4B8", "#C9B8A8"],  # 灰、灰粉、灰绿、灰棕
    secondary_colors=["#A8B5C4", "#C4A8A8", "#B8A8C4"],  # 灰蓝、灰红、灰紫
    accent_colors=["#D4C4B0", "#8B7355", "#A0A0A0"],  # 米色、棕灰
    
    saturation="low",
    brightness="medium",
    contrast="low",
    
    visual_features=[
        "低饱和度",
        "灰度色调",
        "柔和过渡",
        "高级感",
        "宁静氛围",
        "克制内敛"
    ],
    
    reference_works=[
        "莫兰迪静物画",
        "《延禧攻略》",
        "北欧设计",
        "意大利现代艺术"
    ],
    
    ai_prompt_keywords=[
        "Morandi color palette",
        "muted tones",
        "desaturated colors",
        "gray undertones",
        "soft transitions",
        "sophisticated aesthetic",
        "calming atmosphere",
        "earthy neutrals"
    ],
    
    suitable_scenes=[
        "现代家居",
        "时尚摄影",
        "文艺短片",
        "产品广告",
        "生活方式"
    ],
    
    technical_params={
        "saturation_reduction": 0.6,
        "contrast_reduction": 0.7,
        "shadow_lift": "high",
        "highlight_compression": "medium"
    }
)


# ============================================
# 7. 新海诚动画风格
# ============================================
MAKOTO_SHINKAI = ColorStyle(
    name="新海诚风格",
    name_en="Makoto Shinkai Animation",
    description="极致细腻的光影描绘，梦幻唯美的天空与云彩，充满诗意的日式动画美学",
    origin="日本动画",
    era="2000年代至今",
    
    primary_colors=["#87CEEB", "#FFD700", "#FF69B4", "#00CED1"],  # 天蓝、金、粉、青
    secondary_colors=["#FFA500", "#98FB98", "#DDA0DD"],  # 橙、绿、紫
    accent_colors=["#FFFFFF", "#FF1493", "#00BFFF"],  # 白、深粉、蓝
    
    saturation="high",
    brightness="high",
    contrast="medium",
    
    visual_features=[
        "梦幻天空",
        "细腻云彩",
        "光影变幻",
        "城市风景",
        "雨景描绘",
        "情感细腻"
    ],
    
    reference_works=[
        "《你的名字》",
        "《天气之子》",
        "《铃芽之旅》",
        "《言叶之庭》"
    ],
    
    ai_prompt_keywords=[
        "Makoto Shinkai style",
        "anime aesthetic",
        "dramatic sky",
        "volumetric clouds",
        "golden hour lighting",
        "urban landscapes",
        "romantic atmosphere",
        "lens flare",
        "vivid colors"
    ],
    
    suitable_scenes=[
        "青春爱情",
        "城市风景",
        "天空云彩",
        "雨景描绘",
        "奇幻现实"
    ],
    
    technical_params={
        "sky_detail": "high",
        "lighting": "golden_hour",
        "color_grading": "vibrant",
        "atmospheric_perspective": "strong"
    }
)


# ============================================
# 8. 蒂姆波顿哥特风格
# ============================================
TIM_BURTON_GOTHIC = ColorStyle(
    name="蒂姆波顿哥特",
    name_en="Tim Burton Gothic",
    description="暗黑童话与哥特美学的完美融合，怪诞幽默中透着温情，独特的视觉符号",
    origin="美国电影",
    era="1980年代至今",
    
    primary_colors=["#000000", "#4B0082", "#2F4F4F", "#800080"],  # 黑、靛蓝、深灰、紫
    secondary_colors=["#8B0000", "#191970", "#483D8B"],  # 深红、午夜蓝、暗紫
    accent_colors=["#FFFFFF", "#FFD700", "#FF69B4"],  # 白、金、粉
    
    saturation="medium",
    brightness="low",
    contrast="high",
    
    visual_features=[
        "暗黑基调",
        "哥特元素",
        "条纹图案",
        "扭曲造型",
        "黑白对比",
        "怪诞角色"
    ],
    
    reference_works=[
        "《剪刀手爱德华》",
        "《僵尸新娘》",
        "《查理和巧克力工厂》",
        "《圣诞夜惊魂》"
    ],
    
    ai_prompt_keywords=[
        "Tim Burton style",
        "gothic aesthetic",
        "dark fairytale",
        "striped patterns",
        "twisted designs",
        "black comedy",
        "macabre whimsy",
        "Victorian gothic"
    ],
    
    suitable_scenes=[
        "暗黑童话",
        "万圣节主题",
        "怪诞喜剧",
        "哥特建筑",
        "幻想世界"
    ],
    
    technical_params={
        "color_temperature": "cool",
        "desaturation": "partial",
        "shadow_detail": "high",
        "contrast_boost": 1.4
    }
)


# ============================================
# 9. 王家卫电影风格
# ============================================
WONG_KAR_WAI = ColorStyle(
    name="王家卫风格",
    name_en="Wong Kar-wai Cinema",
    description="迷离暧昧的都市情绪，霓虹色彩与慢门拖影，孤独浪漫的氛围美学",
    origin="中国香港",
    era="1990年代至今",
    
    primary_colors=["#FF1493", "#00FF7F", "#FFD700", "#FF4500"],  # 深粉、春绿、金、橙红
    secondary_colors=["#4B0082", "#191970", "#2F4F4F"],  # 靛蓝、午夜蓝、深灰
    accent_colors=["#FFFFFF", "#FF69B4", "#00CED1"],  # 白、粉、青
    
    saturation="high",
    brightness="low",
    contrast="medium",
    
    visual_features=[
        "霓虹色彩",
        "慢门拖影",
        "高对比度",
        "浅景深",
        "不对称构图",
        "前景遮挡"
    ],
    
    reference_works=[
        "《花样年华》",
        "《重庆森林》",
        "《春光乍泄》",
        "《2046》"
    ],
    
    ai_prompt_keywords=[
        "Wong Kar-wai style",
        "neon noir",
        "motion blur",
        "shallow depth of field",
        "urban loneliness",
        "romantic melancholy",
        "Hong Kong cinema",
        "night scenes"
    ],
    
    suitable_scenes=[
        "都市夜景",
        "爱情故事",
        "孤独情绪",
        "雨夜场景",
        "怀旧回忆"
    ],
    
    technical_params={
        "shutter_speed": "slow",
        "aperture": "wide",
        "color_temperature": "warm",
        "grain": "film_emulation"
    }
)


# ============================================
# 10. 黑泽明武士电影
# ============================================
KUROSAWA_SAMURAI = ColorStyle(
    name="黑泽明武士",
    name_en="Kurosawa Samurai Cinema",
    description="黑白对比强烈的武士道美学，动态天气与极简构图，东方哲学的视觉呈现",
    origin="日本电影",
    era="1950-1960年代",
    
    primary_colors=["#000000", "#FFFFFF", "#8B7355", "#D2B48C"],  # 黑白、棕、沙色
    secondary_colors=["#696969", "#A9A9A9", "#D3D3D3"],  # 灰阶
    accent_colors=["#8B0000", "#FFD700", "#DC143C"],  # 深红、金、猩红
    
    saturation="low",
    brightness="medium",
    contrast="very_high",
    
    visual_features=[
        "高对比度黑白",
        "极简构图",
        "动态天气",
        "长镜头",
        "轴向剪辑",
        "水墨意境"
    ],
    
    reference_works=[
        "《七武士》",
        "《罗生门》",
        "《用心棒》",
        "《乱》"
    ],
    
    ai_prompt_keywords=[
        "Kurosawa style",
        "samurai cinema",
        "high contrast black and white",
        "minimalist composition",
        "dynamic weather",
        "long takes",
        "Japanese aesthetic",
        "ink painting influence"
    ],
    
    suitable_scenes=[
        "武士对决",
        "历史史诗",
        "雨中战斗",
        "东方哲学",
        "黑白摄影"
    ],
    
    technical_params={
        "aspect_ratio": "4:3",
        "contrast": "maximum",
        "grain": "film",
        "sharpness": "high"
    }
)


# 所有风格集合
ALL_COLOR_STYLES = {
    "song_dynasty": SONG_DYNASTY,
    "shaw_brothers": SHAW_BROTHERS,
    "unreal5_fantasy": UNREAL5_FANTASY,
    "cyberpunk": CYBERPUNK,
    "wes_anderson": WES_ANDERSON,
    "morandi": MORANDI,
    "makoto_shinkai": MAKOTO_SHINKAI,
    "tim_burton_gothic": TIM_BURTON_GOTHIC,
    "wong_kar_wai": WONG_KAR_WAI,
    "kurosawa_samurai": KUROSAWA_SAMURAI,
}


def get_color_style(style_id: str) -> ColorStyle:
    """获取指定色彩风格"""
    return ALL_COLOR_STYLES.get(style_id)


def list_all_color_styles() -> Dict[str, str]:
    """列出所有色彩风格"""
    return {k: v.name for k, v in ALL_COLOR_STYLES.items()}


def get_style_ai_prompt(style_id: str) -> str:
    """获取风格的AI提示词"""
    style = get_color_style(style_id)
    if style:
        return ", ".join(style.ai_prompt_keywords)
    return ""


if __name__ == "__main__":
    # 测试
    print("="*60)
    print("色彩风格派系库")
    print("="*60)
    
    for style_id, style in ALL_COLOR_STYLES.items():
        print(f"\n【{style.name}】{style.name_en}")
        print(f"  来源: {style.origin} ({style.era})")
        print(f"  主色调: {style.primary_colors[:3]}")
        print(f"  饱和度: {style.saturation} | 明度: {style.brightness}")
        print(f"  参考作品: {', '.join(style.reference_works[:2])}")
