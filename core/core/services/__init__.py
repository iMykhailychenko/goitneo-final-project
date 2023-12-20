from core.services.address import add_address, delete_address, update_address
from core.services.birthday import (
    add_birthday,
    delete_birthday,
    get_birthdays_by_duration,
    update_birthday,
)
from core.services.contact import add_contact
from core.services.notes import add_note, update_note
from core.services.phones import (
    add_phone_number,
    delete_phone_number,
    update_phone_number,
)

__all__ = [
    "add_address",
    "add_contact",
    "add_note",
    "add_phone_number",
    "get_birthdays_by_duration",
    "add_birthday",
    "delete_address",
    "delete_birthday",
    "delete_phone_number",
    "update_address",
    "update_birthday",
    "update_phone_number",
]
