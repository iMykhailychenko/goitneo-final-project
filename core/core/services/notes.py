from uuid import uuid4

from core.database import Database, Entities, write_data
from core.misc import InfoMessages
from core.models import Note, NotePayload, response

db = Database()


@response(InfoMessages.NOTE_ADDED)
@write_data(entity=Entities.NOTES)
def add_note(payload: NotePayload) -> Note:
    return Note(
        id=str(uuid4()),
        value=payload.value,
    )


@response(InfoMessages.NOTE_UPDATED)
@write_data(entity=Entities.NOTES)
def update_note(payload: NotePayload) -> Note:
    record = db.select(entity=Entities.NOTES, key=payload.id)
    if payload.value:
        record.value = payload.value
    if len(payload.tags):
        record.tags = payload.tags
    return record
