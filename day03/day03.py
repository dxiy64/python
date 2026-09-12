# -*- coding: utf-8 -*-
# ============================================
# Day 03 · 列表与 for 循环 —— 装一筐东西，然后一个个处理
# 运行方法：python day03\day03.py
# ============================================

# ① 列表 list：用 [] 装一堆东西，逗号隔开
fruits = ["苹果", "香蕉", "橘子"]
print(fruits)  # 整个筐
print(len(fruits))  # 长度：有几样？ 3

# ② 索引：给每个位置编号，从 0 开始！
print(fruits[0])  # 第1个：苹果
print(fruits[1])  # 第2个：香蕉
print(fruits[-1])  # 倒数第1个：橘子（-1 是快捷方式）

# ③ 改、增
fruits[1] = "芒果"  # 把香蕉换成芒果
print(fruits)
fruits.append("葡萄")  # 末尾追加一个
print(fruits)  # 现在是 ["苹果", "芒果", "橘子", "葡萄"]

# ④ for 循环：把筐里的东西一个个拿出来处理
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")

# ⑤ for + range：数数专用，跟 while 的计数循环对比
# while 写法（还记得吗？）：
# count = 1; while count <= 3: print(count); count+=1

# for 写法（更简洁）：
for i in range(3):  # range(3) -> 0,1,2  循环3次
    print(f"range 第 {i} 次")
for i in range(1, 6):  # range(1,6) -> 1,2,3,4,5  跟昨天 while count<=5 一样
    print(f"数字 {i}")

# ⑥ 实战：用 for 做累加（求总分、平均分的基础）
scores = [85, 92, 78, 90]
total = 0
for s in scores:
    total = total + s  # 每一科都加到 total 上，跟 count 累加一模一样
print(f"总分 {total}, 平均分 {total/len(scores)}")
print(f"最高分 {max(scores)}, 最低分 {min(scores)}")
