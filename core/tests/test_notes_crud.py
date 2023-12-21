from core import Actions, controller
from core.database import Database, Entities
from core.models import NotePayload
from tests.utils import setup_db

db = Database()


def test_add_note(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))

    assert db.select(entity=Entities.NOTES, key=result.value.id).value == "test note"


def test_get_note(setup_db):
    pass


def test_delete_note(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.DELETE_NOTE, NotePayload(id=result.value.id))
    assert db.select(entity=Entities.NOTES, key=result.value.id) == None


def test_update_note(setup_db):
    pass  # TODO implement after test_get_note
