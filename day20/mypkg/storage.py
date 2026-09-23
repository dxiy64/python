import json
import logging

from pathlib import Path

PKG_DIR = Path(__file__).parent
PATH = PKG_DIR / "contacts.json"
OUT = PKG_DIR.parent / "out"
LOG_PATH = OUT / "app.log"

OUT.mkdir(parents=True, exist_ok=True)  # 疑问

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def load(path=PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            contacts = json.load(f)
        return contacts
    except FileNotFoundError:
        logging.error("%s 未找到文件", path)
        return {}
    except json.JSONDecodeError:
        logging.error("读档失败: %s 不是合法 JSON，按空通讯录处理", path)
        return {}


def save(contacts, path=PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
