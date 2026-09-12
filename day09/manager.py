# -*- coding: utf-8 -*-
# ============================================
# Day 09 · 毕业项目①：通讯录管理系统
# 运行方法：cd day09 再 python manager.py
# 用到的全是老朋友：while菜单 + 字典 + 函数 + JSON存盘 + try
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts.json")  # 文件永远跟代码放一起（Day7 踩过的坑）


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
    print("1.看全部  2.查  3.加  4.删  5.改  q.退出")
    print("=" * 30)


def find_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "查无此人"


def main():
    contacts = load()
    print(f"载入 {len(contacts)} 位联系人")
    while True:
        show_menu()
        choose = input("选：").strip()
        if choose == "q":
            print("再见！")
            break
        elif choose == "1":
            if not contacts:
                print("空的，先加一个吧")
            for name, phone in contacts.items():
                print(f"{name}：{phone}")
        elif choose == "2":
            who = input("查谁：")
            print(f"{who}：{find_phone(contacts, who)}")
        elif choose == "3":
            name = input("名字：")
            phone = input("电话：")
            contacts[name] = phone
            save(contacts)  # 每次改完立刻存盘！
            print(f"已加上 {name}")
        elif choose == "4":
            name = input("删谁：")
            if name in contacts:
                del contacts[name]  # del 删一对
                save(contacts)
                print(f"已删除 {name}")
            else:
                print("查无此人")
        elif choose == "5":
            name = input("改谁的电话：")
            if name in contacts:
                contacts[name] = input("新电话：")
                save(contacts)
                print(f"{name} 已更新")
            else:
                print("查无此人")
        else:
            print("只能选 1/2/3/4/5/q，重选！")


if __name__ == "__main__":
    main()
