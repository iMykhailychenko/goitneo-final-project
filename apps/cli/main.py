from pathlib import Path

from core import Database, controller

from config import DB_FOLDER_PATH

db = Database()
db_file = Path(DB_FOLDER_PATH)


def main():
    db.connect(db_file)

    while True:
        print("\nEnter a command: ")
        user_input = input()

        result = controller(user_input)
        if result is None:
            print("\nGood bye!")
            break

        print(result.value)


if __name__ == "__main__":
    main()

