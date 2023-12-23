from typing import Optional, Tuple

from beaupy import select
from core import Actions, controller
from core.models import Contact, PhonePayload
from rich.console import Console

from cli.app.constants import GO_BACK, ContactActions
from cli.app.utils import print_confirmation_message, prompt, with_confirmation

console = Console()


@with_confirmation
def add_phone(paylaod: Contact) -> None:
    phones = ", ".join(paylaod.phones) or "n/a"
    message = f"Enter phone number for {paylaod.id}, current phones: {phones}"
    phone = prompt(message, error_message="Invalid phone number", optional=True)

    if not phone:
        return GO_BACK

    if phone in paylaod.phones:
        console.print(
            f"Phone number {phone} already exists in {paylaod.id}'s phones!\n",
            style="white on red",
        )
        return

    result = controller(Actions.ADD_PHONE, PhonePayload(name=paylaod.id, phone=phone))
    print_confirmation_message(result, "🎉  Phone number added successfully!\n")
    return ContactActions.ALL.value, paylaod


@with_confirmation
def delete_phone(paylaod: Contact) -> None:
    if not len(paylaod.phones):
        console.print("There are no phones in this record\n", style="white on red")
        return

    console.print("Select phone number to delete\n\n", style="white on blue")
    value = select(
        [GO_BACK, *paylaod.phones],
        cursor=">>>",
        cursor_style="cyan",
    )
    if value == GO_BACK:
        return GO_BACK

    result = controller(
        Actions.DELETE_PHONE, PhonePayload(name=paylaod.id, phone=value)
    )
    print_confirmation_message(result, "🎉  Phone number deleted successfully!\n")
    return ContactActions.ALL.value, paylaod
