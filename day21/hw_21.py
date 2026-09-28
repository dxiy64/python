import json
import re


from pathlib import Path
from datetime import datetime
from collections import Counter

HERE = Path(__file__).parent
PATH = HERE / "ledger.json"


class ContactBook:
    def __init__(self, path=PATH):
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
            return {}

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.ledger, f, ensure_ascii=False, indent=4)

    def add(self, money, sort, note):
        if money < 0:
            print("金额不能为负数")
            return
        if re.match(r"\d+\.\d{1,2}", str(money)) is None:
            print("最多保留两位小数")
            return
        self.ledger = {
            "sort": sort,
            "money": money,
            "note": note,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.save()

    def show(self):
        if not self.ledger:
            print("还没有账")
            return
        for k, v in self.ledger.items():
            print(f"{k} : {v}")

    def stats(self):
        if not self.ledger:
            print("还没有账")
            return
        cs = dict(Counter([v["sort"] for v in self.ledger.values()]))
        hj = {}
        for b in cs:
            hj[b["sort"]] = hj.get(b["sort"], 0) + b["money"]
        print("各类累计是：", {k: round(v, 2) for k, v in hj.items()})
        print("总金额是：", round(sum([v["money"] for v in self.ledger.values()]), 2))


def show_menu():
    print("=", *40)
    print("1. 记一笔")
    print("2. 看流水")
    print("3. 统计")
    print("4. 存读档")
    print("5. 退出")
    print("=", *40)
