# -*- coding: utf-8 -*-
# ============================================
# pdb_demo.py · 断点调试演示（Day19 演示 4 的素材）
# 两种玩法：
#   ① 交互式（推荐）：cd day19 然后 python pdb_demo.py
#      程序会在 breakpoint() 那行停下来，进入 (Pdb) 提示符，
#      输入 p total 回车看变量、n 回车走一步、c 回车放行到底
#   ② 非交互（把命令喂给它）：
#      printf 'p total\nn\np total\nc\n' | python pdb_demo.py
# ============================================


def total_price(prices):
    total = 0
    for p in prices:
        breakpoint()             # ← 程序会从这里开始暂停，等你敲命令
        total = total + p
    return total


if __name__ == "__main__":
    prices = [12, 30, 8]
    print("总价：", total_price(prices))
