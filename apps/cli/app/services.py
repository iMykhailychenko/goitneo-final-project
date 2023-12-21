from typing import Tuple

from beaupy import select
from core import Actions, controller
from core.models import (
    BirthdayPayload,
    Contact,
    ContactPayload,
    Entity,
    ResponseType,
    SearchPayload,
)
from rich.console import Console

from app.constants import (
    GO_BACK,
    BaseActions,
    base,
    contacts,
    entities_map,
    search_entities,
    single_contact,
)
from app.utils import make_entyties_list, prompt, prompt_set, with_confirmation

console = Console()


def base_action(*_) -> Tuple[str, None]:
    console.print("\nHow can I help you?\n", style="white on blue")
    return select(base, cursor=">>>", cursor_style="cyan"), None


def contacts_actions(*_) -> Tuple[str, None]:
    console.print(BaseActions.CONTACTS.value, style="white on blue")
    return select(contacts, cursor=">>>", cursor_style="cyan"), None


@with_confirmation
def create_new_contact(*_) -> None:
    name = prompt(
        "Enter contact name",
        error_message="Name is required!",
        validator=lambda value: len(value) > 0,
    )
    payload = ContactPayload(name=name)
    result = controller(Actions.GET, payload)

    if result.value:
        console.print("The record already exists 😅️️️️️️\n", end="\n." * 10)
    else:
        email = prompt("Add email", error_message="Invalid email", optional=True)
        phones = prompt_set(
            question="Add phone number",
            question_next="Add extra phone number",
            error_message="Invalid phone number",
            optional=True,
        )
        birthday = prompt(
            "Add birthday", error_message="Invalid birthday", optional=True
        )

        result = controller(
            Actions.ADD,
            ContactPayload(
                name=name,
                phones=phones,
                birthday=birthday,
                email=email,
            ),
        )

        if result.type.value == ResponseType.ERROR.value:
            console.print(result.message + "\n", end="\n." * 10)
        else:
            console.print("🎉  Contact created successfully!\n", end="\n." * 10)


@with_confirmation
def update_contact(prev: Contact) -> None:
    email = prompt("Update email", error_message="Invalid email", optional=True)
    phones = prompt_set(
        question="Update phone number",
        question_next="Add extra phone number",
        error_message="Invalid phone number",
        optional=True,
    )
    birthday = prompt(
        "Update birthday", error_message="Invalid birthday", optional=True
    )

    result = controller(
        Actions.UPDATE,
        ContactPayload(name=prev.id, phones=phones, birthday=birthday, email=email),
    )

    if result.type.value == ResponseType.ERROR.value:
        console.print(result.message + "\n", end="\n." * 10)
    else:
        console.print("🎉  Contact updated successfully!\n", end="\n." * 10)


@with_confirmation
def get_birthdays_by_duration(*_) -> None:
    day_duration = prompt(
        "Enter days duration from today",
        error_message="Duration should be an Integer",
        optional=True,
    )

    day_amount = day_duration if type(day_duration) == int else 7
    payload = BirthdayPayload(day_amount=day_amount)
    result = controller(Actions.BIRTHDAYS, payload)

    if result.type.value == ResponseType.ERROR.value:
        console.print(f"{result.message} 😅️️️️️️\n", end="\n." * 10)
    else:
        if result.value:
            console.print(
                f"The following users celebrate birthdays in the next {day_amount} days",
                end="\n" * 3,
                style="white on blue",
            )
            return make_entyties_list(result.value, single_contact)
        else:
            console.print(
                f"None from contacts celebrate their birthday in the next {day_amount} days 🫠",
                end="\n" * 3,
                style="white on red",
            )


def get_all_contacts(*_) -> None:
    result = controller(Actions.ALL)
    if result.type.value == ResponseType.ERROR.value:
        console.print(f"{result.message} 😅️️️️️️\n", end="\n." * 10)
        input("\n\nPress Enter to continue...")
        return
    return make_entyties_list(result.value, single_contact)


def search(*_) -> Tuple[str, Entity]:
    entity_key = select(search_entities, cursor=">>>", cursor_style="cyan")

    if entity_key == GO_BACK:
        return None

    query = prompt("Enter search value...")
    result = controller(
        Actions.SEARCH, SearchPayload(entity=entities_map[entity_key], query=query)
    )

    if result.type.value == ResponseType.ERROR.value:
        console.print(f"{result.message} 😅️", end="\n." * 10)
        input("\n\nPress Enter to continue...")
        return
    
    if not len(result.value):
        console.print(f"No results for the search query - {query}", end="\n." * 10, style="white on red")
        input("\n\nPress Enter to continue...")
        return

    return make_entyties_list(result.value, single_contact)
