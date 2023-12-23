from typing import List, Optional
from uuid import uuid4

from core.database import Database, delete_data, write_data
from core.misc import InfoMessages
from core.models import EntitiesType, Note, NotePayload, response

db = Database()


@response(InfoMessages.NOTE_ADDED)
@write_data(entity=EntitiesType.NOTES)
def add_note(payload: NotePayload) -> Note:
    return Note(
        id=str(uuid4())[:8],
        value=payload.value,
        tags=payload.tags,
    )


@response(InfoMessages.NOTE_UPDATED)
@write_data(entity=EntitiesType.NOTES)
def update_note(payload: NotePayload) -> Note:
    if record := db.select(entity=EntitiesType.NOTES, key=payload.id):
        if payload.value:
            record.value = payload.value
        if payload.tags and len(payload.tags):
            record.tags = payload.tags
        return record


@response(InfoMessages.NOTE_DELETED)
@delete_data(entity=EntitiesType.NOTES)
def delete_note(payload: NotePayload) -> Note:
    return db.select(entity=EntitiesType.NOTES, key=payload.id)


@response(InfoMessages.NOTE_ADDED)
def get_all_notes(*_) -> List[Note]:
    return db.select(entity=EntitiesType.NOTES, key="*")
