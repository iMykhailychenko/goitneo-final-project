from datetime import datetime
from typing import Optional

from core.database import Database, delete_data, write_data
from core.misc import exeptions
from core.models import Contact, ContactPayload, EntitiesType, response
from core.validators import Validator

database = Database()


@response()
@write_data(entity=EntitiesType.CONTACTS)
def add_contact(payload: ContactPayload) -> Contact:
    if validate_contact(payload):
        birthday = (
            datetime.strptime(payload.birthday, "%d.%m.%Y").date()
            if payload.birthday
            else None
        )
        return Contact(
            id=payload.name,
            birthday=birthday,
            email=payload.email,
            phones=payload.phones,
            address=payload.address,
        )


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
    if validate_contact(payload):
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


def validate_contact(payload) -> bool:
    errors = []
    if not Validator.validate_name(payload.name):
        errors.append(exeptions.InvalidNameError())
    if not Validator.validate_email(payload.email):
        errors.append(exeptions.InvalidEmailError())
    if not Validator.validate_phone_number(payload.phones):
        errors.append(exeptions.InvalidPhoneError())
    if not Validator.validate_birthday(payload.birthday):
        errors.append(exeptions.InvalidBirthdayError())

    if errors:
        raise exeptions.ValidationErrors(errors)
    else:
        return True
