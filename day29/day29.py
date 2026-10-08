# day29.py · 爬虫第三天：日报（总数/作者数/排行 + 落盘文件）
# 一句话定位：Day27 抓一页，Day28 翻多页，Day29 把库里的数变成一份日报文件。
# 本文件真联网，只抓第 1 页（10 条），可反复跑。
import time
import sqlite3
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"
DB = OUT / "demo.db"

URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "python-learn/29"}


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def seed():
    """抓第 1 页入库，日报的原料（只抓 1 页，快）。"""
    OUT.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    conn = sqlite3.connect(DB)
    conn.execute(
        "CREATE TABLE quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)"
    )
    r = requests.get(f"{URL}/page/1/", timeout=15, headers=HEADERS)
    for q in BeautifulSoup(r.text, "html.parser").select(".quote"):
        conn.execute(
            "INSERT OR IGNORE INTO quotes VALUES (?,?,?)",
            (q.select_one(".text").get_text(strip=True),
             q.select_one(".author").get_text(strip=True), ""),
        )
    conn.commit()
    print("  原料就绪：1 页入库")
    return conn


def demo三个数(conn):
    section(1, "日报只回答三个数：总数 / 作者数 / 谁最多")
    total = conn.execute("SELECT COUNT(*) FROM quotes").fetchone()[0]
    authors = conn.execute("SELECT COUNT(DISTINCT author) FROM quotes").fetchone()[0]
    top = conn.execute(
        "SELECT author, COUNT(*) FROM quotes GROUP BY author "
        "ORDER BY COUNT(*) DESC LIMIT 1"
    ).fetchone()
    print(f"  共 {total} 条，{authors} 位作者，最多：{top[0]}（{top[1]} 条）")


def demo去重数(conn):
    section(2, "COUNT(DISTINCT author)：去重后再数")
    rows = conn.execute("SELECT author FROM quotes").fetchall()
    print(f"  不去重：{len(rows)} 个名字（含重名）")
    n = conn.execute("SELECT COUNT(DISTINCT author) FROM quotes").fetchone()[0]
    print(f"  去重后：{n} 位作者")
    print("  DISTINCT = 先把相同作者压成一个再数，和 Day25 的 GROUP BY 是亲戚。")


def demo文件名():
    section(3, "时间戳文件名：%Y%m%d_%H%M%S，冒号是禁区")
    name = datetime.now().strftime("日报_%Y%m%d_%H%M%S.txt")
    print("  文件名：", name)
    print("  只有数字下划线，没有冒号——Day17 的教训：文件名里写 %H:%M 会炸。")
    print("  每次跑名字都不同，旧日报不会被覆盖。")


def demo落盘(conn):
    section(4, "落盘：out/ 先建目录，再 write_text")
    total = conn.execute("SELECT COUNT(*) FROM quotes").fetchone()[0]
    authors = conn.execute("SELECT COUNT(DISTINCT author) FROM quotes").fetchone()[0]
    top3 = conn.execute(
        "SELECT author, COUNT(*) FROM quotes GROUP BY author "
        "ORDER BY COUNT(*) DESC LIMIT 3"
    ).fetchall()
    lines = [
        f"名言日报 {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"共 {total} 条，{authors} 位作者",
        "Top3：",
    ]
    lines += [f"  {a}：{c} 条" for a, c in top3]
    p = OUT / datetime.now().strftime("日报_%Y%m%d_%H%M%S.txt")
    p.write_text("\n".join(lines), encoding="utf-8")
    print(f"  写到 {p.name}，{p.stat().st_size} 字节")
    print("  内容预览：", lines[1])


def demo成型():
    section(5, "项目②成型：27 抓 → 28 存 → 29 报")
    print("  Day27：抓一页，摘 10 条（requests + BeautifulSoup）。")
    print("  Day28：翻 3 页，30 条增量入库（OR IGNORE + sleep）。")
    print("  Day29（今天）：库里读数，出一份日报文件。")
    print("  抓→存→报闭环 = 路线图项目②的完整形态，简历可写。")


if __name__ == "__main__":
    conn = seed()
    demo三个数(conn)
    demo去重数(conn)
    demo文件名()
    demo落盘(conn)
    conn.close()
    demo成型()
    print("\n零件齐了 —— 作业：2 页日报 + 落盘文件。")
