# -*- coding: utf-8 -*-
# ============================================
# day19.py · 调试（Debug）：报错不是敌人，是线索
# 运行方法：cd day19 再 python day19.py
# 配套素材：crash_demo.py（真实崩溃现场）、pdb_demo.py（断点演示）
# ============================================
import logging
import traceback
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "out"


# ----------------------------------------------------------------------
# 演示 1：traceback 的三段结构，读它要「从下往上」
# ----------------------------------------------------------------------
def demo1_traceback():
    print("=" * 62)
    print("【演示 1】traceback 怎么读：三段结构，顺序是从下往上")
    print("=" * 62)
    print("  真实现场（cd day19 && python crash_demo.py）：")
    print()
    print("    Traceback (most recent call last):")
    print('      File "...\\crash_demo.py", line 30, in <module>')
    print("        main()")
    print('      File "...\\crash_demo.py", line 26, in main')
    print('        print(f"{name} 的平均分：{average(scores):.1f}")')
    print("                                  ^^^^^^^^^^^^^^^")
    print('      File "...\\crash_demo.py", line 11, in average')
    print("        return sum(scores) / len(scores)")
    print("               ~~~~~~~~~~~~^~~~~~~~~~~~~")
    print("    ZeroDivisionError: division by zero")
    print()
    print("  读法三步（★一定从最后一行开始看）：")
    print("    ① 最后一行 = 「什么错 + 为什么」→ ZeroDivisionError: division by zero")
    print("    ② 往上找第一段属于【你自己文件】的记录 → 那就是案发现场")
    print("    ③ 每一段 File \"...\", line N, in 函数名 = 调用链的一环（谁调了谁）")
    print("       最底下的 <module> 表示「从顶层那句代码开始走的」")
    print()
    print("  ⚠️  小箭头 ^^^^ 是 Python 3.11+ 帮你指出的『具体是哪个表达式』：")
    print("      这里指的就是 sum(scores) / len(scores) 这个除法")
    print()
    print("  ── 错误信息也能被程序抓住（写日志的标准做法）──")
    try:
        sum([]) / len([])                      # 故意制造除零
    except ZeroDivisionError as e:
        info = traceback.format_exc()
        print("    type(e).__name__ =", type(e).__name__, " ← 只要错误名的写法")
        print("    str(e)           =", e, " ← 只要原因那句话的写法")
        print("    traceback.format_exc() 有", len(info.splitlines()), "行 ← 要完整现场用这个")
    print()


# ----------------------------------------------------------------------
# 演示 2：最常见的报错，一次看全
# ----------------------------------------------------------------------
def _unbound_error():
    print(总计)          # 先读……
    总计 = 1             # ……后赋值 → 这个名字被判定为「局部变量」，于是读到未绑定


def _name_error():
    return 从来没定义过的名字


def try_it(desc, fn):
    try:
        fn()
        print(f"    {desc:24} → 没报错")
    except Exception as e:
        print(f"    {desc:24} → {type(e).__name__}: {e}")


def demo2_error_zoo():
    print("=" * 62)
    print("【演示 2】这些报错你都见过：读错误名 = 一半的功力")
    print("=" * 62)
    print("  ① 运行期错误（能被 try/except 抓住）：")
    try_it("int('12a')", lambda: int("12a"))
    try_it("{'光羽':'111'}['小明']", lambda: {"光羽": "111"}["小明"])
    try_it("[1,2,3][5]", lambda: [1, 2, 3][5])
    try_it("10 / 0", lambda: 10 / 0)
    try_it("'abc' + 1", lambda: "abc" + 1)
    try_it("'光羽'.strip_phone()", lambda: "光羽".strip_phone())
    try_it("open('没有的文件.txt')", lambda: open("没有的文件.txt", encoding="utf-8"))
    try_it("__import__('nosuchlib')", lambda: __import__("nosuchlib_xyz"))
    try_it("函数里先读后赋值", _unbound_error)
    try_it("读一个没定义的名字", _name_error)
    print()
    print("  ② 编译期错误（还没开始跑就挡下来，只能在写代码时改）：")
    try_it("compile('if True print(1)')", lambda: compile("if True print(1)", "<示例>", "exec"))
    try_it("compile('def f(:')", lambda: compile("def f(:", "<示例>", "exec"))
    print()
    print("  错误名 → 人话 → 怎么修（面试也爱问）：")
    print("    ┌────────────────────┬──────────────────────────────┬──────────────────────────┐")
    print("    │ 错误名             │ 人话                         │ 第一步做什么             │")
    print("    ├────────────────────┼──────────────────────────────┼──────────────────────────┤")
    print("    │ NameError          │ 这个名字没定义过             │ 检查拼写 / 有没有赋值/import │")
    print("    │ UnboundLocalError  │ 名字是局部的，但还没赋值就读 │ 看函数里后面有没有 = 赋值 │")
    print("    │ TypeError          │ 类型不对 / 参数个数不对      │ 打印 type(x) 看真实类型   │")
    print("    │ AttributeError     │ 对象身上没这个属性/方法      │ 看 Did you mean 提示      │")
    print("    │ KeyError           │ 字典里没这个键               │ print(d.keys()) 核对      │")
    print("    │ IndexError         │ 列表下标越界                 │ print(len(x)) 算边界      │")
    print("    │ ValueError         │ 值不对（类型对）             │ int('12a') → 先清洗再转   │")
    print("    │ ZeroDivisionError  │ 除以 0                       │ 分母先判空               │")
    print("    │ FileNotFoundError  │ 文件不存在                   │ print(路径) 看 CWD       │")
    print("    │ ModuleNotFoundError│ 库没装 / 模块名写错          │ pip list 或用全路径       │")
    print("    │ SyntaxError        │ 语法错（编译期）             │ 看箭头指的那一行         │")
    print("    └────────────────────┴──────────────────────────────┴──────────────────────────┘")
    print()


# ----------------------------------------------------------------------
# 演示 3：print 调试法（最土，也最有效）
# ----------------------------------------------------------------------
def demo3_print_debug():
    print("=" * 62)
    print("【演示 3】print 调试法：把『中间值』印出来，别靠脑子猜")
    print("=" * 62)
    scores = ["90", "85", "77"]
    print("  需求：把字符串成绩转成整数求和，但结果不对，找原因")
    print()
    print("  ── 方法①：在关键位置打点 ──")
    total = 0
    for s in scores:
        n = int(s)
        total = total + n
        print(f"    这一轮 s={s!r} n={n} total={total}")
    print(f"    最终 total = {total}")
    print()
    print("  ── 方法②：f\"{x=}\" 自动带变量名（Python 3.8+，最省事）──")
    x = 42
    text = "光羽  "
    print(f"    f\"{{x=}}\"     → {x=}")
    print(f"    f\"{{text=}}\"  → {text=}   ← 一眼看出末尾有空格")
    print()
    print("  ── 方法③：!r / repr 看隐形字符（Day17 学过，调试必备）──")
    print(f"    print(text)   → {text}")
    print(f"    print({text!r}) → {text!r}   ← 引号暴露出两个尾随空格")
    print("    什么时候用：两个『看起来一样』的字符串却比不出相等时")
    print()
    print("  ── 方法④：二分法缩小范围（大段代码里找凶手）──")
    print("    把中间一段用 # 注释掉，还报错 → 凶手在后面；不报错 → 凶手在里面")
    print()


# ----------------------------------------------------------------------
# 演示 4：breakpoint() / pdb
# ----------------------------------------------------------------------
def demo4_breakpoint():
    print("=" * 62)
    print("【演示 4】断点调试：让程序停下来，你能走进它内部看")
    print("=" * 62)
    print("  在 pdb_demo.py 里加一行 breakpoint()，然后：")
    print("    cd day19")
    print("    python pdb_demo.py")
    print()
    print("  程序会在那一行停住，进入 (Pdb) 提示符。真实会话（把命令喂给它）：")
    print()
    print("    > pdb_demo.py(17)total_price()")
    print("    -> total = total + p")
    print("    (Pdb) p total            ← 看变量")
    print("    0")
    print("    (Pdb) c                  ← 放行到下一个断点")
    print("    > pdb_demo.py(17)total_price()")
    print("    (Pdb) p total")
    print("    12")
    print("    (Pdb) c")
    print("    (Pdb) p total")
    print("    42")
    print("    (Pdb) c")
    print("    总价： 50")
    print()
    print("  常用命令（背 5 个就够）：")
    print("    ┌────────┬──────────────────────────────┬──────────────────────────┐")
    print("    │ 命令   │ 作用                         │ 什么时候敲               │")
    print("    ├────────┼──────────────────────────────┼──────────────────────────┤")
    print("    │ p 变量 │ print 变量当前值             │ 想看某个值对不对         │")
    print("    │ n      │ 下一步（不进函数）           │ 只关心本层的推进         │")
    print("    │ s      │ 下一步（进函数内部）         │ 想看被调用的函数里发生了什么 │")
    print("    │ c      │ 继续运行到下一个断点/结束    │ 这段已经看明白了         │")
    print("    │ l      │ 列出断点附近的代码           │ 忘了停在哪一行           │")
    print("    │ q      │ 退出调试                     │ 不想再看了               │")
    print("    └────────┴──────────────────────────────┴──────────────────────────┘")
    print()
    print("  另一种起法（不改源码）：python -m pdb pdb_demo.py，再用 b 行号 打断点")
    print("  VS Code 更简单：行号左边点一下出现红点，然后按 F5 调试")
    print()


# ----------------------------------------------------------------------
# 演示 5：try/except/else/finally —— 四个块各自什么时候跑
# ----------------------------------------------------------------------
def demo5_try_blocks():
    print("=" * 62)
    print("【演示 5】try / except / else / finally：四个块的出场时机")
    print("=" * 62)

    def divide(a, b):
        try:
            result = a / b                  # ① 先试这段
        except ZeroDivisionError as e:
            print(f"      except 跑了：{e}")   # ② 出错才跑
            return None
        else:
            print("      else 跑了：没出错")     # ③ 没出错才跑
            return result
        finally:
            print("      finally 跑了：不管出没出错都跑")   # ④ 永远跑

    print("  ── 正常情况 divide(10, 2) ──")
    print("    返回：", divide(10, 2))
    print()
    print("  ── 出错情况 divide(10, 0) ──")
    print("    返回：", divide(10, 0))
    print()
    print("  ── 自己抛错：raise（把参数校验写成『早失败』）──")

    def set_age(age):
        if age < 0:
            raise ValueError(f"年龄不能是负数：{age}")   # 主动抛，带清楚的信息
        return f"年龄已设置为 {age}"

    print("    set_age(18) →", set_age(18))
    try:
        set_age(-5)
    except ValueError as e:
        print("    set_age(-5) → 被抓住：", e)
    print()
    print("  ⚠️  别写裸 except（except: 或 except Exception: 什么都吞）：")
    print("      它会把『库升级了函数名变了』这种真 bug 也吞掉，让你以为程序没问题。")
    print("      要么写具体错误名，要么在最外层兜底时用 logging.exception 记全现场。")
    print()


# ----------------------------------------------------------------------
# 演示 6：logging —— 正式项目里为什么不用 print
# ----------------------------------------------------------------------
def demo6_logging():
    print("=" * 62)
    print("【演示 6】logging：带级别、带时间、能同时写屏幕和文件")
    print("=" * 62)
    LOG_PATH = OUT / "day19.log"
    print("  五个级别（从轻到重）：DEBUG < INFO < WARNING < ERROR < CRITICAL")
    print("  只有当『消息级别 >= 设置的级别』时才会输出")
    print()
    print("  ① 默认只显示 WARNING 及以上：")
    root = logging.getLogger()
    root.handlers.clear()                      # 清掉之前的配置，方便演示（正常代码不要写）
    logging.basicConfig(level=logging.WARNING, format="    %(levelname)s: %(message)s",
                        force=True)
    logging.debug("这行 DEBUG 不会出现")
    logging.info("这行 INFO 也不会出现")
    logging.warning("这行 WARNING 会出现")
    logging.error("这行 ERROR 会出现")
    print()
    print("  ② 改成 level=INFO 之后，INFO 也出来了（同时写进文件）：")
    root.handlers.clear()
    logging.basicConfig(
        level=logging.INFO,
        format="    %(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(), logging.FileHandler(LOG_PATH, encoding="utf-8")],
        force=True,
    )
    logging.info("程序启动")
    logging.info("读到 5 行数据")
    for i, row in enumerate(["光羽 13800001111", "小明 13912345678", "坏行   "], start=1):
        if "1" in row:
            logging.info("第 %d 行处理成功：%s", i, row.strip())
        else:
            logging.warning("第 %d 行没有手机号，跳过：%r", i, row)
    logging.info("结束")
    print()
    print(f"  ③ 日志文件自己也留了一份：{LOG_PATH.name}")
    print("   " + LOG_PATH.read_text(encoding="utf-8").replace("\n", "\n   ").rstrip())
    print()
    print("  ④ 出错时用 logging.exception()：自动把完整 traceback 记进去")
    print("     （这里用一个只写文件的 logger，避免 stderr 把版面打乱）")
    file_only = logging.getLogger("file_only")
    file_only.handlers.clear()
    file_only.propagate = False
    fh = logging.FileHandler(LOG_PATH, encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
                                      "%Y-%m-%d %H:%M:%S"))
    file_only.addHandler(fh)
    file_only.setLevel(logging.INFO)
    try:
        1 / 0
    except ZeroDivisionError:
        file_only.exception("算平均分时出错")
    fh.close()
    print(f"    {LOG_PATH.name} 末尾几行（注意 traceback 被完整记下了）：")
    tail = LOG_PATH.read_text(encoding="utf-8").splitlines()[-7:]
    print("     " + "\n     ".join(tail))
    print()
    print("  ⑤ print vs logging：")
    print("    ┌──────────┬──────────────────────────────────┬────────────────────────────┐")
    print("    │          │ print                            │ logging                    │")
    print("    ├──────────┼──────────────────────────────────┼────────────────────────────┤")
    print("    │ 级别     │ 没有                             │ 五级，可一行开关上线/下线  │")
    print("    │ 时间     │ 要自己拼                         │ 自动带（asctime）          │")
    print("    │ 写到哪   │ 只能屏幕                         │ 屏幕/文件/网络，可同时多个 │")
    print("    │ 出错现场 │ 要自己 traceback.format_exc()    │ logging.exception 一行搞定 │")
    print("    │ 上线后   │ 删不干净（散落各处）             │ 改级别就行，代码不用动     │")
    print("    └──────────┴──────────────────────────────────┴────────────────────────────┘")
    print()
    print("  ⚠️  坑：basicConfig 一个进程只生效一次（第二次静默失效）。")
    print("      要么只配一次，要么像这里加 force=True 覆盖。")
    print()


# ----------------------------------------------------------------------
# 演示 7：assert 断言
# ----------------------------------------------------------------------
def demo7_assert():
    print("=" * 62)
    print("【演示 7】assert：给『绝不该发生』的情况上一道锁")
    print("=" * 62)

    def average(scores):
        assert len(scores) > 0, "scores 不能为空列表"     # 条件为假 → 抛 AssertionError
        return sum(scores) / len(scores)

    print("    average([90, 80]) =", average([90, 80]))
    try:
        average([])
    except AssertionError as e:
        print("    average([]) → 被抓住：AssertionError:", e)
    print()
    print("  用法：查『内部逻辑假设』，不是查用户输入（用户输入该用 if + raise）。")
    print("  ⚠️  python -O 运行时会跳过所有 assert，所以别用它做业务校验。")
    print()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    demo1_traceback()
    demo2_error_zoo()
    demo3_print_debug()
    demo4_breakpoint()
    demo5_try_blocks()
    demo6_logging()
    demo7_assert()
    print("=" * 62)
    print("【今日总结】调试四板斧")
    print("=" * 62)
    print("  ① 读：从最后一行往上看，先看错误名，再找自己的文件那一行")
    print("  ② 印：print / f\"{x=}\" / !r 把中间值摊开，别靠猜")
    print("  ③ 停：breakpoint() 进 pdb，p / n / s / c 四个命令")
    print("  ④ 记：logging 分级留痕，出错用 logging.exception")
    print("=" * 62)


if __name__ == "__main__":
    main()
