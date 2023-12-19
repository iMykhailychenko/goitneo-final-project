from typing import Optional

from core.misc import Actions, CommandMessages, ValidationMessages, validation
from core.models import Payload, Response, ResponseType
from core.services import (
    add_birthday,
    add_contact,
    add_phone_number,
    delete_birthday,
    get_birthdays_by_duration,
    update_birthday,
    add_note,
)

services_map = {
    # Base
    Actions.EXIT.value: lambda _: None,
    Actions.CLOSE.value: lambda _: None,
    Actions.SEARCH.value: lambda _: None,
    # Contact
    Actions.ADD.value: add_contact,
    Actions.DELETE.value: lambda _: None,
    Actions.ALL.value: lambda _: None,
    # Phone
    Actions.ADD_PHONE.value: add_phone_number,
    Actions.UPDATE_PHONE.value: lambda _: None,
    Actions.DELETE_PHONE.value: lambda _: None,
    # Birthday
    Actions.ADD_BIRTHDAY.value: add_birthday,
    Actions.DELETE_BIRTHDAY.value: delete_birthday,
    Actions.UPDATE_BIRTHDAY.value: update_birthday,
    Actions.BIRTHDAYS.value: get_birthdays_by_duration,
    # Notes
    Actions.ADD_NOTE.value: add_note,
    Actions.DELETE_NOTE.value: lambda _: None,
    Actions.UPDATE_NOTE.value: lambda _: None,
    # Tags
    Actions.ADD_TAG.value: lambda _: None,
    Actions.DELETE_TAG.value: lambda _: None,
    Actions.UPDATE_TAG.value: lambda _: None,
}

default_response = Response(
    message=ValidationMessages.INVALID_COMMAND, type=ResponseType.ERROR
)


@validation
def controller(cmd: Actions, payload: Optional[Payload] = None) -> Optional[Response]:
    return services_map.get(cmd.value, lambda *_: default_response)(payload)
