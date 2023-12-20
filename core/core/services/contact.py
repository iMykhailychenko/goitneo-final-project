from datetime import datetime

from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import ContactPayload, Record, response

database = Database()


@response(InfoMessages.CONTACT_ADDED)
@write_data
def add_contact(payload: ContactPayload) -> Record:
    birthday = (
        datetime.strptime(payload.birthday, "%d.%m.%Y").date()
        if payload.birthday
        else None
    )
    return Record(
        name=payload.name,
        email=payload.email,
        phones=payload.phones,
        tags=payload.tags,
        note=payload.note,
        birthday=birthday,
    )


@response(InfoMessages.CONTACT_UPDATED)
@write_data
def update_contact(payload: ContactPayload) -> Record:
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
    else:
        raise KeyError
