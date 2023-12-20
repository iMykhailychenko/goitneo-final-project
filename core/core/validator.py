import datetime
import re
from core.database import Database

from core.misc import (
    InvalidBirthdayError,
    InvalidEmailError,
    InvalidNameError,
    InvalidPhoneError,
    InvalidPhoneLengthError,
)


def validate_existing_contact(name):
    database = Database()
    record = database[name]

    if record:    
        return record
    else:
        raise KeyError
    
    
def validate_phone_number(phone_number):
    phone_number_pattern = re.compile(r"^[0-9+-]+$")

    if len(phone_number) != 10:
        raise InvalidPhoneLengthError()
    elif not phone_number_pattern.match(phone_number):
        raise InvalidPhoneError()


def validate_name(name):
    if len(name) == 0 or name is None:
        raise InvalidNameError


def validate_email(email):
    email_pattern = re.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$")

    if not email_pattern.match(email):
        raise InvalidEmailError


def validate_birthday(birthday):
    try:
        datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError:
        raise InvalidBirthdayError


__all__ = [
    "validate_birthday",
    "validate_email",
    "validate_existing_contact",
    "validate_name",
    "validate_phone_number",
]
