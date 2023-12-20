import json
import shutil
from enum import Enum
from functools import wraps
from pathlib import Path
from typing import Dict, List, Optional, Union

from core.models import Contact, Note

DB_FOLDER_PATH = Path(__file__).resolve().parent.parent.parent / "tmp"


class Entities(Enum):
    CONTACTS = "contacts"
    NOTES = "notes"


Record = Union[Contact, Note]
Entity = Dict[str, Record]

records = {
    Entities.CONTACTS.value: Contact,
    Entities.NOTES.value: Note,
}


class Database:
    __instance = None
    __path: Optional[Path] = None
    __entities: Dict[str, Entity] = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def select(self, entity: Entities, key: str = "*") -> Union[Record, List[Record]]:
        self.__read(entity)
        if key == "*":
            return self.__entities.get(entity.value, {}).values()
        return self.__entities.get(entity.value, {}).get(key)

    def update(self, entity: Entities, key: str, record: Record) -> None:
        if self.__entities.get(entity.value):
            self.__entities[entity.value][key] = record
        else:
            self.__entities[entity.value] = {key: record}
        self.__write(entity)

    def delete(self, entity: Entities, key: str):
        if key in self.__entities[entity.value]:
            del self.__entities[entity.value][key]
            self.__write(entity)

    def __get_file(self, entity: Entities) -> Path:
        if self.__path is None:
            self.__path = DB_FOLDER_PATH

        file = self.__path / f"{entity.value}.json"

        if not self.__path.exists():
            self.__path.mkdir()

        if not file.exists():
            file.touch()

        return file

    def __read(self, entity: Entities) -> None:
        file = self.__get_file(entity)

        with open(file, "r") as f:
            try:
                data = json.load(f)
                self.__entities[entity.value] = {}
                for key, record in data.items():
                    self.__entities[entity.value][key] = records[entity.value](**record)
            except json.JSONDecodeError:
                pass

    def __write(self, entity: Entities) -> None:
        file = self.__get_file(entity)
        entities = self.__entities.get(entity.value)

        if entities:
            json_data = {}
            with open(file, "w") as f:
                for key, record in entities.items():
                    json_data[key] = record.model_dump(mode="json")
                json.dump(json_data, f, indent=2)

    def drop(self) -> "Database":
        self.__entities.clear()
        if self.__path and self.__path.exists():
            shutil.rmtree(self.__path)
        return self

    def connect(self, path: Path = DB_FOLDER_PATH) -> "Database":
        if not self.__path:
            self.__path = path

        if not self.__path.exists():
            self.__path.mkdir()

        return self


def write_data(entity: Entities = Entities.CONTACTS):
    bd = Database()

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result: Record = func(*args, **kwargs)
            bd.update(entity=entity, key=result.id, record=result)
            return result

        return inner

    return wrapper


def delete_data(entity: Entities = Entities.CONTACTS):
    bd = Database()

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result: Record = func(*args, **kwargs)
            bd.delete(entity=entity, key=result.id)
            return result

        return inner

    return wrapper
