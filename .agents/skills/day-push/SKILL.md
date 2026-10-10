---
name: day-push
description: Use when the user authorizes committing or pushing dayNN work. Update progress from evidence and verify the requested Git result.
---

# 当天收尾

仅用户授权提交/推送时执行，不因验收通过自动提交。先检查git status、diff、暂存区和仓库教学规则；只暂存授权文件，不使用git add -A覆盖未知改动。

README是摘要，LEARNING_PROGRESS.md记录能力证据，ROADMAP记录路线；必要改动同次提交。未验收不标完成，历史记录与当前复测分开；百分比按完成单元计算，不按日历推断。

保留学员文本数据；虚拟环境、测试数据库、生成报告等运行输出按.gitignore排除。提交前检查暂存差异；推送到核实的分支/远程，不假定origin main。分叉先检查原因，不自动rebase或覆盖未知工作。

提交后核对提交内容；若授权推送，核对远程分支SHA与本地提交。超时先核对本地/远程状态，避免重复提交。

python-tutor位于用户技能目录；更新它不意味着授权另一个技能仓库提交或推送，不执行旧hermes-skills自动同步流程。
