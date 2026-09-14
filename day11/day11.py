# -*- coding: utf-8 -*-
# ============================================
# Day 11 · 面向对象②：好看的长相 + 改电话 + 改名字
# 运行方法：cd day11 再 python day11.py
# 今天不装新库。核心三句话：
#   print(对象) 会自动找 __str__；len(对象) 会自动找 __len__；
#   字典的键不能改名，只能“搬家”（拷到新键，再删旧键）
# ============================================

# ① 默认长相：不教它，它只会报地址（Day10 踩过的坑）
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Dog("小黑", 3)
print(a)            # <__main__.Dog object at 0x...>：类型 + 地址，不是数据
print(a.__dict__)   # 口袋里明明有数据，它就是不显示

print("=" * 30)

# ② __str__ / __len__：教通讯录好看的长相 + 直接数人数
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts11.json")


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = self.load()

    def __str__(self):   # 双下划线是 Python 点名的：print(book) 时自动调，不用手动调
        return f"通讯录（{len(self.contacts)}人）：{self.contacts}"

    def __len__(self):   # 同理：len(book) 时自动调，不用写 len(book.contacts)
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
        if not phone.isdigit():   # Day10 的老规矩：电话只能是数字
            print("电话只能是数字！")
            return
        self.contacts[name] = phone
        self.save()
        print(f"已加上 {name}")

    # ③ update：改电话。键不动，只盖值
    def update(self, name, phone):
        if name not in self.contacts:
            print("查无此人")
            return
        if not phone.isdigit():
            print("电话只能是数字！")
            return
        self.contacts[name] = phone   # 键还在，值盖掉
        self.save()
        print(f"{name} 已更新")

    # ④ rename：改名字。键不能改，只能搬家：拷到新键，再删旧键
    def rename(self, old, new):
        if old not in self.contacts:
            print("查无此人")
            return
        if new in self.contacts:
            print(f"{new} 已存在，换个名字吧")
            return
        self.contacts[new] = self.contacts[old]   # 1. 拷一份到新键
        del self.contacts[old]                     # 2. 删掉旧键
        self.save()
        print(f"已改名 {old} -> {new}")


# ⑤ 跑一遍（包在 __main__ 里：直接跑才演示，被导入只借类，不删数据）
if __name__ == "__main__":
    if os.path.exists(PATH):   # 保证演示每次从空开始，可重复运行
        os.remove(PATH)
    book = ContactBook()
    book.add("光羽", "111")
    book.add("小明", "222")
    print(book)               # 通讯录（2人）：{...}
    print("人数：", len(book))  # 2，不用写 len(book.contacts)
    book.update("小明", "abc")   # 拒绝：电话不是数字
    book.update("小明", "333")   # 成功
    book.rename("小明", "大明")  # 搬家成功
    book.rename("阿鬼", "大鬼")  # 拒绝：查无此人
    print(book)
