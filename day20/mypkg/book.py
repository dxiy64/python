import json
import re

from pathlib import Path
from .storage import save, load, PATH


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = load(path)

    def __str__(self):
        名单 = "、".join(self.contacts)
        return f"当前通讯录总人数：{len(self.contacts)}人，名单：{名单}"

    def __len__(self):
        return len(self.contacts)

    def save(self):
        save(self.contacts, self.path)

    def add(self, name, phone):
        if not name:
            print("姓名不能为空")
            return
        if name in self.contacts:
            print("该联系人已存在")
            return
        if not re.fullmatch(r"1[3-9]\d{9}", phone):
            print("手机号格式不正确")
            return
        self.contacts[name] = phone
        print(f"{name}添加成功")
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
        found = False
        for name, phone in self.contacts.items():
            if keyword in name:
                print(f"{name}的号码是：{phone}")
                found = True
        if not found:
            print("没有找到该联系人")

    def rename(self, old, new):
        if new in self.contacts:
            print("该联系人已存在")
            return
        if old not in self.contacts:
            print("该联系人不存在")
            return
        self.contacts[new] = self.contacts.pop(old)
        print(f"{old}重命名为{new}成功")
        self.save()

    def show_all(self):
        if not self.contacts:
            print("通讯录是空的")
            return
        for name, phone in self.contacts.items():
            print(f"{name}的号码是：{phone}")
