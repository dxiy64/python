# -*- coding: utf-8 -*-
# ============================================
# homework18.py · 通讯录数据清洗器（正则实战）
# 运行方法：cd day18 再 python homework18.py
# 这个文件直接运行不会报错，但 TODO 的功能是缺的——补完再运行验证
# ============================================
import re

# 一堆“脏数据”：格式五花八门
RAW = [
    "光羽   138-0000-1111",       # 空格 + 横杠
    "小明|13912345678|深圳",       # 竖线分隔
    "Tel: 13700002222",           # 带前缀
    "鼠鼠 999999999",              # 位数不对
    "   ",                        # 空白行
    "阿鬼 0773-1234567",           # 座机，不是手机
    "光光 138 0000 3333",          # 空格分隔
]


def to_digits(text):
    """把文本里所有非数字去掉，只留数字"""
    # TODO 1（必做）: 用 re.sub 把非数字删掉。
    #   提示：re.sub(模式, 替换成什么, 原文本)
    #         删除 = 替换成空字符串 ''
    #         “非数字”的模式是 \D
    #   验证：to_digits("138-0000-1111") → '13800001111'
    print("[TODO 1 未完成]")
    return ""


def find_mobile(digits):
    """从一串数字里找出第一个手机号（1开头11位），找不到返回 None"""
    # TODO 2（必做）: 用 re.search 找手机号。
    #   手机号模式：1[3-9]\d{9}
    #   search 返回“匹配对象”或 None；匹配成功要用 .group() 取值
    #   提示：
    #     m = re.search(r"1[3-9]\d{9}", digits)
    #     return m.group() if m else None
    #   验证：find_mobile("13800001111") → '13800001111'
    #        find_mobile("999999999")   → None
    print("[TODO 2 未完成]")
    return None


def mask(phone):
    """手机号中间 4 位打码：13800001111 → 138****1111"""
    # TODO 3（必做）: 用 re.sub + 分组。
    #   模式：(前3位)(中间4位)(后4位)  →  (\d{3})\d{4}(\d{4})
    #   替换：\1****\2   （在替换串里用 \1 \2 引用分组）
    #   注意：替换串建议写成 r'\1****\2'（原始字符串）
    #   验证：mask("13800001111") → '138****1111'
    print("[TODO 3 未完成]")
    return phone


def is_valid_mobile(s):
    """校验是不是合法的手机号（整串完全符合）"""
    # TODO 4（必做）: 用 re.fullmatch 校验。
    #   注意用 fullmatch 而不是 match（match 只看开头，'1380000111a' 也会通过）
    #   验证：is_valid_mobile('13800001111') → True
    #        is_valid_mobile('1380000111')  → False
    #        is_valid_mobile('1380000111a') → False
    print("[TODO 4 未完成]")
    return False


def clean_all(raw):
    """批量清洗：返回 (有效手机号列表, 被丢掉的原因说明列表)"""
    # TODO 5（进阶选做）: 遍历 raw，对每条：
    #   ① to_digits 抽数字
    #   ② find_mobile 找手机号
    #   ③ 找到就放进 ok 列表；找不到就把原文放进 bad 列表
    #   提示：写一个循环，最后 return ok, bad
    print("[TODO 5 未完成]")
    return [], []


if __name__ == "__main__":
    print("=== 单条测试 ===")
    print("  to_digits('138-0000-1111') =", to_digits("138-0000-1111"))
    print("  find_mobile('13800001111')  =", find_mobile("13800001111"))
    print("  find_mobile('999999999')    =", find_mobile("999999999"))
    print("  mask('13800001111')         =", mask("13800001111"))
    print("  is_valid_mobile('13800001111')  =", is_valid_mobile("13800001111"))
    print("  is_valid_mobile('1380000111a')  =", is_valid_mobile("1380000111a"))

    print("\n=== 批量清洗 ===")
    ok, bad = clean_all(RAW)
    print(f"  有效 {len(ok)} 条：", ok)
    print(f"  丢弃 {len(bad)} 条：", bad)

    print("\n=== 期望输出（补完 TODO 后应该长这样）===")
    print("  有效 4 条： ['13800001111', '13912345678', '13700002222', '13800003333']")
    print("  丢弃 3 条： ['鼠鼠 999999999', '   ', '阿鬼 0773-1234567']")

    print("\n=== 脱敏后的报表（进阶做完可以试试）===")
    for p in ok:
        print("   ", mask(p))
    # 想更像真报表？结合 Day17 的 csv/pathlib，把清洗结果存成文件
