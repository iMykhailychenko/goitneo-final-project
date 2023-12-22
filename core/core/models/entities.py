from enum import Enum
from typing import Union

from core.models.contact import Contact
from core.models.note import Note


class EntitiesType(Enum):
    CONTACTS = "contacts"
    NOTES = "notes"


Entity = Union[Contact, Note]


entities = {
    EntitiesType.CONTACTS.value: Contact,
    EntitiesType.NOTES.value: Note,
}
