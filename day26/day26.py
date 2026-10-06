# day26.py · sqlite3 第三天：菜单版完整程序 + CSV 导出
# 一句话定位：Day24 搬数据，Day25 学算账，Day26 接菜单——三天拼成完整程序。
# 本文件只演示，不交互：菜单用"假输入列表"驱动，可反复跑。
import csv
import sqlite3
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"
DB = OUT / "demo.db"
CSV_PATH = OUT / "ledger.csv"


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def seed():
    """造表 + 4 笔演示数据（10 月 3 笔 + 8 月 1 笔）。"""
    OUT.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    conn = sqlite3.connect(DB)
    conn.execute(
        """CREATE TABLE ledger(
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


def demo导出(conn):
    section(1, "CSV 导出：SELECT 全端上桌，csv.writer 一行行写")
    rows = conn.execute("SELECT * FROM ledger ORDER BY time").fetchall()
    with open(CSV_PATH, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "金额", "分类", "备注", "时间"])  # 表头中文，当年 Day17 的老规矩
        w.writerows(rows)
    print("  写了", len(rows), "笔 →", CSV_PATH.name)
    print("  两处别丢：encoding=utf-8-sig（Excel 不乱码），newline=（不空行）")
    print("  读回第一行：", CSV_PATH.read_text(encoding="utf-8-sig").splitlines()[1])


def demo菜单(conn):
    section(2, "菜单接线：choice 是绳，分支是灯，一根绳只亮一盏灯")
    # 假输入：模拟用户依次敲 2（看流水）、6（月报表）、q（退出）
    fake_inputs = iter(["2", "6", "2026-10", "q"])
    choice = next(fake_inputs)
    print("  用户敲了：", choice)
    if choice == "2":
        n = conn.execute("SELECT COUNT(*) FROM ledger").fetchone()[0]
        print("  → 看流水分支：共", n, "笔")
    choice = next(fake_inputs)
    print("  用户敲了：6，月份：", end="")
    month = next(fake_inputs)
    print(month)
    if choice == "6":
        total = conn.execute(
            "SELECT SUM(money) FROM ledger WHERE time LIKE ?", ("2026-10%",)
        ).fetchone()[0] or 0
        print("  → 月报表分支：10 月支出", total)
    print("  用户敲了：q → break 出循环，close 关门")
    print("  套路和 Day23 一模一样，只是干活的从 JSON 换成 SQL。")


def demo兜底(conn):
    section(3, "异常兜底：库报错也别崩，try 包住就行")
    try:
        conn.execute("SELECT * FROM 不存在的表").fetchall()
    except sqlite3.Error as e:
        print("  抓住 sqlite3.Error：", e)
    print("  记住：sqlite3.Error 是全家桶，OperationalError（表名写错）")
    print("  IntegrityError（NOT NULL 约束）都是它孩子，一个 except 全接住。")
    print("  金额校验继续用 Day23 的 MONEY_RE，拦在 INSERT 之前。")


def demo收尾():
    section(4, "三天闭环：24/25/26 各解决什么")
    print("  Day24：建表 + 增删改查（INSERT/SELECT/UPDATE/DELETE + commit）")
    print("  Day25：聚合算账（SUM/COUNT/GROUP BY + 空月 or 0）")
    print("  Day26：菜单接线 + CSV 导出 + 异常兜底 = 完整程序")
    print("  下一步（Day27 起）：爬虫 requests + BeautifulSoup，抓下来存进 sqlite。")


if __name__ == "__main__":
    conn = seed()
    demo导出(conn)
    demo菜单(conn)
    demo兜底(conn)
    conn.close()
    demo收尾()
    print("\n零件齐了 —— 作业：菜单版 sqlite 记账本。")
