# -*- coding: utf-8 -*-
# ============================================
# homework06.py · 给猜数字游戏穿防弹衣
# ============================================
import random

secret = random.randint(1, 100)
count = 0

# TODO 1: 把 int(input(...)) 包进 try/except ValueError，
#         敲错（比如 abc）时打印 "只能输数字，重猜！" 并 continue，不计数
# while True:
#     try:
#         guess = int(input("请猜一个数字（1~100）："))
#     except ValueError:
#         print(???)
#         continue
#     count = count + 1
#     ...（三分支判断照抄 Day2，注意 count 只在成功拿到数字后才 +1）

while True:
    try:
        guess = int(input("请猜一个数字（1~100）："))
    except ValueError:
        print("只能输数字，重猜！")
        continue
    count = count + 1
    if guess > secret:
        print("大了，再猜")
    elif guess < secret:
        print("小了，再猜")
    else:
        print(f"恭喜！猜了 {count} 次命中 🎉")
        break


# TODO 2 (进阶选做): 程序启动时如果 account.txt 不存在会崩，
#   参考 day06.py 第③段，给记账本的读取加上 try/except FileNotFoundError

try:
    with open("account.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("记账本不存在，先去记第一笔账吧")

while True:
    choose = input("要记账吗？（y/n）：")
    if choose == "n":
        print("已退出记账，再见！")
        break
    elif choose == "y":
        break

what = input("买了什么：")
money = input("花了多少钱：")
with open("account.txt", "a", encoding="utf-8") as f:
    f.write(f"{what} -{money}元\n")
print("已记入账本！")


# ↑有问题输入n不退出，原因是下面的what和money没有缩进到elif choose == "y":里面，导致不管输入什么都会执行这两行代码。
# 修改如下⬇
try:
    with open("account.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("记账本不存在，先去记第一笔账吧")

while True:
    choose = input("要记账吗？（y/n）：")
    if choose == "n":
        print("已退出记账，再见！")
        break
    elif choose == "y":
        what = input("买了什么：")
        money = input("花了多少钱：")
        with open("account.txt", "a", encoding="utf-8") as f:
            f.write(f"{what} -{money}元\n")
        print("已记入账本！")
        break
    else:
        print("只能输入 y 或 n，重选！")

# 笔记：
# 1. try/except 语句的作用是捕获异常，防止程序崩溃。在使用 try/except 时，应该尽量只捕获可能发生的异常类型，避免捕获过多异常导致调试困难。
# 2. FileNotFoundError 是文件未找到异常，当尝试打开一个不存在的文件时会抛出该异常。
# 3. ValueError 是值错误异常，当尝试将一个无法转换为整数的字符串转换为整数时会抛出该异常。
# 4. Exception 是所有异常的基类，可以捕获所有类型的异常，但不建议滥用。
# 5. continue 语句用于跳过当前循环的剩余部分，直接进入下一次循环。
# 6. break 语句用于终止当前循环，跳出循环体。
# 7. 在使用 input() 函数获取用户输入时，应该对输入进行验证，确保输入符合预期格式，避免程序因输入不合法而崩溃。
# 8. 在使用文件操作时，应该使用 with 语句来确保文件在使用完毕后正确关闭，避免资源泄漏。
# 9. 在编写程序时，应该考虑用户可能的误操作，并通过异常处理和输入验证来提高程序的健壮性和用户体验。
# 10. 在编写循环时，应该注意循环的终止条件，避免出现无限循环的情况。
# 11. 在编写程序时，应该注意代码的缩进，确保代码块的逻辑正确，避免因缩进错误导致程序行为异常。
