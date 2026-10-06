"""Day26 作业：菜单版 sqlite 记账本（骨架 + 5 个 TODO）

跑法（在 day26 目录里）：
    python homework26.py

要求：一次只做一个 TODO，做完就跑一遍验收命令，看着输出往下走。
聚合统计直接抄你 Day25 的 total / month_total / stats_by_sort / month_report。
金额校验沿用 Day23 的正则 MONEY_RE，且 > 0。

验收（验收前先删库，保证从空开始）：
    rm -f ledger.db
    printf '1\\n12.5\\n午饭\\n猪脚饭\\n1\\n6.0\\n交通\\n地铁\\n2\\n6\\n2026-10\\n7\\n2\\nq\\n' | python homework26.py
预期：看流水 2 笔；10 月报表"共2笔"；导出 ledger.csv 2 笔数据+1行表头；exit=0。
"""
import csv
import re
import sqlite3
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
DB = HERE / "ledger.db"
CSV_PATH = HERE / "ledger.csv"

MONEY_RE = r"\d+(\.\d{1,2})?"


class LedgerDB:
    def __init__(self, path=DB):
        # TODO 1：连库 + 建表（照抄 Day24 的 _create_table）
        raise NotImplementedError("TODO 1：连库建表")

    def add(self, money_text, sort, note):
        # TODO 2：金额走 MONEY_RE 校验 + > 0，合法才 INSERT + commit；非法打印"金额不合法"
        raise NotImplementedError("TODO 2：记一笔")

    def show(self):
        # TODO 3：SELECT * ORDER BY time 全打印，空表打印"还没有账"
        raise NotImplementedError("TODO 3：看流水")

    def month_report(self, month):
        # TODO 4：抄 Day25 的 COUNT+SUM+GROUP BY；空月打印"X 月还没有账"
        raise NotImplementedError("TODO 4：月度报表")

    def export_csv(self, path=CSV_PATH):
        # TODO 5：SELECT 全端上桌，csv.writer 写文件（utf-8-sig + newline=""），打印"导出 N 笔"
        raise NotImplementedError("TODO 5：导出CSV")

    def close(self):
        self.conn.close()


def show_menu():
    print("=" * 40)
    print("1. 记一笔")
    print("2. 看流水")
    print("6. 按月统计")
    print("7. 导出csv")
    print("q. 退出")
    print("=" * 40)


def main():
    book = LedgerDB()
    try:
        while True:
            show_menu()
            choice = input("请选择操作：").strip()
            if choice == "1":
                money = input("请输入金额：").strip()
                sort = input("请输入分类：").strip()
                note = input("请输入备注：").strip()
                book.add(money, sort, note)
            elif choice == "2":
                book.show()
            elif choice == "6":
                month = input("请输入月份：").strip()
                book.month_report(month)
            elif choice == "7":
                book.export_csv()
            elif choice == "q":
                break
            else:
                print("输入错误，请重新输入")
    finally:
        book.close()


if __name__ == "__main__":
    main()
