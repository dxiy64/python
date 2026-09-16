# -*- coding: utf-8 -*-
# ============================================
# mybook/book.py · 通讯录本体（业务逻辑）
# 它不直接读写文件，而是叫 storage 帮忙——这叫"分层"
# ============================================
from .storage import load, save, PATH   # ← 相对导入：.storage 就是"同一个包里的 storage"


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = load(self.path)      # 借 storage 的手读档

    def __str__(self):
        return f"通讯录（{len(self.contacts)}人）：{self.contacts}"

    def __len__(self):
        return len(self.contacts)

    def add(self, name, phone):
        if not phone.isdigit():
            print("电话只能是数字！")
            return False
        self.contacts[name] = phone
        save(self.contacts, self.path)       # 借 storage 的手存盘
        print(f"已加上 {name}")
        return True

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            save(self.contacts, self.path)
            print(f"已删除 {name}")
            return True
        print("查无此人")
        return False

    def update(self, name, phone):
        if name not in self.contacts:
            print("查无此人")
            return False
        if not phone.isdigit():
            print("电话只能是数字！")
            return False
        self.contacts[name] = phone
        save(self.contacts, self.path)
        print(f"{name} 已更新")
        return True

    def rename(self, old, new):
        if old not in self.contacts:
            print("查无此人")
            return False
        if new in self.contacts:
            print(f"{new} 已存在，换个名字吧")
            return False
        self.contacts[new] = self.contacts[old]
        del self.contacts[old]
        save(self.contacts, self.path)
        print(f"已改名 {old} -> {new}")
        return True

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
        return found

    def show_all(self):
        if not self.contacts:
            print("空的，先加一个吧")
            return
        for name, phone in self.contacts.items():
            print(f"{name}：{phone}")
