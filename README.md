# Python 学习记录 🐍

从零开始的 Python 学习，每天一个主题 + 一份作业，已学完 Day 01–09。

## 运行方法

```bash
# 进对应天数目录再运行（部分程序读写同目录下的数据文件）
cd day01 && python day01.py
```

需要第三方库的只有 Day 08：`pip install requests`。

## 学习进度

| 天数 | 主题 | 课堂代码 | 作业 |
| ---- | ---- | -------- | ---- |
| Day 01 | 第一行代码：print / 变量 / f-string / input | `day01/day01.py` | `day01/homework01.py` — 个人信息输出 |
| Day 02 | 条件判断与循环：if / while / break，int 类型转换 | `day02/day02.py` | `day02/homework02.py` — 猜数字游戏 |
| Day 03 | 列表与 for 循环：索引、append、range、累加 | `day03/day03.py` | `day03/homework03.py` — 成绩小管家（总分/平均/最高最低） |
| Day 04 | 字典与函数：dict 增删改查、def、返回值 | `day04/day04.py` | `day04/homework04.py` — 通讯录小管家 |
| Day 05 | 文件读写：w / a / r 模式、with 自动关闭 | `day05/day05.py` | `day05/homework05.py` — 记账本（`account.txt`） |
| Day 06 | 异常处理：try/except、ValueError / FileNotFoundError / ZeroDivisionError | `day06/day06.py` | `day06/homework06.py` — 给猜数字游戏穿防弹衣 |
| Day 07 | 模块与 JSON：datetime / random、json.dump / load 结构化存档 | `day07/day07.py` | `day07/homework07.py` — 通讯录存档版（`contacts.json`） |
| Day 08 | 联网小程序：requests + wttr.in 天气查询，写日志 | `day08/day08.py` | `day08/homework08.py` — 天气小管家（`weather_log.txt`） |
| Day 09 | 毕业项目：通讯录管理系统（while 菜单 + 字典 + 函数 + JSON + try） | `day09/manager.py` | `day09/homework09.py` — 读懂 manager.py：save 调用点、del、strip，加"统计"与电话数字校验 |

## 目录结构

```
day01/  day02/  ...  day09/   # 每天：课堂代码 + 作业 + 程序产生的数据文件
```
