from core.database import Database, Entities, write_data
from core.misc import InfoMessages
from core.models import Contact, ContactPayload, response

database = Database()


@response(InfoMessages.ADDRESS_ADDED)
@write_data(entity=Entities.CONTACTS)
def add_address(payload: ContactPayload):
    return set_address(payload)


@response(InfoMessages.ADDRESS_DELETED)
@write_data(entity=Entities.CONTACTS)
def delete_address(payload: ContactPayload):
    record = database.select(entity=Entities.CONTACTS, key=payload.name)
    record.address = ""
    return record


@response(InfoMessages.ADDRESS_UPDATTED)
@write_data(entity=Entities.CONTACTS)
def update_address(payload: ContactPayload):
    return set_address(payload)


def set_address(payload: ContactPayload) -> Contact:
    record = database.select(entity=Entities.CONTACTS, key=payload.name)

    if record:
        record.address = payload.address
        return record
    else:
        return Contact(id=payload.name, address=payload.address)
