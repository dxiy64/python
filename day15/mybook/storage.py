# -*- coding: utf-8 -*-
# ============================================
# mybook/storage.py · 只管"存和读"，不认识通讯录
# 这一层只做一件事：把字典存进文件 / 从文件读出来
# ============================================
import json
import os

# __file__ = .../day15/mybook/storage.py
# 往上一层 dirname 得到 .../day15/mybook（包目录）
PKG_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PKG_DIR, "contacts15.json")


def load(path=PATH):
    """从文件读字典；文件不在就给空本子"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(contacts, path=PATH):
    """把字典写进文件（先清空再写全量）"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
