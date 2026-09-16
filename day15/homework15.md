# Day 15 作业：把自己的通讯录做成一个包

## 任务

在 `day15/` 下建一个新包 **`mypkg/`**，把你 Day14 写的两个文件（`hw_contactbook.py` / `hw_main.py`）改造成标准的四文件包结构：

```
day15/
├── mypkg/
│   ├── __init__.py     门面：出口 ContactBook 和 PATH
│   ├── storage.py      最底层：load() / save()
│   ├── book.py         ContactBook 类
│   └── cli.py          菜单 + main
└── homework15.md       本文件
```

## 具体步骤

1. **`storage.py`**：只放 `load(path)` / `save(contacts, path)` 两个函数 + `PKG_DIR` / `PATH` 常量。
   - `PATH` 指向 `mypkg/contacts15_hw.json`（用 `os.path.dirname(os.path.abspath(__file__))` 算，别写死）
   - 不 import `ContactBook`，不打印任何东西
2. **`book.py`**：把 `ContactBook` 整个搬过来。
   - 顶部用**相对导入**：`from .storage import load, save, PATH`
   - `load()` / `save()` 方法不要再自己读写文件，改成调用 `storage` 的 `load(self.path)` / `save(self.contacts, self.path)`
   - 这样 `book.py` 里就不该再有 `import json` 了
3. **`__init__.py`**：写出口
   ```python
   from .book import ContactBook
   from .storage import PATH
   ```
4. **`cli.py`**：把菜单和 `main()` 搬过来。
   - 顶部：`from .book import ContactBook` 和 `from .storage import PATH`（都要相对导入）
   - 闸门里保留"清空重来"（`os.path.exists(PATH)` + `os.remove(PATH)`）
5. **不要**在 `day15/` 根目录留 `hw_contactbook.py` / `hw_main.py` 的副本——包建好后它们就没用了（留在那儿就是"两份真相"）

## 验收清单（做完自己逐条跑）

```bash
cd day15

# ① 包能被导入，并且拿到类和路径
python -c "import mypkg; print('包版本/出口：', mypkg.ContactBook, mypkg.PATH)"

# ② 用 -m 跑包里的命令行界面：应该打印 通讯录（0人）：{} 和菜单
printf 'q\n' | python -m mypkg.cli

# ③ 完整流程：加人 → 拒绝字母电话 → 看全部 → 退出
printf '3\n光羽\n111\n3\n小明\nabc\n1\nq\n' | python -m mypkg.cli

# ④ 导入包不该有任何输出（闸门生效）
python -c "import mypkg; print('干净')"

# ⑤ 反面验证：直接跑包里的文件应该报相对导入的错
python mypkg/cli.py

# ⑥ 语法检查
python -m py_compile mypkg/__init__.py mypkg/storage.py mypkg/book.py mypkg/cli.py
```

## 验收标准

| 检查 | 期望 |
| --- | --- |
| ① | 打印出 `<class 'mypkg.book.ContactBook'>` 和一条 `...contacts15_hw.json` 路径 |
| ② | 出现 `通讯录（0人）：{}` 和菜单 |
| ③ | `已加上 光羽` → `电话只能是数字！` → `光羽：111` → `共 1 人，再见！` |
| ④ | 只打印"干净"，没有多余输出 |
| ⑤ | 报 `ImportError: attempted relative import with no known parent package`（**这是对的**，说明你用了相对导入） |
| ⑥ | 没有任何输出（没输出=语法全对） |

## 常见坑

- `book.py` 里忘了把 `open()` 换成 `load()/save()` → 分层没做到，等于白拆
- 相对导入写成 `from storage import load` → `ModuleNotFoundError: No module named 'storage'`（少了那个点）
- `cli.py` 里用了 `import book` → 同样报错，包内互相引用一律用 `.`
- 忘了 `__init__.py` → 那个文件夹就不是包，`import mypkg` 直接失败
- 数据文件路径写成相对路径 `"contacts15_hw.json"` → 从别的目录跑时文件会掉到别处（Day7 的老坑）
