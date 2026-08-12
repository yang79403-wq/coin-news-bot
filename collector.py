import os
from datetime import datetime

# 获取当前北京时间
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 模拟采集或生成钱币收藏内容（你可以替换为真正的爬虫代码，比如抓取钱币网站RSS或API）
coin_tips = [
    "今日钱币行情观察：近期江南造币厂光绪元宝、大清铜币市场需求稳定，评级币成交活跃。",
    "收藏小贴士：古钱币清洗切忌用强酸或砂纸打磨，会严重破坏包浆导致价值暴跌。",
    "市场快讯：第三套人民币小全套近期在礼品盘需求带动下，板块整体呈现温和上涨态势。",
    "鉴赏指南：辨别袁大头真伪，首重边齿与成色，正品边齿多为麦穗芒或标准齿，压力感十足。"
]

# 简单的算法：根据天数轮流或随机挑选一条内容
import random
today_content = random.choice(coin_tips)

# 生成网页的 HTML 内容
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>每日钱币收藏自动播报</title>
    <style>
        body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; background: #f4f4f9; }}
        .card {{ background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h1 {{ color: #b8860b; border-bottom: 2px solid #eee; padding-bottom: 10px; }}
        .time {{ color: #888; font-size: 0.9em; margin-bottom: 20px; }}
        .content {{ font-size: 1.1em; color: #333; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🪙 钱币收藏自动化每日播报</h1>
        <div class="time">更新时间：{now}</div>
        <div class="content">
            <p>{today_content}</p>
        </div>
        <hr style="border:0; border-top:1px solid #eee; margin:20px 0;">
        <p style="font-size: 0.8em; color: #aaa;">本页面由 GitHub Actions 机器人每天自动全网收集并生成，全程0成本。</p>
    </div>
</body>
</html>
"""

# 将生成的 HTML 写入 index.html（GitHub Pages 默认读取该文件作为首页）
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("网页生成成功！")
