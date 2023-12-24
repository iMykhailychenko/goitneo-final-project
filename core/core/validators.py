import re
from datetime import datetime

from core.database import Database

class Validator:
    def validate_existing_contact(name):
        database = Database()
        record = database[name]

        if record:
            return record
        else:
            raise KeyError


    def validate_phone_number(phone_number):
        phone_number_pattern = re.compile(r"^[0-9+-]+$")

        if phone_number and len(phone_number) != 10:
            return True
        elif phone_number and not phone_number_pattern.match(phone_number):
            return True


    def validate_name(name):
        if len(name) == 0 or name is None:
            return True


    def validate_email(email):
        email_pattern = re.compile("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$")

        if email and not email_pattern.match(email):
            return True

    def validate_birthday(birthday):
        if birthday:
            try:
                datetime.strptime(birthday, "%d.%m.%Y")
            except ValueError:
                return True
