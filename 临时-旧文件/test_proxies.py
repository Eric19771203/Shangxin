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
    print("加载代理列表...")
    http_proxies = load_proxies("PROXY-List/http.txt")
    socks4_proxies = load_proxies("PROXY-List/socks4.txt")
    socks5_proxies = load_proxies("PROXY-List/socks5.txt")
    
    print(f"HTTP 代理: {len(http_proxies)} 个")
    print(f"SOCKS4 代理: {len(socks4_proxies)} 个")
    print(f"SOCKS5 代理: {len(socks5_proxies)} 个")
    
    # 随机选择一些代理测试
    all_proxies = http_proxies  # 先测试 HTTP 代理
    test_count = min(50, len(all_proxies))
    test_proxies_list = random.sample(all_proxies, test_count) if len(all_proxies) > test_count else all_proxies
    
    print(f"\n开始测试 {len(test_proxies_list)} 个代理...")
    
    working_proxies = []
    
    # 多线程测试
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(test_proxy, proxy): proxy for proxy in test_proxies_list}
        
        for i, future in enumerate(as_completed(futures), 1):
            proxy, works, elapsed = future.result()
            if works:
                print(f"[{i}/{len(test_proxies_list)}] ✅ {proxy} - {elapsed:.2f}s")
                working_proxies.append((proxy, elapsed))
            else:
                print(f"[{i}/{len(test_proxies_list)}] ❌ {proxy}")
    
    # 按速度排序
    working_proxies.sort(key=lambda x: x[1])
    
    print(f"\n测试完成！找到 {len(working_proxies)} 个可用代理")
    
    if working_proxies:
        print("\n最快的 10 个代理:")
        for i, (proxy, elapsed) in enumerate(working_proxies[:10], 1):
            print(f"{i}. {proxy} - {elapsed:.2f}s")
        
        # 保存可用代理
        with open("working_proxies.txt", "w") as f:
            for proxy, elapsed in working_proxies:
                f.write(f"{proxy}\n")
        print(f"\n已保存 {len(working_proxies)} 个可用代理到 working_proxies.txt")

if __name__ == "__main__":
    main()
