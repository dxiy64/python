# -*- coding: utf-8 -*-
# ============================================
# homework19.py · 调试练习台（Day19 作业）
# 运行方法：cd day19 再 python homework19.py
# 说明：这个文件现在就能跑（不报错），但 TODO 没做——补完之后输出应和下面一致
# ============================================
#
# 【期望输出（补完所有 TODO 后应该长这样）】
#
#   === A. 读错误：三个故障各是什么错 ===
#     bug_divide(10, 0)                  → ZeroDivisionError: division by zero
#     bug_lookup({'光羽': '111'}, '小明') → KeyError: '小明'
#     bug_format(None)                   → AttributeError: 'NoneType' object has no attribute 'strip'
#
#   === B. 修 bug：find_max ===
#     find_max([3, 9, 2]) → 9
#     find_max([])        → None
#     find_max([-5])      → -5
#
#   === C. logging：把清洗过程记进日志 ===
#     （屏幕上出现 5 行带时间的日志，同时 out_hw19/run.log 里也有一份）
#     有效 2 条： ['13800001111', '13700001111']
#     丢弃 3 条： ['小明 12800001111', '鼠鼠 999999999', '   ']
#     ↑ '小明 12800001111' 为什么算丢弃？做完 C 自己想清楚（Day18 的正则知识）
# ============================================
import logging
import re
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out_hw19"


# ----------------------------------------------------------------------
# A. 读错误：三个函数各有一个毛病，先用工具把它们「安全地跑一遍」
# ----------------------------------------------------------------------
def bug_divide(a, b):
    """算 a / b（没检查 b 是不是 0）"""
    return f"{a} / {b} = {a / b}"


def bug_lookup(book, name):
    """在字典里查电话（没检查名字在不在）"""
    return f"{name}：{book[name]}"


def bug_format(text):
    """去空格再转大写（没检查 text 是不是字符串）"""
    return text.strip().upper()


# TODO 1：写「安全调用」工具
#   要求：调用 func(*args)，
#     · 成功 → 返回它的返回值
#     · 出错 → 返回字符串 f"{错误类型名}: {错误原因}"，不打印、不往上抛
#   提示：try / except Exception as e / type(e).__name__ / str(e)
#   提示：func(*args) 里的 * 是「把 args 里装的参数一个个摊开传进去」
def run_safely(func, *args):
    # ── TODO 1 从这里开始写（大约 6 行）───────────────────────────
    return "[TODO 1 未完成]"
    # ── TODO 1 结束 ──────────────────────────────────────────────


# ----------------------------------------------------------------------
# B. 修 bug：find_max 有两处问题
# ----------------------------------------------------------------------
def find_max(numbers):
    """返回列表里的最大值；空列表返回 None（不许报错）"""
    best = numbers[0]                   # ← 问题①：空列表在这里就炸
    for i in range(len(numbers)):       # ← 问题②：下标会算到 len(numbers)（越界）
        if numbers[i + 1] > best:
            best = numbers[i + 1]
    return best


# TODO 2：修好 find_max
#   要求：find_max([3,9,2]) → 9；find_max([]) → None；find_max([-5]) → -5
#   提示：先处理「空列表」这种情况；循环直接 for n in numbers 更简单（不用下标）
#   修完后用 B 段的输出自己验证（B 段已经替你调用了）


# ----------------------------------------------------------------------
# C. logging：把清洗过程记进日志
# ----------------------------------------------------------------------
RAW = [
    "光羽   138-0000-1111",      # → 有效 13800001111
    "小明 12800001111",          # → 会被丢弃：第二位是 2，不在 [3-9] 里
    "鼠鼠 999999999",            # → 会被丢弃：不是 11 位手机号
    "   ",                       # → 会被丢弃：空行
    "阿鬼 13700001111",          # → 有效 13700001111
]

LOG_PATH = OUT / "run.log"


def clean_rows(rows):
    """清洗手机号；每处理一行记一条日志。TODO 3：把 print 换成 logging"""
    ok, bad = [], []
    for i, row in enumerate(rows, start=1):
        digits = re.sub(r"\D", "", row)
        m = re.search(r"1[3-9]\d{9}", digits)
        if m:
            ok.append(m.group())
            print(f"[这里应该是 INFO] 第 {i} 行 → {m.group()}")            # ← 换成 logging
        else:
            bad.append(row)
            print(f"[这里应该是 WARNING] 第 {i} 行抽不到手机号：{row!r}")    # ← 换成 logging
    print(f"[这里应该是 INFO] 清洗结束：有效 {len(ok)} 条 / 丢弃 {len(bad)} 条")  # ← 换成 logging
    return ok, bad


# TODO 3：把 clean_rows 里那 3 处 print 换成 logging 调用
#   级别规则：正常的记 INFO，异常的记 WARNING
#   另外：在下面的 main 里把日志配置改成「同时写屏幕和文件 out_hw19/run.log」
#   提示：handlers=[logging.StreamHandler(), logging.FileHandler(LOG_PATH, encoding="utf-8")]
#   提示：basicConfig 一个进程只生效一次，别写两遍（或者加 force=True）
#   提示：日志默认走「标准错误」输出，所以它和 print 的行在屏幕上可能前后交错，属正常
#   最后自己回答：'小明 12800001111' 为什么被算成「丢弃」？
#     （不是 logging 的问题，是正则的问题——Day18 手写版会放过它，正则版不会）


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # 日志配置：现在只写屏幕、且只显示 WARNING 及以上
    # TODO 3：改成 level=INFO，并加上文件 handler（写进 LOG_PATH）
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    print("=== A. 读错误：三个故障各是什么错 ===")
    print("  bug_divide(10, 0)                 →", run_safely(bug_divide, 10, 0))
    print("  bug_lookup({'光羽': '111'}, '小明') →", run_safely(bug_lookup, {"光羽": "111"}, "小明"))
    print("  bug_format(None)                  →", run_safely(bug_format, None))

    print("\n=== B. 修 bug：find_max ===")
    print("  find_max([3, 9, 2]) →", run_safely(find_max, [3, 9, 2]))
    print("  find_max([])        →", run_safely(find_max, []))
    print("  find_max([-5])      →", run_safely(find_max, [-5]))

    print("\n=== C. logging：把清洗过程记进日志 ===")
    ok, bad = clean_rows(RAW)
    print(f"  有效 {len(ok)} 条：", ok)
    print(f"  丢弃 {len(bad)} 条：", bad)
    if LOG_PATH.exists():
        print(f"  （日志文件 {LOG_PATH.name}：{len(LOG_PATH.read_text(encoding='utf-8').splitlines())} 行）")
    else:
        print("  （还没有日志文件——TODO 3 的文件 handler 没配好）")


if __name__ == "__main__":
    main()
