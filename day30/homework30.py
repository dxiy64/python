import re
import sqlite3


from pathlib import Path
from datetime import datetime

HERE = Path(__file__).parent
OUT = HERE / "out"
OUT.mkdir(exist_ok=True)
DB = OUT / "ledger.db"

MONEY_RE = re.compile(r"\d+(\.\d{1,2})?")


class ContactBook:
    def __init__(self, path=DB):
        self.conn = sqlite3.connect(path)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS ledger(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        money REAL NOT NULL,
        sort TEXT NOT NULL,
        note TEXT NOT NULL,
        time TEXT NOT NULL
        )""")

    def add(self, money, sort, note):
        if re.fullmatch(MONEY_RE, money) is None or float(money) <= 0:
            print("金额不合法")
            return
        else:
            self.conn.execute(
                "INSERT INTO ledger(money, sort, note, time) VALUES (?, ?, ?, ?)",
                (money, sort, note, datetime.now().strftime("%Y-%m-%d %H:%M")),
            )
        self.conn.commit()
        print("添加成功")
