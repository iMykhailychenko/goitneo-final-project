from pathlib import Path

from core.database import Database
from rich.console import Console

from cli.app import App
from cli.app.exeptions import ExitException
from cli.app.utils import clear_console

app = App()
console = Console()
db = Database()
DB_PATH = Path(__file__).parent.parent.parent.parent / "tmp"


def main():
    with console.status("Welcome!"):
        clear_console()
        db.connect(DB_PATH)

    while True:
        clear_console()
        try:
            app()
        except ExitException:
            clear_console()
            console.print("\nGoodbye!\n", style="white on red")
            break


if __name__ == "__main__":
    main()
