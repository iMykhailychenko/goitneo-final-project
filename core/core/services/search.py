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
        if search_in_dict(record.model_dump(), query):
            result.append(record)

    return result


def search_in_dict(obj: Dict, query: str) -> bool:
    for value in obj.values():
        if type(value) == str and query in value.lower():
            return True
        elif type(value) == date and query in value.strftime("%d.%m.%Y"):
            return True
        elif type(value) == set:
            for item in value:
                if query in item.lower():
                    return True
