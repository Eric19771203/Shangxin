"""
书籍引用管理模块
==============
管理参考书籍的元数据和引用信息

支持功能：
- 记录书籍基本信息（标题、作者、出版社、ISBN等）
- 按分类管理书籍（分镜、剪辑、导演、摄影等）
- 标记书籍中的重要章节和知识点
- 生成引用格式
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class BookReference:
    """书籍引用数据类"""
    id: str                           # 书籍唯一标识
    title: str                        # 书名
    authors: List[str]                # 作者列表
    publisher: str                    # 出版社
    publish_year: int                 # 出版年份
    category: str                     # 分类
    title_en: Optional[str] = None    # 英文书名
    translators: Optional[List[str]] = None  # 译者列表（中文书）
    isbn: Optional[str] = None        # ISBN
    tags: List[str] = field(default_factory=list)  # 标签
    description: str = ""             # 书籍简介
    key_chapters: Dict[str, str] = field(default_factory=dict)  # 重要章节 {章节名: 简介}
    knowledge_points: List[str] = field(default_factory=list)   # 知识点列表
    file_path: Optional[str] = None   # 本地文件路径（如果已上传）
    upload_date: Optional[str] = None # 上传日期
    notes: str = ""                   # 用户笔记
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'id': self.id,
            'title': self.title,
            'title_en': self.title_en,
            'authors': self.authors,
            'translators': self.translators,
            'publisher': self.publisher,
            'publish_year': self.publish_year,
            'isbn': self.isbn,
            'category': self.category,
            'tags': self.tags,
            'description': self.description,
            'key_chapters': self.key_chapters,
            'knowledge_points': self.knowledge_points,
            'file_path': self.file_path,
            'upload_date': self.upload_date,
            'notes': self.notes
        }
    
    def get_citation(self, style: str = 'apa') -> str:
        """生成引用格式"""
        if style == 'apa':
            authors_str = ', '.join(self.authors)
            return f"{authors_str} ({self.publish_year}). {self.title}. {self.publisher}."
        elif style == 'mla':
            authors_str = ', '.join(self.authors)
            return f"{authors_str}. {self.title}. {self.publisher}, {self.publish_year}."
        elif style == 'chicago':
            authors_str = ', '.join(self.authors)
            return f"{authors_str}. {self.title}. {self.publisher}, {self.publish_year}."
        else:
            return f"{self.title} - {', '.join(self.authors)} ({self.publish_year})"


# 书籍注册表 - 预置经典参考书籍
BOOK_REGISTRY: Dict[str, BookReference] = {
    # 分镜与视觉叙事
    "katz_film_directing": BookReference(
        id="katz_film_directing",
        title="电影导演的电影语言",
        title_en="Film Directing: Cinematic Motion",
        authors=["Steven D. Katz"],
        translators=["井迎兆"],
        publisher="远流出版",
        publish_year=1994,
        isbn="9789573227233",
        category="分镜",
        tags=["分镜", "导演", "镜头语言", "运动", "构图"],
        description="经典的分镜与导演技法书籍，详细讲解镜头运动和场面调度",
        key_chapters={
            "第一章：镜头运动": "摄影机运动的基本类型和叙事功能",
            "第二章：场面调度": "演员调度和空间设计",
            "第三章：叙事空间": "如何通过镜头建立空间关系",
            "第四章：时间设计": "节奏和时间的视觉化"
        },
        knowledge_points=[
            "推轨镜头的叙事功能",
            "场面调度的三角原则",
            "180度规则",
            "视线匹配",
            "动作轴线"
        ]
    ),
    
    "block_visual_story": BookReference(
        id="block_visual_story",
        title="视觉故事",
        title_en="The Visual Story",
        authors=["Bruce Block"],
        translators=["汪忆岚"],
        publisher="书林出版",
        publish_year=2008,
        isbn="9789574452436",
        category="视觉叙事",
        tags=["视觉叙事", "构图", "色彩", "空间", "节奏"],
        description="从视觉元素角度分析电影叙事，涵盖线条、形状、色彩、空间等",
        key_chapters={
            "线条与形状": "视觉线条的情感表达",
            "色彩理论": "色彩的心理学和叙事功能",
            "空间关系": "二维和三维空间的视觉呈现",
            "节奏控制": "视觉节奏和时间感"
        },
        knowledge_points=[
            "视觉重量平衡",
            "色彩对比与和谐",
            "空间深度营造",
            "视觉节奏模式"
        ]
    ),
    
    # 剪辑理论
    "murch_in_blink": BookReference(
        id="murch_in_blink",
        title="眨眼之间",
        title_en="In the Blink of an Eye",
        authors=["Walter Murch"],
        translators=["夏彤"],
        publisher="北京联合出版",
        publish_year=2012,
        isbn="9787550208905",
        category="剪辑",
        tags=["剪辑", "节奏", "情感", "连续性"],
        description="剪辑大师Walter Murch的经典著作，探讨剪辑的本质和直觉",
        key_chapters={
            "剪辑的六个标准": "情感、故事、节奏、视线、二维特性、三维连贯",
            "眨眼理论": "剪辑点与眨眼的关系",
            "数字剪辑vs胶片": "技术变革对剪辑的影响"
        },
        knowledge_points=[
            "剪辑六原则",
            "眨眼理论",
            "情感剪辑",
            "节奏控制"
        ]
    ),
    
    # 导演创作
    "lumet_directing": BookReference(
        id="lumet_directing",
        title="导演",
        title_en="Making Movies",
        authors=["Sidney Lumet"],
        translators=["黄煜文"],
        publisher="时报出版",
        publish_year=1996,
        isbn="9789571320837",
        category="导演",
        tags=["导演", "创作", "制片", "演员指导"],
        description="传奇导演Sidney Lumet的创作心得，从剧本到后期的全流程",
        key_chapters={
            "剧本": "如何选择和改编剧本",
            "演员": "与演员合作的艺术",
            "美术设计": "视觉风格的建立",
            "摄影": "与摄影师的合作",
            "后期": "剪辑和配乐"
        },
        knowledge_points=[
            "导演准备工作",
            "演员沟通技巧",
            "视觉风格统一",
            "后期决策"
        ]
    ),
    
    # 摄影
    "brown_cinematography": BookReference(
        id="brown_cinematography",
        title="电影摄影技巧",
        title_en="Cinematography: Theory and Practice",
        authors=["Blain Brown"],
        translators=["潘天春", "张立", "陈汝洪"],
        publisher="北京联合出版",
        publish_year=2015,
        isbn="9787550253165",
        category="摄影",
        tags=["摄影", "灯光", "镜头", "曝光", "色彩"],
        description="全面的电影摄影技术手册，涵盖从基础到高级的所有技术",
        key_chapters={
            "曝光": "曝光控制和测光",
            "色彩理论": "色彩科学和调色",
            "灯光": "灯光设备和布光技巧",
            "镜头": "镜头选择和光学原理"
        },
        knowledge_points=[
            "曝光三角",
            "色温控制",
            "三点布光",
            "镜头语言"
        ]
    ),
    
    # 中国导演经验
    "zeng_storyboard": BookReference(
        id="zeng_storyboard",
        title="分镜头脚本设计",
        authors=["曾思齐"],
        publisher="中国电影出版社",
        publish_year=2018,
        isbn="9787106048796",
        category="分镜",
        tags=["分镜", "脚本", "中国", "实践"],
        description="中国语境下的分镜设计教材，结合国内制作实际",
        key_chapters={
            "分镜基础": "分镜的基本概念和作用",
            "构图原理": "画面构图的基本原则",
            "镜头语言": "如何通过镜头讲故事",
            "实战案例": "商业项目的分镜案例分析"
        },
        knowledge_points=[
            "分镜绘制规范",
            "中国电视剧分镜特点",
            "广告分镜技巧",
            "分镜与预算"
        ]
    ),
    
    # 动画分镜
    "o_hailey_anim_story": BookReference(
        id="o_hailey_anim_story",
        title="动画分镜头设计",
        title_en="Animation: The Story",
        authors=["Francis Glebas", "O'Haire"],
        translators=["王雷"],
        publisher="中国传媒大学出版社",
        publish_year=2011,
        isbn="9787565702101",
        category="动画",
        tags=["动画", "分镜", "故事板", "视觉开发"],
        description="专门针对动画的分镜设计，强调视觉叙事和表演",
        key_chapters={
            "视觉叙事": "动画特有的叙事技巧",
            "角色表演": "通过分镜设计角色动作",
            "场景设计": "动画场景的视觉呈现",
            "动态分镜": "Animatic的制作"
        },
        knowledge_points=[
            "动画分镜特点",
            "夸张与变形",
            "节奏设计",
            "视觉笑料"
        ]
    ),
    
    # 电影语法
    "bordwell_film_art": BookReference(
        id="bordwell_film_art",
        title="电影艺术：形式与风格",
        title_en="Film Art: An Introduction",
        authors=["David Bordwell", "Kristin Thompson"],
        translators=["曾伟祯"],
        publisher=" McGraw-Hill / 简体版：世界图书出版",
        publish_year=2010,
        isbn="9780073535104",
        category="电影理论",
        tags=["电影理论", "形式", "风格", "分析"],
        description="最权威的电影教材之一，系统讲解电影的形式与风格",
        key_chapters={
            "电影形式": "电影作为艺术形式的基本特征",
            "叙事": "叙事结构和技巧",
            "电影风格": "摄影、剪辑、声音的风格分析",
            "类型": "类型电影研究"
        },
        knowledge_points=[
            "电影形式系统",
            "叙事因果性",
            "风格统一性",
            "类型惯例"
        ]
    )
}


def get_book_info(book_id: str) -> Optional[BookReference]:
    """获取书籍信息"""
    return BOOK_REGISTRY.get(book_id)


def list_all_books() -> List[str]:
    """列出所有书籍ID"""
    return list(BOOK_REGISTRY.keys())


def list_all_books_detail() -> List[Dict[str, Any]]:
    """列出所有书籍详情"""
    return [book.to_dict() for book in BOOK_REGISTRY.values()]


def list_books_by_category(category: str) -> List[BookReference]:
    """按分类列出书籍"""
    return [book for book in BOOK_REGISTRY.values() if book.category == category]


def search_books(keyword: str) -> List[BookReference]:
    """搜索书籍"""
    keyword_lower = keyword.lower()
    results = []
    
    for book in BOOK_REGISTRY.values():
        # 搜索书名
        if keyword_lower in book.title.lower():
            results.append(book)
            continue
        # 搜索英文书名
        if book.title_en and keyword_lower in book.title_en.lower():
            results.append(book)
            continue
        # 搜索作者
        if any(keyword_lower in author.lower() for author in book.authors):
            results.append(book)
            continue
        # 搜索标签
        if any(keyword_lower in tag.lower() for tag in book.tags):
            results.append(book)
            continue
        # 搜索知识点
        if any(keyword_lower in kp.lower() for kp in book.knowledge_points):
            results.append(book)
            continue
    
    return results


def add_book_reference(book: BookReference) -> str:
    """
    添加新书籍引用
    
    Args:
        book: BookReference对象
        
    Returns:
        书籍ID
    """
    if book.id in BOOK_REGISTRY:
        raise ValueError(f"书籍ID '{book.id}' 已存在")
    
    book.upload_date = datetime.now().strftime("%Y-%m-%d")
    BOOK_REGISTRY[book.id] = book
    return book.id


def update_book_notes(book_id: str, notes: str):
    """更新书籍笔记"""
    if book_id in BOOK_REGISTRY:
        BOOK_REGISTRY[book_id].notes = notes


def get_books_by_knowledge_point(point: str) -> List[BookReference]:
    """根据知识点查找相关书籍"""
    results = []
    point_lower = point.lower()
    
    for book in BOOK_REGISTRY.values():
        if any(point_lower in kp.lower() for kp in book.knowledge_points):
            results.append(book)
    
    return results


# 书籍分类列表
BOOK_CATEGORIES = [
    "分镜",
    "视觉叙事",
    "剪辑",
    "导演",
    "摄影",
    "动画",
    "电影理论"
]


def get_category_stats() -> Dict[str, int]:
    """获取各分类书籍数量统计"""
    stats = {}
    for category in BOOK_CATEGORIES:
        stats[category] = len(list_books_by_category(category))
    return stats
