from typing import Optional, Tuple

from core import Actions, Validator, controller
from core.models import BirthdayPayload, Contact, ContactPayload, Entity
from rich.console import Console

from cli.app.constants import GO_BACK, ContactActions, single_contact
from cli.app.utils import (
    confirm_to_continue,
    has_error,
    make_entyties_list,
    print_confirmation_message,
    print_error,
    prompt,
    with_confirmation,
)

console = Console()


def get_birthdays_by_duration(*_) -> None:
    day_amount = prompt(
        "Enter days duration from today",
        error_message="Duration should be a positive Integer",
        validator=lambda value: int(value) > 0,
        target_type=int,
        optional=True,
    )
    payload = BirthdayPayload(day_amount=day_amount)
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


@with_confirmation
def change_birthday(paylaod: Contact) -> Optional[Tuple[str, Entity]]:
    old_birthday = paylaod.birthday or "n/a"
    message = f"Change birthday for {paylaod.id}, current value: {old_birthday}"
    birthday = prompt(
        message,
        error_message="Invalid birthday 😅",
        optional=True,
        validator=lambda value: Validator.validate_birthday(value),
    )
    if not birthday:
        return GO_BACK

    result = controller(
        Actions.UPDATE, ContactPayload(name=paylaod.id, birthday=birthday)
    )
    print_confirmation_message(result, "🎉  Birthday changed successfully!\n")
    return ContactActions.ALL.value, paylaod
