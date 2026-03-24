"""
AI服务配置管理
支持 Gemini 3 和 API聚合平台
"""

import os
from typing import Optional, Dict, Any
from dataclasses import dataclass, field


@dataclass
class AIConfig:
    """AI服务配置"""
    
    # Gemini 3 配置
    gemini_api_key: Optional[str] = None
    gemini_model: str = "gemini-3-pro"  # 或其他 Gemini 3 模型版本
    gemini_base_url: str = "https://generativelanguage.googleapis.com/v1beta"
    
    # API聚合平台配置
    aggregator_enabled: bool = False
    aggregator_base_url: Optional[str] = None  # 例如: https://api.aggregator.com/v1
    aggregator_api_key: Optional[str] = None
    
    # 图像生成配置 (通过聚合平台)
    image_provider: str = "midjourney"  # midjourney / dall-e / stable-diffusion
    
    # 通用配置
    timeout: int = 60
    max_retries: int = 3
    temperature: float = 0.7
    max_tokens: int = 4096
    
    # 缓存配置
    enable_cache: bool = True
    cache_dir: str = ".ai_cache"
    
    @classmethod
    def from_env(cls) -> 'AIConfig':
        """从环境变量加载配置"""
        return cls(
            # Gemini
            gemini_api_key=os.getenv("GEMINI_API_KEY"),
            gemini_model=os.getenv("GEMINI_MODEL", "gemini-3-pro"),
            gemini_base_url=os.getenv("GEMINI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta"),
            
            # 聚合平台
            aggregator_enabled=os.getenv("AGGREGATOR_ENABLED", "false").lower() == "true",
            aggregator_base_url=os.getenv("AGGREGATOR_BASE_URL"),
            aggregator_api_key=os.getenv("AGGREGATOR_API_KEY"),
            
            # 图像
            image_provider=os.getenv("IMAGE_PROVIDER", "midjourney"),
            
            # 通用
            timeout=int(os.getenv("AI_TIMEOUT", "60")),
            max_retries=int(os.getenv("AI_MAX_RETRIES", "3")),
            temperature=float(os.getenv("AI_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("AI_MAX_TOKENS", "4096")),
            enable_cache=os.getenv("AI_ENABLE_CACHE", "true").lower() == "true",
        )
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'AIConfig':
        """从字典加载配置"""
        return cls(**config_dict)
    
    def validate(self) -> bool:
        """验证配置是否有效"""
        if not self.gemini_api_key and not self.aggregator_api_key:
            raise ValueError("必须提供 Gemini API Key 或 聚合平台 API Key")
        return True
    
    def get_active_llm_provider(self) -> str:
        """获取当前使用的LLM提供商"""
        if self.aggregator_enabled and self.aggregator_api_key:
            return "aggregator"
        elif self.gemini_api_key:
            return "gemini"
        return "none"
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "gemini_model": self.gemini_model,
            "aggregator_enabled": self.aggregator_enabled,
            "image_provider": self.image_provider,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }


# 默认配置实例
default_config = AIConfig.from_env()
