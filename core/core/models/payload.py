from typing import Optional, Set, Union

from pydantic import BaseModel


class ContactPayload(BaseModel):
    name: str
    email: Optional[str] = ""
    birthday: Optional[str] = ""
    address: Optional[str] = ""
    phones: set[str] = set()


class BirthdayPayload(BaseModel):
    name: Optional[str] = ""
    birthday: Optional[str] = ""
    day_amount: Optional[int] = 7


class AddressPayload(BaseModel):
    name: str
    address: Optional[str] = ""


class PhonePayload(BaseModel):
    name: str
    phone: str
    old_phone: Optional[str] = None


class TagPayload(BaseModel):
    name: str
    tag: str
    old_tag: Optional[str] = None


class NotePayload(BaseModel):
    id: Optional[str] = None
    value: Optional[str] = None
    tags: Set[str] = set()


class SearchPayload(BaseModel):
    value: str


Payload = Union[
    AddressPayload,
    ContactPayload,
    BirthdayPayload,
    PhonePayload,
    TagPayload,
    NotePayload,
    SearchPayload,
    None,
]
