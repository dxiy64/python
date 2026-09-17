# 新电脑开工指南

换电脑、或者别人拿到这个仓库，按下面 4 步就能跑起来。
（`.venv` 不提交进 git，所以环境必须在每台机器上**重建**——这是故意的，见文末说明。）

---

## 第 0 步：先确认这台机器有 Python 和 git

```bash
python -V          # 要 3.9 以上（当前用的是 3.14）
git --version
```

没有的话：Python 去 python.org 下载（安装时**勾选 "Add python.exe to PATH"**），git 去 git-scm.com。

---

## 第 1 步：把代码拉下来

```bash
git clone https://github.com/dxiy64/python.git
cd python
```

克隆下来只有几百 KB——因为 `.venv/`、`__pycache__/` 这些能自动重建的东西都没被提交。

---

## 第 2 步：进到需要环境的那一天，建虚拟环境

```bash
cd day16                    # 哪一天需要第三方库就进哪一天
python -m venv .venv
```

> 只有用到第三方库的那几天才需要这步（比如 Day08 的 requests、Day16 的 tabulate）。
> 其他天直接用系统 Python 跑 `python day17.py` 即可。

---

## 第 3 步：激活

| 终端 | 命令 |
| --- | --- |
| **git-bash / Mac / Linux** | `source .venv/Scripts/activate`（Mac/Linux 是 `.venv/bin/activate`） |
| **cmd** | `.venv\Scripts\activate.bat` |
| **PowerShell** | `.venv\Scripts\Activate.ps1` |

激活成功的标志：命令行提示符前面出现 `(.venv)`。

验证自己在哪个环境：

```bash
which python        # 应指向 .venv/Scripts/python（cmd/PowerShell 用 where python）
```

---

## 第 4 步：照清单装依赖，然后跑

```bash
python -m pip install -r requirements.txt
python hw16.py
```

`requirements.txt` 就是"这个项目需要哪些库、什么版本"的清单，装了它等于把环境复原。

---

## 验证清单（四条都过就是成功了）

```bash
cd day16
python -c "import sys; print('虚拟环境' if sys.prefix != sys.base_prefix else '系统 Python')"   # ① 虚拟环境
python -m pip show tabulate | grep Location    # ② 库装在 .venv 里
python hw16.py                                  # ③ 表格正常输出
deactivate && python hw16.py                    # ④ 退出后应报 ModuleNotFoundError（隔离生效）
```

---

## 常见报错速查

| 报错 | 原因 | 解决 |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'xxx'` | 没激活，或没装依赖 | 先激活（提示符出现 `(.venv)`），再 `pip install -r requirements.txt` |
| `source: command not found` | 你在 cmd/PowerShell 里 | 换对应命令（见第 3 步表格） |
| `No such file or directory: .venv/Scripts/activate` | 当前目录没有 `.venv`，或还没建 | 先 `cd` 到正确目录，或先执行第 2 步 |
| `python: command not found` | 装了 Python 但没加到 PATH | 重装并勾选 "Add python.exe to PATH" |
| 跑出来还是找不到库 | 只有 `pip` 装到了别的 Python 上 | 一律用 `python -m pip install ...` |
| `ls` 报错但 `dir` 能用 | 你在 cmd 里用了 Linux 命令 | cmd 用 `dir`，或切到 git-bash |

---

## 为什么 `.venv` 不进 git

| 原因 | 说明 |
| --- | --- |
| 太大 | 15 MB / 900+ 文件（整个仓库才 866 KB） |
| 路径写死 | `pyvenv.cfg` 和 `activate` 里存的是**本机绝对路径**，换机器/换目录就失效 |
| 平台绑死 | Windows 是 `Scripts/python.exe`，Mac/Linux 是 `bin/python`，不能通用 |
| 能重建 | 有 `requirements.txt`，一条命令就能复原；克隆 15 MB 不如装一行清单 |

**记住这条规律：能自动重新生成的、只对某台机器有意义的、带机密的，都不进 git。**
