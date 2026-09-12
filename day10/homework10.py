# -*- coding: utf-8 -*-
# ============================================
# homework10.py · 给 ContactBook 加装备
# 运行方法：cd day10 再 python homework10.py
# 本课只学：class / __init__ / self / 方法
# ============================================

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE_DIR, "contacts10_hw.json")


class ContactBook:
    """通讯录：数据装进 self.contacts，操作变成方法"""

    def __init__(self, path=PATH):
        self.path = path
        self.contacts = self.load()  # 开机读档，口袋里直接有数据

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
        """加人：电话非数字直接拒绝，不存盘"""
        if not phone.isdigit():
            print("电话只能是数字！")
            return False
        self.contacts[name] = phone
        self.save()  # 改完立刻存盘（Day09 的规矩保留）
        print(f"已加上 {name}")
        return True

    def count(self):
        """共有几位联系人"""
        return len(self.contacts)

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return "查无此人"

    def search(self, keyword):
        """模糊查找：名字里包含关键字的全部打印"""
        found = False
        for name, phone in self.contacts.items():
            if keyword in name:
                print(f"{name}：{phone}")
                found = True
        if not found:
            print("没有匹配的联系人")


def main():
    if os.path.exists(PATH):
        os.remove(PATH)  # 保证演示从空开始，可重复运行
    book = ContactBook()
    book.add("光羽", "18486311094")
    book.add("小明", "abc")  # 非数字：被拒绝、不存盘
    print(f"共有 {book.count()} 位联系人")
    print("查小明：", book.find("小明"))
    book.search("光")


if __name__ == "__main__":
    main()

# 笔记
# 1. 类 = 数据 + 操作打包：字典住进 self，函数变成方法
# 2. 方法第一个参数必须是 self，调用时不用传，Python 自动递“我”
# 3. 改完调 self.save()：和 manager.py 每次改完存盘同一条规矩
# 4. add 返回 True/False：调用方能知道这次到底存上没有
