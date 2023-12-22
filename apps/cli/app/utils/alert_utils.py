from functools import wraps

from core.models import Response, ResponseType
from rich.console import Console

console = Console()


def confirm_to_continue():
    input("\n\nPress Enter to continue...")


def has_error(response: Response):
    return response.type.value == ResponseType.ERROR.value


def print_error(response: Response):
    console.print(f"{response.message} 😅️", end="\n." * 10)


def print_confirmation_message(response: Response, message: str):
    if has_error(response):
        print_error(response)
    else:
        console.print(message, end="\n." * 10)


def with_confirmation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        confirm_to_continue()
        return result

    return inner
