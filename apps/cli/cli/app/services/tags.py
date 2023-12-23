from typing import Optional, Tuple

from beaupy import select
from core import Actions, controller
from core.models import Note, TagPayload
from rich.console import Console

from cli.app.constants import GO_BACK, NoteActions
from cli.app.utils import print_confirmation_message, prompt, with_confirmation

console = Console()


@with_confirmation
def delete_tag(paylaod: Note) -> Optional[Tuple[str, Note]]:
    if not len(paylaod.tags):
        console.print("There are no tags in this record\n", style="white on red")
        return

    console.print("Select tag to delete\n\n", style="white on blue")
    value = select(
        [GO_BACK, *paylaod.tags],
        cursor=">>>",
        cursor_style="cyan",
    )
    if value == GO_BACK:
        return GO_BACK

    result = controller(Actions.DELETE_TAG, TagPayload(id=paylaod.id, tag=value))
    print_confirmation_message(result, "🎉  Tag deleted successfully!\n")
    return NoteActions.ALL.value, paylaod


@with_confirmation
def add_tag(paylaod: Note) -> Optional[Tuple[str, Note]]:
    new_tag = prompt("Enter new tag")
    if not new_tag:
        return GO_BACK

    result = controller(Actions.ADD_TAG, TagPayload(id=paylaod.id, tag=new_tag))

    print_confirmation_message(result, "🎉  Tag created successfully!\n")
    return NoteActions.ALL.value, paylaod
