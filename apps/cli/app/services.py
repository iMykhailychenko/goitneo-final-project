from beaupy import ValidationError, select
from core import Actions, controller
from core.models import BirthdayPayload, ContactPayload, ResponseType
from rich.console import Console
from rich.table import Table

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
    result = controller(Actions.GET, payload)

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
        phones.remove("")
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
    result = controller(Actions.GET, payload)
    if not result.value:
        console.print("Contact does not exist 😅️️️️️️" + "\n", end="\n." * 10)
        input("\n\nPress Enter to continue...")

    else:
        email = prompt("Update email", error_message="Invalid email", optional=True)
        phones = prompt_set(
            question="Update phone number",
            question_next="Add extra phone number",
            error_message="Invalid phone number",
            optional=True,
        )
        phones.remove("")
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


def get_birthdays_by_duration() -> None:
    day_duration = prompt(
        "Enter days duration from today",
        error_message="Duration should be an Integer",
        optional=True,
    )
    try:
        day_amount = int(day_duration)
    except:
        day_amount = 7

    payload = BirthdayPayload(day_amount=day_amount)
    result = controller(Actions.BIRTHDAYS, payload)

    if result.type.value == ResponseType.ERROR.value:
        console.print(f"{result.message} 😅️️️️️️" + "\n", end="\n." * 10)
    else:
        if result.value:
            console.print(
                f"The following contact(s) celebrate birthdays in the next {day_amount} days \n",
                style="white on blue",
            )
            title = "🎉️️️️️️ List of birthday people 🎉️️️️️️"
            display_data_table(result.value, title)
        else:
            console.print(
                f"None from contacts celebrate their birthday in the next {day_amount} days 🫠",
                style="white on red",
            )
    input("\n\nPress Enter to continue...")


def get_all_contacts() -> None:
    result = controller(Actions.ALL, None)

    if result.type.value == ResponseType.ERROR.value:
        console.print(f"{result.message} 😅️️️️️️" + "\n", end="\n." * 10)
    else:
        if result.value:
            console.print(
                f"The following contact(s) are in the AddressBook \n",
                style="white on blue",
            )
            title = "💃 List of contacts 🕺"
            display_data_table(result.value, title)
        else:
            console.print(
                """Contacts have not been added yet 🫠. To add a contact, please enter the following command: 
    'add contactName phone', where contactName is the name of contact, and phone is a contact phone number.""",
                style="white on red",
            )
    input("\n\nPress Enter to continue...")


def display_data_table(contacts, title):
    table = Table(
        title=title, show_header=True, header_style="bold blue", show_lines=True
    )

    table.add_column("Name", justify="center", min_width=20)
    table.add_column("Birthday", justify="center", min_width=20, style="green")
    table.add_column("Email", justify="center", min_width=20)
    table.add_column("Address", justify="center", min_width=20)
    table.add_column("Phone Numbers", justify="center", max_width=35)
    for contact in contacts:
        birthday_date = contact.birthday
        phone_values = (
            str(contact.phones.pop())
            if len(contact.phones) == 1
            else "; ".join(contact.phones)
            if len(contact.phones) > 1
            else "----"
        )

        table.add_row(
            contact.id,
            birthday_date.strftime("%d.%m.%Y") if contact.birthday else "----",
            contact.email if contact.email else "----",
            contact.address if contact.birthday else "----",
            phone_values,
        )

    console.print(table)
