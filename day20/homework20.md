# Day 20 · 复习日：通讯录从零重写一遍

> **今天的规则只有一条**：**不许打开 `day10` ~ `day19` 里的任何 `.py` 文件**。
> 卡住了怎么办？按这个顺序：
> 1. 先看本目录的 `复习地图.md`（提示"这件事在哪天学过"，但**不给代码**）
> 2. 查官方文档 <https://docs.python.org/zh-cn/3/>（搜索关键词）
> 3. 用 `python -c "..."` 做小实验自己验证
> 4. 还是不行 → 把**你写的代码 + 报错信息**发给我

---

## 为什么今天要重写

前 19 天你一直在"读代码 + 补 TODO"。**能读懂 ≠ 能写出来**。
今天的任务是把过去 10 天的东西**从空白文件里长出来**——这一步才是"能找工作的真正分界线"。

预计用时 **2~4 小时**，做不完明天接着做，不着急。

---

## 交付物（按顺序做，三个阶段）

### 阶段 1（必做）：单文件跑通核心 —— `day20/review.py`

从空文件开始，写出一个**能用的通讯录**：

| # | 功能 | 要求 |
|---|---|---|
| 1 | 数据容器 | 用**字典**存 `姓名 → 电话` |
| 2 | 类封装 | `class ContactBook`，`__init__` 里自己读档 |
| 3 | 持久化 | 读档 `load()` / 存档 `save()`，用 **JSON**（`ensure_ascii=False`） |
| 4 | 增删改查 | `add` / `find` / `update` / `delete` |
| 5 | 模糊查 | `search(keyword)` —— 名字里含关键词的全打印 |
| 6 | 改名 | `rename(old, new)` —— 注意"新名字已存在"要先拒绝 |
| 7 | 看全部 | `show_all()`，空的时候要有提示 |
| 8 | 打印好看 | `__str__`（`print(book)` 出人数 + 名单）、`__len__`（`len(book)` 出人数）|
| 9 | 菜单 | `while True` + `input().strip()`，选 `q` 退出 |
| 10 | 闸门 | `if __name__ == "__main__":` 只放"动作" |

**验收**：

```bash
cd C:/Users/Administrator/python/day20
python review.py            # 菜单能跑，能加人、能看全部、能退出
```

### 阶段 2（必做）：拆成包 —— `day20/mypkg/`

把阶段 1 的单文件拆成**包**（复习 Day14 + Day15）：

```
day20/mypkg/
    __init__.py      ← 门面：导出 ContactBook 和 PATH
    storage.py       ← 只管 load / save + 路径常量
    book.py          ← ContactBook 类
    cli.py           ← 菜单 + 闸门
```

**硬性要求**：

- `cli.py` 里用**相对导入**：`from .book import ContactBook`
- 路径只用 **`pathlib`**，不准用 `os.path`
- `PATH` 只在 `storage.py` 定义一次，别处一律 import 借（**单一数据源**）

**验收**：

```bash
cd C:/Users/Administrator/python/day20
python -m mypkg.cli                     # 必须能跑
python mypkg/cli.py                     # 必须报错！报的是相对导入的错就对了
python -c "import mypkg; print('干净')"   # import 时不能有任何多余输出
```

> 第二条报错是**验收项**，不是 bug——报 `ImportError: attempted relative import with no known parent package` 说明你相对导入写对了。

### 阶段 3（加分）：把最近学的都挂上去

| 加的什么 | 用哪天学的 | 具体要求 |
|---|---|---|
| 手机号校验 | Day18 正则 | `re.fullmatch(r"1[3-9]\d{9}", phone)`，不合法的拒收并提示 |
| 导出 CSV | Day17 `csv`+`pathlib` | 菜单加一项，导出到 `day20/out/通讯录.csv`（`encoding="utf-8-sig"`、`newline=""`） |
| 操作日志 | Day19 `logging` | 每次增/删/改记一条 INFO 到 `day20/out/app.log` |
| 容错 | Day06 + Day19 | 读档遇到坏 JSON 不许崩，`except` 住 + `logging.error` 记下来 |
| 继承 | Day13 | 加一个 `class VipContact(Contact)`，多存一个"备注"字段，`super().__init__` 别忘了 |
| 时间戳报表 | Day17 `datetime` | 导出时文件名带 `f"{now:%Y%m%d_%H%M%S}"` |
| 去重/统计 | Day17 `collections` | 用 `Counter` 统计各城市人数，或 `defaultdict` 按城市分组 |

**验收**：

```bash
cd C:/Users/Administrator/python/day20
printf '1\n光羽\n13800001111\n7\n8\nq\n' | python -m mypkg.cli    # 喂输入走一遍分支
ls out/                                                          # 看到 csv 和 log
```

---

## 自查清单（每做完一段打勾）

- [ ] 我能不看任何旧文件写出 `class` + `__init__` + 方法
- [ ] 我知道 `self` 是"这次造出来的那个对象"，属性由 `self.x = ...` 创建
- [ ] 我记得 `def load(self)` 里文件不存在要返回 **`{}` 而不是 `[]`**（类型要跟容器对上）
- [ ] 我记得 `save` 用 `"w"` 会清空重写、`json.dump` 才真写、`ensure_ascii=False` 保中文
- [ ] 我知道工具箱顶层只放 `import` / `class` / `def` / 常量，"动作"全进闸门
- [ ] 我记得 `Path(__file__).parent` 定位本文件所在目录，`/` 拼路径
- [ ] 我记得 `p.parent.mkdir(parents=True, exist_ok=True)` 才能在写文件前把目录铺好
- [ ] 我记得 csv 要 `encoding="utf-8-sig"` + `newline=""`（Windows 上不加会多空行/乱码）
- [ ] 我知道 `logging.basicConfig` 一个进程只生效一次，配 `handlers` 才能同时写屏幕和文件
- [ ] 遇到报错我先**读最后一行**（错误名 + 原因），再往上找自己文件的那一行
- [ ] 我知道 `re.fullmatch` 才是"整串校验"，`re.match` 会放过 `1380000111a`
- [ ] 我知道 `for n in 列表` 比 `for i in range(len(列表))` 更不容易出错

---

## 自评表（做完自己填，诚实一点）

| 阶段 | 用时 | 卡在哪 | 卡住时怎么解决（查文档 / 实验 / 问我） | 完成度 |
|---|---|---|---|---|
| 阶段 1 单文件 | | | | |
| 阶段 2 拆包 | | | | |
| 阶段 3 加分 | | | | |

**卡点记录最有价值**——把今天每一个"卡住的地方"写下来，那就是你真正的薄弱点清单。

---

## 提交

```bash
cd C:/Users/Administrator/python
git add -A
git commit -m "feat: day20 复习日 通讯录从零重写"
git push origin main
```

自己 push（今天不喊我也行）。写完想让我**逐项验收 + 挑毛病**，把「检查我的作业」发我就行。
