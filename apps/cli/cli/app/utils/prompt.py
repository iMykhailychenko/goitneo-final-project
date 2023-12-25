import beaupy
from rich.console import Console

from cli.app.utils.clear_console import clear_console

console = Console()


def optional_text(value: str) -> str:
    return '[yellow bold][Optional, press "Enter" to skip] [white]' + value


def required_text(value: str) -> str:
    return "[red bold][Required] [white]" + value


def prompt(
    question: str,
    error_message: str = "",
    optional=False,
    *args,
    **kwargs,
) -> str:
    result = None
    while result is None:
        try:
            message = optional_text(question) if optional else required_text(question)
            message += "\n"
            result = beaupy.prompt(message, *args, **kwargs)
        except Exception:
            console.print(error_message, style="white on red")
    clear_console()
    return result


def prompt_set(
    question: str,
    question_next: str,
    error_message: str = "",
    optional=False,
    *args,
    **kwargs,
) -> set[str]:
    result = set()
    while True:
        message = question_next if len(result) else question
        new_result = prompt(
            message,
            *args,
            error_message=error_message,
            optional=optional,
            **kwargs,
        )
        if not new_result.strip():
            break
        result.add(new_result)
    return result
