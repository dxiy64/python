# -*- coding: utf-8 -*-
# ============================================
# contactbook.py · 工具箱（只有类，没有任何菜单）
# 这个文件两种用法：
#   1) 别人 import 它借 ContactBook（这时它一句废话都不说）
#   2) 自己跑 python contactbook.py 做自测（闸门里面那段）
# ============================================
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "contacts14.json")


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


# 闸门：只有自己跑 python contactbook.py 时才做自测
if __name__ == "__main__":
    if os.path.exists(PATH):      # 自测从空本子开始
        os.remove(PATH)
    print("【contactbook.py 自测】")
    book = ContactBook()
    book.add("光羽", "111")
    book.add("小明", "abc")     # 应该被拒绝
    print(book)                  # __str__
    print("人数：", len(book))    # __len__
    book.rename("光羽", "阿光")
    book.show_all()
