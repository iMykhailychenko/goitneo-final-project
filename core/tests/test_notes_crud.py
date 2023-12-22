from core import Actions, controller
from core.database import Database
from core.models import EntitiesType, NotePayload
from tests.utils import setup_db

db = Database()


def test_add_note(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))

    assert (
        db.select(entity=EntitiesType.NOTES, key=result.value.id).value == "test note"
    )


def test_get_note(setup_db):
    pass


def test_delete_note(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.DELETE_NOTE, NotePayload(id=result.value.id))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id) == None


def test_update_note(setup_db):
    pass  # TODO implement after test_get_note


def test_add_tags(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.ADD_TAG, NotePayload(id=result.value.id, tags={"test tag"}))
    controller(Actions.ADD_TAG, NotePayload(id=result.value.id, tags={"test tag2"}))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id).tags == {
        "test tag",
        "test tag2",
    }


def test_update_tag(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.ADD_TAG, NotePayload(id=result.value.id, tags={"test tag"}))
    controller(Actions.UPDATE_TAG, NotePayload(id=result.value.id, tags={"new tag"}))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id).tags == {"new tag"}


def test_delete_tags(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(Actions.ADD_TAG, NotePayload(id=result.value.id, tags={"test tag"}))
    controller(Actions.DELETE_TAG, NotePayload(id=result.value.id))
    assert db.select(entity=EntitiesType.NOTES, key=result.value.id).tags == set()


def test_find_by_tag(setup_db):
    result = controller(Actions.ADD_NOTE, NotePayload(value="test note"))
    controller(
        Actions.ADD_TAG, NotePayload(id=result.value.id, tags={"test find by tag"})
    )
    result2 = controller(Actions.ADD_NOTE, NotePayload(value="test note2"))
    controller(
        Actions.ADD_TAG, NotePayload(id=result2.value.id, tags={"test find by tag"})
    )
    assert (
        len(
            controller(
                Actions.FIND_BY_TAG, NotePayload(tags={"test find by tag"})
            ).value
        )
        == 2
    )
