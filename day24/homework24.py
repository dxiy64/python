"""Day24 作业：把记账本搬进 sqlite（骨架 + 6 个 TODO）

跑法（在 day24 目录里）：
    python homework24.py

要求：一次只做一个 TODO，做完就跑一次，看着报错往下走。
金额校验沿用 Day23 的正则：r"\\d+(\\.\\d{1,2})?" 且 > 0。
"""

import re
import sqlite3
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "ledger.db"

MONEY_RE = r"\d+(\.\d{1,2})?"


class LedgerDB:
    def __init__(self, path=DB):
        self.conn = sqlite3.connect(path)
        self._create_table()

    def _create_table(self):
        # TODO 1：建表 ledger(id 自增主键, money, sort, note, time)
        # 提示：conn.execute("CREATE TABLE IF NOT EXISTS ledger(...)")，5 列怎么定看 day24.py 第 2 节
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS ledger (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                money REAL NOT NULL,
                sort TEXT NOT NULL,
                note TEXT,
                time TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add(self, money, sort, note):
        # TODO 2：INSERT 一笔，time 取现在（格式 "%Y-%m-%d %H:%M"），记得 commit
        # 提示：问号占位符，一天 24.py 第 3 节；money 先判 > 0
        self.conn.execute(
            "INSERT INTO ledger (money, sort, note, time) VALUES (?, ?, ?, ?)",
            (money, sort, note, datetime.now().strftime("%Y-%m-%d %H:%M")),
        )
        self.conn.commit()

    def show(self):
        # TODO 3：SELECT * 全打印，没有账打印"还没有账"
        # 提示：fetchall 回来是元组列表，一行是 (id, money, sort, note, time)
        rows = self.conn.execute("select * from ledger order by time").fetchall()
        if not rows:
            print("还没有账")
        else:
            for row in rows:
                print(row)

    def update_money(self, pid, money_text):
        # TODO 4：按 id 改金额，金额走 MONEY_RE 校验 + > 0，改完 commit
        # 提示：UPDATE ledger SET money = ? WHERE id = ?；改了 0 行说明没这一笔
        if re.fullmatch(MONEY_RE, money_text) is None or float(money_text) <= 0:
            print("金额不合法")
            return
        cur = self.conn.execute(
            "UPDATE ledger SET money = ? WHERE id = ?",
            (float(money_text), pid),
        )
        if cur.rowcount == 0:
            print("没有这一笔")
            return
        self.conn.commit()

    def delete(self, pid):
        # TODO 5：按 id 删一笔，删完 commit
        # 提示：DELETE FROM ledger WHERE id = ?；删之前先 SELECT 打印确认
        row = self.conn.execute("SELECT * FROM ledger WHERE id = ?", (pid,)).fetchone()
        if row is None:
            print("没有这一笔")
            return
        print(f"准备删除：{row}")
        self.conn.execute(
            "DELETE FROM ledger WHERE id = ?",
            (pid,),
        )
        self.conn.commit()

    def month_report(self, month):
        # TODO 6：按月报表，"2026-10" 查出 10 月全部；空月打印"X 月还没有账"
        # 提示：WHERE time LIKE ?，参数是 month + "%"；day24.py 第 4 节
        rows = self.conn.execute(
            "SELECT * FROM ledger WHERE time LIKE ? ORDER BY time",
            (month + "%",),
        ).fetchall()
        if not rows:
            print(f"{month} 月还没有账")
        else:
            for row in rows:
                print(row)

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    import os

    if os.path.exists(DB):
        os.remove(DB)  # 每次演示从空库开始
    book = LedgerDB()
    book.add(12.5, "午饭", "猪脚饭")
    book.add(6.0, "交通", "地铁")
    book.show()
    book.update_money(1, "20.0")
    book.delete(2)
    book.show()
    book.month_report("2026-10")
    book.month_report("2026-08")
    book.close()
    print("全跑通了喊「检查我的作业」。")


# 笔记
# 1. sqlite3 的 execute() 方法可以执行 SQL 语句，支持参数化查询，避免 SQL 注入。
# 2. 使用 ? 占位符来传递参数，execute() 方法的第二个参数是一个元组，包含要传递的参数。
# 3. commit() 方法用于提交事务，将对数据库的更改保存到磁盘。
# 4. fetchall() 方法返回所有结果行，fetchone() 方法返回单个结果行。
# 5. 使用正则表达式进行金额校验，确保金额格式正确且大于
# 6. 设置id为自增主键，方便后续的更新和删除操作。写法为：id INTEGER PRIMARY KEY AUTOINCREMENT
# 7. execute() 方法返回一个 Cursor 对象，可以通过 rowcount 属性获取受影响的行数，用于判断更新或删除操作是否成功。
