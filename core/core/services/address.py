from core.models import response, Record
from core.database import write_data, Database
from core.misc import InfoMessages

database = Database()


@response(InfoMessages.ADDRESS_ADDED)
@write_data
def add_address(payload):
    return set_address(payload)


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

