from datetime import date
from pydantic import BaseModel
from typing import Optional, Set

FIELDS = ["name", "address", "email", "phones", "birthday", "tags", "note"]


class Record(BaseModel):
    name: str
    email: str = ""
    phones: Set[str] = set()
    birthday: Optional[date] = None
    address: str = ""
    tags: Set[str] = set()
    note: str = ""
