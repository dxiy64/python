# -*- coding: utf-8 -*-
# ============================================
# homework08.py · 我的天气小管家
# ============================================
import requests

# TODO 1: 让用户输入城市（input），拼进网址
# city = input(???)
# url = f"https://wttr.in/{city}?format=j1"

city = input("请输入城市名：")
url = f"https://wttr.in/{city}?format=j1"


# TODO 2: try 包住 requests.get + r.json()，
#   超时/断网（requests.exceptions.RequestException）时打印"网络开小差了"并退出
#   状态码不是 200 时打印"查不到这个城市"并退出
try:
    r = requests.get(url, timeout=15)
    if r.status_code != 200:
        print("查不到这个城市")
        exit()

    # 以下是为了承接r.json()，如果网络异常会抛出异常

    data = r.json()
except requests.exceptions.RequestException:
    print("网络开小差了")
    exit()

# TODO 3: 打印当前温度 + 天气描述 + 明天最高/最低温
#   （照抄 day08.py 第③④段，注意 data["weather"][1] 是明天）
now = data["current_condition"][0]  # 当前天气：第0个
print(f"{city}现在 {now['temp_C']}°C，{now['weatherDesc'][0]['value']}")
print(f"体感 {now['FeelsLikeC']}°C，湿度 {now['humidity']}%")

area = data["nearest_area"][0]
print("匹配到的地方：", area["areaName"][0]["value"])

tomorrow = data["weather"][1]  # 明天的天气：第1个
print(
    f"明天 {tomorrow['date']} 最高{tomorrow['maxtempC']}°C 最低{tomorrow['mintempC']}°C"
)

# TODO 4 (进阶选做): 把这次查询结果追加存进 weather_log.txt，
#   一行一条，如 "东莞 28°C 晴 2026-09-10"（Day5 的 "a" 模式回来了）
with open("weather_log.txt", "a", encoding="utf-8") as f:
    f.write(
        f"{city} {now['temp_C']}°C {now['weatherDesc'][0]['value']} {tomorrow['date']}\n"
    )

# 笔记
# 1. requests.get() 用于发送 HTTP GET 请求，相当于在浏览器地址栏输入网址并回车，返回一个 Response 对象，包含了服务器返回的内容和状态码等信息

# 2. requests.get(url，timeout=15)意思是让 requests 模块去访问 url 这个网址，返回一个 Response 对象，timeout=15 表示如果 15 秒内没有响应就报错

# 3. r.json() 用于将返回的 JSON 数据转换为 Python 字典，方便我们操作和提取数据

# 4. 索引和字典的键值对访问方式可以用来获取我们需要的数据，写法类似于 data["current_condition"][0]["temp_C"]，其中 current_condition 是字典的键，0 是列表的索引，temp_C 是字典的键（索引的写法是 列表[索引]，索引从 0 开始，负数索引表示从末尾开始计数）
