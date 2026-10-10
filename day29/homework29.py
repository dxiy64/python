"""Day29 作业：名言日报（骨架 + 3 个 TODO）

跑法（在 day29 目录里）：
    python homework29.py     # 约 6 秒（2 页 × sleep）

要求：一次只做一个 TODO，做完就跑一次，看着报错往下走。
抓取/解析写法抄 Day27-28，聚合抄 Day25。
"""

import sqlite3
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "quotes.db"
OUT = HERE / "out"
URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "python-learn/29"}


def stats(conn):
    # TODO 1：返回 (总数, 作者数)
    # 提示：SELECT COUNT(*) / SELECT COUNT(DISTINCT author)，各 fetchone()[0]
    total = conn.execute("SELECT COUNT(*) FROM quotes").fetchone()[0]
    authors = conn.execute("SELECT COUNT(DISTINCT author) FROM quotes").fetchone()[0]
    return total, authors


def top_authors(conn, n=3):
    # TODO 2：返回 [(作者, 条数), ...] 前 n 名（抄 Day28）
    top = conn.execute(
        "SELECT author, COUNT(*) FROM quotes GROUP BY author "
        "ORDER BY COUNT(*) DESC LIMIT ?",
        (n,),
    ).fetchall()
    return top


def write_report(conn):
    # TODO 3：在 OUT/ 下写日报文件并返回路径 Path
    # 内容 3 行起：标题日期行 + "共 X 条，Y 位作者" + Top3 每行"作者：N 条"
    # 提示：OUT.mkdir(parents=True, exist_ok=True)；文件名 strftime("日报_%Y%m%d_%H%M%S.txt")；
    # write_text(encoding="utf-8")；调用 stats 和 top_authors 组装
    total, authors = stats(conn)
    top = top_authors(conn)
    OUT.mkdir(parents=True, exist_ok=True)
    name = datetime.now().strftime("日报_%Y%m%d_%H%M%S.txt")
    path = OUT / name
    path.write_text(
        f"日报 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"共 {total} 条，{authors} 位作者\n"
        + "\n".join(f"{author}: {count} 条" for author, count in top),
        encoding="utf-8",
    )
    return path


def crawl(pages=2):
    """抓 2 页入库，已给好，不用改。"""
    conn = sqlite3.connect(DB)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)"
    )
    for n in range(1, pages + 1):
        r = requests.get(f"{URL}/page/{n}/", timeout=15, headers=HEADERS)
        for q in BeautifulSoup(r.text, "html.parser").select(".quote"):
            conn.execute(
                "INSERT OR IGNORE INTO quotes VALUES (?,?,?)",
                (
                    q.select_one(".text").get_text(strip=True),
                    q.select_one(".author").get_text(strip=True),
                    ",".join(t.get_text(strip=True) for t in q.select(".tag")),
                ),
            )
        conn.commit()
        time.sleep(1)
    return conn


if __name__ == "__main__":
    import os

    if os.path.exists(DB):
        os.remove(DB)  # 每次演示从空库开始
    conn = crawl(2)
    total, authors = stats(conn)
    print("总数（应为 20）：", total)
    print("作者数（应为 15）：", authors)
    print("Top3（Einstein 应为 4）：", top_authors(conn))
    p = write_report(conn)
    print("日报文件：", p.name)
    print("文件存在且非空：", p.exists() and p.stat().st_size > 0)
    conn.close()
    print("全跑通了喊「检查」（只讲不改版）。")


# 笔记
# 1. DISTINCT = 先把相同作者压成一个再数，和 Day25 的 GROUP BY 是亲戚。
