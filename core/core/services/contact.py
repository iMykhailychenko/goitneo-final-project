from datetime import datetime

from core.database import write_data
from core.models import ContactPayload, Record
from core.models import response
from core.misc import InfoMessages


@response(InfoMessages.CONTACT_CREATED)
@write_data
def add_contact(payload: ContactPayload) -> Record:
    birthday = (
        datetime.strptime(payload.birthday, "%d.%m.%Y").date()
        if payload.birthday
        else None
    )
    return Record(
        name=payload.name,
        email=payload.email,
        phones=payload.phones,
        tags=payload.tags,
        note=payload.note,
        birthday=birthday,
    )
