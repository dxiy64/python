print("你好光羽！")
print("我是你的第一个Python程序")

name = "光羽"
age = 24
height = 1.75

print(f"{name} 今年 {age} 岁，身高{height} 米")
age = age + 1
print("过完生日后：", age)
ger = age + 10
print("十年后的年龄是：", ger)

your_name = input("请输入你的名字：")
print(f"你好,{your_name}!欢迎来到{your_name}的python世界")

# 笔记
# 1. print()：让电脑说话。引号里的内容叫"字符串"
# 2. name = "光羽"给右边的内容起个名字，方便以后使用
# 3. f-string：把变量嵌进文字里，注意前面有个 f
# 4. input()：等待用户输入一行内容（返回的永远是字符串）
# 5. age = age + 1 变量是可以改变的，这就是"变"量的意思
# 6. 变量类型：文字（字符串）、整数、浮点数
# 7. 变量命名规则：只能包含字母、数字和下划线，不能以数字开头，不能使用 Python 的关键字
