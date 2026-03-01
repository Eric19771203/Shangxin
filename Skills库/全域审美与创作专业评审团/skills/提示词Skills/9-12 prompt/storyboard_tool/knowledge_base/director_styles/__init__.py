"""
导演风格知识库主入口
整合所有导演风格模块，提供统一访问接口
"""

from .war_directors import (
    WAR_DIRECTORS,
    get_war_director_style,
    list_war_directors,
    SpielbergStyle,
    NolanStyle,
    RidleyScottStyle
)

from .art_directors import (
    ART_DIRECTORS,
    get_art_director_style,
    list_art_directors,
    WongKarWaiStyle,
    WesAndersonStyle,
    HouHsiaoHsienStyle
)

from .thriller_directors import (
    THRILLER_DIRECTORS,
    get_thriller_director_style,
    list_thriller_directors,
    HitchcockStyle,
    FincherStyle,
    BongJoonHoStyle
)

from .action_directors import (
    ACTION_DIRECTORS,
    get_action_director_style,
    list_action_directors,
    TarantinoStyle
)

from .animation_directors import (
    ANIMATION_DIRECTORS,
    get_animation_director_style,
    list_animation_directors,
    MiyazakiStyle,
    ShinkaiStyle,
    BurtonStyle
)

from .modern_directors import (
    MODERN_DIRECTORS,
    get_modern_director_style,
    list_modern_directors,
    VilleneuveStyle,
    PeeleStyle,
    AsterStyle,
    EggersStyle,
    ZhaoStyle
)

# 所有导演风格的统一字典
ALL_DIRECTORS = {
    # 战争片导演
    "spielberg": SpielbergStyle,
    "nolan": NolanStyle,
    "ridley_scott": RidleyScottStyle,
    # 文艺片导演
    "wong_kar_wai": WongKarWaiStyle,
    "wes_anderson": WesAndersonStyle,
    "hou_hsiao_hsien": HouHsiaoHsienStyle,
    # 悬疑片导演
    "hitchcock": HitchcockStyle,
    "fincher": FincherStyle,
    "bong_joon_ho": BongJoonHoStyle,
    # 动作片导演
    "tarantino": TarantinoStyle,
    # 动画导演
    "miyazaki": MiyazakiStyle,
    "shinkai": ShinkaiStyle,
    "burton": BurtonStyle,
    # 现代新晋导演
    "villeneuve": VilleneuveStyle,
    "peele": PeeleStyle,
    "aster": AsterStyle,
    "eggers": EggersStyle,
    "zhao": ZhaoStyle
}

# 按类型分类
DIRECTORS_BY_GENRE = {
    "war": WAR_DIRECTORS,
    "art": ART_DIRECTORS,
    "thriller": THRILLER_DIRECTORS,
    "action": ACTION_DIRECTORS,
    "animation": ANIMATION_DIRECTORS,
    "modern": MODERN_DIRECTORS
}


def get_director_style(director_name: str, genre: str = None):
    """
    获取指定导演的风格配置
    
    Args:
        director_name: 导演标识名（如 'spielberg', 'wong_kar_wai'）
        genre: 可选，导演类型（war/art/thriller/action/animation/modern）
    
    Returns:
        导演风格类或None
    """
    if genre:
        genre_dict = DIRECTORS_BY_GENRE.get(genre.lower())
        if genre_dict:
            return genre_dict.get(director_name.lower())
    
    return ALL_DIRECTORS.get(director_name.lower())


def list_all_directors():
    """列出所有可用的导演"""
    return {
        "war": list_war_directors(),
        "art": list_art_directors(),
        "thriller": list_thriller_directors(),
        "action": list_action_directors(),
        "animation": list_animation_directors(),
        "modern": list_modern_directors()
    }


def get_director_info(director_name: str, genre: str = None):
    """
    获取导演的基本信息
    
    Args:
        director_name: 导演标识名
        genre: 可选，导演类型
    
    Returns:
        导演信息字典
    """
    style_class = get_director_style(director_name, genre)
    if style_class and hasattr(style_class, 'INFO'):
        return style_class.INFO
    return None


def get_director_techniques(director_name: str, genre: str = None):
    """
    获取导演的标志性技巧
    
    Args:
        director_name: 导演标识名
        genre: 可选，导演类型
    
    Returns:
        技巧字典
    """
    style_class = get_director_style(director_name, genre)
    if style_class and hasattr(style_class, 'SIGNATURE_TECHNIQUES'):
        return style_class.SIGNATURE_TECHNIQUES
    return None


def get_director_works(director_name: str, genre: str = None):
    """
    获取导演的代表作品
    
    Args:
        director_name: 导演标识名
        genre: 可选，导演类型
    
    Returns:
        作品字典
    """
    style_class = get_director_style(director_name, genre)
    if style_class and hasattr(style_class, 'REPRESENTATIVE_WORKS'):
        return style_class.REPRESENTATIVE_WORKS
    return None


def get_director_visual_traits(director_name: str, genre: str = None):
    """
    获取导演的视觉特征
    
    Args:
        director_name: 导演标识名
        genre: 可选，导演类型
    
    Returns:
        视觉特征字典
    """
    style_class = get_director_style(director_name, genre)
    if style_class:
        traits = {}
        if hasattr(style_class, 'VISUAL_CHARACTERISTICS'):
            traits['visual'] = style_class.VISUAL_CHARACTERISTICS
        if hasattr(style_class, 'STORYBOARD_CHARACTERISTICS'):
            traits['storyboard'] = style_class.STORYBOARD_CHARACTERISTICS
        return traits
    return None


def get_director_storyboard_template(director_name: str, genre: str = None):
    """
    获取导演的3×3分镜模板
    
    Args:
        director_name: 导演标识名
        genre: 可选，导演类型
    
    Returns:
        分镜模板字典
    """
    style_class = get_director_style(director_name, genre)
    if style_class and hasattr(style_class, 'STORYBOARD_3X3'):
        return style_class.STORYBOARD_3X3
    return None


def apply_director_style(prompt: str, director_name: str, genre: str = None) -> str:
    """
    将导演风格应用到提示词中
    
    Args:
        prompt: 原始提示词
        director_name: 导演标识名
        genre: 可选，导演类型
    
    Returns:
        应用风格后的提示词
    """
    style_class = get_director_style(director_name, genre)
    if not style_class:
        return prompt
    
    # 获取视觉特征
    visual_traits = []
    if hasattr(style_class, 'VISUAL_CHARACTERISTICS'):
        vc = style_class.VISUAL_CHARACTERISTICS
        if 'color_palette' in vc:
            visual_traits.extend(vc['color_palette'][:2])  # 取前两种颜色
        if 'lighting_style' in vc:
            visual_traits.append(vc['lighting_style'].split('，')[0])  # 取主要照明风格
        if 'composition' in vc:
            visual_traits.append(vc['composition'].split('，')[0])
    
    # 添加导演风格关键词
    director_keywords = f"{style_class.INFO.get('name_en', director_name)} style"
    
    # 组合提示词
    enhanced_prompt = f"{prompt}, {director_keywords}"
    if visual_traits:
        enhanced_prompt += f", {', '.join(visual_traits)}"
    
    return enhanced_prompt


def search_directors_by_keyword(keyword: str):
    """
    根据关键词搜索导演
    
    Args:
        keyword: 搜索关键词
    
    Returns:
        匹配的导演列表
    """
    matches = []
    keyword_lower = keyword.lower()
    
    for name, style_class in ALL_DIRECTORS.items():
        if hasattr(style_class, 'INFO'):
            info = style_class.INFO
            # 检查名称
            if keyword_lower in name.lower():
                matches.append((name, info))
                continue
            # 检查英文名
            if keyword_lower in info.get('name_en', '').lower():
                matches.append((name, info))
                continue
            # 检查风格关键词
            for kw in info.get('style_keywords', []):
                if keyword_lower in kw.lower():
                    matches.append((name, info))
                    break
    
    return matches


# 便捷函数别名
def get_style(director_name: str, genre: str = None):
    """get_director_style的别名"""
    return get_director_style(director_name, genre)


def list_directors():
    """list_all_directors的别名"""
    return list_all_directors()


__all__ = [
    # 导演风格类 - 经典
    'SpielbergStyle', 'NolanStyle', 'RidleyScottStyle',
    'WongKarWaiStyle', 'WesAndersonStyle', 'HouHsiaoHsienStyle',
    'HitchcockStyle', 'FincherStyle', 'BongJoonHoStyle',
    'TarantinoStyle',
    'MiyazakiStyle', 'ShinkaiStyle', 'BurtonStyle',
    # 导演风格类 - 现代
    'VilleneuveStyle', 'PeeleStyle', 'AsterStyle', 'EggersStyle', 'ZhaoStyle',
    # 字典
    'ALL_DIRECTORS', 'DIRECTORS_BY_GENRE',
    'WAR_DIRECTORS', 'ART_DIRECTORS', 'THRILLER_DIRECTORS',
    'ACTION_DIRECTORS', 'ANIMATION_DIRECTORS', 'MODERN_DIRECTORS',
    # 函数
    'get_director_style', 'list_all_directors',
    'get_director_info', 'get_director_techniques',
    'get_director_works', 'get_director_visual_traits',
    'get_director_storyboard_template', 'apply_director_style',
    'search_directors_by_keyword',
    'get_style', 'list_directors'
]
