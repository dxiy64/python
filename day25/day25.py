# day25.py · sqlite3 第二天：聚合查询（SUM / COUNT / GROUP BY）
# 一句话定位：Day24 是把数据搬进库，Day25 是让库替你算账。
# 以前：SELECT 全端上桌，Python 循环累加；今天：SQL 直接交总数。
# 本文件只演示，不交互：每次运行先清空 out/ 再重建，可反复跑。
import shutil
import sqlite3
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"
DB = OUT / "demo.db"


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def seed():
    """造 4 笔演示数据：10 月 3 笔 + 8 月 1 笔，当天的筛子。"""
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    conn = sqlite3.connect(DB)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS ledger(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            money REAL, sort TEXT, note TEXT, time TEXT)"""
    )
    conn.executemany(
        "INSERT INTO ledger(money, sort, note, time) VALUES(?, ?, ?, ?)",
        [
            (12.5, "午饭", "猪脚饭", "2026-10-05 12:30"),
            (6.0, "交通", "地铁", "2026-10-05 08:15"),
            (20.0, "午饭", "加餐", "2026-10-06 12:00"),
            (15.0, "午饭", "旧账", "2026-08-10 12:00"),
        ],
    )
    conn.commit()
    return conn


def demo手算(conn):
    section(1, "痛点先行：以前怎么算 10 月总支出")
    rows = conn.execute(
        "SELECT money FROM ledger WHERE time LIKE ?", ("2026-10%",)
    ).fetchall()
    total = 0
    for (m,) in rows:  # 每个小元组拆出金额，手工累加
        total += m
    print("  端回", len(rows), "行，循环累加 =", round(total, 2))
    print("  行数少没事，行数上万呢？数据全在路上跑一遍。")


def demo聚合(conn):
    section(2, "SUM / COUNT：库直接交总数，只回一个数")
    total = conn.execute(
        "SELECT SUM(money) FROM ledger WHERE time LIKE ?", ("2026-10%",)
    ).fetchone()[0]
    print("  SUM(10 月) =", total, "（fetchone()[0]，就一个数）")
    n = conn.execute(
        "SELECT COUNT(*) FROM ledger WHERE time LIKE ?", ("2026-10%",)
    ).fetchone()[0]
    print("  COUNT(10 月) =", n, "笔")
    print("  对比：SUM 求和，COUNT 数行；* 在 COUNT 里 = 整行。")


def demo分组(conn):
    section(3, "GROUP BY：按分类各算一遍，一次交齐")
    rows = conn.execute(
        """SELECT sort, SUM(money), COUNT(*)
           FROM ledger WHERE time LIKE ?
           GROUP BY sort""",
        ("2026-10%",),
    ).fetchall()
    print("  10 月各分类：", rows)
    print("  读法：一行 = 一个分类（名字，总额，笔数）")
    print("  GROUP BY sort = 先按 sort 分堆，再每堆各算 SUM 和 COUNT。")


def demo空表(conn):
    section(4, "空结果三件套：空列表 / None / 0，各管各")
    rows = conn.execute(
        "SELECT * FROM ledger WHERE time LIKE ?", ("2026-07%",)
    ).fetchall()
    print("  SELECT 明细（空月）=", rows, "→ 空列表，if not rows 判空")
    total = conn.execute(
        "SELECT SUM(money) FROM ledger WHERE time LIKE ?", ("2026-07%",)
    ).fetchone()[0]
    print("  SUM（空月）=", total, "→ None！不是 0，直接 round 会炸")
    n = conn.execute(
        "SELECT COUNT(*) FROM ledger WHERE time LIKE ?", ("2026-07%",)
    ).fetchone()[0]
    print("  COUNT（空月）=", n, "→ 0，这个最老实")
    print("  套路：SUM 回来先 `total or 0` 转成 0 再用。")


def demo组合拳(conn):
    section(5, "组合拳：一句 SQL 交出月度报表要的全部")
    month = "2026-10"
    n = conn.execute(
        "SELECT COUNT(*) FROM ledger WHERE time LIKE ?", (month + "%",)
    ).fetchone()[0]
    total = conn.execute(
        "SELECT SUM(money) FROM ledger WHERE time LIKE ?", (month + "%",)
    ).fetchone()[0] or 0
    by_sort = conn.execute(
        """SELECT sort, SUM(money) FROM ledger
           WHERE time LIKE ? GROUP BY sort""",
        (month + "%",),
    ).fetchall()
    print(f"  月份：{month}，共{n}笔，总支出：{total}，各分类：{dict(by_sort)}")
    print("  作业就是把这 3 句搬进 month_report，空月先判 n == 0。")


if __name__ == "__main__":
    conn = seed()
    demo手算(conn)
    demo聚合(conn)
    demo分组(conn)
    demo空表(conn)
    demo组合拳(conn)
    conn.close()
    print("\n零件齐了 —— 作业：SQL 版分类统计 + 月度报表。")
