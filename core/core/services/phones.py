from core.database import Database, Entities, write_data
from core.misc import InfoMessages
from core.models import Contact, PhonePayload, response

database = Database()


@response(InfoMessages.PHONE_NUMBER_ADDED)
@write_data(entity=Entities.CONTACTS)
def add_phone_number(payload: PhonePayload):
    record = database.select(entity=Entities.CONTACTS, key=payload.name)

    if record:
        record.phones.add(payload.phone)
        return record
    else:
        return Contact(id=payload.name, phones={payload.phone})


@response(InfoMessages.PHONE_NUMBER_DELETED)
@write_data(entity=Entities.CONTACTS)
def delete_phone_number(payload: PhonePayload):
    record = database.select(entity=Entities.CONTACTS, key=payload.name)

    if record:
        record.phones.discard(payload.phone)
        return record


@response(InfoMessages.PHONE_NUMBER_UPDATED)
@write_data(entity=Entities.CONTACTS)
def update_phone_number(payload: PhonePayload):
    record = database.select(entity=Entities.CONTACTS, key=payload.name)

    if record:
        record.phones.discard(payload.old_phone)
        record.phones.add(payload.phone)
        return record
    else:
        return Contact(id=payload.name, phones={payload.phone})
