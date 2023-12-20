from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import Record, response

database = Database()


@response(InfoMessages.ADDRESS_ADDED)
@write_data
def add_address(payload):
    return set_address(payload)


@response(InfoMessages.ADDRESS_DELETED)
@write_data
def delete_address(payload):
    record = database[payload.name]
    record.address = ""
    return record


@response(InfoMessages.ADDRESS_UPDATTED)
@write_data
def update_address(payload):
    return set_address(payload)


def set_address(payload) -> Record:
    record = database[payload.name]

    if record:
        record.address = payload.address
        return record
    else:
        return Record(name=payload.name, address=payload.address)
