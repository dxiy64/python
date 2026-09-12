# -*- coding: utf-8 -*-
# ============================================
# Day 06 · 异常处理 —— 程序不再一敲错就崩
# 运行方法：python day06\day06.py
# ============================================

# ① 没穿防弹衣：敲个 abc 直接崩
# guess = int(input("猜个数字："))   # 输入 abc → ValueError，程序结束

# ② 穿上 try/except：崩了也有人接住
try:
    n = int("abc")          # 故意翻一个翻不动的
    print(f"翻出来是 {n}")
except ValueError:
    print("只能输数字！这次不算")

print("程序还活着，继续跑")

# ③ 读不存在的文件：FileNotFoundError
try:
    with open("根本没有这个文件.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在，先去记第一笔账吧")

# ④ 抓错了类型就白穿：except 只接它认识的错
try:
    print(10 / 0)
except ValueError:          # 除零是 ZeroDivisionError，不是 ValueError，接不住！
    print("这行不会执行")
except ZeroDivisionError:   # 这样才接得住
    print("0 不能当除数！")

# ⑤ 万能兜底 Exception（先知道有这东西，少用）
try:
    print(int("abc") + 10 / 0)
except Exception as e:      # 什么错都接，还能看看错因
    print(f"出小差了：{e}")

# ⑥ 循环 + try：猜数字游戏再也不怕乱敲了
secret = 50
for raw in ["abc", "60", "50"]:
    try:
        guess = int(raw)
    except ValueError:
        print(f"输入 {raw!r} 不是数字，跳过这一轮")
        continue            # 跳过本轮，继续下一轮
    if guess > secret:
        print(f"{guess} 大了")
    elif guess < secret:
        print(f"{guess} 小了")
    else:
        print(f"{guess} 猜中！")
        break
