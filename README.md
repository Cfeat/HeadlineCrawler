# 📰 WeChat News Bot (微信每日热搜推送)

这是一个基于 Python 的轻量级爬虫 Bot，用于抓取百度热搜并通过 PushPlus 推送到微信。支持 GitHub Actions 自动定时运行，完全免费且无需服务器。

## ✨ 功能

- **数据源**: 实时抓取百度热搜 Top 15。
- **推送**: 通过 [PushPlus](http://www.pushplus.plus/) 推送到微信。
- **自动化**: 支持 GitHub Actions 每天定时运行（默认北京时间 08:00）。
- **安全性**: 使用环境变量传递 Token，保护隐私。

## 🚀 快速开始

### 方式一：使用 GitHub Actions (推荐，无需挂机)

1. **Fork 本仓库**
   点击右上角的 `Fork` 按钮，将代码复制到你的 GitHub 账户。

2. **获取 PushPlus Token**
   - 访问 [PushPlus](http://www.pushplus.plus/) 官网。
   - 登录并复制你的 Token。

3. **设置 GitHub Secrets**
   - 进入你 Fork 后的仓库页面。
   - 点击 `Settings` -> `Secrets and variables` -> `Actions` -> `New repository secret`。
   - **Name**: 填入 `PUSHPLUS_TOKEN`
   - **Secret**: 填入你的 Token 字符串。
   - 点击 `Add secret` 保存。

4. **激活 Action**
   - 点击仓库上方的 `Actions` 标签。
   - 如果看到警告，点击 "I understand my workflows, go ahead and enable them"。
   - 可以在左侧选择 "每日新闻推送"，点击右侧 `Run workflow` 进行一次立即测试。

---

### 方式二：本地运行

1. **安装依赖**
   ```bash
   pip install -r requirements.txt

2. **立即执行**
    ```bash
    python main.py --once

3. **定时循环**
    ```bash
    python main.py

4. **后台挂起（Linux）**
    ```bash
    nohup python main.py &
    
### 方式三：脚本运行
   运行`run.bat`