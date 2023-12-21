from uuid import uuid4

from core.database import Database, Entities, delete_data, write_data
from core.misc import InfoMessages
from core.models import Note, NotePayload, response

db = Database()


@response(InfoMessages.TAG_ADDED)
@write_data(entity=Entities.NOTES)
def add_tag(payload: NotePayload) -> Note:
    record = db.select(entity=Entities.NOTES, key=payload.id)
    record.tags = record.tags | payload.tags
    return record


@response(InfoMessages.TAG_UPDATED)
@write_data(entity=Entities.NOTES)
def update_tag(payload: NotePayload) -> Note:
    record = db.select(entity=Entities.NOTES, key=payload.id)
    record.tags = payload.tags
    return record


@response(InfoMessages.TAG_DELETED)
@write_data(entity=Entities.NOTES)
def delete_tag(payload: NotePayload) -> Note:
    record = db.select(entity=Entities.NOTES, key=payload.id)
    record.tags.clear()
    return record


@response()
def find_notes_by_tag(payload: NotePayload) -> list[Note]:
    records = db.select(entity=Entities.NOTES, key="*")
    return [
        record for record in records if record.tags.intersection(payload.tags)
    ] or []
