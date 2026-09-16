# -*- coding: utf-8 -*-
# ============================================
# mybook/cli.py · 命令行界面（只能靠 python -m mybook.cli 跑）
# 运行方法：cd day15 再 python -m mybook.cli
# ============================================
import os

from .book import ContactBook        # 相对导入：.book = 同一个包里的 book.py
from .storage import PATH            # 数据文件路径


def show_menu():
    print("=" * 34)
    print("1.看全部 2.查 3.加 4.删 5.改电话 6.改名 7.模糊搜 q.退出")
    print("=" * 34)


def main():
    book = ContactBook()
    print(book)
    while True:
        show_menu()
        choose = input("选：").strip()
        if choose == "q":
            print(f"共 {len(book)} 人，再见！")
            break
        elif choose == "1":
            book.show_all()
        elif choose == "2":
            who = input("查谁：").strip()
            print(f"{who}：{book.find(who)}")
        elif choose == "3":
            name = input("名字：").strip()
            if not name:
                print("名字不能为空！")
                continue
            book.add(name, input("电话：").strip())
        elif choose == "4":
            book.delete(input("删谁：").strip())
        elif choose == "5":
            name = input("改谁的电话：").strip()
            book.update(name, input("新电话：").strip())
        elif choose == "6":
            old = input("旧名字：").strip()
            book.rename(old, input("新名字：").strip())
        elif choose == "7":
            book.search(input("关键字：").strip())
        else:
            print("只能选 1-7/q，重选！")


if __name__ == "__main__":
    if os.path.exists(PATH):     # 演示从空开始
        os.remove(PATH)
    main()
