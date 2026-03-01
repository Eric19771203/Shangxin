"""
分镜工具 - 电影语法规则模块
包含30°原则、视线匹配、动作轴线、色调演进、声景提示等专业规则
"""

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import math


class GrammarRuleType(Enum):
    """语法规则类型"""
    ANGLE_30_RULE = "30_degree_rule"           # 30°原则
    EYELINE_MATCH = "eyeline_match"            # 视线匹配
    ACTION_AXIS = "action_axis"                # 动作轴线
    COLOR_EVOLUTION = "color_evolution"        # 色调演进
    SOUNDSCAPE = "soundscape"                  # 声景提示


@dataclass
class CameraAngle:
    """摄像机角度定义"""
    name: str                                  # 角度名称
    degrees: float                             # 角度值（度）
    description: str                           # 描述
    emotional_effect: str                      # 情绪效果


class Angle30Rule:
    """
    30°原则
    相邻镜头角度差≥30°，避免跳切造成的视觉跳跃
    """
    
    # 标准角度位置
    STANDARD_ANGLES = [
        CameraAngle("正面", 0, "直接面对被摄体", "正式、直接、亲密"),
        CameraAngle("前侧45°", 45, "左/右前侧45度", "自然、立体、常用"),
        CameraAngle("正侧90°", 90, "正侧面", "分离、对抗、平行"),
        CameraAngle("后侧45°", 135, "左/右后侧45度", "神秘、观察、不安"),
        CameraAngle("背面", 180, "完全背面", "未知、跟随、主观"),
        CameraAngle("反侧135°", 225, "另一侧135度", "对称角度"),
        CameraAngle("反侧90°", 270, "另一正侧面", "对称侧面"),
        CameraAngle("反侧45°", 315, "另一侧45度", "对称前侧"),
    ]
    
    MIN_ANGLE_DIFF = 30                        # 最小角度差
    
    @classmethod
    def check_angle_diff(cls, angle1: float, angle2: float) -> Tuple[bool, float]:
        """
        检查两个角度是否满足30°原则
        
        Returns:
            (是否满足, 实际角度差)
        """
        diff = abs(angle2 - angle1)
        # 考虑360度循环
        diff = min(diff, 360 - diff)
        return diff >= cls.MIN_ANGLE_DIFF, diff
    
    @classmethod
    def get_valid_next_angles(cls, current_angle: float) -> List[CameraAngle]:
        """
        获取当前角度下，满足30°原则的可选角度
        """
        valid_angles = []
        for angle in cls.STANDARD_ANGLES:
            is_valid, diff = cls.check_angle_diff(current_angle, angle.degrees)
            if is_valid:
                valid_angles.append(angle)
        return valid_angles
    
    @classmethod
    def suggest_angle_sequence(cls, start_angle: float = 0, num_shots: int = 3) -> List[float]:
        """
        建议满足30°原则的角度序列
        
        Args:
            start_angle: 起始角度
            num_shots: 镜头数量
        
        Returns:
            角度序列列表
        """
        sequence = [start_angle]
        current = start_angle
        
        for _ in range(num_shots - 1):
            valid_angles = cls.get_valid_next_angles(current)
            if valid_angles:
                # 选择角度差最接近45°的角度（标准变化）
                best_angle = min(valid_angles, 
                    key=lambda a: abs(45 - min(abs(a.degrees - current), 360 - abs(a.degrees - current))))
                sequence.append(best_angle.degrees)
                current = best_angle.degrees
        
        return sequence


class EyelineMatch:
    """
    视线匹配规则
    保持对话或视线交流时的人物视线方向一致性
    """
    
    @staticmethod
    def calculate_eyeline_direction(subject_position: Tuple[float, float], 
                                   look_at_position: Tuple[float, float]) -> str:
        """
        计算视线方向
        
        Args:
            subject_position: 被摄体位置 (x, y)
            look_at_position: 注视目标位置 (x, y)
        
        Returns:
            视线方向描述
        """
        dx = look_at_position[0] - subject_position[0]
        dy = look_at_position[1] - subject_position[1]
        
        # 计算角度
        angle = math.degrees(math.atan2(dy, dx))
        
        # 转换为方向描述
        if -22.5 <= angle < 22.5:
            return "向右看"
        elif 22.5 <= angle < 67.5:
            return "向右上方看"
        elif 67.5 <= angle < 112.5:
            return "向上看"
        elif 112.5 <= angle < 157.5:
            return "向左上方看"
        elif 157.5 <= angle or angle < -157.5:
            return "向左看"
        elif -157.5 <= angle < -112.5:
            return "向左下方看"
        elif -112.5 <= angle < -67.5:
            return "向下看"
        else:
            return "向右下方看"
    
    @staticmethod
    def match_dialogue_eyelines(char1_screen_side: str, char2_screen_side: str) -> Dict[str, str]:
        """
        匹配对话双方的视线方向
        
        Args:
            char1_screen_side: 角色1在画面中的位置 ("left"/"right")
            char2_screen_side: 角色2在画面中的位置 ("left"/"right")
        
        Returns:
            视线方向建议
        """
        if char1_screen_side == "left" and char2_screen_side == "right":
            return {
                "char1_eyeline": "向右看（看向角色2）",
                "char2_eyeline": "向左看（看向角色1）",
                "note": "标准正反打，视线交叉"
            }
        elif char1_screen_side == "right" and char2_screen_side == "left":
            return {
                "char1_eyeline": "向左看（看向角色2）",
                "char2_eyeline": "向右看（看向角色1）",
                "note": "标准正反打，视线交叉"
            }
        else:
            return {
                "char1_eyeline": "根据位置调整",
                "char2_eyeline": "根据位置调整",
                "note": "同侧构图，注意视线方向一致性"
            }
    
    # 视线匹配关键帧（3×3中的第2/5/8格）
    KEYFRAME_POSITIONS = [2, 5, 8]
    
    @classmethod
    def check_keyframe_eyelines(cls, shots: List[Dict]) -> List[Dict]:
        """
        检查关键帧的视线连贯性
        """
        issues = []
        for i, pos in enumerate(cls.KEYFRAME_POSITIONS):
            if pos <= len(shots):
                shot = shots[pos - 1]
                issues.append({
                    "position": pos,
                    "shot_name": shot.get("name", ""),
                    "eyeline_check": "需要保持视线方向一致",
                    "suggestion": f"确保第{pos}格的视线与前后镜头连贯"
                })
        return issues


class ActionAxis:
    """
    动作轴线规则
    3×3用内三角轴线，4×3用Z型轴线
    """
    
    AXIS_TYPES = {
        "inner_triangle": {
            "name": "内三角轴线",
            "description": "适用于3×3标准叙事板，形成稳定的三角形运动轨迹",
            "pattern": [(0, 0), (1, 0.5), (0.5, 1)],  # 相对坐标
            "suitable_for": "3x3_standard",
            "advantage": "稳定、经典、易于理解"
        },
        "z_axis": {
            "name": "Z型轴线",
            "description": "适用于4×3史诗叙事板，形成Z字形递进运动",
            "pattern": [(0, 0), (1, 0), (1, 0.5), (0, 0.5), (0, 1), (1, 1)],
            "suitable_for": "4x3_epic",
            "advantage": "动态、史诗感、空间感强"
        },
        "s_curve": {
            "name": "S型轴线",
            "description": "柔和过渡，适用于情感类叙事",
            "pattern": "平滑曲线",
            "suitable_for": "emotional",
            "advantage": "柔和、流畅、情绪递进"
        },
        "linear": {
            "name": "直线轴线",
            "description": "直接明了，适用于动作追逐场景",
            "pattern": "直线",
            "suitable_for": "action",
            "advantage": "直接、紧张、清晰"
        }
    }
    
    @classmethod
    def get_axis_for_board(cls, board_type: str) -> Dict:
        """根据故事板类型获取推荐轴线"""
        if board_type == "3x3_standard":
            return cls.AXIS_TYPES["inner_triangle"]
        elif board_type == "4x3_epic":
            return cls.AXIS_TYPES["z_axis"]
        return cls.AXIS_TYPES["inner_triangle"]
    
    @staticmethod
    def maintain_axis(shots: List[Dict], axis_type: str = "inner_triangle") -> List[Dict]:
        """
        维护动作轴线一致性
        
        Args:
            shots: 镜头列表
            axis_type: 轴线类型
        
        Returns:
            带轴线建议的镜头列表
        """
        annotated_shots = []
        
        for i, shot in enumerate(shots):
            annotation = {
                "axis_position": i + 1,
                "axis_note": f"保持{axis_type}轴线一致性",
                "direction_check": "检查人物/运动方向是否一致"
            }
            
            if i > 0:
                annotation["continuity"] = f"与前镜头保持轴线关系"
            
            shot_with_axis = {**shot, **annotation}
            annotated_shots.append(shot_with_axis)
        
        return annotated_shots


class ColorEvolution:
    """
    色调演进规则
    根据情感基调进行色调渐变
    """
    
    # 情感色调映射
    EMOTION_COLOR_MAP = {
        "平静": {
            "colors": ["#E8F4F8", "#B8E0F0", "#88CCE8"],
            "description": "冷色调，低饱和度",
            "lighting": "柔和自然光",
            "mood": "宁静、平和"
        },
        "紧张": {
            "colors": ["#4A4A4A", "#6B4C4C", "#8B0000"],
            "description": "暗色调，高对比度",
            "lighting": "侧光、阴影",
            "mood": "压抑、不安"
        },
        "喜悦": {
            "colors": ["#FFE4B5", "#FFD700", "#FFA500"],
            "description": "暖色调，高饱和度",
            "lighting": "明亮、逆光",
            "mood": "温暖、积极"
        },
        "悲伤": {
            "colors": ["#2F4F4F", "#4A6464", "#708090"],
            "description": "灰蓝色调，低饱和度",
            "lighting": "阴天、散射光",
            "mood": "忧郁、沉重"
        },
        "神秘": {
            "colors": ["#191970", "#4B0082", "#800080"],
            "description": "深紫蓝色调",
            "lighting": "局部照明、剪影",
            "mood": "神秘、未知"
        },
        "激情": {
            "colors": ["#DC143C", "#FF4500", "#FF6347"],
            "description": "红橙色调，高饱和度",
            "lighting": "戏剧化照明",
            "mood": "热烈、冲动"
        },
        "怀旧": {
            "colors": ["#D2B48C", "#DEB887", "#F5DEB3"],
            "description": " sepia/暖棕色调",
            "lighting": "柔光、过曝",
            "mood": "回忆、温暖"
        }
    }
    
    @classmethod
    def generate_color_progression(cls, emotions: List[str], num_shots: int) -> List[Dict]:
        """
        生成色调演进序列
        
        Args:
            emotions: 情感序列
            num_shots: 镜头数量
        
        Returns:
            每个镜头的色调建议
        """
        color_sequence = []
        
        # 将情感映射到镜头
        emotion_per_shot = len(emotions) / num_shots
        
        for i in range(num_shots):
            emotion_index = min(int(i * emotion_per_shot), len(emotions) - 1)
            emotion = emotions[emotion_index]
            
            color_info = cls.EMOTION_COLOR_MAP.get(emotion, cls.EMOTION_COLOR_MAP["平静"])
            
            color_sequence.append({
                "shot_index": i + 1,
                "emotion": emotion,
                "primary_color": color_info["colors"][0],
                "secondary_color": color_info["colors"][1] if len(color_info["colors"]) > 1 else None,
                "description": color_info["description"],
                "lighting": color_info["lighting"],
                "mood": color_info["mood"]
            })
        
        return color_sequence
    
    @classmethod
    def suggest_color_transition(cls, from_emotion: str, to_emotion: str) -> Dict:
        """建议两个情感之间的色调过渡"""
        from_color = cls.EMOTION_COLOR_MAP.get(from_emotion, {})
        to_color = cls.EMOTION_COLOR_MAP.get(to_emotion, {})
        
        return {
            "from": from_emotion,
            "to": to_emotion,
            "transition_type": "渐变" if from_emotion != to_emotion else "保持",
            "suggestion": f"从{from_color.get('description', '')}过渡到{to_color.get('description', '')}",
            "technique": "使用滤镜、调色或自然光变化"
        }


class SoundscapeHints:
    """
    声景提示规则
    关键帧标注声音元素
    """
    
    # 声音类型定义
    SOUND_TYPES = {
        "ambient": {
            "name": "环境音",
            "description": "背景环境声音",
            "examples": ["风声", "雨声", "城市噪音", "鸟鸣"],
            "priority": "低",
            "function": "营造氛围"
        },
        "dialogue": {
            "name": "对白",
            "description": "人物对话",
            "examples": ["台词", "独白", "旁白"],
            "priority": "高",
            "function": "叙事推进"
        },
        "foley": {
            "name": "拟音",
            "description": "动作音效",
            "examples": ["脚步声", "关门声", "物体碰撞"],
            "priority": "中",
            "function": "增强真实感"
        },
        "music": {
            "name": "音乐",
            "description": "背景音乐",
            "examples": ["主题曲", "情绪音乐", "过渡音乐"],
            "priority": "中",
            "function": "情绪引导"
        },
        "effect": {
            "name": "特效音",
            "description": "特殊音效",
            "examples": ["爆炸", "魔法", "科幻音效"],
            "priority": "高",
            "function": "视觉冲击"
        },
        "silence": {
            "name": "静默",
            "description": "刻意留白",
            "examples": ["完全安静", "渐弱至无声"],
            "priority": "高",
            "function": "强调、转折"
        }
    }
    
    # 关键帧声音提示（对应3×3的第2/5/8格）
    KEYFRAME_SOUNDS = {
        2: {
            "suggestion": "人物入场音效",
            "types": ["foley", "ambient"],
            "note": "配合人物动作的脚步声或环境音"
        },
        5: {
            "suggestion": "情绪转折音效",
            "types": ["music", "effect"],
            "note": "音乐情绪转变或关键音效"
        },
        8: {
            "suggestion": "心理镜像音效",
            "types": ["silence", "effect"],
            "note": "静默或内心独白的回声效果"
        }
    }
    
    @classmethod
    def get_keyframe_sound_hints(cls, keyframe_positions: List[int] = None) -> Dict:
        """获取关键帧声音提示"""
        if keyframe_positions is None:
            keyframe_positions = [2, 5, 8]
        
        hints = {}
        for pos in keyframe_positions:
            if pos in cls.KEYFRAME_SOUNDS:
                hints[pos] = cls.KEYFRAME_SOUNDS[pos]
        
        return hints
    
    @classmethod
    def generate_soundscape_plan(cls, shots: List[Dict], genre: str = "general") -> List[Dict]:
        """
        生成完整声景计划
        
        Args:
            shots: 镜头列表
            genre: 类型（影响声音选择）
        
        Returns:
            每个镜头的声音提示
        """
        sound_plan = []
        
        for i, shot in enumerate(shots):
            shot_sound = {
                "shot_index": i + 1,
                "shot_name": shot.get("name", ""),
                "primary_sound": None,
                "secondary_sounds": [],
                "transition": None
            }
            
            # 根据镜头类型分配声音
            if "对话" in shot.get("name", "") or "对白" in shot.get("name", ""):
                shot_sound["primary_sound"] = cls.SOUND_TYPES["dialogue"]
            elif "特写" in shot.get("shot_type", ""):
                shot_sound["primary_sound"] = cls.SOUND_TYPES["foley"]
                shot_sound["secondary_sounds"] = [cls.SOUND_TYPES["ambient"]]
            elif "远景" in shot.get("shot_type", ""):
                shot_sound["primary_sound"] = cls.SOUND_TYPES["ambient"]
                shot_sound["secondary_sounds"] = [cls.SOUND_TYPES["music"]]
            else:
                shot_sound["primary_sound"] = cls.SOUND_TYPES["ambient"]
            
            # 关键帧特殊处理
            if (i + 1) in cls.KEYFRAME_SOUNDS:
                keyframe_hint = cls.KEYFRAME_SOUNDS[i + 1]
                shot_sound["keyframe_note"] = keyframe_hint["suggestion"]
            
            sound_plan.append(shot_sound)
        
        return sound_plan


class GrammarRuleEngine:
    """语法规则引擎 - 整合所有规则"""
    
    def __init__(self):
        self.angle_rule = Angle30Rule()
        self.eyeline_rule = EyelineMatch()
        self.axis_rule = ActionAxis()
        self.color_rule = ColorEvolution()
        self.sound_rule = SoundscapeHints()
    
    def apply_all_rules(self, shots: List[Dict], board_type: str = "3x3_standard") -> Dict:
        """
        应用所有语法规则
        
        Args:
            shots: 镜头列表
            board_type: 故事板类型
        
        Returns:
            包含所有规则建议的字典
        """
        return {
            "angle_30_rule": {
                "description": "相邻镜头角度差≥30°",
                "suggested_sequence": self.angle_rule.suggest_angle_sequence(num_shots=len(shots)),
                "note": "避免跳切造成的视觉跳跃"
            },
            "eyeline_match": {
                "description": "关键帧视线连贯",
                "keyframe_positions": [2, 5, 8],
                "check_result": self.eyeline_rule.check_keyframe_eyelines(shots)
            },
            "action_axis": {
                "description": "动作轴线一致性",
                "recommended_axis": self.axis_rule.get_axis_for_board(board_type),
                "annotated_shots": self.axis_rule.maintain_axis(shots, 
                    self.axis_rule.get_axis_for_board(board_type)["name"])
            },
            "color_evolution": {
                "description": "色调渐变",
                "note": "根据情感基调调整色调"
            },
            "soundscape": {
                "description": "声景设计",
                "keyframe_hints": self.sound_rule.get_keyframe_sound_hints(),
                "sound_plan": self.sound_rule.generate_soundscape_plan(shots)
            }
        }


# 便捷函数
def check_30_degree_rule(angle1: float, angle2: float) -> Tuple[bool, float]:
    """检查30°原则"""
    return Angle30Rule.check_angle_diff(angle1, angle2)


def get_color_progression(emotions: List[str], num_shots: int) -> List[Dict]:
    """获取色调演进序列"""
    return ColorEvolution.generate_color_progression(emotions, num_shots)


def get_sound_hints(keyframe_positions: List[int] = None) -> Dict:
    """获取声景提示"""
    return SoundscapeHints.get_keyframe_sound_hints(keyframe_positions)


if __name__ == "__main__":
    # 测试代码
    print("=== 30°原则测试 ===")
    result, diff = check_30_degree_rule(0, 45)
    print(f"角度0°到45°: 满足={result}, 差值={diff}°")
    
    result, diff = check_30_degree_rule(0, 20)
    print(f"角度0°到20°: 满足={result}, 差值={diff}°")
    
    print("\n=== 建议角度序列 ===")
    sequence = Angle30Rule.suggest_angle_sequence(0, 5)
    print(f"从0°开始的5个镜头角度序列: {sequence}")
    
    print("\n=== 视线匹配测试 ===")
    eyeline = EyelineMatch.match_dialogue_eyelines("left", "right")
    print(f"左右对话视线: {eyeline}")
    
    print("\n=== 轴线类型 ===")
    for axis_type, axis_info in ActionAxis.AXIS_TYPES.items():
        print(f"{axis_info['name']}: {axis_info['description']}")
    
    print("\n=== 色调演进 ===")
    emotions = ["平静", "紧张", "悲伤"]
    color_prog = get_color_progression(emotions, 9)
    for c in color_prog[:3]:
        print(f"镜头{c['shot_index']}: {c['emotion']} - {c['primary_color']} ({c['mood']})")
    
    print("\n=== 声景提示 ===")
    sound_hints = get_sound_hints()
    for pos, hint in sound_hints.items():
        print(f"关键帧{pos}: {hint['suggestion']}")
