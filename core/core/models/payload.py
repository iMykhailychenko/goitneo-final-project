from typing import Optional, Set, Union

from pydantic import BaseModel

from core.models.entities import EntitiesType


class ContactPayload(BaseModel):
    name: str
    new_name: Optional[str] = None
    email: Optional[str] = ""
    birthday: Optional[str] = ""
    address: Optional[str] = ""
    phones: set[str] = set()


class BirthdayPayload(BaseModel):
    name: Optional[str] = None
    birthday: Optional[str] = None
    day_amount: Optional[int] = 7


class AddressPayload(BaseModel):
    name: str
    address: Optional[str] = None


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
    query: str
    entity: EntitiesType = EntitiesType.CONTACTS


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
