import json
import re


from pathlib import Path
from datetime import datetime

HERE = Path(__file__).parent
LEDGER = HERE / "ledger.json"


class ContactBook:
    def __init__(self, path=LEDGER):
        self.path = path
        self.ledger = self.load()

    def __str__(self):
        return f"账本:{self.ledger}"

    def __len__(self):
        return len(self.ledger)

    def load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.ledger, f, ensure_ascii=False, indent=4)

    def add(self, money, sort, note):
        if money <= 0:
            print("金额要大于0")
            return
        self.ledger.append(
            {
                "sort": sort,
                "money": money,
                "note": note,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            }
        )
        self.save()

    def show(self):
        if not self.ledger:
            print("还没有账")
            return
        for record in self.ledger:
            print(
                f"{record['time']} "
                f"{record['money']} "
                f"{record['sort']} "
                f"{record['note']}"
            )

    def stats(self):
        if not self.ledger:
            print("还没有账")
            return
        cs = {}
        for record in self.ledger:
            sort = record["sort"]
            money = record["money"]
            cs[sort] = cs.get(sort, 0) + money
        print("各类累计是：", {sort: round(money, 2) for sort, money in cs.items()})
        total = 0
        for record in self.ledger:
            total += record["money"]
        print("总支出：", round(total, 2))


def show_menu():

    print("=", *40)
    print("1. 记一笔")
    print("2. 看流水")
    print("3. 统计")
    print("4. 存读档")
    print("q. 退出")
    print("=", *40)


def main():
    book = ContactBook()
    while True:
        show_menu()
        choice = input("请选择操作：").strip()
        if choice == "1":
            while True:
                money_text = input("请输入金额：").strip()
                if re.fullmatch(r"\d+(\.\d{1,2})?", money_text) is None:
                    print("请输入大于 0 且最多两位小数的金额")
                    continue
                money = float(money_text)
                if money <= 0:
                    print("金额必须大于 0")
                    continue
                break
            sort = input("请输入分类：").strip()
            note = input("请输入备注：").strip()
            book.add(money, sort, note)

        elif choice == "2":
            book.show()
        elif choice == "3":
            book.stats()
        elif choice == "4":
            book.save()
        elif choice == "q":
            break
        else:
            print("输入错误，请重新输入")


if __name__ == "__main__":
    main()
