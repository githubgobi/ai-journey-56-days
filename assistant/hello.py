"""Day 01: confirm the virtual environment and print a welcome message."""

import sys

from rich.console import Console


def main() -> None:
    console = Console()

    # Which Python is running, and where it lives
    console.print(f"[cyan]Python version:[/cyan] {sys.version}")
    console.print(f"[cyan]Environment:[/cyan]    {sys.prefix}")

    console.print("[bold green]AI Journey started[/bold green] :rocket:")


if __name__ == "__main__":
    main()
