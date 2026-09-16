import sys

from tabulate import tabulate

contacts = [
    ["光羽", "1111111111"],
    ["小明", "13800001111"],
    ["鼠鼠", "999999999"],
]

if __name__ == "__main__":
    print(tabulate(contacts, headers=["姓名", "电话"], tablefmt="github"))
    print("解释器：", sys.executable)


# 笔记
# 1. 配置过程：a.python -m venv .venv(创建虚拟环境) b.source .venv/Scripts/activate(激活虚拟环境) c.python -m pip install tabulate(安装tabulate) d.python hw16.py(运行脚本)
