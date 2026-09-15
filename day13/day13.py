# -*- coding: utf-8 -*-
# ============================================
# Day 13 · 面向对象③：继承——儿子直接用爸爸的本事
# 运行方法：cd day13 再 python day13.py
# 今天不装新库。核心三句话：
#   class 儿子(爸爸) = 继承，儿子的对象能直接用爸爸的方法
#   super().__init__(...) = 先让爸爸装好该装的格子，再装自己的
#   同名方法盖掉爸爸的（覆盖），要叫回爸爸那版就写 super().方法名()
# ============================================

# ① 先看痛点：两份几乎一模一样的代码
class StudentOld:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def say_hello(self):
        print(f"我是{self.name}，来自{self.school}")


class TeacherOld:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def say_hello(self):
        print(f"我是{self.name}，来自{self.school}")


StudentOld("光羽", "一中").say_hello()
TeacherOld("王老师", "一中").say_hello()
print("↑ 两段输出一样，代码也几乎一样：改一处就得改两处（复制粘贴的坑）")

print("=" * 30)

# ② 继承：把共同的部分抽到父类 Person，儿子只写自己的不同
class Person:
    def __init__(self, name, school):
        self.name = name
        self.school = school

    def say_hello(self):
        print(f"我是{self.name}，来自{self.school}")


class Student(Person):   # 括号里写爸爸：Student 继承 Person
    pass                 # pass = 先空着，啥都不写也不报错


class Teacher(Person):
    pass


s = Student("光羽", "一中")
t = Teacher("王老师", "一中")
s.say_hello()            # 自己没写，用的是爸爸的
t.say_hello()
print("Student 自己有 say_hello 吗？", "say_hello" in Student.__dict__)   # False：从爸爸那继承的
print("爸爸 Person 有吗？", "say_hello" in Person.__dict__)              # True

print("=" * 30)

# ③ super()：儿子想多装一个格子，又不丢爸爸的
class Teacher2(Person):
    def __init__(self, name, school, subject):
        super().__init__(name, school)   # 先让爸爸装 name 和 school
        self.subject = subject           # 再装自己的

    def say_hello(self):                 # 同名方法 = 覆盖父类的
        super().say_hello()              # 先喊爸爸那一版
        print(f"我教{self.subject}")     # 再补自己的


t2 = Teacher2("李老师", "二中", "Python")
t2.say_hello()
print("李老师的口袋：", t2.__dict__)   # name/school（爸爸装的）+ subject（自己装的）

print("=" * 30)

# ④ 忘了 super().__init__ 会怎样（演示错误，别怕）
class Bad(Person):
    def __init__(self, name, school, subject):
        self.subject = subject   # 只装了自己的，忘了叫爸爸装 name


bad = Bad("倒霉蛋", "三中", "数学")
print("倒霉蛋的口袋：", bad.__dict__)     # 只有 subject！
try:
    bad.say_hello()
except AttributeError as e:
    print("一叫就炸：", e)              # name 没装，爸爸的方法读不到

print("=" * 30)

# ⑤ 多态：同一个函数，传谁进来就喊谁的那一版
def intro(p):
    p.say_hello()


print("--- 多态演示 ---")
intro(Person("路人甲", "无"))
intro(Student("小明", "一中"))
intro(Teacher2("李老师", "二中", "Python"))

print("=" * 30)

# ⑥ isinstance：儿子也算爸爸的人
print("t2 是 Teacher2 吗？", isinstance(t2, Teacher2))   # True
print("t2 是 Person 吗？  ", isinstance(t2, Person))     # True：儿子的对象也是爸爸的“人”
print("t2 是 Student 吗？ ", isinstance(t2, Student))    # False：兄弟之间不认
