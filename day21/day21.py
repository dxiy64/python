# day21.py · 阶段②第一作：命令行记账本 —— 先设计，再动手
# 从今天起玩法变了：不再是"补 TODO"，目标是**从空白文件写出能跑的程序**。
# 施工顺序永远是：需求 → 功能清单 → 数据结构 → 骨架 → 填肉 → 验收。
# 本讲义只有"零件演示"，没有成品 —— 成品是你的 homework21.py。
import json
from datetime import datetime
from collections import Counter


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def demo需求():
    section(1, "需求先落地：把“记账本”翻译成功能清单")
    清单 = [
        "1. 记一笔   —— 输入金额、分类、备注，自动带上时间",
        "2. 看流水   —— 逐行打印所有记录，空的时候要提示",
        "3. 统计     —— 按分类合计支出",
        "4. 存档读档 —— 关掉程序数据不丢（JSON 文件）",
        "5. 退出     —— 菜单循环，选 q 退",
    ]
    for item in 清单:
        print("  " + item)
    print("  口诀：先把功能一条条写下来，再想每条用什么数据、塞进哪个函数。")


def demo数据结构():
    section(2, "数据结构选型：每笔账是一个字典，整本账是一个列表")
    账 = [
        {"金额": 12.5, "分类": "午饭", "备注": "猪脚饭", "时间": "2026-09-23 12:30"},
        {"金额": 6.0, "分类": "交通", "备注": "地铁", "时间": "2026-09-23 08:15"},
    ]
    print("  类型：", type(账).__name__, "装着", len(账), "笔")
    print("  第一笔的分类：", 账[0]["分类"])
    print("  造出来的 JSON 文本：", json.dumps(账, ensure_ascii=False)[:50], "…")
    print("  为什么不用 {姓名: 电话} 那种字典？—— 同一个人能记一百笔，键会撞车；")
    print("  列表不挑键，一笔一个字典，长得就跟真实账本一样。")


def demo金额误差():
    section(3, "新知识：小数会“算不准”—— float 误差")
    print("  0.1 + 0.2 =", 0.1 + 0.2)
    print("  0.1 + 0.2 == 0.3 ？", 0.1 + 0.2 == 0.3)
    print("  修法①：算完 round(..., 2)     →", round(0.1 + 0.2, 2))
    print("  修法②：用“分”当整数存          →", (1250 + 330) / 100, "元")
    print("  记账本选①就够：打印或存档前 round 到 2 位小数。")


def demo统计():
    section(4, "分类统计：Counter 只会“数个数”，求和要自己累加")
    账 = [
        {"金额": 12.5, "分类": "午饭"},
        {"金额": 6.0, "分类": "交通"},
        {"金额": 15.0, "分类": "午饭"},
    ]
    次数 = Counter(b["分类"] for b in 账)
    print("  Counter（这笔账记了几笔）：", dict(次数))
    合计 = {}
    for b in 账:
        合计[b["分类"]] = 合计.get(b["分类"], 0) + b["金额"]
    print("  手动累加（各分类多少钱）：", {k: round(v, 2) for k, v in 合计.items()})
    print("  总支出：", round(sum(b["金额"] for b in 账), 2))
    print("  一句话：数笔数找 Counter，求钱自己 get + 累加。")


def demo时间戳():
    section(5, "记一笔就带一个时间：datetime.now()（复习 Day17）")
    now = datetime.now()
    print("  现在长这样：", f"{now:%Y-%m-%d %H:%M}")
    print("  存进 JSON 的是字符串，读回来照样能直接打印。")


def 读金额(s):
    """把用户敲的字符串变成合法金额；不合法就返回一句拒绝的话（不是异常）。"""
    try:
        v = float(s)
    except ValueError:
        return "拒绝：不是数字"
    if v <= 0:
        return "拒绝：金额必须大于 0"
    return round(v, 2)


def demo金额校验():
    section(6, "输入防呆：float() 会炸，用 except 提前接住（复习 Day06）")
    for s in ["12.5", "-3", "12元", ""]:
        print(f"  敲进来的 {s!r:7} → {读金额(s)}")
    print("  菜单里的写法：金额不合法 → 打印提示 → continue 重新问「这一项」。")


def load():
    """读 ledger.json，文件不存在返回 []（类型要和容器对上，是列表不是字典）"""


def save(rows):
    """把整本账写回 ledger.json（w 模式清空重写，所以每次必须传整本）"""


def add(rows, 金额, 分类, 备注):
    """造一条带时间戳的记录 append 进 rows，然后立刻 save()"""


def show(rows):
    """逐行打印流水；rows 是空列表就打印“还没有账”"""


def stats(rows):
    """按分类合计金额并打印（round 2 位）"""


def main():
    """while True 菜单 + input().strip() + 选 q break；闸门里唯一被调用的函数"""


def demo骨架():
    section(7, "骨架先行：先把结构敲出来跑通，再一个一个填肉")
    for f in (load, save, add, show, stats, main):
        print(f"  {f.__name__:<6} → {(f.__doc__ or '').strip()}")
    print("  注意：这 6 个函数现在只有说明文字没有身体 —— 调用它们会拿到 None。")
    print("  施工三步：① 先把 6 个 def 原样敲出来，python 能跑")
    print("            ② 从 load 开始一个一个往里填")
    print("            ③ 每填完一个就跑一次验收，别攒到最后一起爆。")


if __name__ == "__main__":
    demo需求()
    demo数据结构()
    demo金额误差()
    demo统计()
    demo时间戳()
    demo金额校验()
    demo骨架()
    print("\n零件全在这了 —— 接下来把 homework21.py 从空白文件写出来。")
