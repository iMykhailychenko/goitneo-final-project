from core.database import write_data, Database
from core.models import NotePayload, Record, response
from core.misc import InfoMessages

@response(InfoMessages.NOTE_ADDED)
@write_data
def add_note(payload: NotePayload) -> Record:
    db = Database().connect()
    record = db[payload.name]
    record.note = payload.note
    return record