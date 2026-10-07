"""Day27 作业：抓名言、摘内容、存 sqlite（骨架 + 4 个 TODO）

跑法（在 day27 目录里）：
    python -m pip install requests beautifulsoup4   # 先装（Day08 装过 requests 也重跑一遍确认）
    python homework27.py

要求：一次只做一个 TODO，做完就跑一次，看着报错往下走。
目标站：https://quotes.toscrape.com（练习站，10 条/页，静态 HTML）。
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "quotes.db"
URL = "https://quotes.toscrape.com"

HEADERS = {"User-Agent": "python-learn/27"}


def fetch(url=URL):
    # TODO 1：requests.get 抓页，timeout=10 + headers=HEADERS；
    # 状态码 200 才 return r.text，否则打印状态码并 return None；
    # RequestException 抓住打印并 return None
    try:
        r = requests.get(url, timeout=10, headers=HEADERS)
        if r.status_code == 200:
            return r.text
    except requests.exceptions.RequestException as e:
        print("  没抓到（网没通？）：", e)
        return None


def parse(html):
    # TODO 2：BeautifulSoup 摘出所有名言，每条 (text, author, tags)
    # 提示：soup.select(".quote")；条内 .text / .author 取 get_text(strip=True)；
    # tags 用 [t.get_text(strip=True) for t in 条.select(".tag")] 再 ",".join
    # 返回 list（html 为 None 时返回 []）
    if html is None:
        return []
    soup = BeautifulSoup(html, "html.parser")
    texts = []
    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        tags = ",".join([t.get_text(strip=True) for t in quote.select(".tag")])
        texts.append((text, author, tags))
    return texts


def save(rows, path=DB):
    # TODO 3：存进 sqlite 表 quotes(text, author, tags)，text 当主键去重
    # 提示：CREATE TABLE IF NOT EXISTS quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)；
    # INSERT OR IGNORE；记得 commit；返回新增笔数（cursor.rowcount 累加，或 executemany 后查总数差）
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)"
    )
    added = 0
    for row in rows:
        cursor.execute(
            "INSERT OR IGNORE INTO quotes(text, author, tags) VALUES (?, ?, ?)", row
        )
        added += cursor.rowcount
    conn.commit()
    conn.close()
    print(f"  存入 {len(rows)} 条，新增 {added} 条（去重生效）")
    return added


def report(path=DB):
    # TODO 4：读库打印"共 N 条"，再逐条打印"作者：名言前 30 字"
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM quotes")
    count = cursor.fetchone()[0]
    print(f"共 {count} 条")
    cursor.execute("SELECT author, text FROM quotes")
    for author, text in cursor.fetchall():
        print(f"{author}：{text[:30]}...")
    conn.close()


if __name__ == "__main__":
    import os

    if os.path.exists(DB):
        os.remove(DB)  # 每次演示从空库开始
    html = fetch()
    rows = parse(html)
    print("摘到", len(rows), "条（应为 10）")
    print("新增", save(rows), "条（应为 10）")
    print("重存一次新增（应为 0，去重生效）：", save(rows))
    report()
    print("全跑通了喊「检查我的作业」（只讲不改版）。")


# 笔记
# 1.礼貌访问：requests.get + headers，timeout + 时间间隔，静态页（view-source 能看到的）；
# 2.抓到的 HTML 先存文件再摘，摘错了打开文件看，不用反复抓；
# 3.BeautifulSoup 摘菜套路：select(".条") / select_one(".条")，再 get_text(strip=True)；
# 4. sqlite 去重套路：text 当主键，INSERT OR IGNORE
# 5. cursor.rowcount 累加写法为：for row in rows: cursor.execute(...); added += cursor.rowcount
# 6. sqlite 查总数的写法为：cursor.execute("SELECT COUNT(*) FROM quotes"); count = cursor.fetchone()[0]
