from datetime import date
from typing import Optional, Set

from pydantic import BaseModel


class Contact(BaseModel):
    id: str
    email: str = ""
    phones: Set[str] = set()
    birthday: Optional[date] = None
    address: str = ""

    def __str__(self) -> str:
        self.phones.remove("")
        return f"{self.id} | {", ".join(self.phones)}\n"
