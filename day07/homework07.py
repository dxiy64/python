# -*- coding: utf-8 -*-
# ============================================
# homework07.py · 通讯录存档版（JSON）
# ============================================
import json

# TODO 1: 程序启动时尝试读 contacts.json，
#   有就 load 进 contacts，没有（FileNotFoundError）就用空字典 {}
# try:
#     with open(???, "r", encoding="utf-8") as f:
#         contacts = json.load(f)
# except FileNotFoundError:
#     contacts = ???
try:
    with open("contacts.json", "r", encoding="utf-8") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {"光羽": "18486311094", "小明": "13800001111"}

# TODO 4: 启动时打印上次共有几位（放这里：load 刚结束、新人还没加）
print(f"上次共有 {len(contacts)} 位联系人")


# TODO 2: 让用户输入名字和电话，存进 contacts，
#   然后 dump 回 contacts.json（"w" 模式，ensure_ascii=False）
name = input("请输入联系人姓名：")
phone = input("请输入联系人电话：")
contacts[name] = phone
with open("contacts.json", "w", encoding="utf-8") as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)

# TODO 3: 用 find_phone 的思路（Day4）查一个人并打印
while True:
    find_name = input("要查谁？（输入 q 退出）：")
    if find_name == "q":
        print("已退出查询，再见！")
        break
    if find_name in contacts:
        print(f"{find_name} 查询结果：{contacts[find_name]}")
    else:
        print(f"{find_name} 查询结果：查无此人")


# 笔记
# 1. json.dump() 将字典写入文件，写法为 json.dump(字典, 文件对象, ensure_ascii=False, indent=2)，json.load() 从文件读取字典，写法为 json.load(文件对象)
# 2. datetime的作用是获取当前日期和时间，random的作用是生成随机数
# 3. try-except语句用于处理可能出现的异常情况，例如文件不存在时，程序不会崩溃，而是执行except块中的代码
# 4. len() 函数用于获取字典中键值对的数量
# 5. import语句用于导入模块，模块是别人写好的工具箱，也可以自己写模块，模块可以包含函数、类和变量等
#
