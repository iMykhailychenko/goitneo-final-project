from typing import List, Tuple

from beaupy import select
from core import Actions, controller
from core.models import EntitiesType, Entity, SearchPayload
from rich.console import Console

from cli.app.constants import (
    GO_BACK,
    SearchActions,
    search_entities,
    single_contact,
    single_note,
)
from cli.app.utils import (
    confirm_to_continue,
    has_error,
    make_entyties_list,
    print_error,
    prompt,
)

console = Console()


entities_map = {
    SearchActions.CONTACTS.value: EntitiesType.CONTACTS,
    SearchActions.NOTES.value: EntitiesType.NOTES,
}

actions_map = {
    SearchActions.CONTACTS.value: single_contact,
    SearchActions.NOTES.value: single_note,
}


def make_search(entity: EntitiesType, actions: List[str]) -> Tuple[str, Entity]:
    query = prompt(
        "🔎  Enter search value...",
        error_message="Enter search value",
        validator=lambda input: len(input) > 0,
    )
    result = controller(Actions.SEARCH, SearchPayload(entity=entity, query=query))

    if has_error(result):
        print_error(result)
        confirm_to_continue()
        return

    if not len(result.value):
        console.print(
            f"No results for the search query - {query} \n",
            style="white on red",
        )
        print("\n." * 10)
        confirm_to_continue()
        return

    return make_entyties_list(result.value, actions)


def search_contacts(*_) -> Tuple[str, Entity]:
    return make_search(entity=EntitiesType.CONTACTS, actions=single_contact)


def search_notes(*_) -> Tuple[str, Entity]:
    return make_search(entity=EntitiesType.NOTES, actions=single_note)


def search(*_) -> Tuple[str, Entity]:
    entity_key = select(search_entities, cursor=">>>", cursor_style="cyan")

    if entity_key == GO_BACK:
        return None

    return make_search(entity=entities_map[entity_key], actions=actions_map[entity_key])
