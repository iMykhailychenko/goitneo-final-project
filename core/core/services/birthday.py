from typing import Any
from datetime import date, datetime, timedelta
from core.models import response, Record
from core.database import write_data, Database
from core.misc import InfoMessages

database = Database()


@response(InfoMessages.BIRTHDAY_ADDED)
@write_data
def add_birthday(payload):
    record = database[payload.name]
    birthday = get_valid_birthday(payload.birthday)

    return set_birthday(payload, record, birthday)


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
    record = database[payload.name]
    birthday = get_valid_birthday(payload.birthday)

    return set_birthday(payload, record, birthday)


def get_valid_birthday(birthday: str) -> date:
    birthday = datetime.strptime(birthday, "%d.%m.%Y").date() if birthday else None

    return birthday


def set_birthday(payload, record: Record, birthday_value: date) -> Record:
    if record:
        record.birthday = birthday_value
        return record
    else:
        return Record(name=payload.name, birthday=birthday_value)
