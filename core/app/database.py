import csv
from pathlib import Path


class Database:
    __instance = None
    __filepath = Path(__file__).parent.joinpath("database.db")

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def get_data():
        if not Database.__filepath.exists():
            return None

        with Database.__filepath.open("r") as f:
            r = csv.DictReader(f)
            print(r)

    def set_data(data):
        with Database.__filepath.open("w") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
