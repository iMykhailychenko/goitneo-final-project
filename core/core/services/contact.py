from datetime import datetime
from typing import Optional

from core.database import Database, delete_data, write_data
from core.models import Contact, ContactPayload, EntitiesType, response
from core.validators import Validator

database = Database()


@response()
@write_data(entity=EntitiesType.CONTACTS)
def add_contact(payload: ContactPayload) -> Contact:
    is_invalid = validate_contact(payload)
    if not is_invalid:
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
    else:
        raise ValueError    


@response()
@delete_data(entity=EntitiesType.CONTACTS)
def delete_contact(payload: ContactPayload) -> Contact:
    return database.select(entity=EntitiesType.CONTACTS, key=payload.name)


@response()
@write_data(entity=EntitiesType.CONTACTS)
def update_contact(payload: ContactPayload) -> Contact:
    record: Optional[Contact] = database.select(
        entity=EntitiesType.CONTACTS, key=payload.name
    )

    if payload.new_name:
        database.delete(entity=EntitiesType.CONTACTS, key=payload.name)

    if record:
        record.id = payload.new_name or record.id
        record.email = payload.email or record.email
        record.birthday = (
            datetime.strptime(payload.birthday, "%d.%m.%Y").date()
            if payload.birthday
            else record.birthday
        )
        record.address = payload.address or record.address
        record.phones = payload.phones or record.phones
        return record


@response()
def get_contact(payload: ContactPayload) -> Contact:
    return database.select(entity=EntitiesType.CONTACTS, key=payload.name)


@response()
def get_all_contacts(*_) -> list[Contact]:
    return database.select(entity=EntitiesType.CONTACTS, key="*") or []

def validate_contact(payload)-> bool:
    return (Validator.validate_birthday(payload.birthday) 
            and Validator.validate_email(payload.email) 
            and Validator.validate_name(payload.name)
            and Validator.validate_phone_number(payload.phone))
