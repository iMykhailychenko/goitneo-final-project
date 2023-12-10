from datetime import datetime

from core.database import OperationType, store_data
from core.models import Input, Record


@store_data(type=OperationType.APPEND)
def add_contact(input: Input) -> Record:
    birthday = (
        datetime.strptime(input.birthday, "%d.%m.%Y").date() if input.birthday else None
    )
    print(birthday)

    return Record(
        name=input.name,
        email=input.email,
        phones=input.phones,
        tags=input.tags,
        notes=input.notes,
        birthday=birthday,
    )
