from datetime import datetime

from core.database import store_data
from core.models import Input, Record


@store_data()
def add_contact(input: Input) -> Record:
    birthday = (
        datetime.strptime(input.birthday, "%d.%m.%Y").date() if input.birthday else None
    )
    return Record(
        name=input.name,
        email=input.email,
        phones=input.phones,
        tags=input.tags,
        notes=input.notes,
        birthday=birthday,
    )
