from uuid import uuid4

from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import Note, NotePayload, response, EntitiesType

db = Database()


@response(InfoMessages.TAG_ADDED)
@write_data(entity=EntitiesType.NOTES)
def add_tag(payload: NotePayload) -> Note:
    record = db.select(entity=EntitiesType.NOTES, key=payload.id)
    record.tags = record.tags | payload.tags
    return record


@response(InfoMessages.TAG_UPDATED)
@write_data(entity=EntitiesType.NOTES)
def update_tag(payload: NotePayload) -> Note:
    record = db.select(entity=EntitiesType.NOTES, key=payload.id)
    record.tags = payload.tags
    return record


@response(InfoMessages.TAG_DELETED)
@write_data(entity=EntitiesType.NOTES)
def delete_tag(payload: NotePayload) -> Note:
    record = db.select(entity=EntitiesType.NOTES, key=payload.id)
    record.tags.clear()
    return record


@response()
def find_notes_by_tag(payload: NotePayload) -> list[Note]:
    records = db.select(entity=EntitiesType.NOTES, key="*")
    return [
        record for record in records if record.tags.intersection(payload.tags)
    ] or []
