# Python 学习记录 🐍

从零开始的 Python 学习，每天一个主题 + 一份作业。目标：能自己动手做项目。

![进度](https://img.shields.io/badge/%E8%BF%9B%E5%BA%A6-Day%2014%20%2F%2030-brightgreen)
![天数](https://img.shields.io/badge/%E5%B7%B2%E5%AD%A6%E4%B9%A0-14%20%E5%A4%A9-blue)
![作业](https://img.shields.io/badge/%E4%BD%9C%E4%B8%9A-14%20%E4%BB%BD-success)

## 学习进度

**已完成 14 / 30 天（47%）**

```
Day 01 ├██████████████░░░░░░░░░░░░░░░░┤ 30
```

| 状态 | 天数 | 主题 | 课堂代码 | 作业 |
| ---- | ---- | ---- | -------- | ---- |
| ✅ | Day 01 | 第一行代码：print / 变量 / f-string / input | `day01/day01.py` | `day01/homework01.py` — 个人信息输出 |
| ✅ | Day 02 | 条件判断与循环：if / while / break，int 类型转换 | `day02/day02.py` | `day02/homework02.py` — 猜数字游戏 |
| ✅ | Day 03 | 列表与 for 循环：索引、append、range、累加 | `day03/day03.py` | `day03/homework03.py` — 成绩小管家（总分/平均/最高最低） |
| ✅ | Day 04 | 字典与函数：dict 增删改查、def、返回值 | `day04/day04.py` | `day04/homework04.py` — 通讯录小管家 |
| ✅ | Day 05 | 文件读写：w / a / r 模式、with 自动关闭 | `day05/day05.py` | `day05/homework05.py` — 记账本（`account.txt`） |
| ✅ | Day 06 | 异常处理：try/except、ValueError / FileNotFoundError / ZeroDivisionError | `day06/day06.py` | `day06/homework06.py` — 给猜数字游戏穿防弹衣 |
| ✅ | Day 07 | 模块与 JSON：datetime / random、json.dump / load 结构化存档 | `day07/day07.py` | `day07/homework07.py` — 通讯录存档版（`contacts.json`） |
| ✅ | Day 08 | 联网小程序：requests + wttr.in 天气查询，写日志 | `day08/day08.py` | `day08/homework08.py` — 天气小管家（`weather_log.txt`） |
| ✅ | Day 09 | 毕业项目①：通讯录管理系统（while 菜单 + 字典 + 函数 + JSON + try） | `day09/manager.py` | `day09/homework09.py` — 读懂 manager.py：save 调用点、del、strip，加"统计"与电话数字校验 |
| ✅ | Day 10 | 面向对象：class / 对象 / `__init__` / self / 方法，把通讯录装进 `ContactBook` 类 | `day10/day10.py` | `day10/homework10.py` — 加 `count` 统计、电话数字校验、选做模糊搜索 |
| ✅ | Day 11 | 面向对象②：`__str__` 长相 / `__len__` 人数 / update 改电话 / rename 搬家（键不能改名） | `day11/day11.py` | `day11/homework11.py` — 长相、改电话校验、选做改名搬家 |
| ✅ | Day 12 | 毕业项目②：菜单版通讯录（类 + while 菜单 + main，不再递 contacts） | `day12/day12.py` | `day12/homework12.py` — 补模糊搜分支、空名校验、选做看人数 |
| ✅ | Day 13 | 面向对象③：继承 / 父类子类 / `super().__init__` / 方法覆盖 / 多态 / isinstance | `day13/day13.py` | `day13/homework13.py` — 联系人分类：Friend 加备注、Workmate 加公司、多态显示 |
| 🚧 | Day 14 | 拆文件：工具箱（类）+ 入口（菜单）、`import` 三种写法、`__pycache__` 与闸门 | `day14/day14.py`（搭档 `contactbook.py` + `main.py`） | `day14/homework14.md` — 把 `day14/big.py` 拆成 `hw_contactbook.py` + `hw_main.py` |

### 里程碑

- [x] 基础语法：变量 / 判断 / 循环 / 列表 / 字典 / 函数（Day 01–04）
- [x] 文件与异常：文件读写 / try-except / JSON / 联网（Day 05–08）
- [x] 第一个完整项目：菜单版通讯录（Day 09、12）
- [x] 面向对象：class / self / 双下划线方法 / 继承 / 多态（Day 10–13）
- [ ] 工程化：多文件拆分、模块化、包（Day 14 进行中）
- [ ] 综合项目：把通讯录做成带界面的程序

## 运行方法

```bash
# 进对应天数目录再运行（部分程序读写同目录下的数据文件）
cd day01 && python day01.py
```

需要第三方库的只有 Day 08：`pip install requests`。

菜单类程序（Day 09 起）必须在终端里跑，因为要敲键盘选菜单：

```bash
cd day14 && python main.py
```

## 目录结构

```
day01/  day02/  ...  day14/   # 每天：课堂代码 + 作业 + 程序产生的数据文件
day14/                        # 多文件示例：contactbook.py（工具箱）+ main.py（入口）
```
