Title: 教程：从零搭建个人博客并部署上线
Date: 2026-04-17
Description: 使用 Python + Pelican 搭建中文优先的静态博客，并结合 Vibe Coding 快速部署上线的完整教程。

## 一、环境准备

### 1.1 安装 Python

确保已安装 Python 3.10+，推荐使用 `uv` 或 `pyenv` 管理版本：

```bash
python --version
```

### 1.2 创建项目目录

```bash
mkdir blog && cd blog
```

### 1.3 初始化项目

```bash
py init
```

在 `pyproject.toml` 中添加依赖：

```toml
[project]
name = "blog"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "pelican[markdown]",
    "typogrify",
]
```

### 1.4 安装依赖

```bash
pip install pelican markdown typogrify
```

---

## 二、项目结构

```
blog/
├── content/
│   ├── pages/          # 静态页面（关于、项目等）
│   │   ├── about.md
│   │   └── projects.md
│   └── posts/          # 博客文章
│       ├── welcome.md
│       └── python-decorator.md
├── theme/
│   ├── static/
│   │   └── css/
│   │       └── main.css
│   └── templates/
│       ├── base.html       # 基础布局
│       ├── index.html      # 首页
│       ├── blog.html       # 博客列表页
│       ├── article.html    # 文章详情页
│       ├── page.html        # 页面详情
│       ├── tags.html        # 标签汇总页
│       ├── tag.html         # 单个标签页
│       ├── archives.html    # 归档页
│       ├── categories.html  # 分类汇总页
│       ├── category.html    # 单个分类页
│       └── 404.html         # 404 页面
├── output/              # 构建产物（自动生成）
├── pelicanconf.py       # 开发配置
├── publishconf.py       # 发布配置
└── main.py              # 构建脚本
```

---

## 三、核心配置

### 3.1 pelicanconf.py

```python
SITENAME = "我的博客"
SITEURL = ""
PATH = "content"
TIMEZONE = "Asia/Shanghai"
DEFAULT_LANG = "zh"
DEFAULT_LOCALE = "zh_CN"

THEME = "theme"

# URL 结构
ARTICLE_URL = "posts/{slug}.html"
ARTICLE_SAVE_AS = "posts/{slug}.html"
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"
TAG_URL = "tag/{slug}.html"
TAGS_URL = "tags.html"
ARCHIVES_URL = "archives.html"
INDEX_SAVE_AS = "blog/index.html"

# 导航菜单
MENUITEMS = [
    ("首页", "/"),
    ("博客", "/blog/"),
    ("标签", "/tags.html"),
    ("归档", "/archives.html"),
    ("项目", "/pages/projects.html"),
    ("关于", "/pages/about.html"),
]

# SEO
SITEDESCRIPTION = "一个关于技术与生活的个人博客"
```

### 3.2 publishconf.py

```python
SITEURL = os.environ.get("SITEURL", "")
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
```

---

## 四、设计文档关键要求

根据 `docs/design.md` 的约束，必须遵循：

| 要求 | 实现 |
|------|------|
| `<html lang="zh-CN">` | `base.html` 模板硬编码 |
| 全站中文 UI | 导航、标题、按钮、空状态均为中文 |
| 静态可用 | 核心内容不依赖 JavaScript |
| 渐进增强 | 仅导航折叠、深色模式用 JS 增强 |
| 中文 title 格式 | `页面标题 - 站点名称` |
| 中文 description | 每页输出 meta description |
| 响应式 | 360px / 390px / 768px / 1024px / 1280px |
| 文章 frontmatter | 至少包含 title、description、tags、date |

---

## 五、模板要点

### 5.1 base.html — 统一出口

所有页面继承 `base.html`，统一输出：

- `<html lang="zh-CN">`
- `<meta name="description">`
- Open Graph 标签
- 导航、页脚、CSS

### 5.2 article.html — 文章详情

- title 格式：`文章标题 - 站点名称`
- description 优先使用文章 summary/description，回退到站点描述
- 文章目录（TOC）
- 上/下一篇导航

### 5.3 响应式 CSS

- 使用 CSS 自定义属性实现深色模式（`prefers-color-scheme`）
- 移动端导航折叠（纯 JS 增强，无 JS 时导航仍可用）
- 最小支持 360px 宽度

---

## 六、内容创作

### 6.1 文章 frontmatter 示例

```markdown
Title: 文章标题
Date: 2026-04-17
Category: 技术
Tags: Python, 教程
Summary: 文章摘要（用于列表展示）
Description: 文章描述（用于 SEO meta）

正文内容...
```

### 6.2 页面 frontmatter 示例

```markdown
Title: 关于
Description: 关于这个博客和作者的信息。

页面正文...
```

---

## 七、构建与预览

### 7.1 构建静态站点

```bash
pelican content -s pelicanconf.py
```

### 7.2 本地预览

```bash
pelican --listen
```

浏览器访问 `http://localhost:8000`

### 7.3 开发模式（自动重载）

```bash
pelican --autoreload --listen
```

### 7.4 使用构建脚本

```bash
python main.py build     # 构建
python main.py dev       # 开发模式
python main.py publish   # 生产构建
```

---

## 八、使用 Vibe Coding 快速部署上线

### 8.1 什么是 Vibe Coding

Vibe Coding 是一种借助 AI 辅助编程的工作方式：用自然语言描述需求，AI 生成代码，人工审查和调整。本博客项目就是用这种方式在短时间内完成的。

### 8.2 部署到 GitHub Pages

**步骤一：创建 GitHub 仓库**

```bash
git init
git add .
git commit -m "初始化博客项目"
git remote add origin https://github.com/你的用户名/你的用户名.github.io.git
git push -u origin main
```

**步骤二：配置 GitHub Actions 自动部署**

在项目根目录创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy Blog

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.14'
      - run: pip install pelican[markdown] typogrify
      - run: pelican content -s publishconf.py
      - uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./output
```

**步骤三：推送触发部署**

```bash
git push
```

推送后 GitHub Actions 自动构建并发布到 `https://你的用户名.github.io`。

### 8.3 部署到 Netlify

1. 登录 [Netlify](https://netlify.com)
2. 选择"从 Git 导入"
3. 连接 GitHub 仓库
4. 配置构建命令：`pelican content -s publishconf.py`
5. 发布目录：`output`
6. 点击部署

### 8.4 部署到 Vercel

1. 登录 [Vercel](https://vercel.com)
2. 导入 Git 仓库
3. 构建命令：`pelican content -s publishconf.py`
4. 输出目录：`output`
5. 部署

### 8.5 自定义域名（可选）

在 `pelicanconf.py` 或 `publishconf.py` 中设置：

```python
SITEURL = "https://yourdomain.com"
```

然后在域名商处将域名 CNAME 指向部署平台。

---

## 九、验收检查清单

### 9.1 中文化

- [x] 全站主 UI 文案默认中文
- [x] `<html lang="zh-CN">` 所有页面生效
- [x] 分页、空状态、错误提示中文

### 9.2 静态可用性

- [x] 禁用 JavaScript 后首页可访问
- [x] 禁用 JavaScript 后文章可阅读
- [x] 导航链接可用
- [x] 标签、归档页可访问

### 9.3 SEO

- [x] 每页有中文 `<title>`
- [x] 每页有 `<meta name="description">`
- [x] Open Graph 标签输出
- [x] 无占位文本残留

### 9.4 响应式

- [x] 360px 可读
- [x] 768px 布局正常
- [x] 1280px 无异常

---

## 十、Vibe Coding 实践总结

| 阶段 | 做什么 | AI 辅助 |
|------|--------|---------|
| 需求分析 | 编写设计文档 | AI 帮助梳理检查项 |
| 项目初始化 | 创建结构、安装依赖 | AI 生成脚本和配置 |
| 模板开发 | HTML 模板 + SEO 标签 | AI 生成模板代码 |
| 样式开发 | 响应式 CSS + 深色模式 | AI 生成样式代码 |
| 内容创建 | 文章和页面 | AI 生成示例内容 |
| 部署上线 | CI/CD 配置 | AI 生成部署脚本 |
| 验收检查 | 逐条核对设计文档 | 人工最终确认 |

**核心原则：先保证中文默认输出，先保证静态可用，再增加增强交互，最后优化视觉体验。顺序不可颠倒。**