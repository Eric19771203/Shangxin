"""
图像生成服务
支持通过API聚合平台调用各种图像生成模型
"""

import time
import json
from typing import Optional, Dict, Any, List
import requests
from .config import AIConfig, default_config


class ImageService:
    """图像生成服务"""
    
    def __init__(self, config: Optional[AIConfig] = None):
        self.config = config or default_config
        self.session = requests.Session()
    
    def _call_aggregator_image_api(
        self,
        prompt: str,
        provider: str = "midjourney",
        **kwargs
    ) -> Dict[str, Any]:
        """
        通过聚合平台调用图像生成API
        
        Args:
            prompt: 图像生成提示词
            provider: 图像提供商 (midjourney/dall-e/stable-diffusion)
            **kwargs: 其他参数
        
        Returns:
            包含图像URL或任务ID的字典
        """
        api_key = self.config.aggregator_api_key
        base_url = self.config.aggregator_base_url
        
        url = f"{base_url}/images/generations"
        
        payload = {
            "provider": provider,
            "prompt": prompt,
            "n": kwargs.get('n', 1),  # 生成数量
            "size": kwargs.get('size', '1024x1024'),  # 图像尺寸
            "quality": kwargs.get('quality', 'standard'),  # 质量
            "style": kwargs.get('style', 'vivid'),  # 风格
        }
        
        # 添加provider特定的参数
        if provider == "midjourney":
            payload["midjourney_config"] = {
                "version": kwargs.get('mj_version', '6.0'),
                "aspect_ratio": kwargs.get('aspect_ratio', '16:9'),
                "stylize": kwargs.get('stylize', 100),
                "chaos": kwargs.get('chaos', 0),
            }
        elif provider == "stable-diffusion":
            payload["sd_config"] = {
                "model": kwargs.get('sd_model', 'SDXL'),
                "steps": kwargs.get('steps', 30),
                "cfg_scale": kwargs.get('cfg_scale', 7.0),
            }
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = self.session.post(
            url,
            headers=headers,
            json=payload,
            timeout=self.config.timeout * 2  # 图像生成需要更长时间
        )
        
        if response.status_code != 200:
            raise Exception(f"图像生成API错误: {response.status_code} - {response.text}")
        
        return response.json()
    
    def generate_image(
        self,
        prompt: str,
        provider: Optional[str] = None,
        wait_for_result: bool = True,
        **kwargs
    ) -> Dict[str, Any]:
        """
        生成单张图像
        
        Args:
            prompt: 图像生成提示词
            provider: 图像提供商，默认使用配置中的provider
            wait_for_result: 是否等待结果（对于异步API）
            **kwargs: 其他参数
        
        Returns:
            包含图像URL的字典
        """
        if not self.config.aggregator_enabled or not self.config.aggregator_api_key:
            raise ValueError("未配置聚合平台API密钥")
        
        provider = provider or self.config.image_provider
        
        # 重试机制
        max_retries = kwargs.get('max_retries', self.config.max_retries)
        last_error = None
        
        for attempt in range(max_retries):
            try:
                result = self._call_aggregator_image_api(prompt, provider, **kwargs)
                
                # 检查是否需要轮询结果
                if wait_for_result and 'task_id' in result:
                    return self._poll_task_result(result['task_id'])
                
                return result
                
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue
                else:
                    raise last_error
        
        raise last_error
    
    def _poll_task_result(self, task_id: str, max_attempts: int = 30) -> Dict[str, Any]:
        """
        轮询任务结果（用于异步图像生成）
        
        Args:
            task_id: 任务ID
            max_attempts: 最大轮询次数
        
        Returns:
            任务结果
        """
        api_key = self.config.aggregator_api_key
        base_url = self.config.aggregator_base_url
        
        url = f"{base_url}/tasks/{task_id}"
        headers = {"Authorization": f"Bearer {api_key}"}
        
        for _ in range(max_attempts):
            response = self.session.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                status = result.get('status')
                
                if status == 'completed':
                    return result
                elif status == 'failed':
                    raise Exception(f"图像生成失败: {result.get('error', '未知错误')}")
                
                # 继续等待
                time.sleep(2)
            else:
                raise Exception(f"查询任务状态失败: {response.status_code}")
        
        raise Exception("图像生成超时")
    
    def generate_storyboard_images(
        self,
        shots: List[Dict[str, Any]],
        provider: Optional[str] = None,
        callback=None,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """
        批量生成分镜图像
        
        Args:
            shots: 分镜列表，每个分镜包含prompt等信息
            provider: 图像提供商
            callback: 进度回调函数 (current, total)
            **kwargs: 其他参数
        
        Returns:
            包含图像URL的分镜列表
        """
        results = []
        total = len(shots)
        
        for i, shot in enumerate(shots):
            try:
                # 获取提示词
                prompt = shot.get('prompt', '')
                if not prompt:
                    prompt = shot.get('description', '')
                
                # 生成图像
                image_result = self.generate_image(
                    prompt=prompt,
                    provider=provider,
                    **kwargs
                )
                
                # 更新分镜信息
                shot_with_image = {**shot}
                if 'data' in image_result and len(image_result['data']) > 0:
                    shot_with_image['image_url'] = image_result['data'][0].get('url')
                    shot_with_image['image_revised_prompt'] = image_result['data'][0].get('revised_prompt')
                
                results.append(shot_with_image)
                
                # 调用回调
                if callback:
                    callback(i + 1, total)
                
                # 避免请求过快
                time.sleep(1)
                
            except Exception as e:
                print(f"生成图像 {i+1}/{total} 失败: {e}")
                results.append(shot)
        
        return results
    
    def enhance_for_image_generation(
        self,
        storyboard_prompt: str,
        director_style: Optional[str] = None
    ) -> str:
        """
        优化提示词用于图像生成
        
        Args:
            storyboard_prompt: 分镜提示词
            director_style: 导演风格
        
        Returns:
            优化后的提示词
        """
        # 添加图像生成特定的优化
        enhancements = []
        
        if director_style:
            enhancements.append(f"in the style of {director_style}")
        
        # 添加质量标签
        enhancements.extend([
            "cinematic lighting",
            "professional photography",
            "highly detailed",
            "8k resolution"
        ])
        
        enhanced = f"{storyboard_prompt}, {', '.join(enhancements)}"
        return enhanced
    
    def get_image_variations(
        self,
        image_url: str,
        n: int = 4,
        **kwargs
    ) -> Dict[str, Any]:
        """
        获取图像变体
        
        Args:
            image_url: 原始图像URL
            n: 变体数量
            **kwargs: 其他参数
        
        Returns:
            变体图像列表
        """
        if not self.config.aggregator_enabled:
            raise ValueError("未配置聚合平台")
        
        api_key = self.config.aggregator_api_key
        base_url = self.config.aggregator_base_url
        
        url = f"{base_url}/images/variations"
        
        payload = {
            "image_url": image_url,
            "n": n,
            "size": kwargs.get('size', '1024x1024'),
        }
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = self.session.post(
            url,
            headers=headers,
            json=payload,
            timeout=self.config.timeout * 2
        )
        
        if response.status_code != 200:
            raise Exception(f"获取变体失败: {response.status_code}")
        
        return response.json()
    
    def upscale_image(
        self,
        image_url: str,
        scale: int = 2,
        **kwargs
    ) -> Dict[str, Any]:
        """
        放大图像
        
        Args:
            image_url: 图像URL
            scale: 放大倍数 (2/4)
            **kwargs: 其他参数
        
        Returns:
            放大后的图像信息
        """
        if not self.config.aggregator_enabled:
            raise ValueError("未配置聚合平台")
        
        api_key = self.config.aggregator_api_key
        base_url = self.config.aggregator_base_url
        
        url = f"{base_url}/images/upscale"
        
        payload = {
            "image_url": image_url,
            "scale": scale,
        }
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = self.session.post(
            url,
            headers=headers,
            json=payload,
            timeout=self.config.timeout * 3
        )
        
        if response.status_code != 200:
            raise Exception(f"放大图像失败: {response.status_code}")
        
        return response.json()


# 便捷函数
def get_image_service(config: Optional[AIConfig] = None) -> ImageService:
    """获取图像服务实例"""
    return ImageService(config)
