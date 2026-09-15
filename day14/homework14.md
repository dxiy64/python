# Day 14 作业：把大文件拆成两个

## 任务

`day14/big.py` 是一个能跑的菜单版通讯录，但它把「工具箱」和「入口」混在了一个文件里。
请把它拆成两个文件（都在 `day14/` 目录下）：

| 新文件 | 装什么 | 不该出现什么 |
| --- | --- | --- |
| `hw_contactbook.py` | `import json` / `import os`、`BASE` / `PATH`、`class ContactBook`（全部方法）、闸门里的自测演示 | `show_menu`、`main`、`input()` |
| `hw_main.py` | `show_menu()`、`main()`、`if __name__ == "__main__": main()`、import 工具箱 | `class ContactBook`、`json`／`os` 的读写细节 |

## 具体步骤

1. 新建 `day14/hw_contactbook.py`，把 `big.py` 里 **工具箱部分** 原样搬过去
   - 文件末尾加一段闸门自测（`if __name__ == "__main__":`）：
     删旧数据文件 → 造对象 → 加一个 "光羽" "111" → 加一个 "小明" "abc"（应被拒）→
     `print(book)` → `print("人数：", len(book))` → `book.show_all()`
2. 新建 `day14/hw_main.py`，把 **入口部分** 搬过去
   - 顶部要 import 工具箱：`from hw_contactbook import ContactBook, PATH`
     （`PATH` 要在闸门里删文件用，所以得一起 import 过来）
   - 其它代码照抄，一个字都不用改
3. 数据文件仍用 `contacts14_big.json`（`PATH` 不要改），这样拆完后行为跟 `big.py` 一致

## 验收清单（做完自己逐条跑一遍）

```bash
cd day14

# ① 工具箱自测：应该看到 已加上光羽 / 电话只能是数字！ / 通讯录（1人）...
python hw_contactbook.py

# ② 菜单能进：应该打印 通讯录（0人）：{} 和菜单
printf 'q\n' | python hw_main.py

# ③ 借工具箱不出声：下面这条命令除了"干净"两个字，不该有任何输出
python -c "import hw_contactbook; print('干净')"

# ④ 入口被 import 也不该进菜单：同样只打印"干净"
python -c "import hw_main; print('干净')"
```

四条全过 = 拆成功。

## 常见坑

- 忘了给 `hw_contactbook.py` 加闸门 → 第 ③ 条会打印出一堆演示内容
- 把 `if __name__ == "__main__": main()` 写进 `hw_contactbook.py` → 那里面没有 `main`，直接 `NameError`
- `hw_main.py` 忘了 import `PATH` → 第 ② 条会在删文件那行报 `NameError: name 'PATH' is not defined`
- 两个文件都留着 `class ContactBook` → 不算错，但等于没拆（改一处要改两处，回到了 Day13 之前的坑）
