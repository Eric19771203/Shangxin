#!/usr/bin/env python3
"""
CineBoard Pro - Skill-based 分镜生成器
使用Skill架构重构的分镜生成器
"""

from typing import Dict, Any, Optional
from skills import SkillOrchestrator, SkillContext, StoryboardPipeline
from skills.implementations import *  # 导入所有Skill实现


class SkillBasedStoryboardGenerator:
    """基于Skill架构的分镜生成器
    
    特点：
    1. 各功能节点以Skill形式存在
    2. Skill之间通过依赖关系自动编排
    3. 支持嵌套调用和管道执行
    4. 可扩展性强，易于添加新Skill
    """
    
    def __init__(self):
        self.orchestrator = SkillOrchestrator()
        self._register_all_skills()
    
    def _register_all_skills(self):
        """注册所有Skill（通过import触发装饰器）"""
        # Skill已在导入时通过@skill装饰器自动注册
        from skills.registry import SkillRegistry
        registered = SkillRegistry.list_all()
        print(f"[Generator] 已注册 {len(registered)} 个Skill: {registered}")
    
    def generate(
        self,
        content_type: str,
        subtype: str,
        board_type: str = "3x3",
        scene_description: str = "",
        director_style: Optional[str] = None,
        use_ai_enhancement: bool = False,
        generate_images: bool = False,
        custom_prompts: Optional[Dict[int, str]] = None,
    ) -> Dict[str, Any]:
        """生成分镜方案
        
        Args:
            content_type: 内容类型 (movie/short_drama/comic_drama/tvc)
            subtype: 子类型
            board_type: 分镜板类型 (3x3/4x3)
            scene_description: 场景描述
            director_style: 导演风格
            use_ai_enhancement: 是否使用AI增强
            generate_images: 是否生成图像
            custom_prompts: 自定义提示词
        
        Returns:
            分镜方案字典
        """
        # 创建上下文
        context = SkillContext(
            content_type=content_type,
            subtype=subtype,
            board_type=board_type,
            scene_description=scene_description,
            director_style=director_style,
            use_ai_enhancement=use_ai_enhancement,
            generate_images=generate_images,
        )
        
        # 存储自定义提示词
        if custom_prompts:
            context.set("custom_prompts", custom_prompts)
        
        # 选择管道
        if use_ai_enhancement and generate_images:
            pipeline = StoryboardPipeline.FULL_AI_PIPELINE
        elif use_ai_enhancement:
            pipeline = StoryboardPipeline.AI_ENHANCED_PIPELINE
        else:
            pipeline = StoryboardPipeline.STANDARD_PIPELINE
        
        print(f"\n[Generator] 使用管道: {pipeline}")
        
        # 执行管道
        results = self.orchestrator.execute_pipeline(pipeline, context)
        
        # 获取最终输出
        final_output = context.get("final_output", {})
        
        # 添加执行报告
        final_output["execution_report"] = self.orchestrator.get_execution_report()
        
        return final_output
    
    def generate_with_skills(
        self,
        skill_names: list,
        context: SkillContext = None,
        **kwargs
    ) -> Dict[str, Any]:
        """使用指定Skill列表生成
        
        Args:
            skill_names: Skill名称列表
            context: 初始上下文
            **kwargs: 其他参数用于创建上下文
        
        Returns:
            执行结果
        """
        if context is None:
            context = SkillContext(**kwargs)
        
        results = self.orchestrator.execute_pipeline(skill_names, context)
        
        return {
            "results": [r.to_dict() for r in results],
            "final_context": {
                "shots": context.shots,
                "prompts": context.prompts,
            },
        }
    
    def execute_single_skill(
        self,
        skill_name: str,
        context: SkillContext = None,
        **kwargs
    ) -> Dict[str, Any]:
        """执行单个Skill
        
        Args:
            skill_name: Skill名称
            context: 上下文
            **kwargs: 其他参数
        
        Returns:
            Skill执行结果
        """
        if context is None:
            context = SkillContext(**kwargs)
        
        result = self.orchestrator.execute_skill(skill_name, context)
        return result.to_dict()
    
    def get_available_skills(self) -> list:
        """获取所有可用Skill"""
        from skills.registry import SkillRegistry
        return SkillRegistry.list_all()
    
    def get_skill_info(self, skill_name: str) -> Optional[Dict]:
        """获取Skill信息"""
        from skills.registry import SkillRegistry
        return SkillRegistry.get_info(skill_name)
    
    def build_execution_plan(self, skill_name: str) -> list:
        """构建执行计划"""
        return self.orchestrator.build_execution_plan(skill_name)


# 便捷函数
def create_skill_generator() -> SkillBasedStoryboardGenerator:
    """创建Skill-based生成器"""
    return SkillBasedStoryboardGenerator()


if __name__ == "__main__":
    # 测试
    generator = create_skill_generator()
    
    print("="*60)
    print("Skill-based 分镜生成器测试")
    print("="*60)
    
    # 列出可用Skill
    print("\n可用Skill:")
    for skill_name in generator.get_available_skills():
        info = generator.get_skill_info(skill_name)
        print(f"  - {skill_name}: {info['description']}")
    
    # 测试生成
    print("\n测试生成:")
    result = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="3x3",
        scene_description="诺曼底登陆",
        director_style="spielberg",
    )
    
    print(f"\n生成成功: {result.get('success')}")
    print(f"镜头数: {len(result.get('data', {}).get('storyboard', {}).get('shots', []))}")
    
    # 执行报告
    report = result.get('execution_report', {})
    print(f"\n执行报告:")
    print(f"  总Skill数: {report.get('total_skills')}")
    print(f"  成功: {report.get('success')}")
    print(f"  失败: {report.get('failed')}")
    print(f"  总耗时: {report.get('total_execution_time', 0):.3f}s")
