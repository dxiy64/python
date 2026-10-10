---
name: homework-verify
description: Use when verifying dayNN homework runs. Isolated acceptance with explicit requirements and learner-owned checks.
---

# 作业验收

先读仓库AGENTS.md、TEACHING.md、任务书、代码与种子数据；本次要求与历史案例分开，提前明确通过标准，不把新挑战追溯为旧作业失败。

Windows/PowerShell中优先项目.venv/Scripts/python.exe；验证放在当前工作区work下唯一命名副本或临时数据库，不能污染真实数据。可用Python subprocess.run传input、timeout并检查退出码；未知循环限时与限输出。

分别检查正常、边界、关键失败以及跨进程持久化。依据任务决定合法金额等输入，不能把Day21的某组规则强加所有作业。网络解析用本地样本，联网另记。排行并列明确规则，SQL与Counter对齐。

让学员逐步自己写最小断言或验证表。报告需求、预期/实际、运行条件、帮助程度、阻塞/功能错误/建议；验收事实写入LEARNING_PROGRESS.md。TODO未完成标待完成，不伪造通过。

清理临时副本前确认绝对路径在workspace/work范围内，用原生PowerShell LiteralPath操作；不使用跨shell删除，也不删除学员数据。
