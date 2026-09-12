# -*- coding: utf-8 -*-
# ============================================
# Day 04 · 字典与函数 —— 带标签的筐 + 代码打包机
# 运行方法：python day04\day04.py
# ============================================

# ① 字典 dict：用 {} 装“名字→值”一对对的东西
person = {"name": "光羽", "age": 24, "city": "东莞"}
print(person)               # 整个筐
print(person["name"])       # 按标签取：光羽（中括号里是 key，不是编号了）
print(len(person))          # 有几对？3

# ② 改、增
person["age"] = 25          # 标签已存在 → 改值
person["hobby"] = "剪辑"    # 标签不存在 → 新增一对
print(person)

# ③ 查有没有这个标签
print("city" in person)     # True
print("score" in person)    # False

# ④ for 遍历字典：拿到的默认是 key
for k in person:
    print(f"{k} → {person[k]}")
# 拿键值对一起：
for k, v in person.items():
    print(f"{k} = {v}")

print("=" * 30)

# ⑤ 函数 def：把重复代码打包，起个名字以后直接喊
def say_hello(name):
    print(f"你好，{name}！")

say_hello("光羽")           # 调用一次，执行一遍
say_hello("同学")           # 再调用，又执行一遍

# ⑥ 带返回值的函数：算完把结果递出来
def get_average(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)  # return = 把结果递出来

avg = get_average([88, 92, 79, 93, 85])
print(f"平均分 {avg:.1f}")

# ⑦ 函数也能收字典
def introduce(p):
    print(f"{p['name']}今年{p['age']}岁，在{p['city']}")

introduce(person)
