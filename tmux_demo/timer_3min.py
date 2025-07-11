#!/usr/bin/env python3
"""
Console Timer with rich Progress + colorama 彩色文字
"""

import time
import sys
from rich.console import Console
from rich.progress import Progress, TimeElapsedColumn, BarColumn, TextColumn
from colorama import init as colorama_init, Fore, Style

def run_rich_color_timer(duration: int = 180) -> None:
    """
    用 rich 顯示進度條，用 colorama 輸出彩色完成 / 中斷訊息。
    """
    # 初始化 colorama（自動在 Windows 上處理 ANSI）
    colorama_init(autoreset=True)

    console = Console()

    # 建立一個包含進度條、已耗時、百分比、剩餘時間的 Progress
    with Progress(
        TextColumn("[bold blue]Timer:[/]"),
        BarColumn(bar_width=None),
        TextColumn("{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("", total=duration)
        try:
            while not progress.finished:
                time.sleep(1)
                progress.update(task, advance=1)
        except KeyboardInterrupt:
            # 中斷時用紅色提示
            console.print(f"\n{Fore.RED}[!] 計時中斷！{Style.RESET_ALL}")
            return

    # 完成時用綠色提示
    console.print(f"{Fore.GREEN}[✔] 已完成 {duration} 秒計時！{Style.RESET_ALL}")

def parse_args() -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Console timer: rich 進度條 + colorama 彩色輸出"
    )
    parser.add_argument(
        "-d", "--duration",
        type=int,
        default=180,
        help="總運行時間（秒），預設 180 秒"
    )
    args = parser.parse_args()
    return args.duration

def main() -> None:
    duration = parse_args()
    run_rich_color_timer(duration)
    print("程式結束。")

if __name__ == "__main__":
    main()
