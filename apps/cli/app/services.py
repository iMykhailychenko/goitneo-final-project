from beaupy import ValidationError, select
from core import Actions, ContactPayload, ResponseType, controller
from rich.console import Console

from app.constants import BaseActions, base, contacts
from app.utils import prompt, prompt_set

console = Console()


def base_action() -> str:
    console.print("\nHow can I help you?\n", style="white on blue")
    return select(base, cursor=">>>", cursor_style="cyan")


def contacts_actions() -> str:
    console.print(BaseActions.CONTACTS.value, style="white on blue")
    return select(contacts, cursor=">>>", cursor_style="cyan")


def create_new_contact() -> None:
    name = prompt(
        "Enter contact name",
        error_message="Name is required!",
        validator=lambda value: len(value) > 0,
    )
    payload = ContactPayload(name=name)
    result = controller(Actions.CHECK, payload)

    if result.value:
        console.print("The record already exists 😅️️️️️️" + "\n", end="\n." * 10)
        input("\n\nPress Enter to continue...")
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
        note = prompt("Add note", optional=True)
        tags = prompt_set(
            question="Add tag", question_next="Add extra tag", optional=True
        )

        payload = ContactPayload(
            name=name,
            phones=phones,
            birthday=birthday,
            email=email,
            note=note,
            tags=tags,
        )

        result = controller(Actions.ADD, payload)
        if result.type.value == ResponseType.ERROR.value:
            console.print(result.message + "\n", end="\n." * 10)
        else:
            console.print("🎉  Contact created successfully!\n", end="\n." * 10)
        input("\n\nPress Enter to continue...")


def update_contact() -> None:
    name = prompt(
        "Enter contact name",
        error_message="Name is required!",
        validator=lambda value: len(value) > 0,
    )
    payload = ContactPayload(name=name)
    result = controller(Actions.CHECK, payload)
    if result.type.value == ResponseType.ERROR.value:
        console.print(f"{result.message} 😅️️️️️️" + "\n", end="\n." * 10)
        input("\n\nPress Enter to continue...")

    else:
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

        payload = ContactPayload(
            name=name, phones=phones, birthday=birthday, email=email
        )

        result = controller(Actions.UPDATE, payload)

        if result.type.value == ResponseType.ERROR.value:
            console.print(result.message + "\n", end="\n." * 10)
        else:
            console.print("🎉  Contact updated successfully!\n", end="\n." * 10)
        input("\n\nPress Enter to continue...")


def get_all_contacts() -> None:
    pass
