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
        return f"通讯录：{self.contacts}"

    def __len__(self):
        return len(self.contacts)

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                contacts = json.load(f)
            return contacts
        except FileNotFoundError:
            return {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=2)

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
                break
        else:
            print("没有找到该联系人")

    def rename(self, old, new):
        if new in self.contacts:
            print("该联系人已存在")
            return
        if old in self.contacts:
            self.contacts[new] = self.contacts.pop(old)
        print(f"{old}重命名为{new}成功")
        self.save()

    def show_all(self):
        for name, phone in self.contacts.items():
            print(f"{name}的号码是：{phone}")


def show_menu():
    print("=" * 40)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 更新联系人")
    print("4. 查找联系人")
    print("5. 查找联系人(模糊查询)")
    print("6. 重命名联系人")
    print("7. 显示所有联系人")
    print("q. 退出")
    print("=" * 40)


def main():
    book = ContactBook()
    while True:
        show_menu()
        choose = input("请选择操作：").strip()
        if choose == "q":
            print("退出通讯录")
            break

        elif choose == "1":
            name = input("请输入姓名：").strip()
            phone = input("请输入手机号：").strip()
            book.add(name, phone)

        elif choose == "2":
            name = input("请输入姓名：").strip()
            book.delete(name)

        elif choose == "3":
            name = input("请输入需要更新的姓名：").strip()
            phone = input("请输入更新的手机号：").strip()
            book.update(name, phone)

        elif choose == "4":
            name = input("请输入查找的姓名：").strip()
            book.find(name)

        elif choose == "5":
            keyword = input("请输入查找的关键词：").strip()
            book.search(keyword)

        elif choose == "6":
            old = input("请输入要重命名的姓名：").strip()
            new = input("请输入新的姓名：").strip()
            book.rename(old, new)

        elif choose == "7":
            print("通讯录名单如下：")
            book.show_all()

        elif choose not in ["1", "2", "3", "4", "5", "6", "7", "q"]:
            print("输入有误，请重新输入")


if __name__ == "__main__":
    if not os.path.exists(PATH):
        with open(PATH, "w", encoding="utf-8") as f:
            f.write("{}")
    main()
