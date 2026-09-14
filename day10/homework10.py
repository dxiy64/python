# -*- coding: utf-8 -*-
# ============================================
# homework10.py · 给 ContactBook 加装备（读懂+改，工程师的日常）
# 运行方法：cd day10 再 python homework10.py
# 这个文件直接运行不会报错，但 TODO 的功能是缺的——补完再运行验证
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts10_hw.json")


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
        # TODO 2（必做）: 在这里加电话校验——如果 phone 不是全数字，
        #   打印"电话只能是数字！"并 return（不存盘）。
        #   提示：字符串有个 .isdigit() 方法（homework09 TODO 3 的老朋友）。
        if not phone.isdigit():
            print("电话只能是数字！")
            return
        self.contacts[name] = phone
        self.save()
        print(f"已加上 {name}")

    def count(self):
        # TODO 1（必做）: 返回共有几位联系人。
        #   现在 return 0 是占位的，改成对的那一行（提示：len，Day3 老朋友）。
        return len(self.contacts)

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return "查无此人"

    # TODO 3（进阶选做）: 加一个 search(keyword) 方法，模糊查找——
    #   把名字里包含 keyword 的联系人全部打印出来。
    #   提示：for name, phone in self.contacts.items(): + if keyword in name
    def search(self, keyword):
        found = False
        for name, phone in self.contacts.items():
            if keyword in name:
                print(f"{name} {phone}")
                found = True
        if not found:
            print("查无此人")


if __name__ == "__main__":
    if os.path.exists(PATH):
        os.remove(PATH)
    book = ContactBook()
    book.add("光羽", "18486311094")
    book.add("小明", "abc")  # TODO 2 做完后，这一行应该被拒绝、不存盘
    # TODO 1 做完后，下一行应该打印出正确的数字：
    print(f"共有 {book.count()} 位联系人")
    print("查小明：", book.find("小明"))
    # TODO 3 做完后，取消下面这行的注释验证：
    book.search("光")


# 笔记
# 1. json.dump() 保存文件时，ensure_ascii=False 可以让中文字符正常保存。
# 2. json.dump() 保存文件时，indent=2 可以让文件更易读。他的意思是缩进 2 个空格。
# 3. os.path.abspath(__file__) 获取当前文件的绝对路径。
# 4. os.path.dirname(path) 获取 path 的目录名。
# 5. class 的作用是定义一个类，类可以包含多个方法。写法是 class 类名:，方法写法是 def 方法名(self, 参数1, 参数2):。
# 6. self 是一个特殊的参数，表示当前对象。在类的方法中，self 必须是第一个参数。
# 7. 模糊查找的关键字是 in，比如 "光" in "光羽" 返回 True，"光" in "小明" 返回 False。
