"""
分镜工具使用示例
展示如何使用分镜生成器创建各种类型的故事板
"""

import sys
sys.path.append('..')

from generator import StoryboardGenerator, generate_storyboard, list_types


def example_1_basic_usage():
    """示例1：基本使用"""
    print("=" * 60)
    print("示例1：基本使用 - 生成战争片分镜")
    print("=" * 60)
    
    # 创建生成器
    generator = StoryboardGenerator()
    
    # 生成战争片3×3分镜
    result = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="3x3",
        scene_description="诺曼底登陆场景"
    )
    
    # 格式化输出
    print(generator.format_output(result))
    print("\n")


def example_2_list_all_types():
    """示例2：列出所有可用类型"""
    print("=" * 60)
    print("示例2：查看所有可用类型")
    print("=" * 60)
    
    types = list_types()
    
    for type_key, type_info in types.items():
        print(f"\n【{type_info['name']}】({type_key})")
        print("子类型:")
        for subtype in type_info['subtypes']:
            print(f"  - {subtype}")
    print("\n")


def example_3_different_genres():
    """示例3：不同类型对比"""
    print("=" * 60)
    print("示例3：不同类型对比 - 短剧")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    # 生成不同类型的短剧分镜
    genres = ["action", "emotion", "suspense"]
    
    for genre in genres:
        print(f"\n--- 短剧类型: {genre} ---")
        result = generator.generate(
            content_type="short_drama",
            subtype=genre,
            board_type="3x3"
        )
        
        # 只显示前3个镜头的prompt对比
        shots = result['storyboard']['shots'][:3]
        for shot in shots:
            print(f"  镜头{shot['index']}: {shot['name']}")
            print(f"    Prompt: {shot['prompt'][:80]}...")
    print("\n")


def example_4_board_type_comparison():
    """示例4：3×3 vs 4×3 对比"""
    print("=" * 60)
    print("示例4：故事板类型对比 - 3×3 vs 4×3")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    # 3×3标准叙事板
    print("\n【3×3标准叙事板】")
    result_3x3 = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="3x3"
    )
    storyboard_3x3 = result_3x3['storyboard']
    print(f"模板: {storyboard_3x3['template_name']}")
    print(f"镜头数: {len(storyboard_3x3['shots'])}")
    for shot in storyboard_3x3['shots'][:3]:
        print(f"  {shot['index']}. {shot['name']}")
    
    # 4×3史诗叙事板
    print("\n【4×3史诗叙事板】")
    result_4x3 = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="4x3"
    )
    storyboard_4x3 = result_4x3['storyboard']
    print(f"模板: {storyboard_4x3['template_name']}")
    print(f"描述: {storyboard_4x3.get('description', '')}")
    for row in storyboard_4x3['rows']:
        print(f"  【{row['name']}】")
        for shot in row['shots'][:2]:
            print(f"    {shot['index']}. {shot['name']}")
    print("\n")


def example_5_tvc_advertising():
    """示例5：TVC广告分镜"""
    print("=" * 60)
    print("示例5：TVC广告分镜 - 产品功能型")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    result = generator.generate(
        content_type="tvc",
        subtype="product",
        board_type="3x3",
        scene_description="护肤品广告"
    )
    
    print(generator.format_output(result))
    print("\n")


def example_6_comic_drama():
    """示例6：漫剧分镜"""
    print("=" * 60)
    print("示例6：漫剧分镜 - 战斗类")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    result = generator.generate(
        content_type="comic_drama",
        subtype="battle",
        board_type="3x3",
        scene_description="热血战斗场景"
    )
    
    storyboard = result['storyboard']
    print(f"模板: {storyboard['template_name']}\n")
    
    for shot in storyboard['shots']:
        print(f"【镜头 {shot['index']}】{shot['name']}")
        print(f"  景别: {shot['shot_type']}")
        if 'panel_type' in shot:
            print(f"  格子类型: {shot['panel_type']}")
        print(f"  Prompt: {shot['prompt']}")
        print()


def example_7_export_to_file():
    """示例7：导出到文件"""
    print("=" * 60)
    print("示例7：导出分镜方案到JSON文件")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    result = generator.generate(
        content_type="movie",
        subtype="thriller",
        board_type="3x3",
        scene_description="悬疑推理场景"
    )
    
    # 导出为JSON
    output_file = "thriller_storyboard.json"
    generator.export_to_json(result, output_file)
    print(f"分镜方案已导出到: {output_file}")
    print("\n")


def example_8_custom_prompts():
    """示例8：使用自定义提示词"""
    print("=" * 60)
    print("示例8：使用自定义提示词")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    # 自定义某些镜头的提示词
    custom_prompts = {
        1: "Custom wide shot of a futuristic city, cyberpunk style, neon lights, rain, establishing shot",
        5: "Custom close-up of protagonist's face, determination, dramatic lighting, emotional peak"
    }
    
    result = generator.generate(
        content_type="movie",
        subtype="action",
        board_type="3x3",
        scene_description="科幻动作场景",
        custom_prompts=custom_prompts
    )
    
    storyboard = result['storyboard']
    print("自定义后的分镜:\n")
    for shot in storyboard['shots'][:3]:
        print(f"镜头{shot['index']}: {shot['name']}")
        if shot.get('customized'):
            print(f"  [已自定义] {shot['prompt']}")
        else:
            print(f"  {shot['prompt'][:60]}...")
    print("\n")


def example_9_color_evolution():
    """示例9：查看色调演进建议"""
    print("=" * 60)
    print("示例9：色调演进建议")
    print("=" * 60)
    
    generator = StoryboardGenerator()
    
    # 对比不同类型
    types_to_compare = [
        ("movie", "war", "战争片"),
        ("movie", "romance", "爱情片"),
        ("short_drama", "suspense", "悬疑短剧")
    ]
    
    for content_type, subtype, name in types_to_compare:
        result = generator.generate(
            content_type=content_type,
            subtype=subtype,
            board_type="3x3"
        )
        
        print(f"\n【{name}】")
        colors = result['color_evolution']
        # 只显示前3个和后3个
        for color in colors[:3]:
            print(f"  镜头{color['shot_index']}: {color['emotion']} - {color['primary_color']}")
        print("  ...")
        for color in colors[-3:]:
            print(f"  镜头{color['shot_index']}: {color['emotion']} - {color['primary_color']}")
    print("\n")


def example_10_quick_generate():
    """示例10：快速生成函数"""
    print("=" * 60)
    print("示例10：使用快速生成函数")
    print("=" * 60)
    
    # 使用便捷函数快速生成
    result = generate_storyboard(
        content_type="short_drama",
        subtype="emotion",
        board_type="3x3",
        scene_description="感人重逢场景"
    )
    
    # 获取故事板信息
    storyboard = result['storyboard']
    print(f"模板: {storyboard['template_name']}")
    print(f"镜头数量: {len(storyboard['shots'])}")
    print("\n前3个镜头:")
    for shot in storyboard['shots'][:3]:
        print(f"  {shot['index']}. {shot['name']} - {shot['shot_type']}")
    print("\n")


if __name__ == "__main__":
    print("\n")
    print("*" * 60)
    print("分镜工具使用示例")
    print("*" * 60)
    print("\n")
    
    # 运行所有示例
    example_2_list_all_types()      # 先列出所有类型
    example_1_basic_usage()         # 基本使用
    example_3_different_genres()    # 不同类型对比
    example_4_board_type_comparison()  # 故事板类型对比
    example_5_tvc_advertising()     # TVC广告
    example_6_comic_drama()         # 漫剧
    example_7_export_to_file()      # 导出文件
    example_8_custom_prompts()      # 自定义提示词
    example_9_color_evolution()     # 色调演进
    example_10_quick_generate()     # 快速生成
    
    print("*" * 60)
    print("所有示例运行完成！")
    print("*" * 60)
