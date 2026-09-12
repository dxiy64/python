# -*- coding: utf-8 -*-
# ============================================
# Day 07 · 模块与 JSON —— 结构化存档
# 运行方法：python day07\day07.py
# ============================================
import json  # 处理 JSON 的标准库，不用 pip 装
import datetime  # 处理日期时间的标准库
import random  # 处理随机数的标准库

# ① 模块 = 别人写好的工具箱，import 搬进来
print("今天是：", datetime.date.today())
print("随机抽一个：", random.randint(1, 10))

# ② JSON = 带格式的文字，字典长得像就能存
contacts = {"光羽": "18486311094", "小明": "13800001111"}

# 存：dump = 倒出去（字典 → 文件里的文字）
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)
print("已存进 contacts.json")

# 读：load = 装进来（文件里的文字 → 字典）
with open("contacts.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("读出来：", loaded)
print("类型：", type(loaded).__name__)  # dict！直接能用 contacts["光羽"] 查
print("查光羽：", loaded["光羽"])

# ③ 对比 Day5 的纯文本：纯文本读回来是一大坨字符串，还得自己切；
#    JSON 读回来直接就是字典，零加工
with open("demo_raw.txt", "w", encoding="utf-8") as f:
    f.write(str(contacts))

with open("demo_raw.txt", "r", encoding="utf-8") as f:
    raw = f.read()
print("纯文本读回来：", raw)
print("类型：", type(raw).__name__)  # str！想查电话还得自己解析
