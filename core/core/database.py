import csv
from pathlib import Path
from typing import Optional

from core.misc import DatabaseError

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

    def get_data(self) -> None:
        self.validate()
        with open(Database.__path, "r") as f:
            r = csv.DictReader(f)
            print(r)

    def set_data(self, data: dict) -> None:
        self.validate()
        with open(Database.__path, "w") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

    def connect(self, path: Path = DB_FOLDER_PATH) -> None:
        Database.__path = path / Database.__filename
        if not path.exists():
            path.mkdir()
            Database.__path.touch()

        print(f"Connected to database: {Database.__path}")
