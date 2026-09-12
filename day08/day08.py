# -*- coding: utf-8 -*-
# ============================================
# Day 08 · 联网小程序：天气查询（requests 正式登场）
# 运行方法：python day08\day08.py
# 需要：pip install requests（你已装好）
# ============================================
import requests

# ① 发请求：GET 就像在浏览器地址栏敲网址回车
city = "东莞"
url = f"https://wttr.in/{city}?format=j1"   # j1 = 给我 JSON 版数据
print("正在问：", url)
r = requests.get(url, timeout=15)
print("状态码：", r.status_code)   # 200 = 成功，404 = 没找着，500 = 对方炸了

# ② .json() 把返回的文字翻译成字典/列表（和 json.load 一个家族）
data = r.json()
print("外层有这些键：", list(data.keys()))

# ③ 一层层剥开拿数据（字典套列表套字典，耐心看结构）
now = data["current_condition"][0]   # 当前天气：第0个
print(f"{city}现在 {now['temp_C']}°C，{now['weatherDesc'][0]['value']}")
print(f"体感 {now['FeelsLikeC']}°C，湿度 {now['humidity']}%")

area = data["nearest_area"][0]
print("匹配到的地方：", area["areaName"][0]["value"])

# ④ 明后天预报：weather 是列表，一天一项
for day in data["weather"]:
    print(f"{day['date']} 最高{day['maxtempC']}°C 最低{day['mintempC']}°C")
