from typing import List

from core.database import persist_data
from core.models import Record


@persist_data()
def add_contact(*args: List[str]) -> Record:
    return Record(name=args[0])
