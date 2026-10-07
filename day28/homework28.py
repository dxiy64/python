"""Day28 作业：翻页抓取 + 增量入库 + 作者排行（骨架 + 4 个 TODO）

跑法（在 day28 目录里）：
    python -m pip install requests beautifulsoup4   # 先装
    python homework28.py                            # 约 5 秒（含 3 次 sleep）

要求：一次只做一个 TODO，做完就跑一次，看着报错往下走。
fetch / parse / save 的单页写法直接抄你 Day27 的 homework27.py。
"""
import sqlite3
import time
import requests
from bs4 import BeautifulSoup
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "quotes.db"
URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "python-learn/28"}


def fetch_page(n):
    # TODO 1：抓第 n 页，URL 为 f"{URL}/page/{n}/"，timeout=10 + headers；
    # 200 才 return r.text，否则 return None；RequestException 抓住 return None
    raise NotImplementedError("TODO 1：抓单页")


def parse(html):
    # TODO 2：抄 Day27 的 parse（None 回 []，每条 (text, author, tags)）
    raise NotImplementedError("TODO 2：摘名言")


def save(rows, conn):
    # TODO 3：INSERT OR IGNORE 批量入库，返回本批新增笔数（rowcount 累加）
    # 提示：表 quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)，调用者负责 commit
    raise NotImplementedError("TODO 3：增量入库")


def top_authors(conn, n=3):
    # TODO 4：返回 [(作者, 条数), ...] 前 n 名
    # 提示：GROUP BY author + ORDER BY COUNT(*) DESC + LIMIT ?（Day25 的 GROUP BY 回来了）
    raise NotImplementedError("TODO 4：作者排行")


def crawl(pages=3):
    """翻页主循环：每页抓→摘→存，空页停，页间 sleep(1)。已给好，不用改。"""
    conn = sqlite3.connect(DB)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)"
    )
    total = added_all = 0
    for n in range(1, pages + 1):
        rows = parse(fetch_page(n))
        if not rows:
            print(f"第 {n} 页空，停")
            break
        added = save(rows, conn)
        conn.commit()
        total += len(rows)
        added_all += added
        print(f"第 {n} 页：摘 {len(rows)} 新增 {added}")
        time.sleep(1)
    print("作者 Top3：", top_authors(conn))
    conn.close()
    return total, added_all


if __name__ == "__main__":
    import os

    if os.path.exists(DB):
        os.remove(DB)  # 每次演示从空库开始
    total, added = crawl(3)
    print("共摘", total, "条（应为 30）")
    print("共新增", added, "条（应为 30）")
    print("重跑一次新增（应为 0）：", crawl(3)[1])
    print("全跑通了喊「检查我的作业」（只讲不改版）。")
