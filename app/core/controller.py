from app.core.models import Response
from app.core.misc import Actions


services_map = {
    Actions.ADD.value: lambda *args: None,
    Actions.CHANGE.value: lambda *args: None,
    Actions.PHONE.value: lambda *args: None,
    Actions.ALL.value: lambda *args: None,
    Actions.ADD_BIRTHDAY.value: lambda *args: None,
    Actions.SHOW_BIRTHDAY.value: lambda *args: None,
    Actions.BIRTHDAYS.value: lambda *args: None,
    Actions.DELETE.value: lambda *args: None,
    Actions.HELLO.value: lambda *args: "How can I help you?",
    Actions.EXIT.value: lambda *args: None,
    Actions.CLOSE.value: lambda *args: None,
}


def controller(user_input: str) -> Response:
    return services_map.get(user_input, lambda *_: "Invalid command.")(user_input)
