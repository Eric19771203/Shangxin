#!/usr/bin/env python3
"""
CineBoard Pro - AI增强版分镜生成器
集成 Gemini 3 和 API聚合平台
"""

from typing import Dict, List, Any, Optional
from generator import StoryboardGenerator
from ai_services import LLMService, ImageService, AIConfig


class AIEnhancedGenerator(StoryboardGenerator):
    """
    AI增强版分镜生成器
    
    在基础生成器之上添加：
    1. AI智能提示词增强
    2. 自动图像生成
    3. 导演风格深度分析
    """
    
    def __init__(self, config: Optional[AIConfig] = None):
        super().__init__()
        self.config = config or AIConfig.from_env()
        self.llm_service = LLMService(self.config)
        self.image_service = ImageService(self.config)
        
        # 检查AI服务是否可用
        self.ai_available = self._check_ai_availability()
    
    def _check_ai_availability(self) -> bool:
        """检查AI服务是否可用"""
        try:
            if self.config.gemini_api_key:
                return True
            if self.config.aggregator_enabled and self.config.aggregator_api_key:
                return True
            return False
        except:
            return False
    
    def generate(
        self,
        content_type: str,
        subtype: str,
        board_type: str = "3x3",
        scene_description: str = "",
        custom_prompts: Optional[Dict[int, str]] = None,
        director_style: Optional[str] = None,
        use_ai_enhancement: bool = False,
        generate_images: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        生成分镜方案（AI增强版）
        
        Args:
            content_type: 内容类型
            subtype: 子类型
            board_type: 分镜板类型 (3x3/4x3)
            scene_description: 场景描述
            custom_prompts: 自定义提示词
            director_style: 导演风格
            use_ai_enhancement: 是否使用AI增强提示词
            generate_images: 是否生成图像
            **kwargs: 其他参数
        
        Returns:
            包含分镜方案的字典
        """
        # 首先调用基础生成器
        result = super().generate(
            content_type=content_type,
            subtype=subtype,
            board_type=board_type,
            scene_description=scene_description,
            custom_prompts=custom_prompts,
            director_style=director_style
        )
        
        if "error" in result:
            return result
        
        # AI增强
        if use_ai_enhancement and self.ai_available:
            try:
                result = self._enhance_with_ai(result, scene_description, director_style)
            except Exception as e:
                print(f"AI增强失败: {e}")
                result["ai_enhancement_error"] = str(e)
        
        # 生成图像
        if generate_images and self.ai_available and self.config.aggregator_enabled:
            try:
                result = self._generate_images_for_storyboard(result)
            except Exception as e:
                print(f"图像生成失败: {e}")
                result["image_generation_error"] = str(e)
        
        return result
    
    def _enhance_with_ai(
        self,
        base_result: Dict[str, Any],
        scene_description: str,
        director_style: Optional[str]
    ) -> Dict[str, Any]:
        """
        使用AI增强分镜方案
        
        Args:
            base_result: 基础生成结果
            scene_description: 场景描述
            director_style: 导演风格
        
        Returns:
            增强后的结果
        """
        data = base_result.get("data", {})
        storyboard = data.get("storyboard", {})
        shots = storyboard.get("shots", [])
        
        # 增强每个镜头的提示词
        enhanced_shots = []
        for shot in shots:
            original_prompt = shot.get("prompt", "")
            
            # 使用AI增强
            enhanced_prompt = self.llm_service.enhance_storyboard_prompt(
                base_prompt=original_prompt,
                director_style=director_style,
                content_type=data.get("content_type", "movie"),
                subtype=data.get("subtype", "general")
            )
            
            # 更新镜头信息
            enhanced_shot = {**shot}
            enhanced_shot["original_prompt"] = original_prompt
            enhanced_shot["enhanced_prompt"] = enhanced_prompt
            enhanced_shot["prompt"] = enhanced_prompt  # 使用增强后的提示词
            enhanced_shots.append(enhanced_shot)
        
        # 更新结果
        storyboard["shots"] = enhanced_shots
        storyboard["ai_enhanced"] = True
        data["storyboard"] = storyboard
        base_result["data"] = data
        
        return base_result
    
    def _generate_images_for_storyboard(
        self,
        result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        为分镜生成图像
        
        Args:
            result: 分镜结果
        
        Returns:
            包含图像URL的结果
        """
        data = result.get("data", {})
        storyboard = data.get("storyboard", {})
        shots = storyboard.get("shots", [])
        
        print(f"开始生成 {len(shots)} 个分镜图像...")
        
        # 批量生成图像
        shots_with_images = self.image_service.generate_storyboard_images(
            shots=shots,
            callback=lambda current, total: print(f"进度: {current}/{total}")
        )
        
        # 统计成功数量
        success_count = sum(1 for s in shots_with_images if "image_url" in s)
        print(f"图像生成完成: {success_count}/{len(shots)} 成功")
        
        # 更新结果
        storyboard["shots"] = shots_with_images
        storyboard["images_generated"] = True
        data["storyboard"] = storyboard
        result["data"] = data
        
        return result
    
    def analyze_scene_with_ai(
        self,
        scene_description: str,
        director_style: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        使用AI分析场景
        
        Args:
            scene_description: 场景描述
            director_style: 导演风格
        
        Returns:
            AI分析结果
        """
        if not self.ai_available:
            return {"error": "AI服务不可用"}
        
        system_prompt = """你是一位资深的电影分镜师和视觉艺术家。
请分析以下场景描述，提供专业的分镜建议。

请从以下维度分析：
1. 视觉风格建议
2. 推荐使用的镜头类型和角度
3. 色彩和光线处理
4. 情绪节奏把控
5. 参考影片推荐

以JSON格式输出。"""

        user_prompt = f"""场景描述：{scene_description}
导演风格：{director_style or '无特定风格'}

请提供专业的分镜分析。"""

        try:
            response = self.llm_service.generate(
                prompt=user_prompt,
                system_prompt=system_prompt,
                temperature=0.7
            )
            
            # 尝试解析JSON
            import json
            try:
                return json.loads(response)
            except:
                return {
                    "analysis": response,
                    "parsed": False
                }
        except Exception as e:
            return {"error": str(e)}
    
    def generate_with_full_ai(
        self,
        content_type: str,
        subtype: str,
        board_type: str = "3x3",
        scene_description: str = "",
        director_style: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        完全AI驱动的分镜生成
        
        使用AI从头生成分镜，而不仅仅是增强
        
        Args:
            content_type: 内容类型
            subtype: 子类型
            board_type: 分镜板类型
            scene_description: 场景描述
            director_style: 导演风格
            **kwargs: 其他参数
        
        Returns:
            分镜方案
        """
        if not self.ai_available:
            return {"error": "AI服务不可用，无法使用完全AI生成模式"}
        
        system_prompt = f"""你是一位专业的电影分镜师。
请根据给定的场景描述，生成完整的分镜方案。

要求：
1. 生成{board_type}格式的分镜（{board_type}个镜头）
2. 每个镜头包含：景别、角度、运动、描述、AI提示词
3. 考虑叙事节奏和视觉流畅性
4. 如果指定了导演风格，请体现该风格特点

输出格式必须是JSON：
{{
    "shots": [
        {{
            "index": 1,
            "name": "镜头名称",
            "shot_type": "景别",
            "angle": "角度",
            "movement": "运动",
            "description": "场景描述",
            "prompt": "AI图像生成提示词（英文）"
        }}
    ]
}}"""

        user_prompt = f"""内容类型：{content_type} - {subtype}
场景描述：{scene_description}
导演风格：{director_style or '无特定风格'}

请生成完整的分镜方案。"""

        try:
            response = self.llm_service.generate(
                prompt=user_prompt,
                system_prompt=system_prompt,
                temperature=0.8,
                max_tokens=4000
            )
            
            # 解析JSON
            import json
            ai_result = json.loads(response)
            
            # 构建标准格式的结果
            return {
                "success": True,
                "data": {
                    "content_type": content_type,
                    "subtype": subtype,
                    "board_type": board_type,
                    "template_name": f"AI生成-{board_type}分镜",
                    "storyboard": {
                        "shots": ai_result.get("shots", []),
                        "ai_generated": True,
                        "director_style_applied": director_style is not None
                    },
                    "director_info": {
                        "name": director_style or "AI生成",
                        "techniques": ["AI智能生成"]
                    },
                    "grammar_rules": [],
                    "color_evolution": []
                }
            }
            
        except Exception as e:
            return {"error": f"AI生成失败: {str(e)}"}


# 便捷函数
def create_ai_generator(config: Optional[AIConfig] = None) -> AIEnhancedGenerator:
    """创建AI增强版生成器"""
    return AIEnhancedGenerator(config)


if __name__ == "__main__":
    # 测试
    generator = create_ai_generator()
    
    print(f"AI服务可用: {generator.ai_available}")
    
    # 基础生成（不使用AI）
    result = generator.generate(
        content_type="movie",
        subtype="war",
        scene_description="诺曼底登陆",
        director_style="spielberg"
    )
    
    print("\n基础生成完成")
    
    # AI增强生成（如果AI可用）
    if generator.ai_available:
        result_ai = generator.generate(
            content_type="movie",
            subtype="war",
            scene_description="诺曼底登陆",
            director_style="spielberg",
            use_ai_enhancement=True
        )
        
        print("\nAI增强完成")
        
        # 对比提示词
        base_shots = result.get("data", {}).get("storyboard", {}).get("shots", [])
        ai_shots = result_ai.get("data", {}).get("storyboard", {}).get("shots", [])
        
        if base_shots and ai_shots:
            print("\n提示词对比（第一个镜头）:")
            print(f"原始: {base_shots[0].get('prompt', '')[:100]}...")
            print(f"增强: {ai_shots[0].get('enhanced_prompt', '')[:100]}...")
