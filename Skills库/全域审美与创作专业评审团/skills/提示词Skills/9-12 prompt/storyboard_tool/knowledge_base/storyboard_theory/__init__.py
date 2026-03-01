"""
分镜逻辑知识库
==============
用于管理和检索分镜、电影理论参考书籍的知识体系

功能：
1. 书籍引用管理 - 记录参考书籍信息
2. 知识点分类 - 按主题组织理论知识
3. 检索接口 - 快速查找相关理论
4. 实践应用 - 将理论应用到实际分镜创作

使用方法：
    from knowledge_base.storyboard_theory import (
        get_theory_by_topic,
        search_knowledge,
        list_all_books,
        get_book_info
    )
"""

from .book_manager import (
    BOOK_REGISTRY,
    get_book_info,
    list_all_books,
    list_books_by_category,
    add_book_reference,
    BookReference
)

from .knowledge_base import (
    KNOWLEDGE_BASE,
    get_theory_by_topic,
    search_knowledge,
    get_principle_detail,
    list_all_topics,
    apply_theory_to_storyboard
)

from .visual_glossary import (
    VISUAL_GLOSSARY,
    TermCategory,
    VisualTerm,
    get_term,
    search_terms,
    get_terms_by_category,
    get_ai_keywords,
    get_terms_for_scene_type,
    explain_term_for_ai,
    CATEGORY_NAMES
)

__all__ = [
    # 书籍管理
    'BOOK_REGISTRY',
    'get_book_info',
    'list_all_books',
    'list_books_by_category',
    'add_book_reference',
    'BookReference',
    # 知识库
    'KNOWLEDGE_BASE',
    'get_theory_by_topic',
    'search_knowledge',
    'get_principle_detail',
    'list_all_topics',
    'apply_theory_to_storyboard',
    # 视觉术语
    'VISUAL_GLOSSARY',
    'TermCategory',
    'VisualTerm',
    'get_term',
    'search_terms',
    'get_terms_by_category',
    'get_ai_keywords',
    'get_terms_for_scene_type',
    'explain_term_for_ai',
    'CATEGORY_NAMES'
]
