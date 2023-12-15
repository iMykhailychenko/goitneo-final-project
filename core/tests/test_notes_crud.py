from datetime import datetime

from core import Actions, Database, NotePayload, controller
from tests.utils import setup_test_user

db = Database().connect()


def test_add_note(setup_test_user):
    # controller(Actions.ADD_NOTE, NotePayload(name="Joe", note="test note"))
    # assert db["Joe"].note == "test note"
    pass


def test_delete_note(setup_test_user):
    # controller(Actions.ADD_NOTE, NotePayload(name="Joe", note="test note"))
    # controller(Actions.DELETE_NOTE, NotePayload(name="Joe"))
    # assert db["Joe"].note == None
    pass


def test_update_note(setup_test_user):
    # controller(Actions.ADD_NOTE, NotePayload(name="Joe", note="test note"))
    # controller(Actions.UPDATE_NOTE, NotePayload(name="Joe", note="test note 2"))
    # assert db["Joe"].note == "test note 2"
    pass
