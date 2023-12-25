from typing import Set

from pydantic import BaseModel


class Note(BaseModel):
    id: str
    value: str = ""
    tags: Set[str] = set()

    def truncat_value(self) -> str:
        if len(self.value) > 40:
            return self.value[:60] + "..."
        return self.value

    def __str__(self) -> str:
        return f"📝   id: {self.id}  -  {self.truncat_value()}\n"

    def print(self) -> None:
        tags = " #".join(self.tags)
        print(f"{self.value} \n\nTags: #{tags}\n\n")
