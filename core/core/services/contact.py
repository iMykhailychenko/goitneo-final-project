from datetime import datetime

from core.database import Database, write_data, delete_data
from core.models import Contact, ContactPayload, EntitiesType, response

database = Database()


@response()
@write_data(entity=EntitiesType.CONTACTS)
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
@delete_data(entity=EntitiesType.CONTACTS)
def delete_contact(payload: ContactPayload) -> Contact:
    return database.select(entity=EntitiesType.CONTACTS, key=payload.name)


@response()
@write_data(entity=EntitiesType.CONTACTS)
def update_contact(payload: ContactPayload) -> Contact:
    record = database.select(entity=EntitiesType.CONTACTS, key=payload.name)
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
def get_all_contacts(*args) -> list[Contact]:
    return list(database.select(entity=EntitiesType.CONTACTS, key="*")) or []
