import os
import json

PKG_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PKG_DIR, "contacts15_hw.json")


def load(path=PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save(contacts, path=PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
