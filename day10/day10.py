# -*- coding: utf-8 -*-
# ============================================
# Day 10 · 面向对象：把数据和函数装进同一个盒子
# 运行方法：cd day10 再 python day10.py
# 今天不装新库，全是语法。学完你能把 manager.py 的函数全部装进类
# ============================================

# ① 先看痛点（回想 day09/manager.py）
#    contacts 这个字典，被 load/save/增删改查 5 个函数传来传去。
#    数据（字典）和操作（函数）是分家的：每次调用都得把 contacts 递过去，
#    哪次忘了递、递错了，就崩。类要解决的就是这个。

# ② 类是图纸，对象是造出来的东西
class Dog:
    def __init__(self, name):
        self.name = name    # self 就是"我这个对象自己"，name 存进自己的口袋

    def bark(self):         # 方法 = 写在类里的函数，第一个参数必须是 self
        print(f"{self.name}：汪！")   # 调用时不用传 self，Python 自动把"我"递进去

a = Dog("旺财")   # 照图纸造出一个对象
b = Dog("来福")   # 再造一个，口袋互相独立
a.bark()
b.bark()
print(a.name, "和", b.name, "的口袋是分开的")

print("=" * 30)

# ③ self 口袋实验：改一个，另一个不受影响
a.name = "旺财·改名版"
print(a.name)   # 变了
print(b.name)   # 没变！每个对象有自己的 self 口袋

print("=" * 30)

# ④ 实战：把通讯录装进类（对照着看 day09/manager.py，功能一模一样）
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts10.json")  # 新文件，别污染 day09 的 contacts.json


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path              # 每个通讯录记住自己的文件位置
        self.contacts = self.load()   # 开机就读档，口袋里直接有数据

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
        self.contacts[name] = phone   # 注意：再也不用传 contacts 了，它在 self 口袋里
        self.save()                   # 改完立刻存盘（day09 的规矩保留）
        print(f"已加上 {name}")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save()
            print(f"已删除 {name}")
        else:
            print("查无此人")

    def update(self, name, phone):
        if name in self.contacts:
            self.contacts[name] = phone
            self.save()
            print(f"{name} 已更新")
        else:
            print("查无此人")

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return "查无此人"

    def show_all(self):
        if not self.contacts:
            print("空的，先加一个吧")
        for name, phone in self.contacts.items():
            print(f"{name}：{phone}")


# ⑤ 跑一遍：和 manager 菜单里 1/2/3/4/5 干的事一样，只是换成了"对象.方法"
def main():
    if os.path.exists(PATH):   # 保证演示每次从空开始，可重复运行
        os.remove(PATH)

    book = ContactBook()
    print(f"载入 {len(book.contacts)} 位联系人")
    book.add("光羽", "18486311094")
    book.add("小明", "13800001111")
    print("查光羽：", book.find("光羽"))
    book.update("小明", "13900002222")
    book.delete("光羽")
    print("--- 全部 ---")
    book.show_all()


if __name__ == "__main__":
    main()

print("=" * 30)
# ⑥ 一句话总结：类 = 数据 + 操作打包带走。
#    以后凡是看到"一堆函数围着一个字典/列表转"（比如 manager.py），
#    就把字典装进 self，把函数变成方法。Day11 我们用类重写完整菜单版 manager。
