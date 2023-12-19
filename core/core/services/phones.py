import re
from core.models import response, Record
from core.database import write_data, Database
from core.misc import InfoMessages


database = Database()


@response(InfoMessages.PHONE_NUMBER_ADDED)
@write_data
def add_phone_number(payload):
    record = database[payload.name]

    if record:
        record.phones.add(payload.phone)
    else:
        record = Record(name=payload.name, phones={payload.phone})

    return record


@response(InfoMessages.PHONE_NUMBER_DELETED)
@write_data
def delete_phone_number(payload):
    pass
    
    
@response(InfoMessages.PHONE_NUMBER_UPDATED)
@write_data
def update_phone_number(payload):
    record = database[payload.name]

    if record:
        if payload.old_phone in record.phones:
            record.phones.discard(payload.old_phone)
            record.phones.add(payload.phone)
        else:
            record.phones.add(payload.phone)
        return record
    else:
        return Record(name=payload.name, phones={payload.phone})