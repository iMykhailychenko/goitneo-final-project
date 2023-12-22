from datetime import date
from typing import Dict, List

from core.database import Database
from core.models import Entity, SearchPayload, response

db = Database()


@response()
def search(payload: SearchPayload) -> Entity:
    result = []
    query = payload.query.lower()

    all: List[Entity] = db.select(entity=payload.entity, key="*")
    for record in all:
        print(all)
        if should_include_record(record.model_dump(), query):
            result.append(record)

    return result


def should_include_record(obj: Dict, query: str) -> bool:
    for value in obj.values():
        if isinstance(value, str) and query in value.lower():
            return True
        elif isinstance(value, date) and query in value.strftime("%d.%m.%Y"):
            return True
        elif isinstance(value, set) and any(query in item.lower() for item in value):
            return True
    return False
