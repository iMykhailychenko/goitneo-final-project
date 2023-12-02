from datetime import date
from pydantic import BaseModel
from typing import Optional


class Record(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    birthday: Optional[date] = None