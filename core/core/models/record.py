from datetime import date
from pydantic import BaseModel
from typing import Optional, Set

FIELDS = ["name", "email", "phones", "birthday", "tags"]

class Record(BaseModel):
    name: str
    email: Optional[str] = None
    phones: Set[str] = set()
    birthday: Optional[date] = None
    tags: Set[str] = set()