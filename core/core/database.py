import csv
from datetime import datetime
from enum import Enum
from functools import wraps
from pathlib import Path
from typing import List, Optional

from core.misc import DatabaseError
from core.models import FIELDS, Record, Response

DB_FOLDER_PATH = Path("/tmp/goit-bot")


class Database:
    __instance = None
    __filename = "db.csv"
    __path: Optional[Path] = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def validate(self) -> Path:
        if not Database.__path or not Database.__path.exists():
            raise DatabaseError()

    def get(self) -> List[Record]:
        self.validate()
        records_list = []

        try:
            with open(Database.__path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tags = set(row["tags"].split("|")) if row.get("tags") else set()
                    phones = (
                        set(row["phones"].split("|")) if row.get("phones") else set()
                    )
                    birthday = (
                        datetime.strptime(row["birthday"], "%d.%m.%Y").date
                        if row.get("birthday")
                        else None
                    )

                    records_list.append(
                        Record(
                            name=row.get("name"),
                            email=row.get("email"),
                            birthday=birthday,
                            phones=phones,
                            tags=tags,
                        )
                    )
        finally:
            return records_list

    def append(self, record: Record) -> None:
        self.validate()
        with open(Database.__path, "a") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)

            if f.tell() == 0:
                writer.writeheader()

            self.__write_row(record, writer)

    def override(self, records: List[Record]) -> None:
        self.validate()
        with open(Database.__path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

            for record in records:
                self.__write_row(record, writer)

    def drop(self) -> "Database":
        self.validate()
        with open(Database.__path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
        return self

    def __write_row(self, record: Record, writer: csv.DictWriter[str]) -> None:
        writer.writerow(
            {
                "name": record.name,
                "email": record.email,
                "phones": "|".join(record.phones),
                "birthday": record.birthday,
                "tags": "|".join(record.tags),
            }
        )

    def connect(self, path: Path = DB_FOLDER_PATH) -> "Database":
        Database.__path = path / Database.__filename
        if not path.exists():
            path.mkdir()
            Database.__path.touch()
        print(f"Connected to database: {Database.__path}")
        return self


class OperationType(Enum):
    APPEND = "append"
    OVERRIDE = "override"


def store_data(
    message: str = "Contact created", type: OperationType = OperationType.APPEND
):
    bd = Database()

    operations = {OperationType.APPEND: bd.append, OperationType.OVERRIDE: bd.override}

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            operations[type](result)
            return Response(value=message)

        return inner

    return wrapper
