# -*- coding: utf-8 -*-
# ============================================
# Day 05 · 文件读写 —— 让数据关机也不丢
# 运行方法：python day05\day05.py
# ============================================

# ① 写文件：open(文件名, "w") -> with 自动帮你关好
# "w" = write，整个文件重写（没有就新建，有就清空重来！）
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("光羽 学习 Python 第5天\n")
    f.write("今天是2026年9月\n")
print("写完了，demo.txt 已生成在 day05 文件夹里")

# ② 追加模式 "a" = append，在文件末尾添一行，不动旧内容
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("新追加的一行\n")
print("追加完了")

# ③ 读文件："r" = read
with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()          # 一次读全部，装进字符串
print("--- 文件全部内容 ---")
print(content)

# ④ 按行读：一行一行拿
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("这一行是:", line.strip())   # strip() 去掉行尾的换行符

# ⑤ w 模式的“清空”陷阱：同一个文件用 w 再写，旧的全没了
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("只剩这一行了\n")
print("--- 再读一次，看旧内容还在吗 ---")
with open("demo.txt", "r", encoding="utf-8") as f:
    print(f.read())
