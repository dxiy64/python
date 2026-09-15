# -*- coding: utf-8 -*-
# ============================================
# homework13.py · 给通讯录的联系人分类（读懂+改，工程师的日常）
# 运行方法：cd day13 再 python homework13.py
# 这个文件直接运行不会报错，但 TODO 的功能是缺的——补完再运行验证
# ============================================


# 爸爸：所有联系人都有的东西
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(f"{self.name}：{self.phone}")


# 儿子①：朋友，多一个备注
class Friend(Contact):
    def __init__(self, name, phone, remark):
        # TODO 1（必做）: 先让爸爸装 name 和 phone（提示：super().__init__(...)），
        #   再自己装 self.remark。
        super().__init__(name, phone)
        self.remark = remark

    def show(self):
        # TODO 2（必做）: 先调爸爸那版 show()（提示：super().show()），
        #   再打印一行“  备注：xxx”。
        super().show()
        print(f"  备注：{self.remark}")


# 儿子②：同事，多一个公司
class Workmate(Contact):
    def __init__(self, name, phone, company):
        # TODO 3（进阶选做）: 照 Friend 的写法，装 name/phone/company。
        super().__init__(name, phone)
        self.company = company

    def show(self):
        # TODO 4（进阶选做）: 先 super().show()，再打印“  公司：xxx”。
        super().show()
        print(f"  公司：{self.company}")


# 多态：同一个函数，传谁进来就显示谁的样子
def show_all(contacts):
    for c in contacts:
        c.show()


if __name__ == "__main__":
    people = [
        Contact("路人甲", "100"),
        Friend("光羽", "111", "老同学"),
        Workmate("小明", "222", "Python科技"),
    ]
    show_all(people)
    # 补完 TODO 后，预期输出是：
    # 路人甲：100
    # 光羽：111
    #   备注：老同学
    # 小明：222
    #   公司：Python科技
