from core.models import response, Record
from core.database import write_data, Database
from core.misc import InfoMessages

database = Database()


@response(InfoMessages.ADDRESS_ADDED)
@write_data
def add_address(payload):
    record = database[payload.name]

    return set_address(payload, record)


def set_address(payload, record: Record) -> Record:
    if record:
        record.address = payload.address
        return record
    else:
        return Record(name=payload.name, address=payload.address)

