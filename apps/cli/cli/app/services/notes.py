from typing import Optional, Tuple

from beaupy import select
from core import Actions, controller
from core.models import Entity, Note, NotePayload
from rich.console import Console

from cli.app.constants import GO_BACK, BaseActions, NoteActions, notes, single_note
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


def notes_actions(*_) -> Tuple[str, None]:
    console.print(BaseActions.NOTES.value, style="white on blue")
    return select(notes, cursor=">>>", cursor_style="cyan"), None


def single_note_actions(paylaod: Note) -> Tuple[str, Entity]:
    paylaod.print()
    return select(single_note, cursor=">>>", cursor_style="cyan"), paylaod


def get_all_notes(*_) -> Optional[Tuple[str, Entity]]:
    result = controller(Actions.ALL_NOTES)
    if has_error(result):
        print_error(result)
        confirm_to_continue()
    else:
        return make_entyties_list(result.value, single_note)


@with_confirmation
def add_note(paylaod: Note) -> Optional[Tuple[str, Entity]]:
    value = prompt(
        "Enter your note",
        error_message="This is required field!",
        validator=lambda value: len(value.strip()) > 0,
    )
    tags = prompt_set(
        question="Add tags",
        question_next="Add more tag",
        optional=True,
    )

    result = controller(Actions.ADD_NOTE, NotePayload(value=value, tags=tags))
    print_confirmation_message(result, "🎉  Note created successfully!\n")
    return NoteActions.ALL.value, paylaod


@with_confirmation
def delete_note(paylaod: Note) -> Optional[Tuple[str, Entity]]:
    result = controller(Actions.DELETE_NOTE, NotePayload(id=paylaod.id))
    print_confirmation_message(result, f"🎉  Note {paylaod.id} deleted successfully!\n")
    return NoteActions.ALL.value, paylaod


@with_confirmation
def update_note(paylaod: Note) -> Optional[Tuple[str, Entity]]:
    paylaod.print()
    value = prompt("Enter new note text", initial_value=paylaod.value)
    if not value:
        return GO_BACK

    result = controller(Actions.UPDATE_NOTE, NotePayload(id=paylaod.id, value=value))
    print_confirmation_message(result, f"🎉  Note {paylaod.id} updated successfully!\n")
    return NoteActions.ALL.value, paylaod
