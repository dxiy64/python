# -*- coding: utf-8 -*-
# ============================================
# homework03.py · 成绩小管家
# 运行方法：cd day03 再 python homework03.py
# 本课只学：列表 / for / len / append / max / min
# ============================================

scores = [88, 92, 79, 93, 85]

# 一共几科
print(scores)
print(f"一共 {len(scores)} 科")

# for 累加求总分（和 Day02 的 count 累加一个道理）
total = 0
for score in scores:
    total += score
print(f"你的总分是 {total}")

# 平均分保留 1 位小数
print(f"你的平均分是 {total / len(scores):.1f}")

# 最高分 / 最低分
print(f"最高分是 {max(scores)}")
print(f"最低分是 {min(scores)}")

# 进阶：让用户加一个新成绩，再重算一遍
new_score = int(input("请输入一个新成绩："))
scores.append(new_score)

total = 0
for score in scores:
    total += score
print(f"现在的总分是 {total}")
print(f"现在的平均分是 {total / len(scores):.1f}")

# 笔记
# 1. 列表用 [] 装一堆值：scores = [88, 92, ...]
# 2. len()：数一数有几个元素
# 3. for score in scores：把每个元素拿出来走一遍
# 4. total += score 就是 total = total + score 的简写
# 5. append()：往列表末尾加一个元素
# 6. max() / min()：取最大 / 最小值
# 7. 索引从 0 开始：scores[0] 是第一个
