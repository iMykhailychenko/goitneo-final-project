from datetime import date
from typing import Optional, Set

from pydantic import BaseModel

FIELDS = ["name", "address", "email", "phones", "birthday", "tags", "note"]


class Record(BaseModel):
    name: str
    email: str = ""
    phones: Set[str] = set()
    birthday: Optional[date] = None
    address: str = ""
    tags: Set[str] = set()
    note: str = ""
