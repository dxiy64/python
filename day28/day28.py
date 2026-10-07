# day28.py · 爬虫第二天：翻页 + 限速 + 增量入库
# 一句话定位：Day27 一次抓一页，Day28 一圈抓多页——翻页循环 + 礼貌限速 + 撞主键跳过。
# 本文件真联网（quotes.toscrape.com，只抓 2 页 + 探 1 个空页，可反复跑）。
import time
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com"
HEADERS = {"User-Agent": "python-learn/28"}


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def demo翻页():
    section(1, "翻页规律：页码是 URL 的一部分，拼出来就行")
    for n in (1, 2):
        print(f"  第 {n} 页 URL：{URL}/page/{n}/")
    print("  套路：f\"{URL}/page/{n}/\"，n 从 1 开始往上加，Day03 的 for 循环回来了。")


def demo限速():
    section(2, "限速：time.sleep(1)，两次抓之间歇 1 秒")
    print("  写在循环里，每抓完一页睡 1 秒：")
    print("    time.sleep(1)")
    print("  不睡也跑得动，但 10 页连发等于敲人家门不撒手——会被封 IP。")
    print("  礼貌三件 Day27 讲过，今天只用这一件。")


def demo停页():
    section(3, "停页条件：空页就是终点，[] 一出现就 break")
    r = requests.get(f"{URL}/page/11/", timeout=15, headers=HEADERS)
    rows = BeautifulSoup(r.text, "html.parser").select(".quote")
    print(f"  探第 11 页：状态码 {r.status_code}，摘到 {len(rows)} 条")
    print("  状态码还是 200，但 0 条——所以停页不能看状态码，看摘到条数：")
    print("    if not rows: break")
    print("  while True + 空页 break，和 Day02 猜数字的循环一个形状。")


def demo增量():
    section(4, "增量入库：INSERT OR IGNORE，老面孔自动跳过")
    print("  循环里每页摘完直接 INSERT OR IGNORE，text 主键撞了就跳过。")
    print("  每页记新增：added += cursor.rowcount（0 = 全是老面孔）。")
    print("  第二遍跑同一页：摘 10 条，新增 0 条——Day27 作业验过这条。")
    print("  所以翻页程序随便重跑，不怕数据翻倍。")


def demo闭环():
    section(5, "三天线：28 翻页入库 → 29 日报出报告")
    print("  Day27：抓一页，摘 10 条，存库。")
    print("  Day28（今天）：翻 3 页，30 条入库，GROUP BY 看谁语录最多。")
    print("  Day29：日报——共几条 / 新增几条 / 按作者排行，项目②成型。")


if __name__ == "__main__":
    demo翻页()
    demo限速()
    demo停页()
    demo增量()
    demo闭环()
    print("\n零件齐了 —— 作业：翻 3 页入库 + 作者排行。")
