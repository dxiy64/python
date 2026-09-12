# -*- coding: utf-8 -*-
# ============================================
# homework03.py · 成绩小管家
# 要求：把 TODO 补完，程序能跑，能算对
# ============================================

# 已给你一筐成绩，你来用 for 完成统计
scores = [88, 92, 79, 93, 85]

# TODO 1: 用 len() 打印一共几科
# print(f"一共 {???} 科")

print(scores)
print(f"一共{len(scores)}科")

# TODO 2: 用 for 循环求总分 total（参考 day03.py 第 ⑥ 段）
total = 0
# for s in scores:
#     total = ???
for i in scores:
    total += i
print(f"你的总分是{total}")

# TODO 3: 算出平均分并打印，保留1位小数
# average = total / len(scores)
# print(f"平均分 {average:.1f}")
print(f"你的平均分是{total/len(scores):.1f}")

# TODO 4: 用 max() / min() 打印最高分和最低分
print(f"最高分是{max(scores)}")
print(f"最低分是{min(scores)}")

# TODO 5 (进阶，选做): 让用户输入一个新成绩(用 input+int)，append 到 scores，再重新算一遍平均分
new_scores = int(input("请输入一个新成绩："))
scores.append(new_scores)
total = sum(scores)
print(f"现在的总分是{total}")
print(f"现在的平均分是{total/len(scores):.1f}")

# 笔记
# 1. 列表 list 是用 [] 装一堆东西，逗号隔开，写法是 fruits = ["苹果", "香蕉", "橘子"]
# 2. len() 函数用于获取列表中元素的数量
# 3. for 循环可以遍历列表中的每个元素，进行累加或其他操作，写法是 for 变量 in 列表:,目的是对列表中的每个元素进行以下操作
# 4. 增加元素到列表可以用 append() 方法，写法是 列表.append(新元素)
# 5. total += i 是 total = total + i 的简写，表示把 i 加到 total 上
# 6. max() 和 min() 函数分别用于获取列表中的最大值和最小值
# 7. input() 函数用于获取用户输入，返回值是字符串，需要用 int() 转换成整数
# 8. 索引的写法是 列表[索引]，索引从 0 开始，负数索引表示从末尾开始计数
