# -*- coding: utf-8 -*-
# ============================================
# homework04.py · 通讯录小管家（字典+函数）
# 要求：补完 TODO，能跑，能查到人
# ============================================

# 已给你两个联系人：名字 → 电话
contacts = {"光羽": "18486311094", "小明": "13800001111"}

# TODO 1: 新增一个联系人（直接写死），比如 contacts["小红"] = "13900002222"
contacts["小红"] = "13900002222"


# TODO 2: 写一个函数 find_phone(name)，输入名字返回电话，找不到返回 "查无此人"
# def find_phone(name):
#     if ??? in contacts:
#         return ???
#     else:
#         return "查无此人"
def find_phone(name):
    if name in contacts:  # 如果名字在联系人字典里
        return contacts[name]  # 则输出对应名字的值
    else:  # 否则执行下一步
        return "查无此人"  # 输出结果查无此人


while True:
    name = input("要查谁？（输入 q 退出）：")
    if name == "q":  # 如果对比输入的名字为q则进入西医不
        print("已退出查询，再见！")  # 数据对比结果
        break  # 结束这段代码
    print(f"{name} 查询结果：{find_phone(name)}")  # 调用前面的find_phone函数，输出结果


# TODO 3: 调用你的函数查两个人并打印：
# print(find_phone("光羽"))   # 应打印 18486311094
# print(find_phone("陌生人")) # 应打印 查无此人

print(find_phone("光羽"))
print(find_phone("陌生人"))  # 应打印 查无此人
# TODO 4 (进阶，选做): 用 for + contacts.items() 把所有联系人全部打印成 “名字：电话”

for name, phone in contacts.items():
    print(f"{name}：{phone}")


# 笔记
# 1. 字典 dict 是用 {} 装一堆键值对，逗号隔开，写法是 contacts = {"光羽": "18486311094", "小明": "13800001111"}
# 2. 查找字典里的值可以用 contacts["光羽"]，如果键不存在会报 KeyError
# 3. 改变字典里的值可以用 contacts["age"] = 25，如果键不存在则会新增一对键值对
# 4. 用 in 判断一个键是否在字典里，写法是 "光羽" in contacts，返回 True 或 False
# 5. for 循环可以遍历字典里的键，写法是 for k in contacts:，也可以用 for k, v in contacts.items(): 遍历键值对，第二种会同时拿到键和值
# 6. 函数def和while循环的用法和 day04.py 一样，def 用于打包代码，while 用于重复执行
# 7. return 用于把函数的结果递出来，调用函数时可以用变量接收返回值，也可以直接 print() 打印
# 8. return和print()的区别：return是把结果递出来，print是直接打印到屏幕上，return只能在函数里用，print可以在函数里也可以在函数外
# 9. 结束为