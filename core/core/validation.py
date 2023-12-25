import re
from datetime import date, datetime
from typing import Set

PHONE_PATTERN = re.compile(r"^[0-9+-]{10}$")
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$")


class Validator:
    @classmethod
    def validate_phone_number(cls, phone_number: str):
        if not phone_number:
            return True
        return PHONE_PATTERN.match(phone_number)

    @classmethod
    def validate_all_phones(cls, phones: Set[str]):
        if not phones or not len(phones):
            return True
        for phone in phones:
            if not cls.validate_phone_number(phone):
                return False
        return True

    @classmethod
    def validate_name(cls, name):
        return bool(name and name.strip())

    @classmethod
    def validate_email(cls, email):
        if not email:
            return True
        return bool(EMAIL_PATTERN.match(email)) if len(email) > 0 else True

    @classmethod
    def validate_birthday_str(cls, birthday):
        if not birthday:
            return True
        try:
            return bool(datetime.strptime(birthday, "%d.%m.%Y")) if birthday else True
        except ValueError:
            return False

    @classmethod
    def validate_birthday_date(cls, birthday):
        if not birthday:
            return True
        return isinstance(birthday, date)
