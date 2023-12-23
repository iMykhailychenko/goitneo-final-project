from core import Actions, controller
from core.database import Database
from core.models import EntitiesType, NotePayload, TagPayload
from tests.utils import setup_db

db = Database()


def test_add_note(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))

    assert (
        db.select(entity=EntitiesType.NOTES, key=result.value.id).value == "test note"
    )


def test_get_all_notes(setup_db):
    controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.ADD_NOTE, NotePayload(value="test note2"))

    result = controller(Actions.ALL_NOTES)
    assert len(result.value) == 2


def test_delete_note(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.DELETE_NOTE, NotePayload(id=result.value.id))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id) == None


def test_add_tags(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.ADD_TAG, TagPayload(id=result.value.id, tag="test tag"))
    controller(Actions.ADD_TAG, TagPayload(id=result.value.id, tag="test tag2"))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id).tags == {
        "test tag",
        "test tag2",
    }


def test_update_tag(setup_db):
    result = controller(
        Actions.ADD_NOTE, NotePayload(value="test note", tags={"test tag"})
    )
    controller(Actions.UPDATE_TAG, TagPayload(id=result.value.id, tag="new tag", old_tag="test tag"))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id).tags == {"new tag"}


def test_delete_tags(setup_db):
    result = controller(
        Actions.ADD_NOTE, NotePayload(value="test note", tags={"test tag"})
    )
    controller(Actions.DELETE_TAG, TagPayload(id=result.value.id, tag="test tag"))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id).tags == set()
