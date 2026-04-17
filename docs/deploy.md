# 快速部署

```bash
bash deploy.sh
```

脚本会自动完成：
1. 安装 Pelican 及 Markdown 依赖
2. 生成静态站点到 `output/`
3. 推送到 `gh-pages` 分支

**前提**：项目已关联 GitHub 远程仓库，且 GitHub Pages 设置为从 `gh-pages` 分支读取。
