"""
分镜工具 - 核心框架模块
包含 3×3 标准叙事板和 4×3 沉浸式故事板的基础结构
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class BoardType(Enum):
    """故事板类型"""
    STANDARD_3X3 = "3x3_standard"      # 3×3标准叙事板（精简节奏）
    EPIC_4X3 = "4x3_epic"              # 4×3沉浸式故事板（史诗节奏）


@dataclass
class Shot:
    """单个镜头定义"""
    index: int                         # 镜头序号
    name: str                          # 镜头名称
    shot_type: str                     # 景别类型
    angle: str                         # 角度
    movement: Optional[str] = None     # 运镜方式
    duration: Optional[float] = None   # 时长（秒）
    description: str = ""              # 画面描述
    sound_hint: str = ""               # 声景提示
    color_tone: str = ""               # 色调提示
    prompt: str = ""                   # AI生成提示词


class BaseFramework:
    """基础框架类"""
    
    def __init__(self, board_type: BoardType):
        self.board_type = board_type
        self.shots: List[Shot] = []
        self._init_structure()
    
    def _init_structure(self):
        """初始化故事板结构"""
        if self.board_type == BoardType.STANDARD_3X3:
            self._init_3x3_structure()
        elif self.board_type == BoardType.EPIC_4X3:
            self._init_4x3_structure()
    
    def _init_3x3_structure(self):
        """
        3×3标准叙事板结构（精简节奏）
        9格经典叙事结构
        """
        structure = [
            # 第一行：空间与入场
            {"name": "建立空间", "shot_type": "大远景/远景", "description": "建立故事发生的空间环境"},
            {"name": "人物入场", "shot_type": "全景/全身", "description": "主要人物进入画面"},
            {"name": "关系建立", "shot_type": "中全景", "description": "人物与环境/人物间关系"},
            
            # 第二行：动作与情绪
            {"name": "动作发起", "shot_type": "中景", "description": "核心动作开始"},
            {"name": "情绪转折", "shot_type": "中近景", "description": "情绪发生变化的关键点"},
            {"name": "细节聚焦", "shot_type": "近景", "description": "重要细节展示"},
            
            # 第三行：象征与结局
            {"name": "象征元素", "shot_type": "特写A", "description": "具有象征意义的物品/细节"},
            {"name": "心理镜像", "shot_type": "特写B", "description": "人物内心世界的映射"},
            {"name": "结局留白", "shot_type": "远景/开放式构图", "description": "开放式结局，给观众想象空间"},
        ]
        
        for i, item in enumerate(structure, 1):
            self.shots.append(Shot(
                index=i,
                name=item["name"],
                shot_type=item["shot_type"],
                angle="",
                description=item["description"]
            ))
    
    def _init_4x3_structure(self):
        """
        4×3沉浸式故事板结构（史诗节奏）
        12格史诗结构，三行递进
        """
        structure = [
            # 第一行：世界展开（4个递进远景）
            {"name": "世界全景", "shot_type": "大远景", "description": "宏大世界观展示"},
            {"name": "环境递进", "shot_type": "远景", "description": "环境细节递进"},
            {"name": "空间转换", "shot_type": "远景/全景", "description": "空间层次转换"},
            {"name": "氛围营造", "shot_type": "全景", "description": "整体氛围确立"},
            
            # 第二行：人物轨迹（4个关系镜头）
            {"name": "人物登场", "shot_type": "全景", "description": "主要人物登场"},
            {"name": "关系网络", "shot_type": "中全景", "description": "人物关系网络"},
            {"name": "互动发展", "shot_type": "中景", "description": "人物互动发展"},
            {"name": "冲突建立", "shot_type": "中近景", "description": "矛盾冲突建立"},
            
            # 第三行：冲突核心（4个情绪特写）
            {"name": "情绪爆发", "shot_type": "近景", "description": "情绪达到高潮"},
            {"name": "细节冲击", "shot_type": "特写", "description": "关键细节冲击"},
            {"name": "心理刻画", "shot_type": "大特写", "description": "深度心理刻画"},
            {"name": "余韵留白", "shot_type": "远景/空镜", "description": "余韵与思考空间"},
        ]
        
        for i, item in enumerate(structure, 1):
            self.shots.append(Shot(
                index=i,
                name=item["name"],
                shot_type=item["shot_type"],
                angle="",
                description=item["description"]
            ))
    
    def get_shot(self, index: int) -> Optional[Shot]:
        """获取指定镜头"""
        for shot in self.shots:
            if shot.index == index:
                return shot
        return None
    
    def update_shot(self, index: int, **kwargs) -> bool:
        """更新镜头信息"""
        shot = self.get_shot(index)
        if shot:
            for key, value in kwargs.items():
                if hasattr(shot, key):
                    setattr(shot, key, value)
            return True
        return False
    
    def get_structure_info(self) -> Dict[str, Any]:
        """获取结构信息"""
        return {
            "board_type": self.board_type.value,
            "total_shots": len(self.shots),
            "rows": 3 if self.board_type == BoardType.STANDARD_3X3 else 3,
            "cols": 3 if self.board_type == BoardType.STANDARD_3X3 else 4,
            "shots": [
                {
                    "index": s.index,
                    "name": s.name,
                    "shot_type": s.shot_type,
                    "description": s.description
                }
                for s in self.shots
            ]
        }


class NarrativeFramework:
    """叙事框架管理器"""
    
    # 3×3标准叙事板模板
    STANDARD_3X3_TEMPLATES = {
        "classic_narrative": {
            "name": "经典叙事",
            "description": "适用于大多数叙事场景的标准结构",
            "shots": [
                {"index": 1, "name": "建立空间", "type": "ELS/LS", "function": "空间建立"},
                {"index": 2, "name": "人物入场", "type": "FS", "function": "人物介绍"},
                {"index": 3, "name": "关系建立", "type": "MLS", "function": "关系展示"},
                {"index": 4, "name": "动作发起", "type": "MS", "function": "冲突启动"},
                {"index": 5, "name": "情绪转折", "type": "MCU", "function": "情绪变化"},
                {"index": 6, "name": "细节聚焦", "type": "CU", "function": "细节强调"},
                {"index": 7, "name": "象征元素", "type": "ECU-A", "function": "符号隐喻"},
                {"index": 8, "name": "心理镜像", "type": "ECU-B", "function": "内心映射"},
                {"index": 9, "name": "结局留白", "type": "LS/Open", "function": "开放式结局"},
            ]
        },
        "emotional_arc": {
            "name": "情绪弧线",
            "description": "强调情绪起伏的叙事结构",
            "shots": [
                {"index": 1, "name": "平静开端", "type": "LS", "function": "平静氛围"},
                {"index": 2, "name": "情绪触发", "type": "MS", "function": "触发事件"},
                {"index": 3, "name": "情绪上升", "type": "MCU", "function": "情绪积累"},
                {"index": 4, "name": "情绪高潮", "type": "CU", "function": "情绪爆发"},
                {"index": 5, "name": "转折瞬间", "type": "ECU", "function": "关键转折"},
                {"index": 6, "name": "情绪回落", "type": "MCU", "function": "情绪释放"},
                {"index": 7, "name": "反思时刻", "type": "MS", "function": "内心反思"},
                {"index": 8, "name": "新的领悟", "type": "CU", "function": "领悟瞬间"},
                {"index": 9, "name": "情绪归宿", "type": "LS", "function": "情绪收束"},
            ]
        },
        "suspense_build": {
            "name": "悬念构建",
            "description": "适用于悬疑惊悚类叙事",
            "shots": [
                {"index": 1, "name": "神秘环境", "type": "ELS", "function": "氛围营造"},
                {"index": 2, "name": "异常迹象", "type": "FS", "function": "异常展示"},
                {"index": 3, "name": "怀疑产生", "type": "MLS", "function": "怀疑情绪"},
                {"index": 4, "name": "紧张升级", "type": "MS", "function": "紧张递进"},
                {"index": 5, "name": "危机临近", "type": "MCU", "function": "危机预感"},
                {"index": 6, "name": "真相揭示", "type": "CU", "function": "真相展现"},
                {"index": 7, "name": "关键证据", "type": "ECU", "function": "证据特写"},
                {"index": 8, "name": "心理冲击", "type": "ECU", "function": "冲击瞬间"},
                {"index": 9, "name": "悬念延续", "type": "LS", "function": "悬念保持"},
            ]
        }
    }
    
    # 4×3史诗叙事板模板
    EPIC_4X3_TEMPLATES = {
        "epic_journey": {
            "name": "史诗旅程",
            "description": "适用于宏大叙事的史诗结构",
            "rows": [
                {
                    "name": "世界展开",
                    "shots": [
                        {"index": 1, "name": "宇宙全景", "type": "ELS", "function": "世界观"},
                        {"index": 2, "name": "地域展示", "type": "LS", "function": "地域特征"},
                        {"index": 3, "name": "时代氛围", "type": "LS/FS", "function": "时代感"},
                        {"index": 4, "name": "环境细节", "type": "FS", "function": "环境细节"},
                    ]
                },
                {
                    "name": "人物轨迹",
                    "shots": [
                        {"index": 5, "name": "英雄登场", "type": "FS", "function": "主角登场"},
                        {"index": 6, "name": "群像关系", "type": "MLS", "function": "人物关系"},
                        {"index": 7, "name": "命运交织", "type": "MS", "function": "命运交织"},
                        {"index": 8, "name": "冲突爆发", "type": "MCU", "function": "核心冲突"},
                    ]
                },
                {
                    "name": "冲突核心",
                    "shots": [
                        {"index": 9, "name": "内心挣扎", "type": "CU", "function": "内心戏"},
                        {"index": 10, "name": "关键抉择", "type": "ECU", "function": "抉择瞬间"},
                        {"index": 11, "name": "牺牲时刻", "type": "ECU", "function": "牺牲精神"},
                        {"index": 12, "name": "史诗余韵", "type": "ELS", "function": "史诗收束"},
                    ]
                }
            ]
        },
        "multi_thread": {
            "name": "多线叙事",
            "description": "适用于多线并进的复杂叙事",
            "rows": [
                {
                    "name": "线索展开",
                    "shots": [
                        {"index": 1, "name": "线索A开端", "type": "LS", "function": "线索A"},
                        {"index": 2, "name": "线索B开端", "type": "LS", "function": "线索B"},
                        {"index": 3, "name": "线索C开端", "type": "LS", "function": "线索C"},
                        {"index": 4, "name": "线索D开端", "type": "LS", "function": "线索D"},
                    ]
                },
                {
                    "name": "线索交织",
                    "shots": [
                        {"index": 5, "name": "AB交汇", "type": "MS", "function": "线索交汇"},
                        {"index": 6, "name": "BC碰撞", "type": "MS", "function": "线索碰撞"},
                        {"index": 7, "name": "CD融合", "type": "MS", "function": "线索融合"},
                        {"index": 8, "name": "全面交织", "type": "MCU", "function": "全面交织"},
                    ]
                },
                {
                    "name": "高潮收束",
                    "shots": [
                        {"index": 9, "name": "真相浮现", "type": "CU", "function": "真相揭示"},
                        {"index": 10, "name": "人物抉择", "type": "ECU", "function": "关键抉择"},
                        {"index": 11, "name": "命运收束", "type": "CU", "function": "命运收束"},
                        {"index": 12, "name": "全新开始", "type": "ELS", "function": "新的开始"},
                    ]
                }
            ]
        }
    }
    
    @classmethod
    def get_template(cls, board_type: BoardType, template_name: str) -> Optional[Dict]:
        """获取指定模板"""
        if board_type == BoardType.STANDARD_3X3:
            return cls.STANDARD_3X3_TEMPLATES.get(template_name)
        elif board_type == BoardType.EPIC_4X3:
            return cls.EPIC_4X3_TEMPLATES.get(template_name)
        return None
    
    @classmethod
    def list_templates(cls, board_type: BoardType) -> List[str]:
        """列出所有可用模板"""
        if board_type == BoardType.STANDARD_3X3:
            return list(cls.STANDARD_3X3_TEMPLATES.keys())
        elif board_type == BoardType.EPIC_4X3:
            return list(cls.EPIC_4X3_TEMPLATES.keys())
        return []


# 便捷函数
def create_standard_3x3() -> BaseFramework:
    """创建3×3标准叙事板"""
    return BaseFramework(BoardType.STANDARD_3X3)


def create_epic_4x3() -> BaseFramework:
    """创建4×3史诗叙事板"""
    return BaseFramework(BoardType.EPIC_4X3)


if __name__ == "__main__":
    # 测试代码
    print("=== 3×3标准叙事板 ===")
    board_3x3 = create_standard_3x3()
    info = board_3x3.get_structure_info()
    print(f"类型: {info['board_type']}")
    print(f"总镜头数: {info['total_shots']}")
    for shot in info['shots']:
        print(f"  {shot['index']}. {shot['name']} ({shot['shot_type']}) - {shot['description']}")
    
    print("\n=== 4×3史诗叙事板 ===")
    board_4x3 = create_epic_4x3()
    info = board_4x3.get_structure_info()
    print(f"类型: {info['board_type']}")
    print(f"总镜头数: {info['total_shots']}")
    for shot in info['shots']:
        print(f"  {shot['index']}. {shot['name']} ({shot['shot_type']}) - {shot['description']}")
