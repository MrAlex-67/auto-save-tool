# ️ Auto-Save-Tool：给键盘装个「后悔药按钮」 / A "Regret Medicine" Button for Your Keyboard

>  **一句话简介 / One-liner:** 每隔 N 秒自动存档当前活动窗口内容，让“忘记保存”和“蓝屏崩溃”彻底远离你的工作流。
> Automatically saves the content of your active window every N seconds, keeping "forgot to save" and "blue screen crashes" far away from your workflow.

你是否经历过这些绝望瞬间？ / Have you ever experienced these moments of despair?
- 写了 3 小时文档/代码，突然断电/蓝屏/误关，心血全无 
- 沉迷创作忘记 Ctrl+S，回过神来已过去半小时
- 软件闪退没有自动恢复机制，只能对着空白屏幕发呆

- You've been writing a document/code for 3 hours, then suddenly a power outage/blue screen/accidental closure wipes it all out 
- You get lost in your creative flow and forget to hit Ctrl+S, only to realize half an hour has passed.
- The software crashes without an auto-recovery feature, leaving you staring at a blank screen.

**Auto-Save-Tool** 就是为了解决这个问题而生的轻量级后台守护工具。它像一位沉默的助手，在你专注时悄悄为你按下“保存键”。
**Auto-Save-Tool** is a lightweight background guardian born to solve this problem. Like a silent assistant, it quietly presses the "save" button for you while you're focused.

---

##  核心特性 / Core Features

-  **定时自动保存 / Timed Auto-Save:** 可自定义间隔（默认 30 秒），精准模拟 `Ctrl+S` / Customizable intervals (default 30 seconds), precisely simulating `Ctrl+S`.
-  **智能焦点识别 / Smart Focus Detection:** 仅对当前活跃窗口生效，不会干扰后台程序 / Only affects the currently active window, never interfering with background programs.
- 🪶 **极致轻量 / Extremely Lightweight:** 纯 Python 实现，内存占用 < 10MB，CPU 几乎零感知 / Pure Python implementation, memory usage < 10MB, CPU impact is virtually zero.
-  **安全透明 / Secure & Transparent:** 开源代码，无网络请求，无数据上传，隐私绝对安全 / Open-source code, no network requests, no data uploading—your privacy is absolutely safe.
- ️ **Windows 原生支持 / Windows Native Support:** 基于 `pywin32` 深度集成系统 API / Deeply integrated with system APIs via `pywin32`.

---

##  快速开始 / Quick Start

### 方式一：直接运行源码（推荐开发者）/ Option 1: Run Source Code Directly (Recommended for Developers)

```bash
# 1. 克隆仓库 / Clone the repository
git clone https://github.com/MrAlex-67/auto-save-tool.git
cd auto-save-tool

# 2. 安装依赖 / Install dependencies
pip install pywin32

# 3. 启动工具 / Launch the tool
python auto_save.py

方式二：打包为 .exe（推荐给日常用户）/ Option 2: Package as .exe (Recommended for Daily Users)
无需安装 Python 环境，双击即可运行 / No Python environment required, just double-click to run:
```bash
# 1. 安装打包工具 / Install packaging tool
pip install pyinstaller

# 2. 一键打包（无控制台窗口 + 单文件）/ One-click packaging (no console window + single file)
pyinstaller --onefile --noconsole --name "AutoSaveTool" auto_save.py
```
生成的 AutoSaveTool.exe 位于 dist/ 文件夹中，可复制到任意 Windows 电脑直接使用。
The generated AutoSaveTool.exe will be located in the dist/ folder. You can copy it to any Windows PC and use it directly.
进阶打包（添加自定义图标）/ Advanced Packaging (Add Custom Icon):
```bash
pyinstaller --onefile --noconsole --icon=app.ico --name "AutoSaveTool" auto_save.py
```
️ 配置说明 / Configuration
打开 auto_save.py，修改顶部常量即可自定义行为 / Open auto_save.py and modify the constants at the top to customize behavior:
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `SAVE_INTERVAL` | `30` | 自动保存间隔（秒） |
| `HOTKEY_TOGGLE` | `Ctrl+Shift+S` | 暂停/恢复自动保存的快捷键 |
| `EXCLUDE_APPS` | `["notepad.exe"]` | 排除列表（这些程序不触发自动保存） |

###常见问题 / FAQ
#Q: 杀毒软件报毒怎么办？ / My antivirus software flags it as a virus. What should I do?
A: PyInstaller 打包的 exe 可能被误报。请查看源码确认安全后，添加信任或自行打包。我们承诺代码 100% 透明。
A: Executables packaged with PyInstaller are sometimes flagged as false positives. Please review the source code to confirm its safety, then add it to your trust list or package it yourself. We promise the code is 100% transparent.
#Q: 支持 macOS / Linux 吗？ / Does it support macOS / Linux?
A: 当前版本仅支持 Windows。macOS/Linux 适配已在规划中，欢迎 PR 贡献！
A: The current version only supports Windows. macOS/Linux adaptation is in the planning stages—PR contributions are welcome!
#Q: 会自动覆盖我的文件吗？ / Will it automatically overwrite my files?
A: 本工具仅模拟按键操作，保存逻辑完全由目标应用程序自身决定（如 Word 的自动保存、VSCode 的即时写入等），不会产生额外副本。
A: This tool only simulates keystrokes. The saving logic is entirely determined by the target application itself (e.g., Word's auto-save, VSCode's instant write), so it won't create extra copies.
###贡献与反馈 / Contribution & Feedback
发现 Bug？有新想法？欢迎提交 Issue 或 Pull Request！
Found a bug? Have a new idea? Feel free to submit an Issue or Pull Request!
如果这个小工具帮到了你，请点个 Star 鼓励一下～
If this little tool helped you, please give it a Star to show your support~
#愿你的每一份努力，都被温柔存档。 ️
#May every bit of your effort be gently archived. ️
