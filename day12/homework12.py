# -*- coding: utf-8 -*-
# ============================================
# homework12.py · 给菜单版通讯录加装备（读懂+改，工程师的日常）
# 运行方法：cd day12 再 python homework12.py（交互程序，键盘选功能）
# 这个文件直接运行不会报错，但 TODO 的功能是缺的——补完再运行验证
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts12_hw.json")


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


def show_menu():
    print("=" * 30)
    print("1.看全部  2.精确查  3.加  4.删 5.改电话 6.改名字 7.模糊搜  8.看人数  q.退出")
    print("=" * 30)


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
            # TODO 2（必做）: 名字为空（直接回车）时打印“名字不能为空！”并
            #   跳过本次（提示：if not name: + continue，continue 回循环开头）。
            name = input("名字：").strip()
            if not name:
                print("名字不能为空！")
                continue
            phone = input("电话：").strip()
            book.add(name, phone)
        elif choose == "4":
            book.delete(input("删谁：").strip())
        elif choose == "5":
            name = input("改谁：").strip()
            book.update(name, input("新电话：").strip())
        elif choose == "6":
            old = input("原名字：").strip()
            book.rename(old, input("新名字：").strip())

        # TODO 1（必做）: 补 7 分支——模糊搜：问关键字，调 book.search()。
        #   提示：照抄 day12.py 里 choose == "7" 那两行。
        # TODO 3（进阶选做）: 补 8 分支——看人数：打印 f"共 {len(book)} 人"。
        #   提示：len(book) 会自动找 __len__，day11 第 ② 节的老朋友。
        elif choose == "7":
            book.search(input("关键字：").strip())
        elif choose == "8":
            print(f"共 {len(book)} 人")
        else:
            print("只能选 1/2/3/4/5/6/7/8/q，重选！")


if __name__ == "__main__":
    if os.path.exists(PATH):
        os.remove(PATH)
    main()

# 笔记
# 1. 通讯录类，保存到文件，文件路径在类里，文件内容是字典，字典里是名字和电话
# 2. 把编写的工具放在类里，后面直接调用类的方法即可，写法是：类名.方法名
# 3. 类里要有 __str__ 方法，这样 print(类名) 就会调用这个方法，返回字符串
# 4. 类里要有 __len__ 方法，这样 len(类名) 就会调用这个方法，返回数字
# 5. 类里要有 load 方法，从文件里读取内容，返回字典
