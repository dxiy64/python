# -*- coding: utf-8 -*-
# ============================================
# homework04.py · 通讯录小管家（字典 + 函数）
# 运行方法：cd day04 再 python homework04.py
# 本课只学：dict 增删改查 + def + return
# ============================================

# 名字 → 电话
contacts = {"光羽": "18486311094", "小明": "13800001111"}

# 新增一个联系人（写死即可）
contacts["小红"] = "13900002222"


def find_phone(name):
    """输入名字返回电话，找不到返回“查无此人”"""
    if name in contacts:
        return contacts[name]
    return "查无此人"


def show_all():
    """把所有联系人打印成“名字：电话”"""
    for name, phone in contacts.items():
        print(f"{name}：{phone}")


def main():
    while True:
        name = input("要查谁？（输入 q 退出）：").strip()
        if name == "q":
            print("已退出查询，再见！")
            break
        print(f"{name} 查询结果：{find_phone(name)}")

    # 自测：一个能查到，一个查不到
    print(find_phone("光羽"))  # 应打印 18486311094
    print(find_phone("陌生人"))  # 应打印 查无此人

    print("--- 全部联系人 ---")
    show_all()


if __name__ == "__main__":
    main()

# 笔记
# 1. 字典用 {} 装键值对：{"光羽": "18486311094"}
# 2. 取值 contacts["光羽"]；键不存在会报 KeyError，先用 in 判断
# 3. contacts["小红"] = ...：键已存在是改，不存在是新增
# 4. for k, v in contacts.items()：键和值一起拿
# 5. return 把结果递出来给调用方，print 只是显示到屏幕
