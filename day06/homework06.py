# -*- coding: utf-8 -*-
# ============================================
# homework06.py · 给猜数字游戏穿防弹衣
# 运行方法：cd day06 再 python homework06.py
# 本课只学：try / except + continue / break
# ============================================

import random

ACCOUNT_FILE = "account.txt"


def play_guessing_game():
    """猜数字：敲错字母不崩、不计数，重猜即可"""
    secret = random.randint(1, 100)
    count = 0

    while True:
        try:
            guess = int(input("请猜一个数字（1~100）："))
        except ValueError:
            print("只能输数字，重猜！")
            continue
        count += 1
        if guess > secret:
            print("大了，再猜")
        elif guess < secret:
            print("小了，再猜")
        else:
            print(f"恭喜！猜了 {count} 次命中 🎉")
            break


def show_ledger():
    """读账本：文件不存在也不崩，提示先记第一笔"""
    try:
        with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
            print(f.read(), end="")
    except FileNotFoundError:
        print("记账本不存在，先去记第一笔账吧")


def add_record():
    """记一笔：只有选 y 才问明细、才写文件"""
    while True:
        choose = input("要记账吗？（y/n）：").strip()
        if choose == "n":
            print("已退出记账，再见！")
            return
        if choose == "y":
            break
        print("只能输入 y 或 n，重选！")

    what = input("买了什么：").strip()
    money = input("花了多少钱：").strip()
    with open(ACCOUNT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{what} -{money}元\n")
    print("已记入账本！")


def main():
    play_guessing_game()
    show_ledger()
    add_record()


if __name__ == "__main__":
    main()

# 笔记
# 1. try/except：把可能翻车的一句包起来，翻了走 except，不崩
# 2. ValueError：int("abc") 这类转不成的错
# 3. FileNotFoundError：open 去读一个不存在的文件
# 4. continue：跳过本轮剩下的，直接下一轮（敲错不计数就靠它）
# 5. 缩进即逻辑：记账的 input 必须缩进到选了 y 的分支里，否则选 n 也会执行
# 6. 原稿里“读账本 + 记账”写了两遍，这里合并成一份：修 bug 先去重
