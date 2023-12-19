import csv
from datetime import datetime
from functools import wraps
from pathlib import Path
from typing import Dict, Optional

from core.misc import DatabaseError
from core.models import FIELDS, Record, Response

DB_FOLDER_PATH = Path(__file__).resolve().parent.parent.parent / "tmp"


class Database:
    __instance = None
    __filename = "db.csv"
    __path: Optional[Path] = None
    __records: Dict[str, Record] = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __setitem__(self, key: str, value: Record):
        self.__records[key] = value
        self.__write(self.__records)

    def __getitem__(self, key: str) -> Record:
        if not self.__records:
            self.__read()
        return self.__records.get(key)

    def __delete__(self, key: str):
        if key in self.__records:
            del self.__records[key]
            self.__write(self.__records)

    def all(self) -> Dict[str, Record]:
        return self.__records

    def validate(self) -> Path:
        if not Database.__path or not Database.__path.exists():
            raise DatabaseError()

    def __read(self) -> None:
        self.validate()

        try:
            with open(Database.__path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tags = set(row["tags"].split("|")) if row.get("tags") else set()
                    phones = (
                        set(row["phones"].split("|")) if row.get("phones") else set()
                    )
                    birthday = (
                        datetime.strptime(row["birthday"], "%Y-%m-%d").date()
                        if row.get("birthday")
                        else None
                    )

                    self.__records[row.get("name")] = Record(
                        name=row.get("name"),
                        email=row.get("email"),
                        address=row.get("address"),
                        birthday=birthday,
                        phones=phones,
                        tags=tags,
                    )
        except Exception:
            print(f"Failed to read data from file: {Database.__path}")

    def __write(self, records: Dict[str, Record]) -> None:
        self.validate()
        with open(Database.__path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

            for record in records.values():
                writer.writerow(
                    {
                        "name": record.name,
                        "email": record.email,
                        "address": record.address,
                        "phones": "|".join(record.phones),
                        "birthday": record.birthday,
                        "tags": "|".join(record.tags),
                    }
                )

    def drop(self) -> "Database":
        self.validate()
        self.__write({})
        self.__records.clear()
        return self

    def connect(self, path: Path = DB_FOLDER_PATH) -> "Database":
        Database.__path = path / Database.__filename
        if not path.exists():
            path.mkdir()
            Database.__path.touch()
        print(f"Connected to database: {Database.__path}")
        return self


def write_data(func):
    bd = Database()

    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        bd[result.name] = result
        return result

    return inner


def delete_data(func):
    bd = Database()

    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        del bd[result.name]
        return result

    return inner
