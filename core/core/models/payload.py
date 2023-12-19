from pydantic import BaseModel
from typing import Optional, Union


class ContactPayload(BaseModel):
    name: str
    email: Optional[str] = ''
    note: Optional[str] = ''
    birthday: Optional[str] = ''
    phones: set[str] = set()
    tags: set[str] = set()


class BirthdayPayload(BaseModel):
    name: str
    birthday: Optional[str] = ''
   
    
class AllBirthdaysPayload(BaseModel):
    day_amount: Optional[int] = 7
    
        
class PhonePayload(BaseModel):
    name: str
    phone: str
    old_phone: Optional[str] = None
        
        
class TagPayload(BaseModel):
    name: str
    tag: str
    old_tag: Optional[str] = None


class NotePayload(BaseModel):
    name: str
    note: str


class SearchPayload(BaseModel):
    value: str


Payload = Union[AllBirthdaysPayload, ContactPayload, BirthdayPayload, PhonePayload, TagPayload, NotePayload, SearchPayload, None]