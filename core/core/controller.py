from typing import Optional

from core.misc import Actions, ValidationMessages, validation_pipe
from core.models import Payload, Response, ResponseType
from core.services import (
    add_address,
    add_birthday,
    add_contact,
    add_note,
    add_phone_number,
    add_tag,
    delete_address,
    delete_birthday,
    delete_contact,
    delete_note,
    delete_phone_number,
    delete_tag,
    get_all_contacts,
    get_all_notes,
    get_birthdays_by_duration,
    get_contact,
    search,
    update_address,
    update_birthday,
    update_contact,
    update_note,
    update_phone_number,
    update_tag,
)

services_map = {
    Actions.SEARCH.value: search,
    # Contact
    Actions.ADD.value: add_contact,
    Actions.GET.value: get_contact,
    Actions.DELETE.value: delete_contact,
    Actions.ALL.value: get_all_contacts,
    Actions.UPDATE.value: update_contact,
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
    Actions.ALL_NOTES.value: get_all_notes,
    Actions.ADD_NOTE.value: add_note,
    Actions.DELETE_NOTE.value: delete_note,
    Actions.UPDATE_NOTE.value: update_note,
    # Tags
    Actions.ADD_TAG.value: add_tag,
    Actions.DELETE_TAG.value: delete_tag,
    Actions.UPDATE_TAG.value: update_tag,
}

default_response = Response(
    message=ValidationMessages.INVALID_COMMAND, type=ResponseType.ERROR
)


@validation_pipe
def controller(cmd: Actions, payload: Optional[Payload] = None) -> Optional[Response]:
    return services_map.get(cmd.value, lambda *_: default_response)(payload)
