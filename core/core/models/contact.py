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
