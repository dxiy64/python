# -*- coding: utf-8 -*-
# ============================================
# homework09.py · 把 manager.py 吃透（阅读+改造作业）
# 不用从零写，今天的作业是"读懂+改"——这是工程师的日常
# ============================================

# TODO 1（必做）: 把 manager.py 从头到尾读一遍，回答：
#   (1) save(contacts) 在哪几处被调用？为什么每次改完都要立刻存？
#   (2) del contacts[name] 是干嘛的？（Day4 没教，自己猜+验证）
#   (3) choose = input(...).strip() 里 .strip() 是干嘛的？
#   把答案写成注释贴给我

# 回答
# (1) save(contacts) 在"3.加"、"4.删"、"5.改"三处被调用。每次改完都要立刻存是为了保证数据的持久化，防止程序意外退出导致数据丢失。
# (2) del contacts[name] 是用来删除字典 contacts 中键为 name 的键值对，即删除某个联系人的信息。
# (3) .strip() 是用来去掉输入字符串两端的空白字符（包括空格、制表符等），防止用户输入时不小心加了空格导致匹配失败。

# TODO 2（必做）: 加一个功能——菜单加 "6.统计"，
#   打印"共有 N 位联系人"（len  Day3老朋友）。
#   在 show_menu、while 分支两处加代码。

# def show_menu():
#    print("=" * 30)
#    print("1.看全部  2.查  3.加  4.删  5.改  6.统计  q.退出")
#    print("=" * 30)
#
# while True:
#    choose = input("请选择操作：").strip()
#    if choose == "6":
#        print(f"共有 {len(contacts)} 位联系人")


# TODO 3（进阶选做）: 现在电话随便输字母也存进去，
#   加一个检查：电话必须全是数字（提示：str 有个 .isdigit() 方法），
#   不是数字就打印"电话只能是数字！"并不存。
#   分别在"3.加"和"5.改"两处加。

#    elif choose == "3":
#            name = input("名字：")
#            phone = input("电话：")
#            if not phone.isdigit():
#                print("电话只能是数字！")
#            else:
#                contacts[name] = phone
#                save(contacts)          # 每次改完立刻存盘！
#                print(f"已加上 {name}")

# TODO 4（进阶选做）: 把 weather_log.txt 那个思路搬过来，
#   每次"加/删/改"成功后往 opt_log.txt 追加一行操作记录，
#   如 "加 小红 139... 2026-09-10"（要日期？Day7 的 datetime 回来了）

# import datetime

#        elif choose == "3":
#            name = input("名字：")
#            phone = input("电话：")
#            contacts[name] = phone
#            save(contacts)          # 每次改完立刻存盘！
#            print(f"已加上 {name}")
#            with open("opt_log.txt", "a", encoding="utf-8") as f:
#                f.write(f"今天是 {datetime.date.today()}, 添加了 {name}{phone}\n")
#        elif choose == "4":
#            name = input("删谁：")
#            if name in contacts:
#                del contacts[name]  # del 删一对
#                save(contacts)
#                print(f"已删除 {name}")
#                with open("opt_log.txt", "a", encoding="utf-8") as f:
#                    f.write(f"今天是 {datetime.date.today()}, 删除了 {name}{phone}\n")
#            else:
#                print("查无此人")

import json
import datetime
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts.json")
OPTLOG = os.path.join(BASE, "opt_log.txt")


def load():
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(contacts):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def show_menu():
    print("=" * 30)
    print("1.看全部\n  2.查\n  3.加\n  4.删\n  5.改\n  6.查人数\n  q.退出")
    print("=" * 30)


def find_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "查无此人"


def main():
    contacts = load()
    print(f"载入了 {len(contacts)} 位联系人")
    while True:
        show_menu()
        choose = input("请选择你要做的：").strip()
        if choose == "q":
            print("感谢你的使用，再见！")
            break

        elif choose == "1":
            if not contacts:
                print("暂无联系人，请先添加一个吧")
            for name, phone in contacts.items():
                print(f"{name}：{phone}")

        elif choose == "2":
            who = input("请输入查询姓名：")
            print(f"{who}:{find_phone(contacts, who)}")

        elif choose == "3":
            print("请输入名字和电话")
            name = input("名字：").strip()
            phone = input("电话：").strip()
            if not phone.isdigit():
                print("电话只能是数字！")
            else:
                contacts[name] = phone
                save(contacts)
                print(f"已添加{name}")
                with open(OPTLOG, "a", encoding="utf-8") as f:
                    f.write(f"今天是 {datetime.date.today()}, 添加了 {name}{phone}\n")

        elif choose == "4":
            name = input("删谁：").strip()
            if name in contacts:
                phone = contacts[name]
                del contacts[name]
                save(contacts)
                print(f"已删除 {name}")
                with open(OPTLOG, "a", encoding="utf-8") as f:
                    f.write(f"今天是 {datetime.date.today()}, 删除了 {name}{phone}\n")
            else:
                print("查无此人")

        elif choose == "5":
            name = input("改谁的电话：").strip()
            if name in contacts:
                oldphone = contacts[name]
                newphone = input("新电话：").strip()
                if not newphone.isdigit():
                    print("电话只能是数字！")
                else:
                    contacts[name] = newphone
                    save(contacts)
                    print(f"已修改{name}")
                    with open(OPTLOG, "a", encoding="utf-8") as f:
                        f.write(
                            f"今天是 {datetime.date.today()}, 修改了 {name}:{oldphone}->{newphone}\n"
                        )
            else:
                print("查无此人")

        elif choose == "6":
            print(f"共有 {len(contacts)} 位联系人")

        else:
            print("只能选 1/2/3/4/5/6/q，请重选！")


main()

# 笔记
# 1. 在编写开始前，import好所有需要的模块，以及设定好文件路径，方便后续使用
# 2. 如果有需要，可以提前编写好函数，如load()、save()、show_menu()、find_phone()，并用def打包起名，方便后续使用
# 3. main（）是整个程序的入口，在main（）中调用所有函数，实现整个程序的功能
# 4. 在main()中，开始时如果有需要加载的文件，先调用load()函数，将文件内容加载到程序中
# 5. .strip()()可以去除字符串两端的空格，防止用户输入时误输入空格
# 6. items()可以返回字典中所有的键值对，方便后续使用
# 7. .isdigit()可以判断字符串是否为数字，防止用户输入时误输入非数字字符
# 8. datetime.date.today()可以返回当前日期，方便后续使用
# 9. with open() as f可以打开文件，方便后续使用，写法为with open("文件路径", "打开方式", encoding="编码格式") as f:
# 10. json.dump()可以将字典写入文件，方便后续使用，写法为json.dump(字典, 文件, ensure_ascii=False, indent=2)
# 11. json.load()可以读取文件中的字典，方便后续使用，写法为json.load(文件)
# 12. del 可以删除字典中的键值对，方便后续使用，写法为del 字典[键]
# 13. .get相当于回车，可以获取字典中的值，方便后续使用，写法为字典.get(键)
