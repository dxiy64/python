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
    try:
        r = requests.get(f"{URL}/page/{n}/", timeout=10, headers=HEADERS)
        time.sleep(1)
        rows = BeautifulSoup(r.text, "html.parser").select(".quote")
        if r.status_code == 200:
            return r.text if rows else None
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def parse(html):
    # TODO 2：抄 Day27 的 parse（None 回 []，每条 (text, author, tags)）
    if html is None:
        return []
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        tags = ",".join([t.get_text(strip=True) for t in quote.select(".tag")])
        rows.append((text, author, tags))
    return rows


def save(rows, conn):
    # TODO 3：INSERT OR IGNORE 批量入库，返回本批新增笔数（rowcount 累加）
    # 提示：表 quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)，调用者负责 commit
    conn.execute(
        "CREATE TABLE IF NOT EXISTS quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)"
    )
    added = 0
    for row in rows:
        cursor = conn.execute(
            "INSERT OR IGNORE INTO quotes(text, author, tags) VALUES (?, ?, ?)",
            row,
        )
        added += cursor.rowcount
    return added


def top_authors(conn, n=3):
    # TODO 4：返回 [(作者, 条数), ...] 前 n 名
    # 提示：GROUP BY author + ORDER BY COUNT(*) DESC + LIMIT ?（Day25 的 GROUP BY 回来了）
    return conn.execute(
        "SELECT author, COUNT(*) FROM quotes GROUP BY author ORDER BY COUNT(*) DESC LIMIT ?",
        (n,),
    ).fetchall()


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
