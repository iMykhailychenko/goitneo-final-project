import beaupy
from rich.console import Console

from app.utils.clear_console import clear_console

console = Console()


def optional_text(value: str) -> str:
    return "[yellow bold][Optional, Enter to skip] [white]" + value


def required_text(value: str) -> str:
    return "[red bold][Required] [white]" + value


def prompt(
    question: str,
    error_message: str = "",
    validator: callable = lambda _: True,
    optional=False,
) -> str:
    result = None
    while result is None:
        try:
            message = optional_text(question) if optional else required_text(question)
            result = beaupy.prompt(message, validator=validator)
        except beaupy.ValidationError:
            console.print(error_message, style="white on red")
    clear_console()
    return result


def prompt_set(
    question: str,
    question_next: str,
    error_message: str = "",
    validator: callable = lambda _: True,
    optional=False,
) -> set[str]:
    result = set()
    while True:
        message = question_next if len(result) else question
        new_result = prompt(
            message, validator=validator, error_message=error_message, optional=optional
        )
        result.add(new_result)
        if not new_result:
            break
    return result
