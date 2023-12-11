from typing import Optional

from core.misc import Actions, validation
from core.models import Input, Response, ResponseType
from core.services import add_contact

services_map = {
    # Base
    Actions.HELLO.value: lambda _: Response(value="How can I help you?"),
    Actions.HELP.value: lambda _: None,
    Actions.EXIT.value: lambda _: None,
    Actions.CLOSE.value: lambda _: None,
    Actions.SEARCH.value: lambda _: None,
    # Contact
    Actions.ADD.value: add_contact,
    Actions.DELETE.value: lambda _: None,
    Actions.ALL.value: lambda _: None,
    # Phone
    Actions.ADD_PHONE.value: lambda _: None,
    Actions.UPDATE_PHONE.value: lambda _: None,
    Actions.DELETE_PHONE.value: lambda _: None,
    # Birthday
    Actions.ADD_BIRTHDAY.value: lambda _: None,
    Actions.GET_BIRTHDAY.value: lambda _: None,
    Actions.DELETE_BIRTHDAY.value: lambda _: None,
    Actions.UPDATE_BIRTHDAY.value: lambda _: None,
    Actions.BIRTHDAYS.value: lambda _: None,
    # Notes
    Actions.ADD_NOTE.value: lambda _: None,
    Actions.DELETE_NOTE.value: lambda _: None,
    Actions.UPDATE_NOTE.value: lambda _: None,
}


@validation
def controller(input: Input) -> Optional[Response]:
    return services_map.get(
        input.command.value,
        lambda *_: Response(value="Invalid command.", type=ResponseType.SUCCESS),
    )(input)
