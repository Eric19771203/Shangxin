"""
测试现代新晋导演风格
"""
from generator import generate_storyboard

# 测试维伦纽瓦风格科幻片
print('=== 维伦纽瓦风格科幻片 ===')
result = generate_storyboard('movie', 'action', '3x3', '外星遗迹探索', director_style='villeneuve')
print(f"导演: {result['content_info']['director_style']}")
print(f"导演信息: {result['director_info']['name']} - {result['director_info']['style_keywords']}")
print('\n前3个镜头:')
for shot in result['storyboard']['shots'][:3]:
    print(f"  {shot['index']}. {shot['name']}: {shot['prompt'][:80]}...")

print('\n' + '='*60)
print('=== 乔丹·皮尔风格悬疑片 ===')
result2 = generate_storyboard('movie', 'thriller', '3x3', '郊区神秘事件', director_style='peele')
print(f"导演: {result2['director_info']['name']}")
print(f"风格关键词: {result2['director_info']['style_keywords']}")
print('\n前3个镜头:')
for shot in result2['storyboard']['shots'][:3]:
    print(f"  {shot['index']}. {shot['name']}: {shot['prompt'][:80]}...")

print('\n' + '='*60)
print('=== 赵婷风格文艺片 ===')
result3 = generate_storyboard('movie', 'art', '3x3', '公路旅行', director_style='zhao')
print(f"导演: {result3['director_info']['name']}")
print(f"风格关键词: {result3['director_info']['style_keywords']}")
print('\n前3个镜头:')
for shot in result3['storyboard']['shots'][:3]:
    print(f"  {shot['index']}. {shot['name']}: {shot['prompt'][:80]}...")

print('\n' + '='*60)
print('=== 阿里·艾斯特风格恐怖片 ===')
result4 = generate_storyboard('movie', 'thriller', '3x3', '乡村仪式', director_style='aster')
print(f"导演: {result4['director_info']['name']}")
print(f"风格关键词: {result4['director_info']['style_keywords']}")
print('\n前3个镜头:')
for shot in result4['storyboard']['shots'][:3]:
    print(f"  {shot['index']}. {shot['name']}: {shot['prompt'][:80]}...")

print('\n' + '='*60)
print('=== 罗伯特·艾格斯风格历史片 ===')
result5 = generate_storyboard('movie', 'art', '3x3', '17世纪村庄', director_style='eggers')
print(f"导演: {result5['director_info']['name']}")
print(f"风格关键词: {result5['director_info']['style_keywords']}")
print('\n前3个镜头:')
for shot in result5['storyboard']['shots'][:3]:
    print(f"  {shot['index']}. {shot['name']}: {shot['prompt'][:80]}...")

print('\n\n所有现代导演测试完成！')
