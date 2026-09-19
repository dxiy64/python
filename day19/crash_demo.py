# -*- coding: utf-8 -*-
# ============================================
# crash_demo.py · 一个"故意会崩"的小程序
# 用途：观察真实 traceback 长什么样（Day19 演示 1 的素材）
# 运行：cd day19 然后 python crash_demo.py      ← 预期：报错退出，这是正常的！
# ============================================


def average(scores):
    """算平均分 = 总和 ÷ 个数"""
    return sum(scores) / len(scores)      # ← 当 scores 是空列表，len 是 0 → 除零


def load_scores(name):
    """假装从数据源读成绩（这里用字典模拟，方便看调用链）"""
    data = {
        "光羽": [90, 85, 77],
        "小明": [],                      # ← 小明的成绩表是空的（问题根源）
    }
    return data[name]


def main():
    for name in ["光羽", "小明"]:
        scores = load_scores(name)
        print(f"{name} 的平均分：{average(scores):.1f}")


if __name__ == "__main__":
    main()
