from typing import List, Optional

from core.misc import Actions, validation
from core.models import Input, Response, ResponseType
from core.services import add_contact

services_map = {
    Actions.ADD.value: add_contact,
    Actions.CHANGE.value: lambda _: None,
    Actions.PHONE.value: lambda _: None,
    Actions.ALL.value: lambda _: None,
    Actions.ADD_BIRTHDAY.value: lambda _: None,
    Actions.SHOW_BIRTHDAY.value: lambda _: None,
    Actions.BIRTHDAYS.value: lambda _: None,
    Actions.DELETE.value: lambda _: None,
    Actions.HELLO.value: lambda _: Response(value="How can I help you?"),
    Actions.EXIT.value: lambda _: None,
    Actions.CLOSE.value: lambda _: None,
}


@validation
def controller(input: Input) -> Optional[Response]:
    return services_map.get(
        input.command.value,
        lambda *_: Response(value="Invalid command.", type=ResponseType.SUCCESS),
    )(input)
