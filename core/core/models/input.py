from pydantic import BaseModel
from typing import Optional
from core.misc import Actions

class Input(BaseModel):
    command: Actions
    name: str
    email: Optional[str] = ''
    notes: Optional[str] = ''
    birthday: Optional[str] = ''
    phones: set[str] = set()
    tags: set[str] = set()
