from core.controller import controller


def cli_app():
    while True:
        print("\nEnter a command: ")
        user_input = input()

        result = controller(user_input)
        if result is None:
            print("\nGood bye!")
            break

        print(result)
