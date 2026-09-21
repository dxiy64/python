import os
import sys
import re
import json

from pathlib import Path

HERE = Path(__file__).parent
PATH = HERE / "contacts.json"


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = self.load()

    def __str__(self):
        return f"当前通讯录总人数：{len(self.contacts)}人"

    def __len__(self):
        return len(self.contacts)

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                contacts = json.load(f)
        except FileNotFoundError:
            return {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=4)

    def add(self, name, phone):
        if not name:
            print("姓名不能为空")
            return
        if name in self.contacts:
            print("该联系人已存在")
            return
        if re.fullmatch(r"1[3-9]\d{9}", phone):
            print("手机号格式不正确")
            return
        self.contacts[name] = phone
        print(f"{name+phone}添加成功")
        self.save()

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name}删除成功")
            self.save()
        else:
            print("该联系人不存在")

    def update(self, name, phone):
        if not re.fullmatch(r"1[3-9]\d{9}", phone):
            print("手机号格式不正确")
            return
        if name not in self.contacts:
            print("该联系人不存在")
            return
        self.contacts[name] = phone
        print(f"{name}更新成功")
        self.save()

    def find(self, name):
        if name in self.contacts:
            print(f"{name}的号码是：{self.contacts[name]}")
        else:
            print("该联系人不存在")

    def search(self, keyword):
        for name, phone in self.contacts.items():
            if keyword in name:
                print(f"{name}的号码是：{phone}")
            else:
                print("没有找到该联系人")

    def rename(self, old, new):
        if new in self.contacts:
            print("该联系人已存在")
            return
        if old in self.contacts:
            self.contacts[new] = self.contacts.pop(old)
        del self.contacts[old]
        print(f"{old}重命名为{new}成功")
        self.save()

    def show_all(self):
        for name, phone in self.contacts.items():
            print(f"{name}的号码是：{phone}")
