from pydantic import BaseModel
from typing import Optional, Union


class ContactPayload(BaseModel):
    name: str
    email: Optional[str] = ''
    notes: Optional[str] = ''
    birthday: Optional[str] = ''
    phones: set[str] = set()
    tags: set[str] = set()


class BirthdayPayload(BaseModel):
    name: str
    birthday: Optional[str] = ''


class PhonePayload(BaseModel):
    name: str
    phone: str
    old_phone: Optional[str] = None


class TagPayload(BaseModel):
    name: str
    tag: str
    old_tag: Optional[str] = None


Payload = Union[ContactPayload, BirthdayPayload, PhonePayload, TagPayload, None]