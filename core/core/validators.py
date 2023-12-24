import re
from datetime import datetime

from core.database import Database
from core.models import EntitiesType


class Validator:
    def validate_existing_contact(name):
        database = Database()
        return bool(database.select(entity=EntitiesType.CONTACTS, key=name))

    def validate_phone_number(phone_numbers):
        if not phone_numbers:
            return True

        phone_number_pattern = re.compile(r"^[0-9+-]{10}$")

        for phone_number in phone_numbers:
            if len(phone_number) > 0 and (
                len(phone_number) != 10 or not phone_number_pattern.match(phone_number)
            ):
                return False

        return True

    def validate_name(name):
        return bool(name and name.strip())

    def validate_email(email):
        email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$")
        return bool(email_pattern.match(email)) if len(email) > 0 else True

    def validate_birthday(birthday):
        try:
            if birthday:
                return bool(datetime.strptime(birthday, "%d.%m.%Y"))
            else:
                return True
        except ValueError:
            return False
