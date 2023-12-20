from datetime import datetime

from core.database import Entities, Database, write_data
from core.misc import InfoMessages
from core.models import Contact, ContactPayload, response

database = Database()


@response(InfoMessages.CONTACT_CREATED)
@write_data(entity=Entities.CONTACTS)
def add_contact(payload: ContactPayload) -> Contact:
    birthday = (
        datetime.strptime(payload.birthday, "%d.%m.%Y").date()
        if payload.birthday
        else None
    )
    return Contact(
        id=payload.name,
        email=payload.email,
        phones=payload.phones,
        birthday=birthday,
        address=payload.address,
    )


@response()
@write_data(entity=Entities.CONTACTS)
def update_contact(payload: ContactPayload) -> Contact:
    record = database[payload.name]

    if record:
        if payload.name:
            record.name = payload.name
        if payload.email:
            record.email = payload.email
        if payload.note:
            record.note = payload.note
        if payload.birthday:
            record.birthday = datetime.strptime(payload.birthday, "%d.%m.%Y").date()
        if payload.address:
            record.address = payload.address
        if payload.phones:
            record.phones = payload.phones
        if payload.tags:
            record.tags = payload.tags
        return record


@response()
def get_contact(payload: ContactPayload) -> Contact:
    record = database[payload.name]

    if record:
        return record
    else:
        raise KeyError
