from .storage import load, save, PATH


class ContactBook:
    def __init__(self, path=PATH):
        self.path = path
        self.contacts = load(self.path)

    def __str__(self):
        return f"通讯录（{len(self.contacts)}人）：{self.contacts}"

    def __len__(self):
        return len(self.contacts)

    def add(self, name, phone):
        if not phone.isdigit():
            print("电话只能是数字！")
            return
        self.contacts[name] = phone
        save(self.contacts, self.path)
        print(f"已加上 {name}")

    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            save(self.contacts, self.path)
            print(f"已删除 {name}")
        else:
            print("查无此人")

    def update(self, name, phone):
        if name not in self.contacts:
            print("查无此人")
            return
        if not phone.isdigit():
            print("电话只能是数字！")
            return
        self.contacts[name] = phone
        save(self.contacts, self.path)
        print(f"{name} 已更新")

    def rename(self, old, new):
        if old not in self.contacts:
            print("查无此人")
            return
        if new in self.contacts:
            print(f"{new} 已存在，换个名字吧")
            return
        self.contacts[new] = self.contacts[old]
        del self.contacts[old]
        save(self.contacts, self.path)
        print(f"已改名 {old} -> {new}")

    def find(self, name):
        if name in self.contacts:
            return self.contacts[name]
        return "查无此人"

    def search(self, keyword):
        found = False
        for name, phone in self.contacts.items():
            if keyword in name:
                print(f"{name} {phone}")
                found = True
        if not found:
            print("查无此人")

    def show_all(self):
        if not self.contacts:
            print("空的，先加一个吧")
        for name, phone in self.contacts.items():
            print(f"{name}：{phone}")
