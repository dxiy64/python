# -*- coding: utf-8 -*-
# ============================================
# homework09.py · 把 manager.py 吃透（阅读 + 改造）
# 运行方法：cd day09 再 python homework09.py
# ============================================
"""TODO 1 自问自答（读懂 manager.py 再看实现）：
(1) save(contacts) 在“加 / 删 / 改”三处调用：改完立刻存盘，
    进程意外退出也不丢数据。
(2) del contacts[name]：删掉字典里该键的一整对键值对。
(3) input(...).strip()：去掉首尾空白，防止“小红 ”查不到“小红”。
"""

import datetime
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_PATH = os.path.join(BASE_DIR, "contacts.json")
OPT_LOG_PATH = os.path.join(BASE_DIR, "opt_log.txt")


def load():
    """读档：没文件就从空字典开始"""
    try:
        with open(CONTACTS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(contacts):
    """存盘：每次改完立刻调用"""
    with open(CONTACTS_PATH, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def log_operation(action):
    """往 opt_log.txt 追加一行操作记录"""
    today = datetime.date.today()
    with open(OPT_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{today} {action}\n")


def find_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "查无此人"


def is_valid_phone(phone):
    """电话必须全是数字"""
    return phone.isdigit()


def show_menu():
    print("=" * 30)
    print("1.看全部  2.查  3.加  4.删  5.改  6.统计  q.退出")
    print("=" * 30)


def add_contact(contacts):
    name = input("名字：").strip()
    phone = input("电话：").strip()
    if not is_valid_phone(phone):
        print("电话只能是数字！")
        return
    contacts[name] = phone
    save(contacts)
    log_operation(f"加 {name} {phone}")
    print(f"已添加 {name}")


def delete_contact(contacts):
    name = input("删谁：").strip()
    if name not in contacts:
        print("查无此人")
        return
    phone = contacts[name]
    del contacts[name]
    save(contacts)
    log_operation(f"删 {name} {phone}")
    print(f"已删除 {name}")


def update_contact(contacts):
    name = input("改谁的电话：").strip()
    if name not in contacts:
        print("查无此人")
        return
    old_phone = contacts[name]
    new_phone = input("新电话：").strip()
    if not is_valid_phone(new_phone):
        print("电话只能是数字！")
        return
    contacts[name] = new_phone
    save(contacts)
    log_operation(f"改 {name} {old_phone}->{new_phone}")
    print(f"已修改 {name}")


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
            who = input("请输入查询姓名：").strip()
            print(f"{who}：{find_phone(contacts, who)}")
        elif choose == "3":
            add_contact(contacts)
        elif choose == "4":
            delete_contact(contacts)
        elif choose == "5":
            update_contact(contacts)
        elif choose == "6":
            print(f"共有 {len(contacts)} 位联系人")
        else:
            print("只能选 1/2/3/4/5/6/q，请重选！")


if __name__ == "__main__":
    main()

# 笔记
# 1. 先 import + 定好路径常量，后面所有函数共用
# 2. load / save / find_phone 先打包好，main 只负责串流程
# 3. 加/删/改各抽成一个函数：校验电话、存盘、写日志都在里面
# 4. 日志三处原来一模一样，抽成 log_operation(action) 消灭重复
# 5. .strip() 去首尾空格；.isdigit() 拦下非数字电话
# 6. del 字典[键] 删一整对；items() 遍历全部键值对
