from datetime import datetime

from core.database import Entities, write_data
from core.misc import InfoMessages
from core.models import Contact, ContactPayload, response


@response(InfoMessages.CONTACT_CREATED)
@write_data(entity=Entities.CONTACTS)
def add_contact(payload: ContactPayload) -> Contact:
    birthday = (
        datetime.strptime(payload.birthday, "%d.%m.%Y").date()
        if payload.birthday
        else None
    )
    return Contact(
        id=payload.name,
        email=payload.email,
        phones=payload.phones,
        birthday=birthday,
        address=payload.address,
    )
