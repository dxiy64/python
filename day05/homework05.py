# -*- coding: utf-8 -*-
# ============================================
# homework05.py · 记账本（存进文件，关机不丢）
# 运行方法：cd day05 再 python homework05.py
# 本课只学：open 的 w / a / r + with 自动关闭
# ============================================

ACCOUNT_FILE = "account.txt"


def add_record():
    """先问清内容再开文件：打开时间越短越好"""
    what = input("买了什么：").strip()
    money = input("花了多少钱：").strip()
    with open(ACCOUNT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{what} -{money}元\n")


def show_records():
    """读一遍文件：既打印明细，又数出有几笔"""
    count = 0
    with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
            count += 1
    print(f"一共记了 {count} 笔账目")


def main():
    add_record()
    show_records()


if __name__ == "__main__":
    main()

# 笔记
# 1. with open(...) as f：标准写法，退出 with 自动关文件
# 2. "w" 重写整份文件；"a" 在末尾追加；"r" 只读
# 3. 先 input 问完再 open 写：别占着文件等用户打字
# 4. 一次 for 循环同时做“打印 + 计数”，不用读两遍文件
# 5. line.strip()：去掉行尾换行符再显示
