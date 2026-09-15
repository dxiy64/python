# -*- coding: utf-8 -*-
# ============================================
# day14.py · 讲义：把大文件拆成"工具箱 + 入口"
# 运行方法：cd day14 再 python day14.py
# 今天不装新库。学完你能把一个 200 行的文件拆成两个各司其职的文件
# ============================================
import os          # 规矩：import 一律写在文件最上面（下面第③节有讲解）

# ① 痛点：你现在的 homework12.py 有 140 行
#    class ContactBook（工具）+ show_menu + main（用法）全挤在一个文件里。
#    后果：
#      a. 想复用通讯录 → 得把整个文件复制走，连菜单一起搬
#      b. 想看菜单逻辑 → 得先滑过 90 行类的代码
#      c. 两个项目同时改 → 改同一个文件，容易打架
#    解决办法：拆文件。一个放"工具"，一个放"用法"。

print("本讲义搭档的三个文件：")
print("  contactbook.py  工具箱：只有类，谁都能 import")
print("  main.py         入口：只有菜单和输入")
print("  bad_tool.py     反面教材：没闸门的工具箱")
print()

# ② 工具箱自己有闸门那段自测，可以单独跑：python contactbook.py
print("=" * 40)
print("【演示 1】工具箱自己跑 python contactbook.py 会走它的自测段（见文件末尾）")
print("=" * 40)

# ③ import 的三种写法，效果一模一样
import contactbook                      # 写法1：整包拿进门，用的时候 contactbook.xxx
from contactbook import ContactBook     # 写法2：只拿 ContactBook 这一个名字
import contactbook as cb                # 写法3：拿进来但改个短名 cb

print("【演示 2】三种 import 写法，都是造一个通讯录对象：")
book1 = contactbook.ContactBook("demo_a.json")
book2 = ContactBook("demo_b.json")
book3 = cb.ContactBook("demo_c.json")
print("  写法1 contactbook.ContactBook →", book1)
print("  写法2 ContactBook             →", book2)
print("  写法3 cb.ContactBook          →", book3)
print("  三种是不是同一个类？", book1.__class__ is book2.__class__ is book3.__class__)
print("  （是。文件只被装载一次，三种写法只是给同一把钥匙起了不同叫法）")
print()

# ④ 为什么工具箱必须有闸门——反面教材现场翻车
print("=" * 40)
print("【演示 3】现在 import 那个没闸门的工具箱 bad_tool.py：")
print("=" * 40)
import bad_tool      # ← 这一行看着人畜无害
print("↑ 看到了吗？我什么都没干，只是 import 了它，它就自己演了一遍。")
print("  如果它里面写的是 input()，下面就轮到你敲键盘了；")
print("  如果它写的是删文件，你的数据就没了（Day12 那个实验）。")
print()

# ⑤ __pycache__ 是什么
print("=" * 40)
print("【演示 4】导入之后，目录里多了个 __pycache__ 文件夹")
print("=" * 40)
pycache = os.path.join(contactbook.BASE, "__pycache__")
print("  __pycache__ 存在吗？", os.path.exists(pycache))
if os.path.exists(pycache):
    for f in os.listdir(pycache):
        print("    里面躺着：", f)
print("  它是 Python 把 .py 翻译成机器码后的缓存（.pyc），下次导入更快。")
print("  可以删，下次导入自动重建；提交到 git 时一般不要它。")
print()

print("=" * 40)
print("【结论】怎么跑那两个文件：")
print("  cd day14")
print("  python contactbook.py    ← 工具箱自测（闸门里那段）")
print("  python main.py           ← 真正的菜单程序")
print("=" * 40)
