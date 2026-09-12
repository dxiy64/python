# -*- coding: utf-8 -*-
# ============================================
# homework02.py · 你的第一个游戏《猜数字》
# 注意：这个骨架直接运行会报错 expected an indented block
# 这是正常的——把下面的 TODO 全部补完再运行！
# 卡住了就把代码贴给老师，不许抄答案（也没有答案）
# ============================================

import random  # 导入随机模块，Python 自带的"骰子"

secret = random.randint(1, 100)  # 程序偷偷抽一个 1~100 的整数，存进 secret
count = 0  # 记录玩家猜了几次


while True:
    # TODO 1: 用 input() 让玩家输入猜测，记得用 int() 转成整数，存进变量 guess
    guess = int(input("请输入你猜的数字（1~100）："))
    # TODO 2: 每猜一次，count 加 1
    count = count + 1
    print(f"你已经猜了 {count} 次")

    # TODO 3: 用 if / elif / else 判断三种情况：
    #   guess 比 secret 大   -> print("大了，再猜")
    #   guess 比 secret 小   -> print("小了，再猜")
    #   否则（猜中了！）      -> print(f"恭喜！猜了 {count} 次命中 🎉")
    #                            并用 break 结束游戏
    if guess > secret:
        print("大了，再猜")
    elif guess < secret:
        print("小了，再猜")
    else:
        print(f"恭喜！猜了 {count} 次命中 🎉")
        break

# 笔记
# 1. random.randint(a, b) 会返回一个 a~b 的随机整数，包括 a 和 b
# 2. while True: 创建一个无限循环，直到遇到 break 语句
# 3. input() 会暂停程序，等待用户输入，返回值是字符串
# 4. int() 可以把字符串转换成整数，如果输入的不是数字会报错
# 5. f-string（f"..."）可以在字符串中嵌入变量，方便打印
# 6 if / elif / else 是条件判断语句，elif 是 else if 的缩写
# 7. count = count + 1 可以简写为 count += 1
# 8. 比较运算符有 >、<、==、!=、>=、<=，返回值是布尔值 True 或 False
# 9. break 会立即跳出当前循环，继续执行循环之后的代码
