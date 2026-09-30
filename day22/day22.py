# day22.py · 记账本扩展 —— 筛选、月度报表、导出 CSV
# Day22 = Day21 的延续：账本已经能记能看了，今天加三个本事。
# 讲义规则不变：只有"零件演示"，没有成品 —— 成品是你自己 hw 文件里长出来的。
import csv
from datetime import datetime


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def demo时间切片():
    section(1, "时间是字符串，切片就能取年月日")
    t = "2026-09-23 12:30"
    print("  原串：", t)
    print("  年月（前 7 位）：", t[:7])
    print("  日期（前 10 位）：", t[:10])
    print("  比对月份：", t[:7] == "2026-09", "→ 同月就留下，不同月就跳过")
    print("  为什么能这样切？—— 时间是固定格式的字符串（strftime 造的），")
    print("  位置永远对齐：第 1~7 位是年月，第 1~10 位是日期。")


def demo筛选():
    section(2, "筛选 = for 循环 + if 留下想要的")
    账 = [
        {"金额": 12.5, "分类": "午饭", "时间": "2026-09-23 12:30"},
        {"金额": 6.0, "分类": "交通", "时间": "2026-09-23 08:15"},
        {"金额": 15.0, "分类": "午饭", "时间": "2026-08-10 12:00"},
    ]
    结果 = [b for b in 账 if b["分类"] == "午饭"]
    print("  只看午饭：", len(结果), "笔")
    结果 = [b for b in 账 if b["时间"][:7] == "2026-09"]
    print("  只看 2026-09：", len(结果), "笔")
    print("  形状：[b for b in 账 if 条件] —— 留下满足条件的那几笔。")
    print("  筛完照样是列表，后面 show / stats / 导出都能直接吃。")


def demo月度报表():
    section(3, "月度报表 = 先筛出当月，再跑一遍分类求和")
    账 = [
        {"金额": 12.5, "分类": "午饭", "时间": "2026-09-23 12:30"},
        {"金额": 6.0, "分类": "交通", "时间": "2026-09-23 08:15"},
        {"金额": 15.0, "分类": "午饭", "时间": "2026-08-10 12:00"},
    ]
    当月 = [b for b in 账 if b["时间"][:7] == "2026-09"]
    合计 = {}
    for b in 当月:
        合计[b["分类"]] = 合计.get(b["分类"], 0) + b["金额"]
    print(f"  2026-09 共 {len(当月)} 笔：", {k: round(v, 2) for k, v in 合计.items()})
    print("  套路：筛选（第 2 节）+ 求和（Day21 第 4 节）拼起来就是报表。")


def demo导出():
    section(4, "导出 CSV：DictWriter 三件套（复习 Day17）")
    账 = [
        {"金额": 12.5, "分类": "午饭", "备注": "猪脚饭", "时间": "2026-09-23 12:30"},
        {"金额": 6.0, "分类": "交通", "备注": "地铁", "时间": "2026-09-23 08:15"},
    ]
    p = "demo_报表.csv"
    with open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["时间", "金额", "分类", "备注"])
        w.writeheader()
        w.writerows(账)
    print("  写出", p, "—— 三件套：open(utf-8-sig + newline) → 表头 → writerows。")
    import os
    os.remove(p)
    print("  （演示完删掉，不留垃圾。你的作业里导出的是真实文件，要留着。）")
    print("  别忘了：DictWriter 只认 fieldnames 里列出的键，多一个键就报错。")


def report(rows, month):
    """按月份出报表：筛出 month（如 2026-09）当月的记录，打印分类合计 + 总支出"""


def export_csv(rows, path):
    """把 rows 导出成 CSV：utf-8-sig + newline=''，表头 时间/金额/分类/备注"""


def demo骨架():
    section(5, "骨架：昨天 6 个函数不动，今天只加 2 个")
    for f in (report, export_csv):
        print(f"  {f.__name__:<10} → {(f.__doc__ or '').strip()}")
    print("  施工顺序：① 先把两个 def 空壳敲进 hw 文件，python 能跑")
    print("            ② 填 report（筛选 + 求和都是现成的零件）")
    print("            ③ 填 export_csv（DictWriter 三件套）")
    print("            ④ 菜单加 2 个分支，跑验收。")


if __name__ == "__main__":
    demo时间切片()
    demo筛选()
    demo月度报表()
    demo导出()
    demo骨架()
    print("\n零件全在这了 —— 接下来在你自己的 hw 文件里把两个函数长出来。")
