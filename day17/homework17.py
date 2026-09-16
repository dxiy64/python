# -*- coding: utf-8 -*-
# ============================================
# homework17.py · 通讯录导出器（pathlib + csv + datetime + collections）
# 运行方法：cd day17 再 python homework17.py
# 这个文件直接运行不会报错，但 TODO 的功能是缺的——补完再运行验证
# ============================================
import csv
import datetime
import shutil
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out_hw"          # 所有产出都丢进这个目录

CONTACTS = [
    {"姓名": "光羽", "电话": "18486311094", "城市": "东莞"},
    {"姓名": "小明", "电话": "13800001111", "城市": "深圳"},
    {"姓名": "鼠鼠", "电话": "999999999", "城市": "东莞"},
    {"姓名": "小强", "电话": "13700002222", "城市": "广州"},
    {"姓名": "光光", "电话": "13900003333", "城市": "深圳"},
]


def export_csv(rows, path):
    """把联系人写成 CSV 文件（表头：姓名/电话/城市）"""
    # TODO 1（必做）: 用 csv.DictWriter 写文件。
    #   提示（三行核心）：
    #     with path.open("w", encoding="utf-8-sig", newline="") as f:
    #         writer = csv.DictWriter(f, fieldnames=["姓名", "电话", "城市"])
    #         writer.writeheader()          # 写表头
    #         writer.writerows(rows)        # 一次写多行
    #   注意 newline="" 不能省（Windows 上会多出空行），encoding 用 utf-8-sig（Excel 打开不乱码）
    print(f"[TODO 1 未完成] 应该把 {len(rows)} 行写到 {path.name}")


def load_csv(path):
    """读回 CSV，返回字典列表"""
    # TODO 2（必做）: 用 csv.DictReader 读回来并 return 列表。
    #   提示：
    #     with path.open("r", encoding="utf-8-sig", newline="") as f:
    #         return list(csv.DictReader(f))
    #   验证：读回来的每行应该是 {'姓名': '光羽', '电话': '...', '城市': '...'}
    print(f"[TODO 2 未完成] 应该从 {path.name} 读回 {len(CONTACTS)} 行")
    return []


def make_report(rows, now):
    """生成报表文件，返回文件路径。文件名带时间戳"""
    # TODO 3（必做）: 拼出报表内容并写文件。
    #   要求：
    #     ① 文件名形如 报表_20260916_180000.txt
    #        写法：path = OUT / f"报表_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    #        ⚠️ 别写成 OUT / "报表_" + now.strftime(...) + ".txt" —— / 的优先级比 + 高，
    #           会被理解成 (OUT / "报表_") + ... → TypeError: unsupported operand type(s) for +: 'WindowsPath' and 'str'
    #     ② 内容四部分：
    #        - 导出时间：now.strftime("%Y-%m-%d %H:%M:%S")
    #        - 共 N 人
    #        - 按城市分组：东莞（2人）：光羽、鼠鼠       ← 用 defaultdict(list)
    #        - 电话后 5 位统计：出现最多的 2 个           ← 用 Counter + most_common(2)
    #   提示（写文件一行搞定）：path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("[TODO 3 未完成] 应该生成带时间戳的报表文件")
    return None


def main():
    # 每次从干净状态开始（Day17 演示里用 shutil.rmtree + mkdir）
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    print("输出目录：", OUT)

    csv_path = OUT / "contacts17_hw.csv"
    export_csv(CONTACTS, csv_path)

    rows = load_csv(csv_path)
    for r in rows:
        print("  读回一行：", r)

    now = datetime.datetime.now()
    report_path = make_report(rows, now)
    if report_path:
        print("\n--- 报表文件叫：", report_path.name, "---")
        print(report_path.read_text(encoding="utf-8"))

    # TODO 4（进阶选做）: 打印一条汇总，比如
    #   "本次共导出 5 人，覆盖 3 个城市，输出目录 ...\n   "
    #   城市数量可以用 len({r['城市'] for r in rows})（集合推导式，去重）


if __name__ == "__main__":
    main()
