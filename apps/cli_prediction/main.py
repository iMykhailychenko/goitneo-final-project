from core import Actions, controller
from core.database import Database
from prompt_toolkit import prompt
from utils.completer import CommandCompleter
from utils.parser import parse_input
from rich.console import Console

database = Database()
console = Console()


def main():
    with console.status("Welcome!"):
        database.connect()

    while True:
        user_input = prompt('Enter command: ', completer=CommandCompleter(), style="white on red")
        if user_input:
            command, *args = parse_input(user_input)
            
        result = controller(command, args)
        if not result:
            console.print("\nGoodbye!\n", style="white on red")
            break
        console.print(result)  

if __name__ == "__main__":
    main()