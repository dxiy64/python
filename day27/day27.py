# day27.py · 爬虫第一天：requests 抓网页 + BeautifulSoup 摘内容
# 一句话定位：requests 是跑腿（把网页拿回来），BeautifulSoup 是摘菜（把要的字挑出来）。
# 需要：python -m pip install requests beautifulsoup4（你 Day08 装过 requests，今天加 bs4）
# 本文件真联网抓 example.com（静态页，免翻墙，可反复跑）。
import requests
from bs4 import BeautifulSoup
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"

URL = "https://example.com"


def section(n, title):
    print(f"\n【第 {n} 节】{title}")
    print("=" * 50)


def demo抓(conn_note=None):
    section(1, "抓：requests.get + 两件套（timeout + status_code）")
    try:
        r = requests.get(URL, timeout=10)  # timeout=10：10 秒没回就放弃，不卡死
    except requests.exceptions.RequestException as e:
        print("  没抓到（网没通？）：", e)
        return None
    print("  状态码：", r.status_code, "（200 = 拿到了，404 = 没这页）")
    print("  拿回", len(r.text), "个字符，头 60 个：", r.text[:60].replace("\n", " "))
    print("  记住：r.text 是整页 HTML（含标签），不是正文。")
    print("   transport 出问题（断网/超时/DNS）全进 RequestException，一个 except 接住。")
    return r.text


def demo摘(html):
    section(2, "摘：BeautifulSoup + select，一句话拿标题和正文")
    if html is None:
        print("  没抓到，跳过摘菜。")
        return
    soup = BeautifulSoup(html, "html.parser")  # html.parser 是标准库自带的，不用装
    print("  锅（soup）类型：", type(soup).__name__)
    title = soup.select_one("title")  # select_one：只端第一碗
    print("  网页标题 title：", title.get_text(strip=True) if title else "没找到")
    ps = soup.select("p")  # select：全端上桌
    print("  正文 p 共", len(ps), "段，首段前 40 字：",
          ps[0].get_text(strip=True)[:40] if ps else "没找到")
    print("  三件套：select_one 取一个 / select 取一堆 / get_text 只要字不要标签。")
    print("  注意：这页没有 h1 和 a——摘之前先 view-source 看一眼有啥，别硬套。")


def demo存(html):
    section(3, "存：抓到的存文件，Day05 的老手艺")
    if html is None:
        print("  没抓到，跳过存盘。")
        return
    OUT.mkdir(parents=True, exist_ok=True)
    p = OUT / "example.html"
    p.write_text(html, encoding="utf-8")
    print("  存到", p.name, "，", p.stat().st_size, "字节")
    print("  调试套路：先存文件再摘，摘错了打开文件看，不用反复抓。")


def demo礼貌():
    section(4, "礼貌三件：headers + 限速 + 只抓静态")
    print("  headers：报上名字，别装浏览器也别裸奔：")
    print("    requests.get(URL, timeout=10, headers={'User-Agent': 'python-learn/27'})")
    print("  限速：两次抓之间 sleep(1)，别把人家服务器当你家 sqlite 使。")
    print("  只抓静态：JS 渲染的页（翻页靠点击加载的）requests 拿不到，")
    print("    那是 Day30+ 的话题，这三天只玩 view-source 能看到的页。")


def demo闭环():
    section(5, "三天爬虫线：27 抓摘 → 28 存库去重 → 29 日报")
    print("  Day27（今天）：抓 example.com，摘标题+正文，存文件。")
    print("  Day28：抓到的存进 sqlite，URL 当主键去重，抓过的不重抓。")
    print("  Day29：从库里读，出一份日报（共几条/新增几条/标题列表）。")
    print("  这就是路线图项目②的缩小版：抓 → 存库 → 出日报。")


if __name__ == "__main__":
    html = demo抓()
    demo摘(html)
    demo存(html)
    demo礼貌()
    demo闭环()
    print("\n零件齐了 —— 作业：抓 quotes.toscrape.com，摘名言存库。")
