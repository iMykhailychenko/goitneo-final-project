from typing import Optional

from core.misc import Actions, CommandMessages, ValidationMessages, validation
from core.models import Payload, Response, ResponseType
from core.services import (
    add_address,
    add_birthday,
    add_contact,
    add_note,
    add_phone_number,
    delete_address,
    delete_birthday,
    delete_phone_number,
    get_birthdays_by_duration,
    update_address,
    update_birthday,
    update_note,
    update_phone_number,
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
    Actions.UPDATE_PHONE.value: update_phone_number,
    Actions.DELETE_PHONE.value: delete_phone_number,
    # Address
    Actions.ADD_ADDRESS.value: add_address,
    Actions.DELETE_ADDRESS.value: delete_address,
    Actions.UPDATE_ADDRESS.value: update_address,
    # Birthday
    Actions.ADD_BIRTHDAY.value: add_birthday,
    Actions.DELETE_BIRTHDAY.value: delete_birthday,
    Actions.UPDATE_BIRTHDAY.value: update_birthday,
    Actions.BIRTHDAYS.value: get_birthdays_by_duration,
    # Notes
    Actions.ADD_NOTE.value: add_note,
    Actions.DELETE_NOTE.value: lambda _: None,
    Actions.UPDATE_NOTE.value: update_note,
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
