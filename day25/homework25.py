"""Day25 作业：SQL 版统计（骨架 + 4 个 TODO）

跑法（在 day25 目录里）：
    python homework25.py

要求：一次只做一个 TODO，做完就跑一次，看着报错往下走。
只许用 SQL 聚合（SUM / COUNT / GROUP BY）算数，不许 SELECT 明细回来循环累加。
"""

import sqlite3
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "ledger.db"


class LedgerDB:
    def __init__(self, path=DB):
        self.conn = sqlite3.connect(path)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS ledger(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                money REAL, sort TEXT, note TEXT, time TEXT)""")
        self.conn.commit()

    def add(self, money, sort, note, time):
        self.conn.execute(
            "INSERT INTO ledger(money, sort, note, time) VALUES(?, ?, ?, ?)",
            (money, sort, note, time),
        )
        self.conn.commit()

    def total(self):
        # TODO 1：整表总支出，一句 SELECT SUM，空表回 0（提示：or 0）
        return self.conn.execute("SELECT SUM(money) FROM ledger").fetchone()[0] or 0

    def month_total(self, month):
        # TODO 2：某月总支出，WHERE time LIKE month + "%"，空月回 0
        return (
            self.conn.execute(
                "SELECT SUM(money) FROM ledger WHERE time LIKE ?", (month + "%",)
            ).fetchone()[0]
            or 0
        )

    def stats_by_sort(self, month=None):
        # TODO 3：按分类统计，返回 {分类: 总额}；给了 month 只算当月
        # 提示：GROUP BY sort；month 为 None 时不加 WHERE
        if month is None:
            return dict(
                self.conn.execute(
                    "SELECT sort, SUM(money) FROM ledger GROUP BY sort"
                ).fetchall()
            )
        else:
            return dict(
                self.conn.execute(
                    "SELECT sort, SUM(money) FROM ledger WHERE time LIKE ? GROUP BY sort",
                    (month + "%",),
                ).fetchall()
            )

    def month_report(self, month):
        # TODO 4：月度报表——空月打印"X 月还没有账"；
        # 有账打印"月份：X，共N笔，总支出：T，各分类：{...}"（N 用 COUNT，T 用 SUM）
        count, total = self.conn.execute(
            "SELECT COUNT(*), SUM(money) FROM ledger WHERE time LIKE ?", (month + "%",)
        ).fetchone()
        if count == 0:
            print(f"{month} 月还没有账")
        else:
            stats = self.stats_by_sort(month)
            print(f"月份：{month}，共{count}笔，总支出：{total}，各分类：{stats}")

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    import os

    if os.path.exists(DB):
        os.remove(DB)  # 每次演示从空库开始
    book = LedgerDB()
    print("空表总支出（应为 0）：", book.total())
    book.add(12.5, "午饭", "猪脚饭", "2026-10-05 12:30")
    book.add(6.0, "交通", "地铁", "2026-10-05 08:15")
    book.add(20.0, "午饭", "加餐", "2026-10-06 12:00")
    book.add(15.0, "午饭", "旧账", "2026-08-10 12:00")
    print("整表总支出（应为 53.5）：", book.total())
    print("10 月支出（应为 38.5）：", book.month_total("2026-10"))
    print("8 月支出（应为 15.0）：", book.month_total("2026-08"))
    print("7 月支出（应为 0）：", book.month_total("2026-07"))
    print("全部分类（应为 3 个数）：", book.stats_by_sort())
    print("10 月分类（应为 午饭 32.5 / 交通 6.0）：", book.stats_by_sort("2026-10"))
    book.month_report("2026-10")
    book.month_report("2026-07")
    book.close()
    print("全跑通了喊「检查我的作业」（只讲不改版）。")
