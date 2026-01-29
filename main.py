import requests
from bs4 import BeautifulSoup
import datetime
import schedule
import time
import os
from dotenv import load_dotenv
import argparse
import sys

load_dotenv()  # 加载 .env 文件中的环境变量

# 如果本地运行，需要先设置环境变量，或者使用 python-dotenv（下文会教）
PUSHPLUS_TOKEN = os.getenv("PUSHPLUS_TOKEN")

def get_baidu_hot_news():
    """爬取百度热搜"""
    url = "https://top.baidu.com/board?tab=realtime"
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select('.c-single-text-ellipsis')
        
        if not titles: return None, "未找到数据"

        today_str = datetime.date.today().strftime("%Y-%m-%d")
        content_lines = [f"<h3>📅 {today_str} 百度热搜</h3><hr>"]
        
        seen = set()
        count = 1
        for title in titles:
            text = title.get_text().strip()
            if text and text not in seen:
                content_lines.append(f"<p><b>{count}.</b> {text}</p>")
                seen.add(text)
                count += 1
            if count > 15: break
            
        return today_str, "".join(content_lines)
    except Exception as e:
        return None, f"爬虫错误: {e}"

def send_push():
    """发送推送逻辑"""
    if not PUSHPLUS_TOKEN:
        print("❌ 错误：未检测到 PUSHPLUS_TOKEN 环境变量！")
        return

    print("正在获取新闻并推送...")
    date_str, content = get_baidu_hot_news()
    
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": f"{date_str} 每日新闻",
        "content": content,
        "template": "html"
    }
    
    try:
        resp = requests.post(url, json=data)
        print(f"推送结果: {resp.json()}")
    except Exception as e:
        print(f"推送异常: {e}")

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="立即执行一次并退出")
    args = parser.parse_args()

    # 检查 Token 是否存在
    if not PUSHPLUS_TOKEN:
        print("⚠️ 警告：环境变量 'PUSHPLUS_TOKEN' 未设置。")
        print("如果是本地运行，请在终端执行: export PUSHPLUS_TOKEN='你的token'")
        print("如果是 GitHub Actions，请在 Secrets 中设置。")
        sys.exit(1)

    if args.once:
        # 模式1：立即执行（适用于 GitHub Actions 或 手动测试）
        send_push()
    else:
        # 模式2：本地定时循环
        print("🚀 机器人已启动，等待定时任务 (每天 08:00)...")
        schedule.every().day.at("08:00").do(send_push)
        
        while True:
            schedule.run_pending()
            time.sleep(60)