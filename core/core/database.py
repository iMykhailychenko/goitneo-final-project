import csv
from pathlib import Path

from core.config import DB_FOLDER_PATH
from core.misc.exeptions import DatabaseError


class Database:
    __instance = None
    __filename = 'db.csv'
    __path = Path(DB_FOLDER_PATH)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
    
    def get_file_path() -> Path:
        db_file = Database.__path / Database.__filename
        if not Database.__path.exists():
            raise DatabaseError()
        return db_file

    def get_data(self) -> None:
        path = self.get_file_path()
        with open(path, "r") as f:
            r = csv.DictReader(f)
            print(r)

    def set_data(self, data: dict) -> None:
        path = self.get_file_path()
        with open(path, "w") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

    def connect(self) -> None:
        db_file = Database.__path / Database.__filename
        if not Database.__path.exists():
            Database.__path.mkdir()
            db_file.touch()

        print(f"Connected to database: {db_file}")
