from time import sleep

from core.database import Database
from rich.console import Console

from cli.app import App
from cli.app.exeptions import ExitException
from cli.app.utils import clear_console

controller = App()
console = Console()
db = Database()


def main():
    with console.status("Welcome!"):
        print("\n\n")
        db.connect()
        sleep(0.5)

    while True:
        clear_console()

        try:
            controller()
        except ExitException:
            clear_console()
            console.print("\nGoodbye!\n", style="white on red")
            break


if __name__ == "__main__":
    main()
