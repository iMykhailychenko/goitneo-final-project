from typing import Optional

from core.misc import Actions, CommandMessages, ValidationMessages, validation
from core.models import Payload, Response, ResponseType
from core.services import add_contact, get_birthdays_this_week

services_map = {
    # Base
    Actions.HELLO.value: lambda _: Response(message=CommandMessages.HELP_QUESTION),
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
    Actions.BIRTHDAYS.value: get_birthdays_this_week,
    # Notes
    Actions.ADD_NOTE.value: lambda _: None,
    Actions.DELETE_NOTE.value: lambda _: None,
    Actions.UPDATE_NOTE.value: lambda _: None,
}

default_response = Response(
    message=ValidationMessages.INVALID_COMMAND, type=ResponseType.ERROR
)


@validation
def controller(cmd: Actions, payload: Optional[Payload] = None) -> Optional[Response]:
    return services_map.get(cmd.value, lambda *_: default_response)(payload)
