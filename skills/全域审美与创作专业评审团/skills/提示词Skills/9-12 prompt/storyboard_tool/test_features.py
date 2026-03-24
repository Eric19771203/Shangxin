#!/usr/bin/env python3
"""
CineBoard Pro - 纯Python功能测试脚本
无需UI界面，直接测试核心功能
"""

import json
from generator import StoryboardGenerator
from knowledge_base.director_styles import (
    list_all_directors, 
    get_director_style,
    apply_director_style
)
from knowledge_base.storyboard_theory import (
    list_all_books,
    get_book_info,
    list_all_topics,
    get_theory_by_topic,
    get_term,
    search_terms
)
from knowledge_base.movie import list_film_types
from knowledge_base.short_drama import list_short_drama_types
from knowledge_base.comic_drama import list_comic_types
from knowledge_base.tvc import list_tvc_types

# 初始化生成器
generator = StoryboardGenerator()

def print_header(title):
    """打印标题"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def print_subheader(title):
    """打印子标题"""
    print(f"\n📌 {title}")
    print("-"*50)

def test_content_types():
    """测试内容类型系统"""
    print_header("🎬 内容类型系统测试")
    
    print_subheader("电影类型")
    film_types = list_film_types()
    for i, t in enumerate(film_types, 1):
        print(f"  {i}. {t}")
    
    print_subheader("短剧类型")
    drama_types = list_short_drama_types()
    for i, t in enumerate(drama_types, 1):
        print(f"  {i}. {t}")
    
    print_subheader("漫剧类型")
    comic_types = list_comic_types()
    for i, t in enumerate(comic_types, 1):
        print(f"  {i}. {t}")
    
    print_subheader("TVC广告类型")
    tvc_types = list_tvc_types()
    for i, t in enumerate(tvc_types, 1):
        print(f"  {i}. {t}")

def test_director_styles():
    """测试导演风格系统"""
    print_header("🎭 导演风格系统测试")
    
    directors = list_all_directors()
    print_subheader(f"共有 {sum(len(v) if isinstance(v, list) else len(v) for v in directors.values())} 位导演")
    
    for genre, director_list in directors.items():
        print(f"\n  【{genre.upper()}】")
        if isinstance(director_list, list):
            for name in director_list:
                print(f"    • {name}")
        else:
            for name in director_list:
                print(f"    • {name}")
    
    # 测试获取导演详情
    print_subheader("导演详情示例 - 斯皮尔伯格")
    spielberg = get_director_style("spielberg")
    if spielberg and hasattr(spielberg, 'INFO'):
        info = spielberg.INFO
        print(f"  姓名: {info.get('name')}")
        print(f"  英文名: {info.get('name_en')}")
        print(f"  国籍: {info.get('nationality')}")
        print(f"  活跃时期: {info.get('active_period')}")
        print(f"  风格关键词: {', '.join(info.get('style_keywords', []))}")

def test_knowledge_base():
    """测试知识库系统"""
    print_header("📚 分镜理论知识库测试")
    
    # 书籍
    print_subheader("参考书籍")
    books = list_all_books()
    for i, book_id in enumerate(books, 1):
        book = get_book_info(book_id)
        if book:
            print(f"  {i}. {book.title}")
            print(f"     作者: {', '.join(book.authors)}")
            print(f"     分类: {book.category}")
    
    # 理论知识
    print_subheader("理论知识主题")
    topics = list_all_topics()
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic}")
    
    # 详细理论
    print_subheader("构图原理详情")
    theory = get_theory_by_topic("构图原理")
    if theory:
        print(f"  描述: {theory.get('description', '')[:100]}...")
        print(f"  核心原则: {len(theory.get('principles', {}))} 个")
    
    # 视觉术语
    print_subheader("视觉术语搜索 - '特写'")
    terms = search_terms("特写")
    for term in terms[:3]:
        print(f"  • {term.term} ({term.english})")
        print(f"    {term.definition[:60]}...")

def test_generate_war_movie():
    """测试战争片生成"""
    print_header("🎬 测试1: 战争片分镜生成 (斯皮尔伯格风格)")
    
    result = generator.generate(
        content_type="movie",
        subtype="war",
        board_type="3x3",
        scene_description="诺曼底登陆，士兵们在枪林弹雨中冲向海滩",
        director_style="spielberg"
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return
    
    # 显示结果
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("分镜方案")
    print(f"  模板: {storyboard.get('template_name', 'N/A')}")
    print(f"  镜头数: {len(shots)}")
    
    for shot in shots[:3]:  # 只显示前3个
        print(f"\n  【镜头 {shot.get('index')}】{shot.get('name')}")
        print(f"    景别: {shot.get('shot_type')}")
        print(f"    角度: {shot.get('angle')}")
        print(f"    运动: {shot.get('movement')}")
        print(f"    描述: {shot.get('description', '')[:80]}...")
        print(f"    AI提示词: {shot.get('prompt', '')[:80]}...")
    
    # 导演信息
    director_info = data.get("director_info", {})
    print_subheader("导演风格应用")
    print(f"  导演: {director_info.get('name', 'N/A')}")
    print(f"  技巧: {', '.join(director_info.get('techniques', [])[:3])}")

def test_generate_art_film():
    """测试文艺片生成"""
    print_header("🎬 测试2: 文艺片分镜生成 (王家卫风格)")
    
    result = generator.generate(
        content_type="movie",
        subtype="art",
        board_type="3x3",
        scene_description="雨夜，失恋的女子独自走在霓虹灯闪烁的街道",
        director_style="wong_kar_wai"
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("分镜方案")
    for shot in shots[:3]:
        print(f"\n  【镜头 {shot.get('index')}】{shot.get('name')}")
        print(f"    景别: {shot.get('shot_type')}")
        print(f"    描述: {shot.get('description', '')[:80]}...")
    
    # 色彩演进
    color_evolution = data.get("color_evolution", [])
    print_subheader("色彩演进方案")
    for ce in color_evolution[:3]:
        print(f"  镜头{ce.get('shot_index')}: {ce.get('emotion')} - {ce.get('primary_color')}")

def test_generate_short_drama():
    """测试短剧生成"""
    print_header("🎬 测试3: 短剧分镜生成 (无导演风格)")
    
    result = generator.generate(
        content_type="short_drama",
        subtype="suspense",
        board_type="3x3",
        scene_description="女主角发现丈夫的秘密，在房间里寻找线索"
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("分镜方案")
    for shot in shots[:3]:
        print(f"\n  【镜头 {shot.get('index')}】{shot.get('name')}")
        print(f"    景别: {shot.get('shot_type')}")
        print(f"    描述: {shot.get('description', '')[:80]}...")

def test_generate_with_custom_prompts():
    """测试自定义提示词"""
    print_header("🎬 测试4: 自定义提示词生成")
    
    custom_prompts = {
        1: "航拍城市夜景，霓虹灯光，赛博朋克风格",
        5: "主角面部特写，眼神坚定，逆光拍摄"
    }
    
    result = generator.generate(
        content_type="movie",
        subtype="thriller",
        board_type="3x3",
        scene_description="科幻惊悚片开场",
        custom_prompts=custom_prompts
    )
    
    if "error" in result:
        print(f"❌ 错误: {result['error']}")
        return
    
    data = result.get("data", {})
    storyboard = data.get("storyboard", {})
    shots = storyboard.get("shots", [])
    
    print_subheader("自定义镜头")
    for shot in shots:
        if shot.get('index') in [1, 5]:
            print(f"\n  【镜头 {shot.get('index')}】(自定义)")
            print(f"    描述: {shot.get('description', '')}")

def test_director_style_application():
    """测试导演风格应用"""
    print_header("🎭 导演风格应用测试")
    
    base_prompt = "雨夜街道，孤独的人影"
    
    directors = ["nolan", "wong_kar_wai", "wes_anderson", "villeneuve"]
    
    print_subheader("同一场景的不同导演风格")
    for director_id in directors:
        styled_prompt = apply_director_style(base_prompt, director_id)
        director = get_director_style(director_id)
        name = director.INFO.get('name', director_id) if hasattr(director, 'INFO') else director_id
        print(f"\n  【{name}】")
        print(f"    原始: {base_prompt}")
        print(f"    增强: {styled_prompt}")

def test_4x3_board():
    """测试4x3沉浸分镜板"""
    print_header("🎬 测试5: 4×3沉浸分镜板生成")
    
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
    print(f"  模板: {storyboard.get('template_name', 'N/A')}")
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

def export_example():
    """导出示例"""
    print_header("💾 导出功能示例")
    
    result = generator.generate(
        content_type="movie",
        subtype="romance",
        board_type="3x3",
        scene_description="初恋的告白场景，樱花树下"
    )
    
    if "error" not in result:
        # 保存为JSON
        filename = "example_storyboard.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"✅ 已导出到: {filename}")
        
        # 显示文件大小
        import os
        size = os.path.getsize(filename)
        print(f"   文件大小: {size} 字节")

def main():
    """主函数"""
    print("\n" + "🎬"*35)
    print("  CineBoard Pro - 纯Python功能测试")
    print("🎬"*35)
    
    try:
        # 基础系统测试
        test_content_types()
        test_director_styles()
        test_knowledge_base()
        
        # 生成功能测试
        test_generate_war_movie()
        test_generate_art_film()
        test_generate_short_drama()
        test_generate_with_custom_prompts()
        test_director_style_application()
        test_4x3_board()
        
        # 导出测试
        export_example()
        
        # 完成
        print_header("✅ 所有测试完成！")
        print("\n  提示:")
        print("  • 生成的分镜方案已保存到 example_storyboard.json")
        print("  • 可以修改 test_features.py 中的参数进行自定义测试")
        print("  • 所有功能均可直接调用，无需UI界面")
        print("\n" + "="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ 测试出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
