# -*- coding: utf-8 -*-
# ============================================
# bad_tool.py · 反面教材：一个"没闸门"的工具箱
# 别学它！它的存在只是为了让你看到 import 的副作用
# ============================================
import json
import os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bad_demo.json")


class SimpleBook:
    def __init__(self):
        self.contacts = {}


# ↓↓↓ 下面这些是"演示代码"，但它没被闸门包住 ↓↓↓
print("[bad_tool] 我一被装载就开演了：")
print("[bad_tool] 清空重来！")
if os.path.exists(PATH):
    os.remove(PATH)
print("[bad_tool] 演示结束，轮到别人用我了")
# ↑↑↑ 谁 import 它，谁就得先看完这一段（甚至被删文件） ↑↑↑
