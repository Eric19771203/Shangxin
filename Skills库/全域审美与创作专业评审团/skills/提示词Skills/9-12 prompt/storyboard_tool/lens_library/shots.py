"""
镜头语言库 - 景别系统
包含各种景别的定义、特点和应用场景
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class ShotType:
    """景别类型定义"""
    code: str                          # 缩写代码
    name: str                          # 中文名称
    english_name: str                  # 英文名称
    description: str                   # 描述
    framing: str                       # 取景范围
    emotional_effect: str              # 情绪效果
    typical_use: List[str]             # 典型用途
    lens_suggestion: str               # 镜头建议


class ShotLibrary:
    """景别库"""
    
    SHOTS = {
        "ELS": ShotType(
            code="ELS",
            name="大远景",
            english_name="Extreme Long Shot",
            description="展现宏大场景和环境",
            framing="人物占画面比例很小，重点展现场景",
            emotional_effect="史诗感、渺小感、环境压迫",
            typical_use=["开场建立", "史诗场景", "环境展示", "结尾留白"],
            lens_suggestion="广角镜头 16-35mm"
        ),
        "LS": ShotType(
            code="LS",
            name="远景",
            english_name="Long Shot",
            description="展示人物全身及周围环境",
            framing="人物全身，头部到脚部",
            emotional_effect="客观、疏离、环境关系",
            typical_use=["人物入场", "动作展示", "空间关系"],
            lens_suggestion="广角至标准 24-50mm"
        ),
        "FS": ShotType(
            code="FS",
            name="全景",
            english_name="Full Shot",
            description="人物全身，接近画面边缘",
            framing="人物全身，填满画面",
            emotional_effect="完整、正式、展示",
            typical_use=["人物介绍", "服装展示", "动作完整"],
            lens_suggestion="标准镜头 35-50mm"
        ),
        "MLS": ShotType(
            code="MLS",
            name="中全景",
            english_name="Medium Long Shot",
            description="膝盖以上",
            framing="人物膝盖以上",
            emotional_effect="社交距离、关系建立",
            typical_use=["双人对话", "关系展示", "肢体语言"],
            lens_suggestion="标准镜头 50mm"
        ),
        "MS": ShotType(
            code="MS",
            name="中景",
            english_name="Medium Shot",
            description="腰部以上，最常用景别",
            framing="人物腰部以上",
            emotional_effect="中性、舒适、对话标准",
            typical_use=["对话场景", "动作细节", "叙事推进"],
            lens_suggestion="标准至中长焦 50-85mm"
        ),
        "MCU": ShotType(
            code="MCU",
            name="中近景",
            english_name="Medium Close-Up",
            description="胸部以上",
            framing="人物胸部以上",
            emotional_effect="亲密、情绪开始显现",
            typical_use=["情绪表达", "重要对话", "反应镜头"],
            lens_suggestion="中长焦 85mm"
        ),
        "CU": ShotType(
            code="CU",
            name="近景",
            english_name="Close-Up",
            description="头部和肩部",
            framing="头部和肩部",
            emotional_effect="亲密、情绪强烈",
            typical_use=["情绪高潮", "重要细节", "反应特写"],
            lens_suggestion="长焦 85-135mm"
        ),
        "ECU": ShotType(
            code="ECU",
            name="大特写",
            english_name="Extreme Close-Up",
            description="面部局部或物品细节",
            framing="眼睛、嘴巴或物品细节",
            emotional_effect="极度亲密、心理深度",
            typical_use=["心理刻画", "关键道具", "强烈情绪"],
            lens_suggestion="长焦或微距 100-135mm"
        ),
    }
    
    @classmethod
    def get_shot(cls, code: str) -> ShotType:
        """获取指定景别"""
        return cls.SHOTS.get(code)
    
    @classmethod
    def get_all_shots(cls) -> Dict[str, ShotType]:
        """获取所有景别"""
        return cls.SHOTS
    
    @classmethod
    def get_shot_sequence(cls, emotion_progression: str = "neutral_to_intense") -> List[str]:
        """
        获取推荐的景别序列
        
        Args:
            emotion_progression: 情绪递进类型
                - neutral_to_intense: 中性到强烈
                - distant_to_intimate: 疏离到亲密
                - epic_to_personal: 史诗到个人
        
        Returns:
            景别代码列表
        """
        sequences = {
            "neutral_to_intense": ["LS", "MS", "MCU", "CU", "ECU"],
            "distant_to_intimate": ["ELS", "LS", "MLS", "MS", "CU"],
            "epic_to_personal": ["ELS", "FS", "MS", "MCU", "ECU"],
            "dialogue_standard": ["MS", "MCU", "MS", "MCU"],
            "action_sequence": ["LS", "MS", "CU", "ECU", "LS"],
        }
        return sequences.get(emotion_progression, sequences["neutral_to_intense"])


# 便捷函数
def get_shot_info(code: str) -> ShotType:
    """获取景别信息"""
    return ShotLibrary.get_shot(code)


def list_all_shots() -> List[str]:
    """列出所有景别代码"""
    return list(ShotLibrary.SHOTS.keys())


def get_shot_sequence(emotion_type: str = "neutral_to_intense") -> List[str]:
    """获取景别序列"""
    return ShotLibrary.get_shot_sequence(emotion_type)


if __name__ == "__main__":
    print("=== 景别库 ===")
    for code, shot in ShotLibrary.SHOTS.items():
        print(f"\n{code} - {shot.name} ({shot.english_name})")
        print(f"  描述: {shot.description}")
        print(f"  取景: {shot.framing}")
        print(f"  情绪: {shot.emotional_effect}")
        print(f"  镜头: {shot.lens_suggestion}")
