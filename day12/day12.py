# -*- coding: utf-8 -*-
# ============================================
# Day 12 · 毕业项目②：通讯录菜单版（类 + 菜单 + main）
# 运行方法：cd day12 再 python day12.py（交互程序，键盘选功能）
# 全是老朋友：day09 的菜单 + day10/11 的 ContactBook，
# 区别：数据和操作住一起了，main 里再也不递 contacts
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts12.json")


# ① 类：day10/11 的完整版，直接搬过来
class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = self.load()

    def __str__(self):
        return f"通讯录（{len(self.contacts)}人）：{self.contacts}"

    def __len__(self):
        return len(self.contacts)

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=2)

    def add(self, name, phone):
        if not phone.isdigit():
            print("电话只能是数字！")
            return
        self.contacts[name] = phone
        self.save()
        print(f"已加上 {name}")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save()
            print(f"已删除 {name}")
        else:
            print("查无此人")

    def update(self, name, phone):
        if name not in self.contacts:
            print("查无此人")
            return
        if not phone.isdigit():
            print("电话只能是数字！")
            return
        self.contacts[name] = phone
        self.save()
        print(f"{name} 已更新")

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return "查无此人"

    def search(self, keyword):
        found = False
        for name, phone in self.contacts.items():
            if keyword in name:
                print(f"{name} {phone}")
                found = True
        if not found:
            print("查无此人")

    def show_all(self):
        if not self.contacts:
            print("空的，先加一个吧")
        for name, phone in self.contacts.items():
            print(f"{name}：{phone}")

    def rename(self, old, new):
        if old not in self.contacts:
            print("查无此人")
            return
        if new in self.contacts:
            print(f"{new} 已存在，换个名字吧")
            return
        self.contacts[new] = self.contacts[old]
        del self.contacts[old]
        self.save()
        print(f"已改名 {old} -> {new}")


# ② 菜单：只管打印，不管逻辑（day09 的老朋友）
def show_menu():
    print("=" * 30)
    print("1.看全部  2.精确查  3.加  4.删  5.改电话  6.改名  7.模糊搜  q.退出")
    print("=" * 30)


# ③ main：死循环 + 分支。每个分支三步：问 → 调对象的方法 → 方法里自己存盘
def main():
    book = ContactBook()
    print(book)   # 开机先报家门
    while True:
        show_menu()
        choose = input("选：").strip()   # strip 去掉首尾空格，防手滑
        if choose == "q":
            print(f"共 {len(book)} 人，再见！")
            break
        elif choose == "1":
            book.show_all()
        elif choose == "2":
            who = input("查谁：").strip()
            print(f"{who}：{book.find(who)}")
        elif choose == "3":
            name = input("名字：").strip()
            phone = input("电话：").strip()
            book.add(name, phone)
        elif choose == "4":
            book.delete(input("删谁：").strip())
        elif choose == "5":
            name = input("改谁的电话：").strip()
            book.update(name, input("新电话：").strip())
        elif choose == "6":
            old = input("旧名字：").strip()
            book.rename(old, input("新名字：").strip())
        elif choose == "7":
            book.search(input("关键字：").strip())
        else:
            print("只能选 1-7/q，重选！")


# ④ 入口：直接跑才进 main，被导入只借类
if __name__ == "__main__":
    if os.path.exists(PATH):   # 演示从空开始，可重复运行
        os.remove(PATH)
    main()
