# -*- coding: utf-8 -*-
# ============================================
# homework07.py · 通讯录存档版（JSON）
# 运行方法：cd day07 再 python homework07.py
# 本课只学：json.dump / load + try 读档
# ============================================

import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """启动读档：有文件就装进来，没有就从空字典开始"""
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    """改完立刻存盘：字典 → 文件里的文字"""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)


def find_phone(contacts, name):
    """查电话：沿用 Day04 的思路，查不到返回“查无此人”"""
    if name in contacts:
        return contacts[name]
    return "查无此人"


def main():
    contacts = load_contacts()
    print(f"上次共有 {len(contacts)} 位联系人")

    name = input("请输入联系人姓名：").strip()
    phone = input("请输入联系人电话：").strip()
    contacts[name] = phone
    save_contacts(contacts)

    while True:
        keyword = input("要查谁？（输入 q 退出）：").strip()
        if keyword == "q":
            print("已退出查询，再见！")
            break
        print(f"{keyword} 查询结果：{find_phone(contacts, keyword)}")


if __name__ == "__main__":
    main()

# 笔记
# 1. json.dump(字典, 文件)：倒出去存盘；json.load(文件)：装进来变回字典
# 2. ensure_ascii=False：中文直接存中文，不变成 \u 转义
# 3. try/except FileNotFoundError：第一次运行没文件也不崩
# 4. JSON 读回来直接是字典；纯文本读回来是字符串，还得自己切
