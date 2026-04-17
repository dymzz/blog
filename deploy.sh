#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/output"
BRANCH="gh-pages"

echo "==> 安装依赖..."
pip install pelican markdown

echo "==> 生成静态站点..."
pelican "$SCRIPT_DIR/content" -o "$OUTPUT_DIR" -s "$SCRIPT_DIR/publishconf.py"

echo "==> 部署到 GitHub Pages ($BRANCH)..."
if [ ! -d "$OUTPUT_DIR/.git" ]; then
    git -C "$OUTPUT_DIR" init
fi

git -C "$OUTPUT_DIR" checkout --orphan "$BRANCH" 2>/dev/null || git -C "$OUTPUT_DIR" checkout "$BRANCH"
git -C "$OUTPUT_DIR" add -A
git -C "$OUTPUT_DIR" commit -m "Deploy: $(date +%Y-%m-%d %H:%M:%S)" --allow-empty

REMOTE_URL=$(git -C "$SCRIPT_DIR" remote get-url origin 2>/dev/null || echo "")
if [ -n "$REMOTE_URL" ]; then
    git -C "$OUTPUT_DIR" remote add origin "$REMOTE_URL" 2>/dev/null || git -C "$OUTPUT_DIR" remote set-url origin "$REMOTE_URL"
    git -C "$OUTPUT_DIR" push -f origin "$BRANCH"
    echo "==> 部署完成！"
else
    echo "==> 未检测到 remote origin，请手动推送 output 目录到 $BRANCH 分支"
fi
