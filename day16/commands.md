# Day 16 命令速查：虚拟环境与依赖

> 在哪个目录执行？**项目目录**（比如 `C:/Users/Administrator/python/day16`）。

## 一、创建环境（一个项目只做一次）

```bash
python -m venv .venv
```

* `-m venv` = 跑 venv 这个模块（不是外部命令，装不了额外东西）
* `.venv` 是环境文件夹的名字，习惯叫 `.venv` 或 `venv`（两个都已在 `.gitignore` 里）
* 建一次大约 5–10 秒，文件夹约 20–30 MB

## 二、激活 / 退出

| 终端 | 激活 | 退出 |
| --- | --- | --- |
| **git-bash / MSYS**（你现在用的） | `source .venv/Scripts/activate` | `deactivate` |
| **cmd（命令提示符）** | `.venv\Scripts\activate.bat` | `deactivate` |
| **PowerShell** | `.venv\Scripts\Activate.ps1` | `deactivate` |

激活成功的标志：**命令行提示符前面多出 `(.venv)`**。

```bash
# 验证自己在哪个 Python 里
which python          # git-bash 写法 → 应指向 .venv/Scripts/python
where python          # cmd / PowerShell 写法
python -V
```

## 三、装库 / 卸库 / 看清单

```bash
python -m pip install requests          # 装
python -m pip install requests==2.31.0  # 装指定版本
python -m pip uninstall requests        # 卸
python -m pip list                      # 看这个环境装了啥
python -m pip show requests             # 看某个包的详情（版本、装在哪）
```

> 永远写 `python -m pip`：能保证"装给正在用的这个 Python"。直接写 `pip` 有时会指向另一个 Python（你电脑上装了 3.14，还有 Windows 商店的 python 别名）。

## 四、requirements.txt（依赖清单）

```bash
python -m pip freeze > requirements.txt          # 导出当前环境的所有包+版本
python -m pip install -r requirements.txt        # 照清单一键安装（别人复现你的项目）
```

清单内容示例：

```
requests==2.34.2
tabulate==0.9.0
```

## 五、一句话环境自检

```bash
python -c "import sys; print('在虚拟环境里' if sys.prefix != sys.base_prefix else '在系统 Python 里')"
```

## 六、踩坑速查

| 现象 | 原因 | 解决 |
| --- | --- | --- |
| 装完还是 `ModuleNotFoundError` | 没激活，装到全局了 | 先激活，提示符出现 `(.venv)` 再装 |
| `activate` 找不到文件 | 路径或终端不对 | git-bash 用 `source .venv/Scripts/activate`；cmd 用 `.venv\Scripts\activate.bat` |
| pip 装到别处 | 用了裸 `pip` | 改用 `python -m pip` |
| git 里冒出几百 MB | 把 `.venv` 提交了 | 别提交；`.gitignore` 里已有 `venv/`、`.venv/` |
| 换了电脑跑不起来 | 没带 `requirements.txt` | 导出清单，新机器 `pip install -r requirements.txt` |
| 想删掉重来 | — | 直接删文件夹（`.venv`），重新 `python -m venv .venv` |
