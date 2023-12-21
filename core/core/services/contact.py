from datetime import datetime

from core.database import Database, Entities, write_data
from core.misc import InfoMessages
from core.models import Contact, ContactPayload, response

database = Database()


@response()
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
    record = database.select(entity=Entities.CONTACTS, key=payload.name)
    if record:
        if payload.name:
            record.id = payload.name
        if payload.email:
            record.email = payload.email
        if payload.birthday:
            record.birthday = datetime.strptime(payload.birthday, "%d.%m.%Y").date()
        if payload.address:
            record.address = payload.address
        if payload.phones:
            record.phones = payload.phones
        return record


@response()
def get_contact(payload: ContactPayload) -> Contact:
    record = database[payload.name]

    if record:
        return record
    else:
        return None


@response()
def all_contacts(*args) -> list[Contact]:
    records = list(database.select(entity=Entities.CONTACTS, key="*"))
    if records:
        return records
    else:
        return []
