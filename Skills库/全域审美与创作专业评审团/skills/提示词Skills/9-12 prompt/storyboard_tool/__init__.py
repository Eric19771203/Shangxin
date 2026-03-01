"""
分镜工具 - 完整的故事板生成系统

提供电影、短剧、漫剧、TVC广告的专业分镜生成
"""

from .generator import StoryboardGenerator, generate_storyboard, list_types
from .core.base_framework import BoardType, create_standard_3x3, create_epic_4x3
from .core.grammar_rules import (
    Angle30Rule, EyelineMatch, ActionAxis, 
    ColorEvolution, SoundscapeHints
)

__version__ = "1.0.0"
__author__ = "Storyboard Tool"

__all__ = [
    'StoryboardGenerator',
    'generate_storyboard',
    'list_types',
    'BoardType',
    'create_standard_3x3',
    'create_epic_4x3',
    'Angle30Rule',
    'EyelineMatch',
    'ActionAxis',
    'ColorEvolution',
    'SoundscapeHints',
]
