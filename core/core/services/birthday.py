from datetime import date, datetime, timedelta
from typing import List

from core.database import Database, write_data
from core.misc import InfoMessages, exeptions
from core.models import BirthdayPayload, Contact, EntitiesType, response
from core.validators import Validator

database = Database()


@response(InfoMessages.BIRTHDAY_ADDED)
@write_data(entity=EntitiesType.CONTACTS)
def add_birthday(payload: BirthdayPayload) -> Contact:
    if validate_birthday(payload.birthday):
        return set_birthday(payload)


@response()
def get_birthdays_by_duration(payload: BirthdayPayload) -> Contact:
    records = database.select(EntitiesType.CONTACTS, key="*")
    today = date.today()
    records_with_this_week_birthday: List[Contact] = []

    for contact in records:
        if contact.birthday:
            birthday = contact.birthday
            birthday_this_year = birthday.replace(year=today.year)
            if today <= birthday_this_year and birthday_this_year <= today + timedelta(
                days=payload.day_amount
            ):
                records_with_this_week_birthday.append(contact)

    return sorted(records_with_this_week_birthday, key=lambda x: x.birthday)


@response(InfoMessages.BIRTHDAY_DELETED)
@write_data(entity=EntitiesType.CONTACTS)
def delete_birthday(payload: BirthdayPayload) -> Contact:
    if record := database.select(EntitiesType.CONTACTS, key=payload.name):
        record.birthday = None
    return record


@response(InfoMessages.BIRTHDAY_UPDATTED)
@write_data(entity=EntitiesType.CONTACTS)
def update_birthday(payload: BirthdayPayload):
    if validate_birthday(payload.birthday):
        return set_birthday(payload)


def get_valid_birthday(birthday: str) -> date:
    return datetime.strptime(birthday, "%d.%m.%Y").date() if birthday else None


def set_birthday(payload: BirthdayPayload) -> Contact:
    birthday = get_valid_birthday(payload.birthday)
    if record := database.select(entity=EntitiesType.CONTACTS, key=payload.name):
        record.birthday = birthday
        return record
    else:
        return Contact(id=payload.name, birthday=birthday)


def validate_birthday(birthday):
    if not Validator.validate_birthday(birthday):
        raise exeptions.InvalidBirthdayError
    else:
        return True
