# ⌨️ Auto-Save-Tool：给键盘装个「后悔药按钮」

> 💡 **一句话简介**：每隔 N 秒自动存档当前活动窗口内容，让“忘记保存”和“蓝屏崩溃”彻底远离你的工作流。

你是否经历过这些绝望瞬间？
- 写了 3 小时文档/代码，突然断电/蓝屏/误关，心血全无 😭
- 沉迷创作忘记 Ctrl+S，回过神来已过去半小时
- 软件闪退没有自动恢复机制，只能对着空白屏幕发呆

**Auto-Save-Tool** 就是为了解决这个问题而生的轻量级后台守护工具。它像一位沉默的助手，在你专注时悄悄为你按下“保存键”。

---

## ✨ 核心特性

- 🔄 **定时自动保存**：可自定义间隔（默认 30 秒），精准模拟 `Ctrl+S`
- 🎯 **智能焦点识别**：仅对当前活跃窗口生效，不会干扰后台程序
- 🪶 **极致轻量**：纯 Python 实现，内存占用 < 10MB，CPU 几乎零感知
- 🔒 **安全透明**：开源代码，无网络请求，无数据上传，隐私绝对安全
- 🖥️ **Windows 原生支持**：基于 `pywin32` 深度集成系统 API

---

## 🚀 快速开始

### 方式一：直接运行源码（推荐开发者）

```bash
# 1. 克隆仓库
git clone https://github.com/MrAlex-67/auto-save-tool.git
cd auto-save-tool

# 2. 安装依赖
pip install pywin32

# 3. 启动工具
python 自动保存.py

方式二：打包为 .exe（推荐给日常用户）
无需安装 Python 环境，双击即可运行：

```bash
# 1. 安装打包工具
pip install pyinstaller

# 2. 一键打包（无控制台窗口 + 单文件）
pyinstaller --onefile --noconsole --name "AutoSaveTool" 自动保存.py

✅ 生成的 AutoSaveTool.exe 位于 dist/ 文件夹中，可复制到任意 Windows 电脑直接使用。
💡 进阶打包（添加自定义图标）：
```bash
pyinstaller --onefile --noconsole --icon=app.ico --name "AutoSaveTool" 自动保存.py
#⚙️ 配置说明
打开 自动保存.py，修改顶部常量即可自定义行为：
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `SAVE_INTERVAL` | `30` | 自动保存间隔（秒） |
| `HOTKEY_TOGGLE` | `Ctrl+Shift+S` | 暂停/恢复自动保存的快捷键 |
| `EXCLUDE_APPS` | `["notepad.exe"]` | 排除列表（这些程序不触发自动保存） |



