from typing import Set

from pydantic import BaseModel


class Note(BaseModel):
    id: str
    value: str = ""
    tags: Set[str] = set()
