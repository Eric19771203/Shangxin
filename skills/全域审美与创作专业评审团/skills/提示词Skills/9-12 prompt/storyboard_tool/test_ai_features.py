#!/usr/bin/env python3
"""
CineBoard Pro - AI增强版功能测试
测试AI增强版生成器的所有功能
"""

import json
from generator_ai import create_ai_generator
from ai_services import AIConfig, LLMService, ImageService

def print_header(title):
    """打印标题"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def print_subheader(title):
    """打印子标题"""
    print(f"\n📌 {title}")
    print("-"*50)

def test_ai_availability():
    """测试AI服务可用性"""
    print_header("🤖 AI服务可用性检查")
    
    generator = create_ai_generator()
    
    print(f"AI服务可用: {generator.ai_available}")
    print(f"配置提供商: {generator.config.get_active_llm_provider()}")
    
    if not generator.ai_available:
        print("\n⚠️  提示: AI服务不可用，请检查 .env 文件中的API密钥配置")
        print("   复制 .env.example 为 .env 并填写你的API密钥")
    
    return generator

def test_basic_generation(generator):
    """测试基础生成（不使用AI）"""
    print_header("🎬 测试1: 基础分镜生成（无AI）")
    
    result = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="3x3",
        scene_description="诺曼底登陆，士兵们在枪林弹雨中冲向海滩",
        director_style="spielberg"
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return None
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("生成结果")
    print(f"  模板: {storyboard.get('template_name')}")
    print(f"  镜头数: {len(shots)}")
    print(f"  导演: {data.get('director_info', {}).get('name')}")
    
    print_subheader("前3个镜头")
    for shot in shots[:3]:
        print(f"\n  【镜头 {shot.get('index')}】{shot.get('name')}")
        print(f"    景别: {shot.get('shot_type')}")
        print(f"    描述: {shot.get('description', '')[:60]}...")
        print(f"    提示词: {shot.get('prompt', '')[:60]}...")
    
    return result

def test_ai_enhancement(generator):
    """测试AI增强功能"""
    print_header("🤖 测试2: AI增强分镜生成")
    
    if not generator.ai_available:
        print("⚠️  AI服务不可用，跳过此测试")
        print("   如需测试AI增强功能，请配置API密钥")
        return None
    
    print("正在使用AI增强提示词...")
    
    result = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="3x3",
        scene_description="诺曼底登陆，士兵们在枪林弹雨中冲向海滩",
        director_style="spielberg",
        use_ai_enhancement=True
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return None
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("AI增强结果")
    print(f"  AI增强: {storyboard.get('ai_enhanced', False)}")
    
    print_subheader("提示词对比（第一个镜头）")
    if shots:
        shot = shots[0]
        print(f"\n  原始提示词:")
        print(f"    {shot.get('original_prompt', 'N/A')[:100]}...")
        print(f"\n  增强提示词:")
        print(f"    {shot.get('enhanced_prompt', 'N/A')[:100]}...")
    
    return result

def test_full_ai_generation(generator):
    """测试完全AI生成"""
    print_header("🤖 测试3: 完全AI驱动的分镜生成")
    
    if not generator.ai_available:
        print("⚠️  AI服务不可用，跳过此测试")
        return None
    
    print("正在使用AI从头生成分镜...")
    print("(这可能需要一些时间)")
    
    result = generator.generate_with_full_ai(
        content_type="movie",
        subtype="thriller",
        board_type="3x3",
        scene_description="深夜，女主角独自在家，听到门外有奇怪的声响",
        director_style="fincher"
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return None
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("完全AI生成结果")
    print(f"  AI生成: {storyboard.get('ai_generated', False)}")
    print(f"  镜头数: {len(shots)}")
    
    print_subheader("所有镜头")
    for shot in shots:
        print(f"\n  【镜头 {shot.get('index')}】{shot.get('name')}")
        print(f"    景别: {shot.get('shot_type')}")
        print(f"    角度: {shot.get('angle')}")
        print(f"    运动: {shot.get('movement')}")
        print(f"    描述: {shot.get('description', '')[:50]}...")
    
    return result

def test_scene_analysis(generator):
    """测试场景分析"""
    print_header("🔍 测试4: AI场景分析")
    
    if not generator.ai_available:
        print("⚠️  AI服务不可用，跳过此测试")
        return
    
    scene = "雨夜，霓虹灯下的侦探站在窗前，手指颤抖着拿起神秘信封"
    
    print(f"场景描述: {scene}")
    print("\n正在分析场景...")
    
    analysis = generator.analyze_scene_with_ai(
        scene_description=scene,
        director_style="wong_kar_wai"
    )
    
    if "error" in analysis:
        print(f"❌ 错误: {analysis['error']}")
        return
    
    print_subheader("分析结果")
    print(json.dumps(analysis, ensure_ascii=False, indent=2))

def test_different_styles(generator):
    """测试不同导演风格"""
    print_header("🎭 测试5: 不同导演风格对比")
    
    scene = "主角站在高楼边缘，准备做出重要决定"
    directors = ["nolan", "spielberg", "wong_kar_wai"]
    
    print(f"场景: {scene}\n")
    
    for director_id in directors:
        print_subheader(f"导演: {director_id}")
        
        result = generator.generate(
            content_type="movie",
            subtype="thriller",
            board_type="3x3",
            scene_description=scene,
            director_style=director_id
        )
        
        if "error" not in result:
            data = result.get("data", {})
            storyboard = data.get("storyboard", {})
            shots = storyboard.get("shots", [])
            
            director_info = data.get("director_info", {})
            print(f"  风格: {director_info.get('style', 'N/A')}")
            print(f"  技巧: {', '.join(director_info.get('techniques', [])[:3])}")
            
            if shots:
                print(f"\n  第一个镜头:")
                print(f"    {shots[0].get('name')} - {shots[0].get('shot_type')}")
                print(f"    {shots[0].get('description', '')[:60]}...")

def test_4x3_board(generator):
    """测试4x3分镜板"""
    print_header("🎬 测试6: 4×3沉浸分镜板生成")
    
    result = generator.generate(
        content_type="movie",
        subtype="action",
        board_type="4x3",
        scene_description="追车戏，主角驾驶跑车在城市中逃避追捕",
        director_style="nolan"
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("4×3分镜方案")
    print(f"  模板: {storyboard.get('template_name')}")
    print(f"  镜头数: {len(shots)}")
    
    # 按幕显示
    acts = {
        "第一幕 (沉浸引入)": [1, 2, 3, 4],
        "第二幕 (发展递进)": [5, 6, 7, 8],
        "第三幕 (高潮沉浸)": [9, 10, 11, 12]
    }
    
    for act_name, indices in acts.items():
        print(f"\n  {act_name}")
        act_shots = [s for s in shots if s.get('index') in indices]
        for shot in act_shots:
            print(f"    镜头{shot.get('index')}: {shot.get('name')} - {shot.get('shot_type')}")

def export_comparison(generator):
    """导出对比示例"""
    print_header("💾 导出对比示例")
    
    scene = "初恋的告白场景，樱花树下"
    
    # 基础生成
    result_basic = generator.generate(
        content_type="movie",
        subtype="romance",
        board_type="3x3",
        scene_description=scene
    )
    
    results = {
        "scene": scene,
        "basic_generation": result_basic.get("data", {}),
    }
    
    # AI增强（如果可用）
    if generator.ai_available:
        result_ai = generator.generate(
            content_type="movie",
            subtype="romance",
            board_type="3x3",
            scene_description=scene,
            use_ai_enhancement=True
        )
        results["ai_enhanced"] = result_ai.get("data", {})
    
    # 保存
    filename = "ai_comparison.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 已导出对比到: {filename}")
    
    import os
    size = os.path.getsize(filename)
    print(f"   文件大小: {size} 字节")

def main():
    """主函数"""
    print("\n" + "🤖"*35)
    print("  CineBoard Pro - AI增强版功能测试")
    print("🤖"*35)
    
    # 检查AI可用性
    generator = test_ai_availability()
    
    try:
        # 基础功能测试
        test_basic_generation(generator)
        test_ai_enhancement(generator)
        test_full_ai_generation(generator)
        test_scene_analysis(generator)
        test_different_styles(generator)
        test_4x3_board(generator)
        
        # 导出
        export_comparison(generator)
        
        # 完成
        print_header("✅ 所有测试完成！")
        
        if not generator.ai_available:
            print("\n  💡 提示:")
            print("  • 当前使用的是基础生成功能")
            print("  • 如需使用AI增强功能，请:")
            print("    1. 复制 .env.example 为 .env")
            print("    2. 填写 GEMINI_API_KEY 或 AGGREGATOR_API_KEY")
            print("    3. 重新运行测试")
        else:
            print("\n  ✨ AI服务已启用！")
            print("  • 可以使用AI增强提示词")
            print("  • 可以使用完全AI生成功能")
            if generator.config.aggregator_enabled:
                print("  • 可以使用图像生成功能")
        
        print("\n" + "="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ 测试出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
