# -*- coding: utf-8 -*-
# ============================================
# homework08.py · 我的天气小管家
# 运行方法：cd day08 再 python homework08.py
# 需要：pip install requests
# 本课只学：requests.get + .json() + try 包住网络请求
# ============================================

import sys

import requests

WEATHER_LOG = "weather_log.txt"


def fetch_weather(city):
    """问 wttr.in 要天气：断网超时返回 None，城市不对返回“查不到”"""
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=15)
    except requests.exceptions.RequestException:
        print("网络开小差了")
        return None
    if response.status_code != 200:
        print("查不到这个城市")
        return None
    return response.json()


def show_weather(city, data):
    """打印：当前实况 + 匹配地点 + 明天最高最低温"""
    now = data["current_condition"][0]
    print(f"{city}现在 {now['temp_C']}°C，{now['weatherDesc'][0]['value']}")
    print(f"体感 {now['FeelsLikeC']}°C，湿度 {now['humidity']}%")

    area = data["nearest_area"][0]
    print("匹配到的地方：", area["areaName"][0]["value"])

    tomorrow = data["weather"][1]
    print(f"明天 {tomorrow['date']} 最高{tomorrow['maxtempC']}°C 最低{tomorrow['mintempC']}°C")
    return now, tomorrow


def append_log(city, now, tomorrow):
    """追加记一笔：一行一条，Day05 的 "a" 模式回来了"""
    with open(WEATHER_LOG, "a", encoding="utf-8") as f:
        f.write(f"{city} {now['temp_C']}°C {now['weatherDesc'][0]['value']} {tomorrow['date']}\n")


def main():
    city = input("请输入城市名：").strip()
    data = fetch_weather(city)
    if data is None:
        sys.exit(1)
    now, tomorrow = show_weather(city, data)
    append_log(city, now, tomorrow)


if __name__ == "__main__":
    main()

# 笔记
# 1. requests.get(url, timeout=15)：像在地址栏回车，15 秒没回就报错
# 2. 状态码 200 才是成功；404/500 直接按“查不到”处理
# 3. r.json()：把返回文字翻成字典/列表，和 json.load 一个家族
# 4. data["current_condition"][0]：字典套列表套字典，一层层剥
# 5. 网络请求必须包 try：RequestException 接住超时和断网
