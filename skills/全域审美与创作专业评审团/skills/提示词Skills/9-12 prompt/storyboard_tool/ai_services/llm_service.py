"""
语言模型服务
支持 Gemini 3 和 API聚合平台
"""

import json
import time
import hashlib
from typing import Dict, List, Optional, Any, Generator
import requests
from .config import AIConfig, default_config


class LLMService:
    """语言模型服务"""
    
    def __init__(self, config: Optional[AIConfig] = None):
        self.config = config or default_config
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })
    
    def _get_cache_key(self, prompt: str, **kwargs) -> str:
        """生成缓存键"""
        cache_data = f"{prompt}:{json.dumps(kwargs, sort_keys=True)}"
        return hashlib.md5(cache_data.encode()).hexdigest()
    
    def _call_gemini(self, prompt: str, system_prompt: Optional[str] = None, **kwargs) -> str:
        """
        调用 Gemini 3 API
        
        文档: https://ai.google.dev/docs/gemini_api_overview
        """
        api_key = self.config.gemini_api_key
        model = kwargs.get('model', self.config.gemini_model)
        
        url = f"{self.config.gemini_base_url}/models/{model}:generateContent"
        
        # 构建请求体
        contents = []
        if system_prompt:
            contents.append({
                "role": "user",
                "parts": [{"text": system_prompt}]
            })
        
        contents.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })
        
        payload = {
            "contents": contents,
            "generationConfig": {
                "temperature": kwargs.get('temperature', self.config.temperature),
                "maxOutputTokens": kwargs.get('max_tokens', self.config.max_tokens),
                "topP": kwargs.get('top_p', 0.95),
                "topK": kwargs.get('top_k', 40),
            }
        }
        
        # 发送请求
        response = self.session.post(
            url,
            params={"key": api_key},
            json=payload,
            timeout=self.config.timeout
        )
        
        if response.status_code != 200:
            raise Exception(f"Gemini API错误: {response.status_code} - {response.text}")
        
        result = response.json()
        
        # 提取生成的文本
        if 'candidates' in result and len(result['candidates']) > 0:
            candidate = result['candidates'][0]
            if 'content' in candidate and 'parts' in candidate['content']:
                return candidate['content']['parts'][0]['text']
        
        raise Exception(f"Gemini API返回格式异常: {result}")
    
    def _call_aggregator(self, prompt: str, system_prompt: Optional[str] = None, **kwargs) -> str:
        """
        调用 API聚合平台
        
        聚合平台统一接口格式
        """
        api_key = self.config.aggregator_api_key
        base_url = self.config.aggregator_base_url
        
        url = f"{base_url}/chat/completions"
        
        # 构建消息
        messages = []
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        payload = {
            "model": kwargs.get('model', 'gemini-3-pro'),  # 聚合平台支持的模型名称
            "messages": messages,
            "temperature": kwargs.get('temperature', self.config.temperature),
            "max_tokens": kwargs.get('max_tokens', self.config.max_tokens),
            "stream": False
        }
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = self.session.post(
            url,
            headers=headers,
            json=payload,
            timeout=self.config.timeout
        )
        
        if response.status_code != 200:
            raise Exception(f"聚合平台API错误: {response.status_code} - {response.text}")
        
        result = response.json()
        
        # 提取生成的文本
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        
        raise Exception(f"聚合平台API返回格式异常: {result}")
    
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        use_aggregator: Optional[bool] = None,
        **kwargs
    ) -> str:
        """
        生成文本
        
        Args:
            prompt: 用户提示词
            system_prompt: 系统提示词
            use_aggregator: 是否使用聚合平台（默认根据配置）
            **kwargs: 其他参数
        
        Returns:
            生成的文本
        """
        # 确定使用哪个提供商
        if use_aggregator is None:
            use_aggregator = self.config.aggregator_enabled
        
        # 重试机制
        max_retries = kwargs.get('max_retries', self.config.max_retries)
        last_error = None
        
        for attempt in range(max_retries):
            try:
                if use_aggregator and self.config.aggregator_api_key:
                    return self._call_aggregator(prompt, system_prompt, **kwargs)
                elif self.config.gemini_api_key:
                    return self._call_gemini(prompt, system_prompt, **kwargs)
                else:
                    raise ValueError("未配置有效的API密钥")
                    
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # 指数退避
                    time.sleep(wait_time)
                    continue
                else:
                    raise last_error
        
        raise last_error
    
    def generate_stream(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        use_aggregator: Optional[bool] = None,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        流式生成文本
        
        Yields:
            生成的文本片段
        """
        # 注意：Gemini的流式API实现略有不同
        # 这里简化处理，实际使用时需要适配
        
        full_text = self.generate(prompt, system_prompt, use_aggregator, **kwargs)
        # 模拟流式输出
        words = full_text.split()
        for word in words:
            yield word + " "
            time.sleep(0.05)
    
    def enhance_storyboard_prompt(
        self,
        base_prompt: str,
        director_style: Optional[str] = None,
        content_type: str = "movie",
        subtype: str = "general"
    ) -> str:
        """
        使用AI增强分镜提示词
        
        Args:
            base_prompt: 基础场景描述
            director_style: 导演风格
            content_type: 内容类型
            subtype: 子类型
        
        Returns:
            增强后的提示词
        """
        system_prompt = """你是一位专业的电影分镜师和提示词工程师。
你的任务是将简单的场景描述转化为详细的、适合AI图像生成的分镜提示词。

要求：
1. 保持场景的核心内容和情感
2. 添加专业的电影摄影术语（景别、角度、光线、色彩等）
3. 使用英文输出，便于AI图像生成
4. 提示词应该详细但不超过200词
5. 包含：主体、环境、光线、色彩氛围、摄影风格

输出格式：
直接输出优化后的提示词，不需要解释。"""

        user_prompt = f"""场景描述：{base_prompt}
内容类型：{content_type} - {subtype}
导演风格：{director_style or '无特定风格'}

请优化这个场景描述，生成专业的AI图像生成提示词。"""

        try:
            enhanced = self.generate(user_prompt, system_prompt, temperature=0.8)
            return enhanced.strip()
        except Exception as e:
            print(f"AI增强失败，使用原始提示词: {e}")
            return base_prompt
    
    def analyze_director_style(
        self,
        director_name: str,
        scene_description: str
    ) -> Dict[str, Any]:
        """
        分析导演风格在特定场景中的应用
        
        Args:
            director_name: 导演名称
            scene_description: 场景描述
        
        Returns:
            风格分析结果
        """
        system_prompt = """你是一位电影导演风格分析专家。
分析指定导演的风格特点如何应用到特定场景中。"""

        user_prompt = f"""导演：{director_name}
场景：{scene_description}

请分析：
1. 该导演的典型视觉特征
2. 推荐的镜头运用方式
3. 色彩和光线处理建议
4. 特殊的拍摄技巧
5. 参考该导演的哪部作品

以JSON格式输出。"""

        try:
            response = self.generate(user_prompt, system_prompt, temperature=0.7)
            # 尝试解析JSON
            return json.loads(response)
        except:
            return {
                "director": director_name,
                "analysis": response if 'response' in dir() else "分析失败",
                "error": "无法解析为JSON"
            }
    
    def batch_generate_prompts(
        self,
        scenes: List[Dict[str, str]],
        **kwargs
    ) -> List[str]:
        """
        批量生成提示词
        
        Args:
            scenes: 场景列表，每个场景包含 description, director_style 等
        
        Returns:
            生成的提示词列表
        """
        results = []
        for scene in scenes:
            prompt = self.enhance_storyboard_prompt(
                base_prompt=scene.get('description', ''),
                director_style=scene.get('director_style'),
                content_type=scene.get('content_type', 'movie'),
                subtype=scene.get('subtype', 'general')
            )
            results.append(prompt)
        return results


# 便捷函数
def get_llm_service(config: Optional[AIConfig] = None) -> LLMService:
    """获取LLM服务实例"""
    return LLMService(config)
