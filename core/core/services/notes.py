from core.database import Database, write_data
from core.misc import InfoMessages
from core.models import NotePayload, Record, response


@response(InfoMessages.NOTE_ADDED)
@write_data
def add_note(payload: NotePayload) -> Record:
    db = Database().connect()
    record = db[payload.name]
    record.note = payload.note
    return record


@response(InfoMessages.NOTE_UPDATED)
@write_data
def update_note(payload: NotePayload) -> Record:
    db = Database().connect()
    record = db[payload.name]
    record.note = payload.note
    return record
