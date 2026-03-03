#!/usr/bin/env python3
import requests

# 测试代理
proxy = "111.79.111.126:3128"

proxies = {
    "http": f"http://{proxy}",
    "https": f"http://{proxy}",
}

print(f"使用代理: {proxy}")
print("=" * 50)

# 测试多个网站
test_urls = [
    ("GitHub", "https://github.com"),
    ("X/Twitter", "https://x.com"),
    ("Google", "https://www.google.com"),
    ("HTTPBin", "https://httpbin.org/get"),
]

for name, url in test_urls:
    try:
        print(f"\n测试 {name} ({url})...")
        response = requests.get(url, proxies=proxies, timeout=10)
        print(f"✅ {name} - 状态码: {response.status_code}")
        if response.status_code == 200:
            print(f"   响应长度: {len(response.content)} 字节")
    except Exception as e:
        print(f"❌ {name} - 错误: {e}")

print("\n" + "=" * 50)
print("测试完成！")
