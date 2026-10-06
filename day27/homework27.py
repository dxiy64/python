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
    raise NotImplementedError("TODO 1：抓页")


def parse(html):
    # TODO 2：BeautifulSoup 摘出所有名言，每条 (text, author, tags)
    # 提示：soup.select(".quote")；条内 .text / .author 取 get_text(strip=True)；
    # tags 用 [t.get_text(strip=True) for t in 条.select(".tag")] 再 ",".join
    # 返回 list（html 为 None 时返回 []）
    raise NotImplementedError("TODO 2：摘名言")


def save(rows, path=DB):
    # TODO 3：存进 sqlite 表 quotes(text, author, tags)，text 当主键去重
    # 提示：CREATE TABLE IF NOT EXISTS quotes(text TEXT PRIMARY KEY, author TEXT, tags TEXT)；
    # INSERT OR IGNORE；记得 commit；返回新增笔数（cursor.rowcount 累加，或 executemany 后查总数差）
    raise NotImplementedError("TODO 3：存库去重")


def report(path=DB):
    # TODO 4：读库打印"共 N 条"，再逐条打印"作者：名言前 30 字"
    raise NotImplementedError("TODO 4：读库日报")


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
