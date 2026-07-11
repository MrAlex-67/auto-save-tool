import sys
import time
from datetime import datetime

try:
    import pyautogui
    from rich.console import Console
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.table import Table
    from rich.live import Live
    from rich.text import Text
except ImportError as e:
    print(f"[!] 缺少依赖库: {e}")
    print("请执行: pip install pyautogui rich")
    sys.exit(1)

# ============================================================
# ⚙️ 配置区
# ============================================================
INTERVAL_SECONDS = 300       # 保存间隔 (秒) | 5分钟 = 300秒
HOTKEY_COMBO     = ['ctrl', 's']  # 快捷键组合
FAILSAFE         = True      # 鼠标移到左上角紧急停止
# ============================================================

console = Console()
save_count = 0
start_time = time.time()
log_history = []

def get_uptime():
    """计算程序运行时长"""
    elapsed = int(time.time() - start_time)
    h, m, s = elapsed // 3600, (elapsed % 3600) // 60, elapsed % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def generate_dashboard(next_save_in: float):
    """生成科技感仪表盘"""
    global save_count

    # --- 顶部标题 ---
    title = Text("⟨ 自动保存协议 v2.0 ⟩", style="bold cyan", justify="center")

    # --- 状态面板 ---
    status_table = Table.grid(padding=(0, 2))
    status_table.add_column(style="dim", width=14)
    status_table.add_column(style="bold green")

    status_table.add_row("运行状态", "● 在线")
    status_table.add_row("保存间隔", f"{INTERVAL_SECONDS}秒 ({INTERVAL_SECONDS//60}分钟)")
    status_table.add_row("触发快捷键", " + ".join(HOTKEY_COMBO).upper())
    status_table.add_row("已运行时长", get_uptime())
    status_table.add_row("累计保存次数", str(save_count))

    countdown = max(0, int(next_save_in))
    bar_width = 30
    progress = 1 - (countdown / INTERVAL_SECONDS)
    filled = int(bar_width * progress)
    bar = "█" * filled + "░" * (bar_width - filled)
    status_table.add_row("下次保存倒计时", f"[cyan]{bar}[/] {countdown}秒")

    # --- 日志面板 ---
    log_text = "\n".join(log_history[-8:]) if log_history else "[dim]等待首次保存...[/]"

    # --- 组装布局 ---
    layout = Layout()
    layout.split_column(
        Layout(title, size=3),
        Layout(Panel(status_table, title="[ 系统状态 ]", border_style="cyan", padding=(1, 2)), size=10),
        Layout(Panel(log_text, title="[ 事件日志 ]", border_style="magenta", padding=(1, 2))),
        Layout(Text("🛑 Ctrl+C 终止 | 鼠标移至左上角紧急制动", style="dim yellow", justify="center"), size=3)
    )
    return layout

def execute_save():
    """执行保存并记录日志"""
    global save_count
    try:
        pyautogui.hotkey(*HOTKEY_COMBO)
        save_count += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] ✔ 第 {save_count:04d} 次保存成功"
        log_history.append(f"[green]{log_entry}[/]")
        console.bell()  # 终端提示音
    except Exception as e:
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_history.append(f"[red][{timestamp}] ✘ 保存失败: {e}[/]")

def main():
    pyautogui.FAILSAFE = FAILSAFE
    pyautogui.PAUSE = 0.05

    console.clear()
    console.print("\n[bold cyan]⟨ 正在初始化自动保存协议 ⟩[/]")
    console.print("[dim]系统将在 3 秒后启动...\n[/]")
    time.sleep(3)

    last_save_time = time.time()

    with Live(generate_dashboard(INTERVAL_SECONDS), console=console, refresh_per_second=4, screen=True) as live:
        while True:
            now = time.time()
            next_save_in = INTERVAL_SECONDS - (now - last_save_time)

            if next_save_in <= 0:
                execute_save()
                last_save_time = time.time()
                next_save_in = INTERVAL_SECONDS

            live.update(generate_dashboard(next_save_in))
            time.sleep(0.25)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.clear()
        console.print("\n[bold red]⟨ 用户已手动终止自动保存协议 ⟩[/]")
        console.print(f"[dim]总会话保存次数: {save_count} | 运行时长: {get_uptime()}[/]\n")
        sys.exit(0)