# -*- coding: utf-8 -*-
# ============================================
# homework11.py · 通讯录再升级（读懂+改，工程师的日常）
# 运行方法：cd day11 再 python homework11.py
# 这个文件直接运行不会报错，但 TODO 的功能是缺的——补完再运行验证
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts11_hw.json")


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = self.load()

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

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return "查无此人"

    def show_all(self):
        if not self.contacts:
            print("空的，先加一个吧")
        for name, phone in self.contacts.items():
            print(f"{name}：{phone}")

    # TODO 1（必做）: 教通讯录好看的长相——print(book) 要显示出人数和名单，
    #   比如：通讯录（2人）：{'光羽': '111', ...}。
    #   提示：day11.py 第 ② 节，f-string + len(self.contacts) + self.contacts。
    def __str__(self):
        return f"当前通讯录人数为：{len(self.contacts)}，通讯录内容为：{self.contacts}"

    # TODO 2（必做）: 改电话 update(name, phone)——
    #   名字不存在打印“查无此人”并 return；
    #   电话不是全数字打印“电话只能是数字！”并 return；
    #   都通过才盖值 + 存盘 + 打印“XXX 已更新”。
    #   提示：day11.py 第 ③ 节。
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

    # TODO 3（进阶选做）: 改名字 rename(old, new)——
    #   旧名不存在打印“查无此人”并 return；
    #   新名已存在打印“XXX 已存在，换个名字吧”并 return；
    #   都通过才搬家（拷到新键，再删旧键）+ 存盘 + 打印“已改名”。
    #   提示：day11.py 第 ④ 节，字典的键不能直接改。
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
        print("已改名")


if __name__ == "__main__":
    if os.path.exists(PATH):
        os.remove(PATH)
    book = ContactBook()
    book.add("光羽", "111")
    book.add("小明", "222")
    # TODO 1 做完后，下一行应该显示人数和名单，而不是“占位”：
    print(book)
    # TODO 2 做完后，小明变 333，abc 那次被拒绝：
    book.update("小明", "abc")
    book.update("小明", "333")
    # TODO 3 做完后，小明搬家成大明，阿鬼那次被拒绝：
    book.rename("小明", "大明")
    book.rename("阿鬼", "大鬼")
    print("--- 全部 ---")
    book.show_all()

# 笔记
# 1. 双下划线是魔术方法，__str__ 是 print 的默认方法，不用写 print(book) 也能显示通讯录。
# 2. 字典的值可以改，键不能直接改，他们长这样：{'光羽': '111', '小明': '222'}。前面的键是名字，后面的值是电话。
# 3. 键可以通过 del 删除，但是不能直接改，改键需要拷贝到新键，再删除旧键。
# 4. 字典的键不能重复，重复会覆盖。
