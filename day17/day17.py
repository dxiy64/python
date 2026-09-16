# -*- coding: utf-8 -*-
# ============================================
# day17.py · 讲义：四个最常用的标准库
#   pathlib / csv / datetime / collections
# 运行方法：cd day17 再 python day17.py
# 不用装任何库（全是 Python 自带）
# ============================================
import csv
import datetime
import shutil
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent          # 本文件所在目录，Path 对象
OUT = HERE / "out"                    # 用 / 拼路径，比 os.path.join 顺眼
if OUT.exists():                      # 每次从干净状态开始
    shutil.rmtree(OUT)
OUT.mkdir()

# ① 痛点：老写法 vs 新写法
print("=" * 50)
print("【演示 1】同一件事，老写法 vs 新写法")
print("=" * 50)
print("老写法（os.path 系列，一串函数拼来拼去）：")
print("   os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'a.csv')")
print("新写法（pathlib，像操作对象一样）：")
print("   Path(__file__).parent / 'out' / 'a.csv'")
print("   实际结果 =", HERE / "out" / "a.csv")
print()

# ② pathlib：路径本身就是一个对象
print("=" * 50)
print("【演示 2】pathlib：路径是对象，自带一堆方法")
print("=" * 50)
p = HERE / "data" / "通讯录.txt"
print("  拼出来的路径     ：", p)
print("  只要文件名 .name ：", p.name)
print("  去掉后缀 .stem   ：", p.stem)
print("  只要后缀 .suffix ：", p.suffix)
print("  上一层目录 .parent：", p.parent)
print("  存在吗 .exists() ：", p.exists())
p.parent.mkdir(parents=True, exist_ok=True)      # 父目录不存在就一起建
p.write_text("光羽：111\n小明：222\n", encoding="utf-8")   # 一行写文件
print("  写完后再问存在吗 ：", p.exists())
print("  读回来 .read_text()：", repr(p.read_text(encoding="utf-8")))
print("  文件多大 .stat().st_size：", p.stat().st_size, "字节")
p.unlink(missing_ok=True)                        # 删除；不存在也不报错（Day14 那个 if exists 的替代）
print("  删掉后再问存在吗 ：", p.exists())
print()

# ③ csv：表格数据不要手拼逗号
print("=" * 50)
print("【演示 3】csv：读写表格，别再手拼字符串")
print("=" * 50)
rows = [
    {"姓名": "光羽", "电话": "18486311094", "城市": "东莞"},
    {"姓名": "小明", "电话": "13800001111", "城市": "深圳"},
    {"姓名": "鼠鼠", "电话": "999999999", "城市": "东莞"},
]
csv_path = OUT / "contacts17.csv"
# newline="" 是 Windows 上的关键：不加会多出空行
with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "电话", "城市"])
    writer.writeheader()          # 先写表头
    writer.writerows(rows)        # 再写数据
print("  写好的文件：", csv_path)
print("  文件内容：")
print("   " + csv_path.read_text(encoding="utf-8-sig").replace("\n", "\n   ").rstrip())

with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)    # 每行变成字典，表头自动变键
    for row in reader:
        print(f"  读到的每行是字典：{row}   → 取电话 {row['电话']}")
print()

# ④ datetime：时间要当"日期对象"用，别当字符串拼
print("=" * 50)
print("【演示 4】datetime：算时间、格式化、时间戳文件名")
print("=" * 50)
now = datetime.datetime.now()
print("  现在的时间对象     ：", now)
print("  格式化成人类读的    ：", now.strftime("%Y-%m-%d %H:%M:%S"))
print("  只要日期           ：", now.strftime("%Y-%m-%d"))
print("  适合做文件名的时间戳：", now.strftime("%Y%m%d_%H%M%S"))
print("  今天是星期几        ：", ["一", "二", "三", "四", "五", "六", "日"][now.weekday()])
print("  现在秒级时间戳      ：", int(now.timestamp()))

text = "2026-09-01"
d = datetime.datetime.strptime(text, "%Y-%m-%d")     # 字符串 → 日期对象
print(f"  把字符串 {text!r} 转成日期对象：", d, type(d).__name__)
print("  加 30 天           ：", (d + datetime.timedelta(days=30)).strftime("%Y-%m-%d"))
print("  减 7 天            ：", (d - datetime.timedelta(days=7)).strftime("%Y-%m-%d"))
diff = now - d
print(f"  今天减 {text} 差了多少天：", diff.days, "天")
print()

# ⑤ collections：计数和分组，别自己写循环
print("=" * 50)
print("【演示 5】collections：Counter 计数 / defaultdict 分组")
print("=" * 50)
names = ["光羽", "小明", "鼠鼠", "小强", "光光"]
print("  数据：", names)

c = Counter(names)
print("  Counter（每个名字出现几次）：", dict(c))
print("  Counter 另一种常见用法——统计首字母：")
first = Counter(n[0] for n in names)
print("    ", dict(first))
print("    出现最多的 2 个 .most_common(2)：", first.most_common(2))

print("  defaultdict：按首字母分组，不用先判断键存在不存在")
groups = defaultdict(list)
for n in names:
    groups[n[0]].append(n)
for k, v in groups.items():
    print(f"     {k} 开头：{v}")
print("  （对比：用普通 dict 得写 if k not in d: d[k] = [] 再 append）")
print()

# ⑥ 合体：给通讯录做一份带时间戳的报表
print("=" * 50)
print("【演示 6】四个库合体：导出 CSV + 生成报表")
print("=" * 50)
report = OUT / f"通讯录报表_{now.strftime('%Y%m%d_%H%M%S')}.txt"
lines = [f"导出时间：{now.strftime('%Y-%m-%d %H:%M:%S')}", f"共 {len(rows)} 人", ""]
by_city = defaultdict(list)
for r in rows:
    by_city[r["城市"]].append(r["姓名"])
for city, people in by_city.items():
    lines.append(f"{city}（{len(people)}人）：{'、'.join(people)}")
report.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("  报表文件：", report.name)
print("  报表内容：")
print("   " + report.read_text(encoding="utf-8").replace("\n", "\n   ").rstrip())
print()
print("  产出的文件都在：", OUT)
for f in sorted(OUT.iterdir()):
    print("    ", f.name, "→", f.stat().st_size, "字节")
print()
print("=" * 50)
print("【一句话总结】")
print("  pathlib     管路径（对象化，别用字符串拼）")
print("  csv         管表格（别手写逗号）")
print("  datetime    管时间（算的时候用对象，给人看时再格式化）")
print("  collections 管计数和分组（Counter / defaultdict）")
print("=" * 50)
