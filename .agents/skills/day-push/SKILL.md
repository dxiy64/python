---
name: day-push
description: Use when committing dayNN work. README progress update plus git push with verification.
---

# 当天收尾推送

## 何时用

作业验收通过后，提交代码 + 更新 README 进度 + 推送到 GitHub 时用。

## 流程（已验证）

```bash
git status --short
git diff --stat

git add -A
git commit -m "feat: dayNN 一句话说明"
git pull --rebase origin main
git push origin main

# 验证远端真的动了（HEAD 必须等于 REMOTE）
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

## README 进度（和代码同一次提交）

- 徽章数字、百分比、emoji 方格数从 day 地图重数，不目测（如 21/90 = 23%）。
- 中文徽章 URL 必须 percent-encode，提交前 `curl -s -o /dev/null -w "%{http_code}" "<url>"` 确认 200。
- 规则：README 只写已验收的事实，不写预告（作业没验收前不标 ✅）。

## 项目约束

- `ledger.json`、`contacts.json` 是学员数据，**跟代码一起提交**。
- `dayNN/out/`、`out_hw*/` 是运行产出，**不进版本库**（见 `.gitignore`）。
- `push` 超时（exit 124）时：先 `git log --oneline -3` 确认本地提交已生成，再 `git ls-remote` 看远端，最后补一次 `git push origin main` 即可，不要重做 commit。
