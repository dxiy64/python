# Day30 作业：复习日——不许翻旧文件，从零重写记账本 + 爬虫日报

## 一条铁律

**不许打开 day21–day29 的任何 `.py`**（讲义、作业、你的旧代码全不许看）。
能看的只有：`day30/复习地图.md`、官方文档、报错信息。
能读懂 ≠ 能写出来——这天要过的就是这关。

## 为什么是今天

Day21–29 你连走了 9 天：从零记账本 → sqlite 三连 → 爬虫三连，
中间一次都没停下来重写过。上次（Day20）就是这么验收的，同样标准再来一次。

## 阶段①：单文件 sqlite 记账本（`review30.py`）

从空文件起写，一个文件里搞定：建表、记账、查账、月报。
表 `ledger(id INTEGER PRIMARY KEY AUTOINCREMENT, sort TEXT, money REAL, time TEXT)`，
`time` 存 `'%Y-%m-%d %H:%M'` 形状。

- 记 3 笔（至少两个分类、两个不同月份）
- `month_report('2026-10')`：返回当月条数和总和（SQL 里算，不许 SELECT 全表再循环）
- 空月（比如 `2000-01`）返回 `(0, 0)`，不许炸

验收（`day30` 目录里）：

```bash
python review30.py
```

应打印：全部条数 3、当月条数和总和、空月 `(0, 0)`。

## 阶段②：拆成包（`book30/`）

把阶段①拆成包：`book30/__init__.py`（门面）+ `book30/store.py`（存取函数）
+ `book30/cli.py`（菜单/演示入口），包内互相 `from .x import`。

两个启动命令都要试：

```bash
python -m book30.cli    # 应跑起来
python book30/cli.py    # 应报错（ attempted relative import …），报错才算对
```

第二个报错是验收项：它证明你用的是相对导入，不许改成绝对导入绕过去。

## 阶段③：爬虫日报挂回来（`daily30.py`）

抓 `https://quotes.toscrape.com` 前 2 页 → `quotes30.db`
（`INSERT OR IGNORE`，主键去重）→ 写日报文件：

- 文件名带时间戳、无冒号（`日报_%Y%m%d_%H%M%S.txt`）
- 内容：标题日期行 + `共 X 条，Y 位作者` + Top3 每行 `作者：N 条`
- 再导一份 CSV（`utf-8-sig` + `newline=""`）
- 用 `collections.Counter` 在内存里也排一遍 Top3，跟 SQL 的排行对得上才算过

验收：

```bash
python daily30.py
```

应打印：总数 20、作者数 15、Einstein 4、日报文件名、CSV 行数 21（含表头）。

## 自查清单（这些坑你全踩过，写完逐条打勾）

- [ ] SQL 值全走 `?` 占位，不拼 f-string（`老陈's店` 那课）
- [ ] 写操作后 `commit()`，否则关门白干
- [ ] 取数 `fetchone()[0]`，`SUM` 空结果是 `None` 要兜底
- [ ] 单参数元组有尾逗号：`(month + '%',)`
- [ ] `UPDATE`/`DELETE` 前先 `SELECT` 看行在不在
- [ ] 报表用 `fetchall()` 接住行，不许调只打印不返回的函数
- [ ] 校验用 `fullmatch` 不用 `match`
- [ ] 排行取 `[0]` 前先想空表怎么办
- [ ] 主键去重用 `OR IGNORE`，不数 `total_changes`
- [ ] `write_text` 前先 `mkdir`，文件名无冒号
- [ ] 函数用传进来的 `conn`，不自己重连；`return` 交卷不 `print` 交卷

## 自评表（这列才是你真正的弱点清单）

| 任务 | 一次写对？ | 卡在哪（贴报错/输出） |
| --- | --- | --- |
| 阶段① 建表+记3笔 | | |
| 阶段① 月报+空月 | | |
| 阶段② 拆包+双启动 | | |
| 阶段③ 抓存+日报+CSV | | |
| 阶段③ Counter 对账 | | |

## 卡住了按这个顺序走

复习地图 → 那天的讲义 → 官方文档 → `python -c` 小实验 →
带代码 + **完整** traceback 问我。别跳步，跳步等于白复习。
