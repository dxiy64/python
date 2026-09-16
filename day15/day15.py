# -*- coding: utf-8 -*-
# ============================================
# day15.py · 讲义：模块与包（一堆文件怎么组织成"项目"）
# 运行方法：cd day15 再 python day15.py
# 今天不装新库。学完你能把一个项目组织成"包"，并知道怎么正确运行它
# ============================================
import os
import sys

# ① 痛点：Day14 我们拆成了两个文件，但都在同一个目录里
#    如果项目长大：storage、book、cli、utils、config、report……
#    十个 .py 全堆在根目录，名字还会互相打架（都叫 utils.py 怎么办？）
#    解决办法：建"包"——用文件夹分组。
#
#    模块 module = 一个 .py 文件
#    包   package = 一个文件夹（里面必须有 __init__.py）

HERE = os.path.dirname(os.path.abspath(__file__))

print("本讲义搭档的包：mybook/")
for f in sorted(os.listdir(os.path.join(HERE, "mybook"))):
    if f.endswith(".py"):
        print("   mybook/" + f)
print("   ↑ 一个大文件拆成了 4 个，各管一件事")
print()

# ② 用包里的东西：import 路径 = 包名.模块名
print("=" * 44)
print("【演示 1】三种写法都能拿到 ContactBook")
print("=" * 44)
import mybook                                  # 写法1：只导包名，再用 mybook.ContactBook
from mybook import ContactBook                 # 写法2：靠 __init__.py 的"出口"（推荐，最短）
from mybook.book import ContactBook as CB2     # 写法3：绕过出口，直接点模块（长，但明确）

print("  写法1 mybook.ContactBook →", mybook.ContactBook)
print("  写法2 ContactBook         →", ContactBook)
print("  写法3 mybook.book 里的    →", CB2)
print("  三个是同一个类吗？", mybook.ContactBook is ContactBook is CB2)
print()

# ③ 包里的分层：包是"箱套箱"
print("=" * 44)
print("【演示 2】包内部长什么样（谁用谁）")
print("=" * 44)
print("  __init__.py  门面：对外出口 ContactBook / PATH")
print("  storage.py   最底层：只管 读文件/写文件（load/save）")
print("  book.py      中间层：ContactBook 类，叫 storage 帮忙（from .storage import ...）")
print("  cli.py       最上层：菜单，叫 book 干活（from .book import ...）")
print()
print("  调用方向是单向的：cli → book → storage")
print("  好处：以后想把 JSON 换成数据库，只改 storage.py 一个文件，上面两层不用动")
print()

# ④ 包的门面：__init__.py 帮你把长名字变短
print("=" * 44)
print("【演示 3】有没有 __init__.py 的差别")
print("=" * 44)
print("  __init__.py 是包的\"门面\"，里面写了出口名单：")
with open(os.path.join(HERE, "mybook", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.startswith("from ."):
            print("     " + line.rstrip())
print("  所以外面可以简写：from mybook import ContactBook")
print("  没有它就得写：    from mybook.book import ContactBook")
print("  包的版本号也放在这里：mybook.__version__ =", mybook.__version__)
print()

# ⑤ 装进来的包到底在哪
print("=" * 44)
print("【演示 4】包在硬盘上的哪个位置（排查问题用）")
print("=" * 44)
print("  mybook.__file__ =", mybook.__file__)
print("  mybook.PATH     =", mybook.PATH)
print("  当前 sys.path[0] =", sys.path[0])
print()

print("=" * 44)
print("【结论】怎么跑这个项目：")
print("  cd day15")
print("  python day15.py          ← 本讲义")
print("  python -m mybook.cli     ← 跑包里的命令行界面（-m 后面写 包名.模块名，不加 .py）")
print("=" * 44)
print()
print("⚠️ 别这么跑：python mybook/cli.py —— 会因为\"相对导入\"直接报错，原因见讲义末尾注释。")

# ⑥ 为什么不能 python mybook/cli.py ？
#    cli.py 里写的是 from .book import ContactBook，那个 "." 意思是"我这个包里的兄弟模块"。
#    Python 要确定"我是哪个包的孩子"才能翻译这个 "."。
#    你直接跑 mybook/cli.py 时，Python 把 cli.py 当成一个孤立的脚本（__main__），
#    它不知道自己属于 mybook 这个包，于是翻译不了 "." → ImportError。
#    用 python -m mybook.cli 时，Python 明确知道"跑的是 mybook 包里的 cli 模块"，"." 就能翻译了。
#    （等价写法：写绝对导入 from mybook.book import ContactBook，然后就能直接跑——
#      但那样必须在包外面跑，且项目改名时要改多处，所以包内互相引用一律用相对导入。）
