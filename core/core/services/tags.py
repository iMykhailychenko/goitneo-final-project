from typing import Optional

from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import EntitiesType, Note, TagPayload, response

db = Database()


@response(InfoMessages.TAG_ADDED)
@write_data(entity=EntitiesType.NOTES)
def add_tag(payload: TagPayload) -> Optional[Note]:
    if record := db.select(entity=EntitiesType.NOTES, key=payload.id):
        record.tags.add(payload.tag)
        return record


@response(InfoMessages.TAG_UPDATED)
@write_data(entity=EntitiesType.NOTES)
def update_tag(payload: TagPayload) -> Optional[Note]:
    if record := db.select(entity=EntitiesType.NOTES, key=payload.id):
        record.tags.discard(payload.old_tag)
        record.tags.add(payload.tag)
        return record


@response(InfoMessages.TAG_DELETED)
@write_data(entity=EntitiesType.NOTES)
def delete_tag(payload: TagPayload) -> Optional[Note]:
    if record := db.select(entity=EntitiesType.NOTES, key=payload.id):
        record.tags.discard(payload.tag)
        return record
