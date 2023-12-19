from beaupy import select, ValidationError
from rich.console import Console
from core import controller, Actions, ContactPayload, ResponseType

from app.constants import BaseActions, contacts, base
from app.utils import prompt, prompt_set

console = Console()


def base_action() -> str:
    console.print("\nHow can I help you?\n", style="white on blue")
    return select(base, cursor=">>>", cursor_style="cyan")


def contacts_actions() -> str:
    console.print(BaseActions.CONTACTS.value, style="white on blue")
    return select(contacts, cursor=">>>", cursor_style="cyan")


def create_new_contact() -> None:
    name = prompt("Enter contact name", error_message="Name is required!", validator=lambda value: len(value) > 0)
    # TODO - show error if name already exists

    email = prompt("Add email", error_message="Invalid email", optional=True)
    phones = prompt_set(question="Add phone number", question_next="Add extra phone number", error_message="Invalid phone number", optional=True)
    birthday = prompt("Add birthday", error_message="Invalid birthday", optional=True)
    note = prompt("Add note", optional=True)
    tags = prompt_set(question="Add tag", question_next="Add extra tag", optional=True)

    payload = ContactPayload(name=name, phones=phones, birthday=birthday, email=email, note=note, tags=tags)

    result = controller(Actions.ADD, payload)
    if result.type.value == ResponseType.ERROR.value:
        console.print(result.message + "\n", end="\n." * 10)
    else:
        console.print("🎉  Contact created successfully!\n", end="\n." * 10)
    input("\n\nPress Enter to continue...")


def get_all_contacts() -> None:
    pass