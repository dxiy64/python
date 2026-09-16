# Day 16 作业：给你的项目配一个独立的"工作间"

## 目标

亲手走完 **建环境 → 激活 → 装库 → 写脚本用库 → 导出清单 → 隔离验证** 六步。

## 任务

### 第 1 步：建环境并激活

```bash
cd C:/Users/Administrator/python/day16
python -m venv .venv
source .venv/Scripts/activate      # cmd 用 .venv\Scripts\activate.bat
```

确认提示符前面出现 `(.venv)`，且 `which python` 指向 `day16/.venv/Scripts/python`。

### 第 2 步：装一个第三方库

```bash
python -m pip install tabulate
```

`tabulate` 是个小库，能把一组数据打印成漂亮的表格（你的系统 Python 里没有它，正好用来证明"隔离"）。

### 第 3 步：写 `hw16.py`

要求：

1. 顶部 `from tabulate import tabulate`
2. 准备一份通讯录数据（**直接写在代码里就行**，不用读文件）：
   ```python
   contacts = [
       ["光羽", "18486311094"],
       ["小明", "13800001111"],
       ["鼠鼠", "999999999"],
   ]
   ```
3. 用 `tabulate(contacts, headers=["名字", "电话"], tablefmt="github")` 打印成表格
4. 顺便打印一行环境信息：`import sys; print("解释器：", sys.executable)`
5. 包在 `if __name__ == "__main__":` 里（老规矩）

跑起来应该看到：

```
| 名字   |        电话 |
|--------|-------------|
| 光羽   | 18486311094 |
| 小明   | 13800001111 |
| 鼠鼠   |   999999999 |
解释器： C:\...\day16\.venv\Scripts\python.exe
```

### 第 4 步：导出依赖清单

```bash
python -m pip freeze > requirements.txt
```

### 第 5 步：隔离验证（**这步是重点**）

```bash
deactivate                                        # 退出虚拟环境
python hw16.py                                    # 应该报 ModuleNotFoundError: No module named 'tabulate'
```

能报错 = 成功。因为那个库只装在 `.venv` 里，系统 Python 看不到它。

### 第 6 步：重建验证（证明清单真的管用）

```bash
rm -rf .venv                                      # 删掉整个环境
python -m venv .venv                              # 重建
source .venv/Scripts/activate                     # 重新激活
python -m pip install -r requirements.txt         # 照清单一键装回来
python hw16.py                                    # 表格又出来了
```

## 验收清单

```bash
cd C:/Users/Administrator/python/day16

# ① 环境存在，且能自检
source .venv/Scripts/activate
python -c "import sys; print('虚拟环境' if sys.prefix != sys.base_prefix else '系统 Python')"
which python

# ② 库装在这个环境里
python -m pip show tabulate

# ③ 脚本能跑出表格
python hw16.py

# ④ 清单存在且内容正确
cat requirements.txt

# ⑤ 退出后跑不了（隔离证据）
deactivate
python hw16.py
```

| 检查 | 期望 |
| --- | --- |
| ① | 打印 `虚拟环境`；`which python` 指向 `day16/.venv/Scripts/python` |
| ② | 输出里有 `Name: tabulate` 和 `Location: ...day16\.venv\Lib\site-packages` |
| ③ | 出现表格 + 解释器路径指向 `.venv` |
| ④ | 至少有 `tabulate==0.9.x` 一行 |
| ⑤ | `ModuleNotFoundError: No module named 'tabulate'` |

## 常见坑

- **忘了激活**：第②条会显示 `Location: ...Python314\Lib\site-packages`（装到全局去了），这时 `python -m pip uninstall tabulate` 卸掉，激活后重装
- **激活后关掉终端再打开**：环境不会自动激活，每次开新终端都要重新 `source .../activate`
- **`source` 命令在 cmd 里不存在**：cmd 要用 `.venv\Scripts\activate.bat`（详见 `commands.md` 的表格）
- **把 `.venv` 提交到 git**：别提交。它已在 `.gitignore` 里，`git status` 不该看到它
- **`requirements.txt` 里出现一堆不相干的包**：说明你在**没激活**的状态下 freeze 了全局环境。激活后再 freeze
