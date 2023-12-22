from typing import Optional, Tuple

from beaupy import select
from core import Actions, controller
from core.models import (
    BirthdayPayload,
    Contact,
    ContactPayload,
    Entity,
    Response,
    ResponseType,
    SearchPayload,
)
from rich.console import Console

from cli.app.constants import (
    GO_BACK,
    BaseActions,
    base,
    contacts,
    entities_map,
    search_entities,
    single_contact,
)
from cli.app.utils import (
    confirm_to_continue,
    has_error,
    make_entyties_list,
    print_confirmation_message,
    print_error,
    prompt,
    prompt_set,
    with_confirmation,
)

console = Console()


def base_action(*_) -> Tuple[str, None]:
    console.print("\nHow can I help you?\n", style="white on blue")
    return select(base, cursor=">>>", cursor_style="cyan"), None


def contacts_actions(*_) -> Tuple[str, None]:
    console.print(BaseActions.CONTACTS.value, style="white on blue")
    return select(contacts, cursor=">>>", cursor_style="cyan"), None


def get_contact() -> Tuple[Response, str]:
    name = prompt(
        "Enter contact name",
        error_message="Name is required!",
        validator=lambda value: len(value) > 0,
    )
    return controller(Actions.GET, ContactPayload(name=name)), name


@with_confirmation
def create_new_contact(*_) -> None:
    contact, name = get_contact()

    if has_error(contact):
        return print_error(contact)
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
        address = prompt("Add address", error_message="Invalid address", optional=True)
        payload = ContactPayload(
            name=name,
            phones=phones,
            birthday=birthday,
            email=email,
            address=address,
        )

        result = controller(Actions.ADD, payload=payload)
        print_confirmation_message(result, "🎉  Contact created successfully!\n")


@with_confirmation
def update_contact(prev: Contact) -> None:
    prev_email = prev.email or "n/a"
    email = prompt(
        f"Update email [{prev_email}]", error_message="Invalid email", optional=True
    )

    prev_birthday = prev.birthday.strftime("%d.%m.%Y") if prev.birthday else "n/a"
    birthday = prompt(
        f"Update birthday {prev_birthday}",
        error_message="Invalid birthday",
        optional=True,
    )

    prev_address = prev.address or "n/a"
    address = prompt(
        f"Add address [{prev_address}]", error_message="Invalid address", optional=True
    )

    result = controller(
        Actions.UPDATE,
        ContactPayload(
            name=prev.id,
            birthday=birthday,
            email=email,
            address=address,
        ),
    )
    print_confirmation_message(result, "🎉  Contact updated successfully!\n")


@with_confirmation
def delete_contact(prev: Contact) -> None:
    result = controller(
        Actions.DELETE,
        ContactPayload(name=prev.id),
    )
    print_confirmation_message(result, "🎉  Contact deleted successfully!\n")


def get_birthdays_by_duration(*_) -> None:
    day_duration = prompt(
        "Enter days duration from today",
        error_message="Duration should be an Integer",
        optional=True,
    )
    day_amount = day_duration if type(day_duration) == int else 7
    payload = BirthdayPayload(day_amount=day_duration)
    result = controller(Actions.BIRTHDAYS, payload)

    if has_error(result):
        print_error(result)
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
            confirm_to_continue()


def get_all_contacts(*_) -> Optional[Tuple[str, Entity]]:
    result = controller(Actions.ALL)
    if has_error(result):
        print_error(result)
        confirm_to_continue()
    else:
        return make_entyties_list(result.value, single_contact)


def search(*_) -> Tuple[str, Entity]:
    entity_key = select(search_entities, cursor=">>>", cursor_style="cyan")

    if entity_key == GO_BACK:
        return None

    query = prompt("Enter search value...")
    result = controller(
        Actions.SEARCH, SearchPayload(entity=entities_map[entity_key], query=query)
    )

    if has_error(result):
        print_error(result)
        confirm_to_continue()
        return

    if not len(result.value):
        console.print(
            f"No results for the search query - {query}",
            end="\n." * 10,
            style="white on red",
        )
        confirm_to_continue()
        return

    return make_entyties_list(result.value, single_contact)
