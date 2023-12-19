import re
from core.models import response, Record
from core.database import write_data, Database
from core.misc import InfoMessages


database = Database()


@response(InfoMessages.PHONE_NUMBER_ADDED)
@write_data
def add_phone_number(payload):
    record = database[payload.name]

    return set_phone_number(payload, record)


def set_phone_number(payload, record: Record) -> Record:
    if record:
        record.phones.add(payload.phone)
        return record
    else:
        return Record(name=payload.name, phones={payload.phone})


# This code is for the implementation of the US-19
# def validate_phone_number(phone_number):
#         pattern = re.compile(r'^[0-9+-]+$')

#         if len(phone_number) != 10:
#             raise InvalidPhoneLengthError()
#         elif not pattern.match(phone_number):
#             raise InvalidPhoneError()
