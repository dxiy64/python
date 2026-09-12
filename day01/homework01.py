# -*- coding: utf-8 -*-
# ============================================
# homework01.py · 个人信息输出
# 运行方法：cd day01 再 python homework01.py
# 本课只学：print / 变量 / f-string / input
# ============================================

print("你好光羽！")
print("我是你的第一个 Python 程序")

# 变量：名字 → 值，方便后面反复用
name = "光羽"
age = 24
height = 1.75  # 米

print(f"{name} 今年 {age} 岁，身高 {height} 米")

# 变量可变：过完生日 age 就变了，原值不再保留
age = age + 1
print("过完生日后：", age)

# 推算：十年后的年龄，另起一个名字，不覆盖 age
age_after_10_years = age + 10
print("十年后的年龄是：", age_after_10_years)

# input() 永远返回字符串，这里直接拼进 f-string 即可
your_name = input("请输入你的名字：")
print(f"你好，{your_name}！欢迎来到 {your_name} 的 Python 世界")

# 笔记
# 1. print()：把括号里的内容显示到屏幕上，引号里的是字符串
# 2. name = "光羽"：把右边的值起个名字存起来
# 3. f-string：f"..." 里用 {变量} 把值嵌进文字
# 4. age = age + 1：用旧值算出新值再存回去
# 5. input()：暂停等用户敲一行字，拿回来永远是字符串
# 6. 变量类型：字符串 / 整数 / 浮点数（小数）
# 7. 命名规则：字母、数字、下划线，不能以数字开头，不用关键字
