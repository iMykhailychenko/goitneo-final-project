from typing import Tuple

from beaupy import select
from rich.console import Console

from cli.app.constants import base

console = Console()


def base_action(*_) -> Tuple[str, None]:
    console.print("\nHow can I help you?\n", style="white on blue")
    return select(base, cursor=">>>", cursor_style="cyan"), None
