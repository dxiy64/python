import logging

from pathlib import Path
from .storage import PATH
from .book import ContactBook


def show_menu():
    print("=" * 40)
    print("1. 添加联系人")
    print("2. 删除联系人")
    print("3. 更新联系人")
    print("4. 查找联系人")
    print("5. 查找联系人(模糊查询)")
    print("6. 重命名联系人")
    print("7. 显示所有联系人")
    print("8. 导出通讯录")
    print("9. 统计")
    print("q. 退出")
    print("=" * 40)


def main():
    book = ContactBook()
    while True:
        show_menu()
        choose = input("请选择操作：").strip()
        if choose == "q":
            print("退出通讯录")
            break

        elif choose == "1":
            name = input("请输入姓名：").strip()
            phone = input("请输入手机号：").strip()
            book.add(name, phone)

        elif choose == "2":
            name = input("请输入姓名：").strip()
            book.delete(name)

        elif choose == "3":
            name = input("请输入需要更新的姓名：").strip()
            phone = input("请输入更新的手机号：").strip()
            book.update(name, phone)

        elif choose == "4":
            name = input("请输入查找的姓名：").strip()
            book.find(name)

        elif choose == "5":
            keyword = input("请输入查找的关键词：").strip()
            book.search(keyword)

        elif choose == "6":
            old = input("请输入要重命名的姓名：").strip()
            new = input("请输入新的姓名：").strip()
            book.rename(old, new)

        elif choose == "7":
            print("通讯录名单如下：")
            book.show_all()

        elif choose == "8":
            print("导出通讯录")
            book.export()

        elif choose == "9":
            book.stats()

        elif choose not in ["1", "2", "3", "4", "5", "6", "7", "q"]:
            print("输入有误，请重新输入")


if __name__ == "__main__":
    if not PATH.exists():
        PATH.write_text("{}", encoding="utf-8")
    main()
