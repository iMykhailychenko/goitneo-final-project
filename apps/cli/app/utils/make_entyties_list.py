from datetime import date
from typing import Dict, List, Tuple

from beaupy import select
from core.models import Entity

from app.constants import GO_BACK


def get_row(entity: List[Entity]) -> str:
    row = []
    for value in entity.model_dump().values():
        if type(value) == date:
            row.append(value.strftime("%A %d %B %Y"))
        elif type(value) == set:
            value.remove("")
            row.append(", ".join(value))
        else:
            row.append(value)

    return (len(row) * "|{: ^20}" + "\n").format(*row)


def make_entyties_map(entyties: List[Entity]) -> Dict[str, Entity]:
    result = {}
    for entity in entyties:
        result[get_row(entity)] = entity
    return result


def make_entyties_list(
    entyties: List[Entity], actions: List[str]
) -> Tuple[str, Entity]:
    entyties_map = make_entyties_map(entyties)
    key = select(
        [GO_BACK, *list(entyties_map.keys())], cursor=">>>", cursor_style="cyan"
    )
    if key == GO_BACK:
        return GO_BACK, None
    next_action = select(actions, cursor=">>>", cursor_style="cyan")
    return next_action, entyties_map[key]
