# -*- coding: utf-8 -*-
# ============================================
# big.py · 作业原料：一个"什么都在里面"的菜单版通讯录
# 运行方法：cd day14 再 python big.py
# 这个文件本身是好的、能跑——它只是太挤了（工具和菜单混在一起）
# 你的任务：把它拆成 hw_contactbook.py（工具箱）+ hw_main.py（入口）
# 详细要求和验收清单见 homework14.md
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts14_big.json")


# ---------- 工具箱部分：应该搬到 hw_contactbook.py ----------
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


# ---------- 入口部分：应该搬到 hw_main.py ----------
def show_menu():
    print("=" * 34)
    print("1.看全部 2.查 3.加 4.删 5.改电话 6.改名 7.模糊搜 q.退出")
    print("=" * 34)


def main():
    book = ContactBook()
    print(book)
    while True:
        show_menu()
        choose = input("选：").strip()
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
            if not name:
                print("名字不能为空！")
                continue
            book.add(name, input("电话：").strip())
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


if __name__ == "__main__":
    if os.path.exists(PATH):
        os.remove(PATH)
    main()
