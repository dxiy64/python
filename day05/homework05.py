# -*- coding: utf-8 -*-
# ============================================
# homework05.py · 记账本（存进文件，关机不丢）
# ============================================

# TODO 1: 让用户输入一笔支出说明和金额，用 f-string 拼成一行
#         例如 "奶茶 -25元"，用 "a" 模式追加进 account.txt
# what = input("买了什么：")
# money = input("花了多少钱：")
# with open(???, "a", encoding="utf-8") as f:
#     f.write(???)

with open("account.txt", "a", encoding="utf-8") as f:
    what = input("买了什么：")
    money = input("花了多少钱：")
    f.write(f"{what} -{money}元\n")

# 优化建议
#   what = input("买了什么：")
#   money = input("花了多少钱：")
#   with open("account.txt", "a", encoding="utf-8") as f:
#        f.write(f"{what} -{money}元\n")
#   区别是先写完数据再开门

# TODO 2: 读取 account.txt，按行打印所有账目（用 for line in f）
with open("account.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# TODO 3 (进阶选做): 顺便统计一共记了几笔（提示：len(打开的文件对象) 不行哦，
#   想办法在 for 循环里数，跟 Day3 的 count 累加一个道理）

count = 0
with open("account.txt", "r", encoding="utf-8") as f:
    for line in f:
        count += 1
print(f"一共记了 {count} 笔账目")

# 笔记
# 1. with open("文件名", "模式") as f: 是 Python 里读写文件的标准写法，with 会帮你自动关好文件，f不是固定写法，可以换成其他名字，但习惯上都用 f
# 2. "w" = write，整个文件重写（没有就新建，有就清空重来！）
# 3. "a" = append，在文件末尾添一行，不动旧内容
# 4. "r" = read，读文件，默认模式，文件不存在会报错
# 5. f.write("内容") 写入内容，f.read() 一次读全部，f.readline() 一次读一行，f.readlines() 一次读多行
# 6. for line in f: 可以一行一行遍历文件内容，line.strip() 的作用是去掉行尾的换行符，例如 "奶茶 -25元\n" 变成 "奶茶 -25元"
# 7. w 模式的“清空”陷阱：同一个文件用 w 再写，旧的全没了
