---
name: homework-verify
description: Use when verifying dayNN homework runs. Scratch-copy acceptance without polluting learner data.
---

# 作业验收（scratch 隔离）

## 何时用

验收 `dayNN/hw_*.py` 这类带菜单 + 写数据文件的作业时用。

## 流程（已验证）

```bash
rm -rf /tmp/dNNcheck && cp -r dayNN /tmp/dNNcheck
cd /tmp/dNNcheck && rm -f ledger.json

# 全分支走一遍：记两笔（第二笔金额 -3 被拒后重问）、看流水、统计、退出
printf '1\n12.5\n午饭\n猪脚饭\n1\n-3\n6.0\n交通\n地铁\n2\n3\nq\n' | python hw_21.py; echo "EXIT=$?"

# 跨进程 persistence：新进程看流水，两笔必须还在
printf '2\nq\n' | python hw_21.py

# JSON 落盘笔数
python -c "import json;print(len(json.load(open('ledger.json',encoding='utf-8'))),'笔')"
```

验收标准：`EXIT=0`、拒绝提示后重问金额、统计数字正确、新进程数据还在。

## 常见错误

### `print("=", *40)` → TypeError

```text
TypeError: Value after * must be an iterable, not int
```

原因：`*40` 是解包语法，只能 unpack iterable，`40` 是 int。
正确写法：`print("=" * 40)`（字符串重复）。

排查方法：读 traceback 最后一行拿错误名，再往上找自己文件的行号（`show_menu` 第 78/84 行是重灾区）。

## 约束

- 一律在 `/tmp/dNNcheck` 副本里跑，不直接跑仓库里的真文件，避免 `ledger.json` 被测试数据污染。
- 验完删除副本：`rm -rf /tmp/dNNcheck`。
- 边界输入另测一组：`abc` / `0` / `12.555` 都必须被拒收后重问；删 `ledger.json` 后跑 `2`/`3` 分支必须打印"还没有账"且不崩。
