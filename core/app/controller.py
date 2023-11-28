from app.misc import Actions, validation
from app.models import Response
from app.services import parse_input

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


@validation
def controller(user_input: str) -> Response:
    cmd, *args = parse_input(user_input)
    return services_map.get(cmd, lambda *_: "Invalid command.")(args)
