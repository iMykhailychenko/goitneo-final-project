from typing import Dict, List, Tuple

from beaupy import select
from core.models import Entity

from cli.app.constants import GO_BACK


def make_entyties_map(entyties: List[Entity]) -> Dict[str, Entity]:
    result = {}
    for entity in entyties:
        result[str(entity)] = entity
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

    entity = entyties_map[key]
    entity.print()

    next_action = select(actions, cursor=">>>", cursor_style="cyan")
    return next_action, entity
