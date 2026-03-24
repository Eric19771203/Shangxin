#!/usr/bin/env python3
import requests
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def test_proxy(proxy, test_url="https://httpbin.org/get", timeout=5):
    """测试一个代理是否可用"""
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        response = requests.get(test_url, proxies=proxies, timeout=timeout)
        if response.status_code == 200:
            return (proxy, True, response.elapsed.total_seconds())
    except Exception as e:
        pass
    return (proxy, False, None)

def load_proxies(file_path):
    """从文件加载代理列表"""
    proxies = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and ':' in line:
                    proxies.append(line)
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    return proxies

def main():
    # 加载代理列表
    print("加载 Databay 代理列表...")
    http_proxies = load_proxies("free-proxy-list/http.txt")
    socks5_proxies = load_proxies("free-proxy-list/socks5.txt")
    
    print(f"HTTP 代理: {len(http_proxies)} 个")
    print(f"SOCKS5 代理: {len(socks5_proxies)} 个")
    
    # 随机选择一些代理测试
    all_proxies = http_proxies
    test_count = min(100, len(all_proxies))
    test_proxies_list = random.sample(all_proxies, test_count) if len(all_proxies) > test_count else all_proxies
    
    print(f"\n开始测试 {len(test_proxies_list)} 个代理...")
    
    working_proxies = []
    
    # 多线程测试
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(test_proxy, proxy): proxy for proxy in test_proxies_list}
        
        for i, future in enumerate(as_completed(futures), 1):
            proxy, works, elapsed = future.result()
            if works:
                print(f"[{i}/{len(test_proxies_list)}] ✅ {proxy} - {elapsed:.2f}s")
                working_proxies.append((proxy, elapsed))
            else:
                if i % 10 == 0:
                    print(f"[{i}/{len(test_proxies_list)}] 测试中...")
    
    # 按速度排序
    working_proxies.sort(key=lambda x: x[1])
    
    print(f"\n测试完成！找到 {len(working_proxies)} 个可用代理")
    
    if working_proxies:
        print("\n最快的 10 个代理:")
        for i, (proxy, elapsed) in enumerate(working_proxies[:10], 1):
            print(f"{i}. {proxy} - {elapsed:.2f}s")
        
        # 保存可用代理
        with open("databay_working_proxies.txt", "w") as f:
            for proxy, elapsed in working_proxies:
                f.write(f"{proxy}\n")
        print(f"\n已保存 {len(working_proxies)} 个可用代理到 databay_working_proxies.txt")
        
        # 用最快的代理测试 X/Twitter
        if working_proxies:
            best_proxy = working_proxies[0][0]
            print(f"\n\n用最快的代理 {best_proxy} 测试 X/Twitter 和 Google...")
            
            proxies = {
                "http": f"http://{best_proxy}",
                "https": f"http://{best_proxy}",
            }
            
            test_urls = [
                ("GitHub", "https://github.com"),
                ("X/Twitter", "https://x.com"),
                ("Google", "https://www.google.com"),
            ]
            
            for name, url in test_urls:
                try:
                    print(f"\n测试 {name}...")
                    response = requests.get(url, proxies=proxies, timeout=10)
                    print(f"✅ {name} - 状态码: {response.status_code}")
                except Exception as e:
                    print(f"❌ {name} - 错误: {e}")

if __name__ == "__main__":
    main()
