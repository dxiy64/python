# -*- coding: utf-8 -*-
# ============================================
# day16.py · 讲义：虚拟环境与依赖（venv / pip / requirements.txt）
# 运行方法：cd day16 再 python day16.py
# 这个文件跑两次对比最有价值：
#   ① 在系统 Python 里跑（没激活 venv）
#   ② 激活虚拟环境后再跑
#   两次的「环境指纹」会不一样——那就是今天的知识点
# ============================================
import sys
import os
import glob

# ① 痛点：为什么要虚拟环境
#    你现在所有库都装在“全局”——整台电脑共用一套。
#    问题：
#      a. 项目A 要 requests 2.31，项目B 要 2.34 → 只能二选一，另一个坏掉
#      b. 半年后换电脑，你不知道当初装过啥 → 程序一跑就 ModuleNotFoundError
#      c. pip install 装错了 Python（电脑上可能有好几个 python）→ 装完还是用不了
#    解法：一个项目一个“独立小环境”，各装各的，互不干扰。

print("=" * 48)
print("【环境指纹】这个判断以后天天要用")
print("=" * 48)
in_venv = sys.prefix != sys.base_prefix
print("  sys.executable  =", sys.executable)
print("      ↑ 现在正在跑的这个解释器是谁")
print("  sys.prefix      =", sys.prefix)
print("      ↑ 当前环境的根目录（装库的位置就在它下面）")
print("  sys.base_prefix =", sys.base_prefix)
print("      ↑ 创建它的那个“源”Python")
print()
if in_venv:
    print("  当前是否在虚拟环境里：是 ✅（prefix 和 base_prefix 不一样）")
    print("  环境名：", os.path.basename(sys.prefix))
else:
    print("  当前是否在虚拟环境里：否 ❌（prefix 和 base_prefix 一样）")
    print("  你用的是系统 Python，所有项目共用一套库")
print()
site = [p for p in sys.path if p.endswith("site-packages")]
print("  第三方库装在哪：")
for p in site:
    print("     ", p)
print()

# ② 数一数这个环境里装了多少个第三方库
print("=" * 48)
print("【装了多少库】换个环境这个数字就变")
print("=" * 48)
if site:
    infos = glob.glob(os.path.join(site[0], "*.dist-info"))
    # 文件夹名长这样：requests-2.34.2.dist-info
    # removesuffix 砍掉结尾的 .dist-info，剩下的就是“包名-版本号”
    names = sorted(os.path.basename(p).removesuffix(".dist-info") for p in infos)
    print("  dist-info 文件夹数量 =", len(names), "（每个包对应一个）")
    print("  前 10 个：", names[:10])
print()

# ③ venv 是什么（一句话 + 长什么样）
print("=" * 48)
print("【venv 是什么】")
print("=" * 48)
print("  一个文件夹，里面有一份指向系统 Python 的快捷方式 + 自己的 site-packages。")
print("  创建后目录长这样：")
print("     .venv/")
print("     ├── Scripts/                ← python.exe、pip.exe、activate（Windows）")
print("     ├── Lib/site-packages/      ← 这个环境独占的库都装这里")
print("     └── pyvenv.cfg              ← 一张纸条：源 Python 在哪、要不要用系统库")
print()
print("  三步曲（详细命令见 commands.md）：")
print("     python -m venv .venv            ① 创建（只做一次）")
print("     source .venv/Scripts/activate   ② 激活（每次开工都要）")
print("     python -m pip install 包名       ③ 装库（装进这个环境）")
print()

# ④ requirements.txt 是什么
print("=" * 48)
print("【requirements.txt】把“这个项目需要哪些库”写成一张清单")
print("=" * 48)
print("  导出：python -m pip freeze > requirements.txt")
print("  别人拿到你的项目：python -m pip install -r requirements.txt  一键复现")
print("  内容长这样（版本号用 == 锁住，保证别人装到一样的）：")
print("     requests==2.34.2")
print("     tabulate==0.9.0")
print()

# ⑤ 三个最常见的坑
print("=" * 48)
print("【三个坑】")
print("=" * 48)
print("  1. 忘了激活就装库 → 装进全局，项目里还是用不了")
print("     （激活成功的标志：命令行提示符前面多了 (.venv)）")
print("  2. 用 pip 而不是 python -m pip → 可能装到另一个 Python 上")
print("     永远写 python -m pip install xxx，稳。")
print("  3. 把 .venv 提交到 git → 几百 MB 的垃圾（.gitignore 里已经有它了）")
print()

print("=" * 48)
print("【自测】把同样的命令跑两遍，对比上面那几行：")
print("  cd day16")
print("  python day16.py                  ← 第 1 遍（系统 Python）")
print("  source .venv/Scripts/activate    ← 激活")
print("  python day16.py                  ← 第 2 遍（虚拟环境）")
print("  deactivate                       ← 退出")
print("=" * 48)
