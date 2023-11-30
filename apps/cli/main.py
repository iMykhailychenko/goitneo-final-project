from core import controller, Database

db = Database()

def main():
    db.connect()
    
    while True:
        print("\nEnter a command: ")
        user_input = input()

        result = controller(user_input)
        if result is None:
            print("\nGood bye!")
            break

        print(result)


if __name__ == "__main__":
    main()
