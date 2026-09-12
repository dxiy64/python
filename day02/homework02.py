# -*- coding: utf-8 -*-
# ============================================
# homework02.py · 猜数字游戏
# 运行方法：cd day02 再 python homework02.py
# 本课只学：if / while / break + int 类型转换
# ============================================

import random  # 自带“骰子”：用来抽一个随机整数

secret = random.randint(1, 100)  # 程序偷偷抽一个 1~100 的整数
guess_count = 0  # 玩家猜了几次


while True:
    guess = int(input("请输入你猜的数字（1~100）："))
    guess_count += 1
    print(f"你已经猜了 {guess_count} 次")

    if guess > secret:
        print("大了，再猜")
    elif guess < secret:
        print("小了，再猜")
    else:
        print(f"恭喜！猜了 {guess_count} 次命中 🎉")
        break

# 笔记
# 1. random.randint(a, b)：返回 a~b 的随机整数，含两端
# 2. while True：无限循环，遇到 break 才停
# 3. input() 返回字符串，int() 转成整数才能比大小
# 4. guess_count += 1 就是 guess_count = guess_count + 1 的简写
# 5. if / elif / else：大、小、猜中三选一
# 6. break：立即跳出当前循环
