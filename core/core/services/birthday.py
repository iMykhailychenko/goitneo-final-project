from datetime import date, datetime, timedelta
from typing import Any

from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import Record, response

database = Database()


@response(InfoMessages.BIRTHDAY_ADDED)
@write_data
def add_birthday(payload):
    return set_birthday(payload)


@response()
def get_birthdays_by_duration(payload):
    records = database.all()
    today = date.today()
    records_with_this_week_birthday: list[Record] = []

    for contact in records.values():
        if contact.birthday:
            birthday = contact.birthday
            birthday_this_year = birthday.replace(year=today.year)
            if today <= birthday_this_year and birthday_this_year <= today + timedelta(
                days=payload.day_amount
            ):
                records_with_this_week_birthday.append(contact)

    return sorted(records_with_this_week_birthday, key=lambda x: x.birthday)


@response(InfoMessages.BIRTHDAY_DELETED)
@write_data
def delete_birthday(payload):
    record = database[payload.name]
    record.birthday = None
    return record


@response(InfoMessages.BIRTHDAY_UPDATTED)
@write_data
def update_birthday(payload):
    return set_birthday(payload)


def get_valid_birthday(birthday: str) -> date:
    birthday = datetime.strptime(birthday, "%d.%m.%Y").date() if birthday else None

    return birthday


def set_birthday(payload) -> Record:
    birthday = get_valid_birthday(payload.birthday)
    record = database[payload.name]

    if record:
        record.birthday = birthday
        return record
    else:
        return Record(name=payload.name, birthday=birthday)
