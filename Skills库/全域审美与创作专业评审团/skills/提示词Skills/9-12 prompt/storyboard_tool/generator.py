"""
分镜工具 - 主生成器
整合所有知识库，根据用户输入生成完整的分镜方案
"""

from typing import Dict, List, Any, Optional
import json

from core.base_framework import BaseFramework, BoardType, NarrativeFramework
from core.grammar_rules import GrammarRuleEngine
from knowledge_base.movie import get_film_storyboard, list_film_types
from knowledge_base.short_drama import get_short_drama_storyboard, list_short_drama_types
from knowledge_base.comic_drama import get_comic_storyboard, list_comic_types
from knowledge_base.tvc import get_tvc_storyboard, list_tvc_types
from knowledge_base.director_styles import (
    get_director_style,
    list_all_directors,
    apply_director_style,
    get_director_storyboard_template
)


class StoryboardGenerator:
    """分镜生成器主类"""
    
    # 内容类型映射
    CONTENT_TYPES = {
        "movie": {
            "name": "电影",
            "subtypes": list_film_types(),
            "getter": get_film_storyboard
        },
        "short_drama": {
            "name": "短剧",
            "subtypes": list_short_drama_types(),
            "getter": get_short_drama_storyboard
        },
        "comic_drama": {
            "name": "漫剧",
            "subtypes": list_comic_types(),
            "getter": get_comic_storyboard
        },
        "tvc": {
            "name": "TVC广告",
            "subtypes": list_tvc_types(),
            "getter": get_tvc_storyboard
        }
    }
    
    def __init__(self):
        self.grammar_engine = GrammarRuleEngine()
    
    def generate(self,
                 content_type: str,
                 subtype: str,
                 board_type: str = "3x3",
                 scene_description: str = "",
                 custom_prompts: Optional[Dict[int, str]] = None,
                 director_style: Optional[str] = None) -> Dict[str, Any]:
        """
        生成分镜方案
        
        Args:
            content_type: 内容类型 (movie/short_drama/comic_drama/tvc)
            subtype: 子类型
            board_type: 故事板类型 (3x3/4x3)
            scene_description: 场景描述
            custom_prompts: 自定义提示词 {镜头序号: 提示词}
            director_style: 导演风格 (如 'spielberg', 'wong_kar_wai', 'miyazaki')
        
        Returns:
            完整的分镜方案
        """
        # 1. 获取基础模板
        template = self._get_template(content_type, subtype, board_type)
        if not template:
            return {"error": f"未找到模板: {content_type}/{subtype}"}
        
        # 2. 创建基础框架
        framework = self._create_framework(board_type)
        
        # 3. 合并模板和框架
        storyboard = self._merge_template_framework(template, framework, board_type)
        
        # 4. 应用导演风格（如果指定）
        director_info = None
        if director_style:
            storyboard, director_info = self._apply_director_style_to_storyboard(
                storyboard, director_style, board_type
            )
        
        # 5. 应用自定义提示词
        if custom_prompts:
            storyboard = self._apply_custom_prompts(storyboard, custom_prompts)
        
        # 6. 应用电影语法规则
        grammar_rules = self.grammar_engine.apply_all_rules(
            storyboard.get("shots", []),
            board_type
        )
        
        # 7. 生成色调演进建议
        color_evolution = self._generate_color_evolution(
            content_type, subtype, board_type, director_style
        )
        
        # 8. 组装最终输出
        result = {
            "content_info": {
                "type": content_type,
                "subtype": subtype,
                "board_type": board_type,
                "scene_description": scene_description,
                "director_style": director_style
            },
            "storyboard": storyboard,
            "director_info": director_info,
            "grammar_rules": grammar_rules,
            "color_evolution": color_evolution,
            "usage_guide": self._generate_usage_guide(content_type, subtype, board_type, director_style)
        }
        
        return result
    
    def _get_template(self, content_type: str, subtype: str, board_type: str) -> Optional[Dict]:
        """获取模板"""
        type_info = self.CONTENT_TYPES.get(content_type)
        if not type_info:
            return None
        
        getter = type_info["getter"]
        return getter(subtype, board_type)
    
    def _create_framework(self, board_type: str) -> BaseFramework:
        """创建基础框架"""
        if board_type == "4x3":
            return BaseFramework(BoardType.EPIC_4X3)
        return BaseFramework(BoardType.STANDARD_3X3)
    
    def _merge_template_framework(self, template: Dict, framework: BaseFramework, board_type: str) -> Dict:
        """合并模板和框架"""
        if board_type == "4x3":
            return self._merge_4x3(template, framework)
        return self._merge_3x3(template, framework)
    
    def _merge_3x3(self, template: Dict, framework: BaseFramework) -> Dict:
        """合并3×3模板"""
        template_shots = template.get("shots", [])
        framework_shots = framework.shots
        
        merged_shots = []
        for i, fw_shot in enumerate(framework_shots):
            template_shot = template_shots[i] if i < len(template_shots) else {}
            
            merged_shot = {
                "index": fw_shot.index,
                "name": template_shot.get("name", fw_shot.name),
                "shot_type": template_shot.get("shot_type", fw_shot.shot_type),
                "angle": template_shot.get("angle", ""),
                "movement": template_shot.get("movement", ""),
                "duration": template_shot.get("duration", ""),
                "description": template_shot.get("description", fw_shot.description),
                "sound": template_shot.get("sound", ""),
                "color": template_shot.get("color", ""),
                "prompt": template_shot.get("prompt", "")
            }
            merged_shots.append(merged_shot)
        
        return {
            "template_name": template.get("template_name", "标准3×3"),
            "shots": merged_shots
        }
    
    def _merge_4x3(self, template: Dict, framework: BaseFramework) -> Dict:
        """合并4×3模板"""
        rows = template.get("rows", [])
        framework_shots = framework.shots
        
        merged_rows = []
        shot_index = 0
        
        for row in rows:
            row_shots = row.get("shots", [])
            merged_row_shots = []
            
            for row_shot in row_shots:
                if shot_index < len(framework_shots):
                    fw_shot = framework_shots[shot_index]
                    merged_shot = {
                        "index": row_shot.get("index", fw_shot.index),
                        "name": row_shot.get("name", fw_shot.name),
                        "shot_type": row_shot.get("shot_type", fw_shot.shot_type),
                        "prompt": row_shot.get("prompt", "")
                    }
                    merged_row_shots.append(merged_shot)
                    shot_index += 1
            
            merged_rows.append({
                "name": row.get("name", ""),
                "shots": merged_row_shots
            })
        
        return {
            "template_name": template.get("template_name", "史诗4×3"),
            "description": template.get("description", ""),
            "rows": merged_rows
        }
    
    def _apply_director_style_to_storyboard(self, storyboard: Dict, director_style: str, board_type: str) -> tuple:
        """应用导演风格到故事板"""
        style_class = get_director_style(director_style)
        if not style_class:
            return storyboard, None
        
        # 获取导演信息
        director_info = {
            "name": style_class.INFO.get("name", ""),
            "name_en": style_class.INFO.get("name_en", ""),
            "style_keywords": style_class.INFO.get("style_keywords", []),
            "visual_traits": style_class.VISUAL_CHARACTERISTICS if hasattr(style_class, 'VISUAL_CHARACTERISTICS') else {},
            "techniques": list(style_class.SIGNATURE_TECHNIQUES.keys()) if hasattr(style_class, 'SIGNATURE_TECHNIQUES') else []
        }
        
        # 应用导演风格到每个镜头的prompt
        shots = storyboard.get("shots", [])
        director_template = get_director_storyboard_template(director_style)
        
        for i, shot in enumerate(shots):
            original_prompt = shot.get("prompt", "")
            
            # 使用导演风格增强prompt
            enhanced_prompt = apply_director_style(original_prompt, director_style)
            shot["prompt"] = enhanced_prompt
            shot["director_style_applied"] = director_style
            
            # 如果有导演模板，添加导演特定的镜头信息
            if director_template and "shots" in director_template:
                director_shots = director_template["shots"]
                if i < len(director_shots):
                    director_shot = director_shots[i]
                    shot["director_technique"] = director_shot.get("technique", "")
                    shot["director_reference"] = director_shot.get("name", "")
        
        storyboard["shots"] = shots
        storyboard["director_template_name"] = director_template.get("template_name", "") if director_template else ""
        
        return storyboard, director_info
    
    def _apply_custom_prompts(self, storyboard: Dict, custom_prompts: Dict[int, str]) -> Dict:
        """应用自定义提示词"""
        shots = storyboard.get("shots", [])
        for shot in shots:
            index = shot.get("index")
            if index in custom_prompts:
                shot["prompt"] = custom_prompts[index]
                shot["customized"] = True
        
        storyboard["shots"] = shots
        return storyboard
    
    def _generate_color_evolution(self, content_type: str, subtype: str, board_type: str, director_style: str = None) -> List[Dict]:
        """生成色调演进建议"""
        # 如果指定了导演风格，使用导演的色彩偏好
        if director_style:
            style_class = get_director_style(director_style)
            if style_class and hasattr(style_class, 'VISUAL_CHARACTERISTICS'):
                vc = style_class.VISUAL_CHARACTERISTICS
                color_palette = vc.get('color_palette', [])
                if color_palette:
                    num_shots = 12 if board_type == "4x3" else 9
                    colors = []
                    for i in range(num_shots):
                        color = color_palette[i % len(color_palette)]
                        colors.append({
                            'shot_index': i + 1,
                            'emotion': '导演风格',
                            'primary_color': color,
                            'lighting': vc.get('lighting_style', ''),
                            'mood': vc.get('composition', '')
                        })
                    return colors
        
        # 根据类型确定情感序列
        emotion_maps = {
            "movie": {
                "war": ["紧张", "紧张", "悲伤"],
                "art": ["平静", "怀旧", "平静"],
                "thriller": ["神秘", "紧张", "神秘"],
                "action": ["紧张", "激情", "喜悦"],
                "romance": ["喜悦", "激情", "喜悦"]
            },
            "short_drama": {
                "action": ["紧张", "激情", "喜悦"],
                "emotion": ["平静", "喜悦", "怀旧"],
                "urban": ["平静", "喜悦", "平静"],
                "suspense": ["神秘", "紧张", "神秘"]
            },
            "comic_drama": {
                "battle": ["紧张", "激情", "喜悦"],
                "romance": ["喜悦", "激情", "喜悦"],
                "story": ["平静", "紧张", "平静"]
            },
            "tvc": {
                "product": ["平静", "喜悦", "喜悦"],
                "brand": ["平静", "喜悦", "怀旧"],
                "promo": ["喜悦", "激情", "激情"],
                "corporate": ["平静", "喜悦", "平静"]
            }
        }
        
        emotions = emotion_maps.get(content_type, {}).get(subtype, ["平静", "喜悦", "平静"])
        num_shots = 12 if board_type == "4x3" else 9
        
        from core.grammar_rules import ColorEvolution
        return ColorEvolution.generate_color_progression(emotions, num_shots)
    
    def _generate_usage_guide(self, content_type: str, subtype: str, board_type: str, director_style: str = None) -> Dict:
        """生成使用指南"""
        guide = {
            "prompt_usage": {
                "description": "每个镜头的prompt可用于AI图像生成工具",
                "tips": [
                    "可根据实际需求修改描述细节",
                    "保持整体风格一致性",
                    "注意人物/场景的连贯性"
                ]
            },
            "grammar_rules": {
                "description": "电影语法规则确保专业质量",
                "key_points": [
                    "30°原则：相邻镜头角度差≥30°",
                    "视线匹配：关键帧保持视线连贯",
                    "动作轴线：保持运动方向一致",
                    "色调演进：根据情感调整色调"
                ]
            },
            "workflow": {
                "steps": [
                    "1. 根据生成的提示词创建视觉参考",
                    "2. 检查语法规则的应用",
                    "3. 调整色调演进方案",
                    "4. 添加声景设计",
                    "5. 输出最终分镜脚本"
                ]
            }
        }
        
        # 如果指定了导演风格，添加导演风格指南
        if director_style:
            style_class = get_director_style(director_style)
            if style_class:
                guide["director_style"] = {
                    "description": f"已应用 {style_class.INFO.get('name', director_style)} 的导演风格",
                    "key_characteristics": style_class.INFO.get("style_keywords", []),
                    "techniques": list(style_class.SIGNATURE_TECHNIQUES.keys()) if hasattr(style_class, 'SIGNATURE_TECHNIQUES') else [],
                    "tips": [
                        "参考导演的代表作品获取视觉灵感",
                        "注意导演标志性的色彩 palette 和光影处理",
                        "学习导演独特的镜头语言和叙事节奏"
                    ]
                }
        
        return guide
    
    def list_available_types(self) -> Dict:
        """列出所有可用类型"""
        result = {}
        for key, info in self.CONTENT_TYPES.items():
            result[key] = {
                "name": info["name"],
                "subtypes": info["subtypes"]
            }
        return result
    
    def list_available_directors(self) -> Dict:
        """列出所有可用导演风格"""
        return list_all_directors()
    
    def get_director_details(self, director_name: str) -> Dict:
        """获取导演详细信息"""
        from knowledge_base.director_styles import (
            get_director_info,
            get_director_techniques,
            get_director_works,
            get_director_visual_traits,
            get_director_storyboard_template
        )
        
        return {
            "info": get_director_info(director_name),
            "techniques": get_director_techniques(director_name),
            "works": get_director_works(director_name),
            "visual_traits": get_director_visual_traits(director_name),
            "storyboard_template": get_director_storyboard_template(director_name)
        }
    
    def export_to_json(self, result: Dict, filepath: str):
        """导出为JSON文件"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
    
    def format_output(self, result: Dict) -> str:
        """格式化输出为可读文本"""
        lines = []
        
        info = result.get("content_info", {})
        lines.append(f"=== 分镜方案 ===")
        lines.append(f"类型: {info.get('type', '')} - {info.get('subtype', '')}")
        lines.append(f"故事板: {info.get('board_type', '')}")
        if info.get('scene_description'):
            lines.append(f"场景: {info['scene_description']}")
        lines.append("")
        
        # 故事板
        storyboard = result.get("storyboard", {})
        lines.append(f"【{storyboard.get('template_name', '')}】")
        lines.append("")
        
        if "rows" in storyboard:
            # 4×3格式
            for row in storyboard["rows"]:
                lines.append(f"--- {row.get('name', '')} ---")
                for shot in row.get("shots", []):
                    lines.append(f"  {shot['index']}. {shot['name']} ({shot['shot_type']})")
                    lines.append(f"     Prompt: {shot.get('prompt', '')}")
                lines.append("")
        else:
            # 3×3格式
            for shot in storyboard.get("shots", []):
                lines.append(f"【镜头 {shot['index']}】{shot['name']}")
                lines.append(f"  景别: {shot['shot_type']}")
                if shot.get('duration'):
                    lines.append(f"  时长: {shot['duration']}")
                if shot.get('angle'):
                    lines.append(f"  角度: {shot['angle']}")
                if shot.get('movement'):
                    lines.append(f"  运镜: {shot['movement']}")
                if shot.get('description'):
                    lines.append(f"  描述: {shot['description']}")
                if shot.get('sound'):
                    lines.append(f"  声音: {shot['sound']}")
                lines.append(f"  Prompt: {shot.get('prompt', '')}")
                lines.append("")
        
        # 色调演进
        lines.append("=== 色调演进建议 ===")
        for color in result.get("color_evolution", []):
            lines.append(f"镜头{color['shot_index']}: {color['emotion']} - {color['primary_color']} ({color['mood']})")
        lines.append("")
        
        # 使用指南
        guide = result.get("usage_guide", {})
        lines.append("=== 使用指南 ===")
        for key, value in guide.items():
            if isinstance(value, dict):
                lines.append(f"\n{key}:")
                lines.append(f"  {value.get('description', '')}")
                if "tips" in value:
                    for tip in value["tips"]:
                        lines.append(f"  - {tip}")
                if "key_points" in value:
                    for point in value["key_points"]:
                        lines.append(f"  - {point}")
                if "steps" in value:
                    for step in value["steps"]:
                        lines.append(f"  {step}")
        
        return "\n".join(lines)


# 便捷函数
def generate_storyboard(content_type: str,
                       subtype: str,
                       board_type: str = "3x3",
                       scene_description: str = "",
                       director_style: str = None) -> Dict:
    """
    快速生成分镜方案
    
    Args:
        content_type: 内容类型 (movie/short_drama/comic_drama/tvc)
        subtype: 子类型
        board_type: 故事板类型 (3x3/4x3)
        scene_description: 场景描述
        director_style: 导演风格 (如 'spielberg', 'wong_kar_wai')
    
    Returns:
        分镜方案字典
    """
    generator = StoryboardGenerator()
    return generator.generate(content_type, subtype, board_type, scene_description, director_style=director_style)


def list_types() -> Dict:
    """列出所有可用类型"""
    generator = StoryboardGenerator()
    return generator.list_available_types()


def list_directors() -> Dict:
    """列出所有可用导演风格"""
    generator = StoryboardGenerator()
    return generator.list_available_directors()


def get_director_info_full(director_name: str) -> Dict:
    """获取导演完整信息"""
    generator = StoryboardGenerator()
    return generator.get_director_details(director_name)


# 示例使用
if __name__ == "__main__":
    print("=== 分镜生成器 ===\n")
    
    # 列出可用类型
    print("可用类型:")
    types = list_types()
    for type_key, type_info in types.items():
        print(f"  {type_key} ({type_info['name']}):")
        for subtype in type_info['subtypes']:
            print(f"    - {subtype}")
    print()
    
    # 列出可用导演
    print("可用导演风格:")
    directors = list_directors()
    for genre, director_list in directors.items():
        print(f"  {genre}:")
        for director in director_list:
            print(f"    - {director}")
    print()
    
    # 生成示例：战争片 3×3 无导演风格
    print("=== 示例1：战争片 3×3 分镜（标准） ===\n")
    result = generate_storyboard("movie", "war", "3x3", "诺曼底登陆场景")
    
    generator = StoryboardGenerator()
    print(generator.format_output(result))
    print("\n" + "="*50 + "\n")
    
    # 生成示例：战争片 3×3 斯皮尔伯格风格
    print("=== 示例2：战争片 3×3 分镜（斯皮尔伯格风格） ===\n")
    result_spielberg = generate_storyboard("movie", "war", "3x3", "诺曼底登陆场景", director_style="spielberg")
    print(generator.format_output(result_spielberg))
    print("\n" + "="*50 + "\n")
    
    # 生成示例：文艺片 王家卫风格
    print("=== 示例3：文艺片 3×3 分镜（王家卫风格） ===\n")
    result_wong = generate_storyboard("movie", "art", "3x3", "都市夜晚相遇", director_style="wong_kar_wai")
    print(generator.format_output(result_wong))
