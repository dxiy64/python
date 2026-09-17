# -*- coding: utf-8 -*-
# ============================================
# day18.py · 讲义：正则表达式 re（找模式，不是找字面）
# 运行方法：cd day18 再 python day18.py
# 不用装库（re 是标准库）
# ============================================
import re

# ① 痛点：不用正则，你得自己一个个字符判断
print("=" * 52)
print("【演示 1】同一个需求，手写 vs 正则")
print("=" * 52)
phone = "13800001111"

# 手写版
manual_ok = len(phone) == 11 and phone[0] == "1" and phone.isdigit()
print("  手写版：len==11 and phone[0]=='1' and phone.isdigit() →", manual_ok)
print("      问题：只认“11位数字开头1”，但“1391234567a”这种也得写更多判断")
print("  再手写“提取文本里的电话”就基本写不动了（要逐字符扫描）")

# 正则版
m = re.fullmatch(r"1[3-9]\d{9}", phone)
print("  正则版：re.fullmatch(r'1[3-9]\\d{9}', phone) →", bool(m))
print()

# ② search / findall：从文本里“找”
print("=" * 52)
print("【演示 2】找：search（第一个）vs findall（全部）")
print("=" * 52)
text = "联系人：光羽 13800001111，小明 13912345678，座机 0769-8888888"
print("  原文：", text)
print("  re.search(r'1[3-9]\\d{9}', text)      →", re.search(r"1[3-9]\d{9}", text).group())
print("  re.findall(r'1[3-9]\\d{9}', text)     →", re.findall(r"1[3-9]\d{9}", text))
print("  re.findall(r'\\d+', text)             →", re.findall(r"\d+", text))
print("  re.findall(r'[\\u4e00-\\u9fa5]{2,}', text) →", re.findall(r"[\u4e00-\u9fa5]{2,}", text))
print()

# ③ sub：替换（脱敏、清洗）
print("=" * 52)
print("【演示 3】sub：把匹配到的部分换掉（真实项目里的“脱敏”）")
print("=" * 52)
p = "13800001111"
print("  原文：", p)
print("  中间四位打码 re.sub(r'(\\d{3})\\d{4}(\\d{4})', r'\\1****\\2', p) →",
      re.sub(r"(\d{3})\d{4}(\d{4})", r"\1****\2", p))
print("  去掉所有非数字 re.sub(r'\\D', '', '138-0000-1111') →", re.sub(r"\D", "", "138-0000-1111"))
print("  多个空白合成一个 re.sub(r'\\s+', ' ', '光羽   东莞\\t\\t111') →",
      repr(re.sub(r"\s+", " ", "光羽   东莞\t\t111")))
print()

# ④ fullmatch：校验（整串必须完全符合）
print("=" * 52)
print("【演示 4】校验：fullmatch 要求“整串完全符合”")
print("=" * 52)
samples = ["13800001111", "1380000111", "138000011112", "01800001111", "1380000111a"]
for s in samples:
    ok = bool(re.fullmatch(r"1[3-9]\d{9}", s))
    print(f"  {s:14} → {ok}")
print("  ⚠️ 对比 re.match：它只要求“开头匹配”，不管后面有什么")
print("      re.match(r'\\d+', '123abc')   → 匹配成功！", bool(re.match(r"\d+", "123abc")))
print("      re.fullmatch(r'\\d+', '123abc') → None      ", re.fullmatch(r"\d+", "123abc"))
print()

# ⑤ 分组 ( )：不只是“匹配到”，还想要里面的部分
print("=" * 52)
print("【演示 5】分组：把匹配结果拆成几块")
print("=" * 52)
row = "光羽|13800001111|东莞"
m = re.fullmatch(r"(.+?)\|(\d+)\|(.+)", row)
print("  原文：", row)
print("  模式：(.+?)\\|(\\d+)\\|(.+)")
print("  整体 group(0)  →", m.group(0))
print("  第1组 group(1) →", m.group(1))
print("  第2组 group(2) →", m.group(2))
print("  第3组 group(3) →", m.group(3))
print("  一次拿全部 groups() →", m.groups())
print("  带名字的分组 (?P<名字>...) →", re.fullmatch(r"(?P<name>.+?)\|(?P<phone>\d+)", "光羽|111").groupdict())
print()

# ⑥ 元字符速查（打印给你抄）
print("=" * 52)
print("【演示 6】常用元字符速查表")
print("=" * 52)
table = [
    (r"\d", "一个数字 0-9"),
    (r"\D", "非数字"),
    (r"\w", "字母/数字/下划线（中文也算）"),
    (r"\s", "空白（空格、Tab、换行）"),
    (r".", "任意一个字符（默认不含换行）"),
    (r"[abc]", "a 或 b 或 c 中任意一个"),
    (r"[^abc]", "除 a b c 以外任意一个"),
    (r"[3-9]", "范围：3 到 9"),
    (r"*", "前一个东西 0 次或多次"),
    (r"+", "前一个东西 1 次或多次"),
    (r"?", "前一个东西 0 次或 1 次"),
    (r"{3}", "前一个东西正好 3 次"),
    (r"{2,4}", "前一个东西 2 到 4 次"),
    (r"^", "字符串开头"),
    (r"$", "字符串结尾"),
    (r"|", "或"),
    (r"( )", "分组，可单独取出来"),
]
for code, desc in table:
    print(f"    {code:10} {desc}")
print()

# ⑦ 实战：清洗一堆脏数据
print("=" * 52)
print("【演示 7】实战：清洗脏数据")
print("=" * 52)
dirty = [
    "光羽   138-0000-1111",
    "小明|13912345678|深圳",
    "Tel: 13700002222",
    "鼠鼠 999999999",
    "  ",
]
print("  原始数据：")
for d in dirty:
    print("   ", repr(d))
print("  清洗：抽数字 → 只留手机号 → 空行的丢掉")
cleaned = []
for d in dirty:
    digits = re.sub(r"\D", "", d)
    phone = re.search(r"1[3-9]\d{9}", digits)
    if phone:
        cleaned.append(phone.group())
print("  结果：", cleaned, f"（{len(cleaned)}/{len(dirty)} 条有效）")
print()

# ⑧ 两个必踩的坑
print("=" * 52)
print("【演示 8】两个坑")
print("=" * 52)
print("  坑1：反斜杠——普通字符串里 \\d 会被当成转义")
print("      '\\d' 实际是：", repr("\\d"), " ← 侥幸没坏")
print("      '\\b' 实际是：", repr("\b"), " ← 变成了退格符！匹配全乱")
print("      正解：用 r'' 原始字符串 →", repr(r"\d"), repr(r"\b"), " ← 原样保留")
print()
print("  坑2：贪婪 vs 非贪婪")
s = "<a>光羽</a><b>小明</b>"
print("      原文：", s)
print("      .*  贪婪  →", re.findall(r"<.*>", s))
print("      .*? 非贪婪→", re.findall(r"<.*?>", s))
print()

print("=" * 52)
print("【一句话总结】")
print("  re 是“按模式找/换/校验”，不是“按字面找”")
print("  search 找第一个 / findall 找全部 / sub 替换 / fullmatch 整串校验")
print("  () 分组取细节；r'...' 原始字符串防转义；.*? 非贪婪")
print("=" * 52)
