from time import sleep

from core.database import Database
from rich.console import Console

from app.controller import Controller
from app.exeptions import ExitException
from app.utils import clear_console

controller = Controller()
console = Console()
db = Database()


def main():
    with console.status("Welcome!"):
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
