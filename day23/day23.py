# day23.py · 记账本收尾 —— 删除、修改、空月不断
# Day23 = 项目①最后一天：不加新零件，把程序补成"完整程序"。
# 讲义只有零件演示，没有成品 —— 成品是你 hw 文件里长出来的。
import json


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def demo删():
    section(1, "删除一笔：按序号删，删前先打印确认")
    账 = [
        {"金额": 12.5, "分类": "午饭", "备注": "猪脚饭", "时间": "2026-09-23 12:30"},
        {"金额": 6.0, "分类": "交通", "备注": "地铁", "时间": "2026-09-23 08:15"},
    ]
    print("  删之前：", len(账), "笔")
    idx = 0
    print("  准备删：", 账[idx])
    del 账[idx]
    print("  删之后：", len(账), "笔，剩下：", 账[0]["分类"])
    print("  越界会怎样：序号 >= len(账) → IndexError，所以先判 0 <= idx < len(账)。")
    print("  删完必须 save()，不然重启又回来了（Day21 教训）。")


def demo改():
    section(2, "修改一笔：按序号改，哪个字段填了改哪个")
    账 = [{"金额": 12.5, "分类": "午饭", "备注": "猪脚饭", "时间": "2026-09-23 12:30"}]
    idx = 0
    账[idx]["金额"] = 15.0
    print("  改后金额：", 账[idx]["金额"])
    print("  金额照样要校验（>0、最多两位小数，Day21 那套正则直接搬）。")
    print("  时间字段不改 —— 它是记账那一刻的证据。")


def demo空月():
    section(3, "空月报表不断：没账的月份也要给句话")
    账 = [{"金额": 12.5, "分类": "午饭", "时间": "2026-09-23 12:30"}]
    month = "2026-08"
    当月 = [b for b in 账 if b["时间"][:7] == month]
    if not 当月:
        print(f"  {month} 还没有账")
    print("  sum([]) =", sum([]), "—— 空列表求和是 0，不会崩。")
    print("  套路：先判空给提示，再求和打印，和 show / stats 同一个形状。")


def demo跨月():
    section(4, "跨月验收：拿 9 月报表当筛子，8 月数据不许漏进来")
    账 = [
        {"金额": 12.5, "分类": "午饭", "时间": "2026-09-23 12:30"},
        {"金额": 6.0, "分类": "交通", "时间": "2026-09-23 08:15"},
        {"金额": 15.0, "分类": "午饭", "时间": "2026-08-10 12:00"},
    ]
    当月 = [b for b in 账 if b["时间"][:7] == "2026-09"]
    print("  9 月报表笔数：", len(当月), "（8 月那笔必须被筛掉）")
    print("  8 月数据还在总账里：", len(账), "笔 —— 筛选不删数据，只是挑出来看。")


def delete(rows, idx):
    """删第 idx 笔：越界返回 False，成功 del + save 返回 True"""


def update(rows, idx, money=None, sort=None, note=None):
    """改第 idx 笔：只改传了的参数，金额要校验，改完 save"""


def report(rows, month):
    """按月报表：空月打印“X 月还没有账”，不崩"""


def demo骨架():
    section(5, "骨架：加 2 个函数，report 补一个判空")
    for f in (delete, update, report):
        print(f"  {f.__name__:<6} → {(f.__doc__ or '').strip()}")
    print("  施工顺序：① delete（序号校验 + del + save）")
    print("            ② update（只改传了的字段 + 金额校验 + save）")
    print("            ③ report 补空月分支")
    print("            ④ 菜单加 2 个分支，跑跨月验收。")


if __name__ == "__main__":
    demo删()
    demo改()
    demo空月()
    demo跨月()
    demo骨架()
    print("\n零件全在这了 —— 项目①收尾，把它写成完整程序。")
