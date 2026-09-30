import json
import re
import csv


from pathlib import Path
from datetime import datetime

HERE = Path(__file__).parent
LEDGER = HERE / "ledger.json"
OUT_PATH = HERE / "ledger.csv"


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

    # 第22天作业

    def sort_out(self, sort):
        dy = [b for b in self.ledger if b["sort"] == sort]
        if not dy:
            print("该分类还没有账")
            return
        for record in dy:
            print(
                f"{record['time']} {record['money']} {record['sort']} {record['note']}"
            )

    def month_out(self, month):
        dy = [b for b in self.ledger if b["time"][:10] == month]
        hj = {}
        for b in dy:
            hj[b["sort"]] = hj.get(b["sort"], 0) + b["money"]

    def monthcsv_out(self, month):
        yd = [b for b in self.ledger if b["time"][:7] == month]

        # 23天作业
        if not yd:
            print("{month}月份还没有账")
            return

        hj = {}
        for b in yd:
            hj[b["sort"]] = hj.get(b["sort"], 0) + b["money"]
        print(
            f"月份：{month}，共{len(yd)}笔，总支出：{sum(hj.values())}，各分类消费如下：{hj},"
        )

    def out_csv(self):
        with open(OUT_PATH, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["时间", "金额", "分类", "备注"])
            for record in self.ledger:
                writer.writerow(
                    [
                        record["time"],
                        record["money"],
                        record["sort"],
                        record["note"],
                    ]
                )

    # 第23天作业

    def delete(self, index, sx):
        if re.fullmatch(r"\d+", sx) is None:
            print("请输入数字")
            return
        elif sx <= 0:
            print("请输入大于0的数字")
            return
        index = sx - 1
        del self.ledger[index]
        self.save()

    def update(self, index, sx, money=None, sort=None, note=None):
        if re.fullmatch(r"\d+(\.\d{1,2})?", money) is None:
            print("请输入大于0且最多两位小数的金额")
            return
        money = float(money)
        if money <= 0:
            print("金额必须大于0")
            return
        if money is not None:
            self.ledger[index]["money"] = money
        if sort is not None:
            self.ledger[index]["sort"] = sort
        if note is not None:
            self.ledger[index]["note"] = note
        self.save()


def show_menu():

    print("=" * 40)
    print("1. 记一笔")
    print("2. 看流水")
    print("3. 统计")
    print("4. 存读档")
    print("5. 分类统计")
    print("6. 按月统计")
    print("7. 导出csv")
    print("8. 删一笔")
    print("9. 改一笔")
    print("q. 退出")
    print("=" * 40)


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
        elif choice == "5":
            sort = input("请输入分类：").strip()
            book.sort_out(sort)
        elif choice == "6":
            month = input("请输入月份：").strip()
            book.monthcsv_out(month)
        elif choice == "7":
            book.out_csv()
        elif choice == "8":
            sx = input("要删除第几笔：").strip()
            book.delete()
        elif choice == "9":
            sx = input("要修改第几笔：").strip()
            print("提示：如果不修改某一项，请直接回车")
            money = input("请输入金额：").strip()
            sort = input("请输入分类：").strip()
            note = input("请输入备注：").strip()
            book.update(sx, money, sort, note)
        elif choice == "q":
            break
        else:
            print("输入错误，请重新输入")


if __name__ == "__main__":
    main()
