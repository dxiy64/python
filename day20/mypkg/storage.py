import json

from pathlib import Path

PKG_DIR = Path(__file__).parent
PATH = PKG_DIR / "contacts.json"


def load(path=PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            contacts = json.load(f)
        return contacts
    except FileNotFoundError:
        return {}


def save(contacts, path=PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
