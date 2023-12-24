from typing import Optional, Tuple

from beaupy import select
from core import Actions, controller
from core.models import Contact, ContactPayload, Entity, Response
from rich.console import Console

from cli.app.constants import (
    GO_BACK,
    BaseActions,
    ContactActions,
    contacts,
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


def contacts_actions(*_) -> Tuple[str, None]:
    console.print(BaseActions.CONTACTS.value, style="white on blue")
    return select(contacts, cursor=">>>", cursor_style="cyan"), None


def get_contact() -> Tuple[Response, str]:
    name = prompt(
        "Enter contact name",
        error_message="Name is required!",
        validator=lambda value: len(value.strip()) > 0,
    )
    return controller(Actions.GET, ContactPayload(name=name)), name


@with_confirmation
def create_new_contact(*_) -> None:
    contact, name = get_contact()

    if has_error(contact):
        return print_error(contact)
    elif contact.value:
        console.print(
            f"Contact with name {name} already exists!\n", style="white on red"
        )
        confirm_to_continue()
        return
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


def get_all_contacts(*_) -> Optional[Tuple[str, Entity]]:
    result = controller(Actions.ALL)
    if has_error(result):
        print_error(result)
        confirm_to_continue()
    else:
        return make_entyties_list(result.value, single_contact)


@with_confirmation
def delete_contact(paylaod: Contact) -> Tuple[str, Entity]:
    result = controller(
        Actions.DELETE,
        ContactPayload(name=paylaod.id),
    )
    print_confirmation_message(result, "🎉  Contact deleted successfully!\n")
    return ContactActions.ALL.value, paylaod


@with_confirmation
def change_name(paylaod: Contact) -> Tuple[str, Entity]:
    message = f"Enter new name for {paylaod.id}"
    new_name = prompt(message)
    if not new_name:
        return GO_BACK

    result = controller(
        Actions.UPDATE, ContactPayload(name=paylaod.id, new_name=new_name)
    )
    print_confirmation_message(result, "🎉  Name changed successfully!\n")
    return ContactActions.ALL.value, paylaod


@with_confirmation
def change_email(paylaod: Contact) -> Tuple[str, Entity]:
    old_email = paylaod.email or "n/a"
    message = f"Change email for {paylaod.id}, current value: {old_email}"
    email = prompt(message, error_message="Invalid email", optional=True)
    if not email:
        return GO_BACK

    result = controller(Actions.UPDATE, ContactPayload(name=paylaod.id, email=email))
    print_confirmation_message(result, "🎉  Email changed successfully!\n")
    return ContactActions.ALL.value, paylaod


@with_confirmation
def change_addresa(paylaod: Contact) -> Tuple[str, Entity]:
    old_address = paylaod.address or "n/a"
    message = f"Change address for {paylaod.id}, current value: {old_address}"
    address = prompt(message, error_message="Invalid address", optional=True)
    if not address:
        return GO_BACK

    result = controller(
        Actions.UPDATE, ContactPayload(name=paylaod.id, address=address)
    )
    print_confirmation_message(result, "🎉  Address changed successfully!\n")
    return ContactActions.ALL.value, paylaod


