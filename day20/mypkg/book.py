import json
import re
import csv
import logging

from pathlib import Path
from .storage import save, load, PATH, LOG_PATH, OUT
from datetime import datetime
from collections import Counter

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


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
            logging.info("添加失败: %s 已存在", name)
            return
        if not re.fullmatch(r"1[3-9]\d{9}", phone):
            print("手机号格式不正确")
            logging.info("添加失败: %s 手机号格式错误", phone)
            return
        self.contacts[name] = phone
        print(f"{name}添加成功")
        self.save()
        logging.info("添加: %s -> %s", name, phone)

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name}删除成功")
            self.save()
            logging.info("删除: %s ", name)
        else:
            print("该联系人不存在")
            logging.info(
                "删除失败: %s 不存在",
                name,
            )

    def update(self, name, phone):
        if not re.fullmatch(r"1[3-9]\d{9}", phone):
            print("手机号格式不正确")
            logging.info("更新失败: %s 手机号格式错误", phone)
            return
        if name not in self.contacts:
            print("该联系人不存在")
            logging.info("更新失败: %s 联系人不存在", name)
            return
        self.contacts[name] = phone
        print(f"{name}更新成功")
        self.save()
        logging.info("更新: %s -> %s", name, phone)

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

    def stats(self):
        if not self.contacts:
            print("通讯录是空的")
            return
        groups = Counter(name[0] for name in self.contacts)
        print("按名字首字统计：")
        for key, n in groups.most_common():
            print(f"  {key}：{n}人")

    def export(self):
        now = datetime.now()
        path = OUT / f"通讯录_{now:%Y%m%d_%H%M%S}.csv"
        with path.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["姓名", "电话"])
            writer.writeheader()
            for name, phone in self.contacts.items():
                writer.writerow({"姓名": name, "电话": phone})


class Contact:
    """单个联系人：姓名 + 电话"""

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"


class VipContact(Contact):  # ← 括号里写父类 = 我继承你
    """VIP 联系人：比普通联系人多一个备注"""

    def __init__(self, name, phone, note):  # ← 比父类多一个参数
        super().__init__(name, phone)  # ← 爸爸负责 name/phone（任务书点名提醒的那句）
        self.note = note  # ← 儿子只负责多出来的备注

    def __str__(self):  # ← 覆盖父类的打印格式
        return f"[VIP] {super().__str__()}（备注：{self.note}）"
        # ↑ 连爸爸的 __str__ 也借来用，不重造轮子
