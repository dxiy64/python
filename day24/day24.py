# day24.py · sqlite3 第一天：建表 / 增删改查
# 一句话定位：JSON 是整本重写，sqlite 是抽屉柜——只动一行也行。
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


def fresh_conn():
    """清空 out/，返回一个全新的连接（演示专用，作业里别这么干）。"""
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    return sqlite3.connect(DB)


def demo版本(conn):
    section(1, "先认人：sqlite 是标准库，不用 pip")
    print("  sqlite 版本：", sqlite3.sqlite_version)
    print("  连接对象：", type(conn).__name__)
    print("  数据文件：", DB.name, "（表和数据都住这一个文件里）")


def demo建表(conn):
    section(2, "建表：CREATE TABLE，一次建成，以后只管用")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS ledger(
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            money REAL,
            sort  TEXT,
            note  TEXT,
            time  TEXT
        )
        """
    )
    rows = conn.execute("PRAGMA table_info(ledger)").fetchall()
    print("  表 ledger 的 5 根柱子：")
    for cid, name, ctype, *_ in rows:
        print(f"    {cid} 号柱子：{name}（{ctype}）")
    print("  id 是自增主键：你只管存，编号它自己发（1、2、3…）")


def demo增(conn):
    section(3, "增：INSERT + 问号占位符，别拼字符串")
    # 痛点先行：备注里带个单引号，拼接写法当场炸
    note = "老陈's店"
    try:
        conn.execute(
            f"INSERT INTO ledger(money, sort, note, time)"
            f"VALUES(12.5, '午饭', '{note}', '2026-10-05 12:30')"
        )
    except sqlite3.OperationalError as e:
        print("  拼接写法遇到单引号就炸：", e)
    # 正解：问号占位，值另给，单引号随便写
    cur = conn.execute(
        "INSERT INTO ledger(money, sort, note, time) VALUES(?, ?, ?, ?)",
        (12.5, "午饭", note, "2026-10-05 12:30"),
    )
    print("  问号写法：第 1 笔入库，拿到的 id =", cur.lastrowid)
    # executemany：一次塞多笔，省得循环
    conn.executemany(
        "INSERT INTO ledger(money, sort, note, time) VALUES(?, ?, ?, ?)",
        [
            (6.0, "交通", "地铁", "2026-10-05 08:15"),
            (15.0, "午饭", "加餐", "2026-08-10 12:00"),
        ],
    )
    conn.commit()
    n = conn.execute("SELECT COUNT(*) FROM ledger").fetchone()[0]
    print("  commit 之后：表里共", n, "笔")


def demo查(conn):
    section(4, "查：SELECT 拿回的是元组列表，筛选用 WHERE")
    rows = conn.execute("SELECT * FROM ledger ORDER BY id").fetchall()
    print("  整表：", len(rows), "笔，第一笔的类型是", type(rows[0]).__name__)
    print("  第一笔：", rows[0], "→ id 取 [0]，金额取 [1]")
    one = conn.execute(
        "SELECT money, note FROM ledger WHERE sort = ?", ("午饭",)
    ).fetchall()
    print("  只查午饭：", one)
    oct_rows = conn.execute(
        "SELECT COUNT(*) FROM ledger WHERE time LIKE ?", ("2026-10%",)
    ).fetchone()[0]
    print("  10 月几笔：", oct_rows, "（8 月那笔被 LIKE 筛掉——跨月直接在 SQL 里做）")


def demo改删(conn):
    section(5, "改和删：UPDATE / DELETE，WHERE 就是保险丝")
    conn.execute("UPDATE ledger SET money = ? WHERE id = ?", (20.0, 2))
    conn.commit()
    print("  改后第 2 笔金额：",
          conn.execute("SELECT money FROM ledger WHERE id = 2").fetchone()[0])
    conn.execute("DELETE FROM ledger WHERE id = ?", (1,))
    conn.commit()
    left = conn.execute("SELECT COUNT(*) FROM ledger").fetchone()[0]
    print("  删掉 id=1 后剩", left, "笔")
    print("  记住：不带 WHERE 的 DELETE 会清空整表，先 SELECT 对笔数再动手")


def demo不commit就没了():
    section(6, "commit 就是 Day21 的 save：不 commit，关门就清零")
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO ledger(money, sort, note, time) VALUES(?, ?, ?, ?)",
        (99.0, "测试", "没commit", "2026-10-05 00:00"),
    )
    conn.close()  # 故意不 commit 直接关门
    conn2 = sqlite3.connect(DB)
    n1 = conn2.execute(
        "SELECT COUNT(*) FROM ledger WHERE sort = '测试'"
    ).fetchone()[0]
    print("  没 commit 就关门：测试笔数 =", n1, "（白干了）")
    conn2.execute(
        "INSERT INTO ledger(money, sort, note, time) VALUES(?, ?, ?, ?)",
        (99.0, "测试", "commit了", "2026-10-05 00:00"),
    )
    conn2.commit()
    conn2.close()
    conn3 = sqlite3.connect(DB)
    n2 = conn3.execute(
        "SELECT COUNT(*) FROM ledger WHERE sort = '测试'"
    ).fetchone()[0]
    print("  commit 再关门：测试笔数 =", n2, "（落盘了）")
    conn3.execute("DELETE FROM ledger WHERE sort = '测试'")
    conn3.commit()
    conn3.close()
    print("  演示数据已清掉，demo.db 里只剩 2 笔真账")


if __name__ == "__main__":
    conn = fresh_conn()
    demo版本(conn)
    demo建表(conn)
    demo增(conn)
    demo查(conn)
    demo改删(conn)
    conn.close()
    demo不commit就没了()
    print("\n零件齐了 —— 作业：把 Day23 记账本搬进 sqlite。")
