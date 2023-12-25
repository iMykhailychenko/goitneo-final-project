from datetime import date, datetime
from typing import Optional, Set, Union

from pydantic import BaseModel, field_validator

from core.misc import ValidationError, ValidationMessages
from core.validation import Validator


class Contact(BaseModel):
    id: str
    email: str = ""
    phones: Set[str] = set()
    birthday: Optional[Union[date, str]] = None
    address: str = ""

    @field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, value):
        if not Validator.validate_email(value):
            raise ValidationError(ValidationMessages.INVALID_EMAIL.value)
        return value

    @field_validator("phones", mode="before")
    @classmethod
    def validate_phones(cls, value):
        if not Validator.validate_all_phones(value):
            raise ValidationError(ValidationMessages.INVALID_PHONE.value)
        return value

    @field_validator("birthday", mode="before")
    @classmethod
    def validate_birthday(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, "%Y-%m-%d").date()
        if not Validator.validate_birthday_date(value):
            raise ValidationError(ValidationMessages.INVALID_BIRTHDAY.value)
        return value

    def __str__(self) -> str:
        phones = " | ".join(self.phones) or "n/a"
        email = self.email or "n/a"
        return f"👥  {self.id} - {email} - {phones}\n"

    def print(self) -> None:
        phones = " | ".join(self.phones)
        birthday = self.birthday.strftime("%d.%m.%Y %A") if self.birthday else "n/a"
        email = self.email or "n/a"
        address = self.address or "n/a"

        print(
            f"Name: {self.id}\nEmail : {email}\nPhones: {phones}\nBirthday: {birthday}\nAddress: {address}\n\n"
        )
