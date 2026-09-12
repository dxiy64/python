# -*- coding: utf-8 -*-
# ============================================
# Day 02 · 条件判断与循环 —— 让程序学会"思考"和"重复"
# 运行方法：python day02\day02.py
# ============================================

# ① 昨天挑战的答案：int() 类型转换
# input() 返回的永远是字符串，"24" + 10 会报错
# 用 int() 把字符串变成整数，就能做数学了
print(int("24") + 10)        # 输出 34，不再是报错！

# ② 比较运算：结果只有两种 True（真）/ False（假）
print(10 > 3)       # True
print(3 == 10)      # False  注意：== 是"比较"，= 是"赋值"，千万别混！
print("a" == "a")   # True

# ③ if / elif / else：程序的分岔路口
# ⚠️ Python 靠【缩进】（行首的4个空格）识别哪些代码属于 if
temperature = 31

if temperature >= 35:
    print("高温预警！别出门")
elif temperature >= 28:
    print("有点热，注意防晒")
else:
    print("天气不错")

# 只有 temperature >= 35 不成立、>= 28 成立，所以打印第二句
# 自行实验：把 temperature 改成 36 或 10，看输出怎么变

# ④ while 循环：让代码重复执行，直到条件不成立
count = 1
while count <= 5:            # 条件为 True 就一直循环
    print(f"这是第 {count} 次循环")
    count = count + 1        # 忘了这句会怎样？程序永远停不下来（试试就逝世）

print("循环结束")

# ⑤ break：立即跳出循环
number = 0
while True:                  # 死循环：条件永远成立
    number = number + 1
    if number == 3:
        print("数到 3 了，跑！")
        break                # 无视一切，直接退出整个 while
print(f"break 之后 number = {number}")
