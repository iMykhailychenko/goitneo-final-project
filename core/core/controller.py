from typing import List

from core.misc import Actions, validation
from core.models import Response, ResponseType

services_map = {
    Actions.ADD.value: lambda *args: None,
    Actions.CHANGE.value: lambda *args: None,
    Actions.PHONE.value: lambda *args: None,
    Actions.ALL.value: lambda *args: None,
    Actions.ADD_BIRTHDAY.value: lambda *args: None,
    Actions.SHOW_BIRTHDAY.value: lambda *args: None,
    Actions.BIRTHDAYS.value: lambda *args: None,
    Actions.DELETE.value: lambda *args: None,
    Actions.HELLO.value: lambda *args: Response(value="How can I help you?"),
    Actions.EXIT.value: lambda *args: None,
    Actions.CLOSE.value: lambda *args: None,
}


@validation
def controller(user_input: List[str]) -> Response:
    cmd, *args = user_input
    return services_map.get(
        cmd, lambda *_: Response(value="Invalid command.", type=ResponseType.SUCCESS)
    )(args)
