from typing import Optional

from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import Contact, EntitiesType, PhonePayload, response

database = Database()


@response(InfoMessages.PHONE_NUMBER_ADDED)
@write_data(entity=EntitiesType.CONTACTS)
def add_phone_number(payload: PhonePayload) -> Contact:
    if record := database.select(entity=EntitiesType.CONTACTS, key=payload.name):
        record.phones.add(payload.phone)
        return record
    else:
        return Contact(id=payload.name, phones={payload.phone})


@response(InfoMessages.PHONE_NUMBER_DELETED)
@write_data(entity=EntitiesType.CONTACTS)
def delete_phone_number(payload: PhonePayload) -> Optional[Contact]:
    if record := database.select(entity=EntitiesType.CONTACTS, key=payload.name):
        record.phones.discard(payload.phone)
        return record


@response(InfoMessages.PHONE_NUMBER_UPDATED)
@write_data(entity=EntitiesType.CONTACTS)
def update_phone_number(payload: PhonePayload) -> Contact:
    if record := database.select(entity=EntitiesType.CONTACTS, key=payload.name):
        record.phones.discard(payload.old_phone)
        record.phones.add(payload.phone)
        return record
    else:
        return Contact(id=payload.name, phones={payload.phone})
