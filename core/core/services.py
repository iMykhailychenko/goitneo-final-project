from typing import List

from core.database import OperationType, store_data
from core.models import Record


@store_data(type=OperationType.APPEND)
def add_contact(*args: List[str]) -> Record:
    return Record(name=args[0])
