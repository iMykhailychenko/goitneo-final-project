from datetime import date

from core import Actions, controller
from core.database import Database
from core.models import (
    Contact,
    ContactPayload,
    EntitiesType,
    NotePayload,
    SearchPayload,
)
from tests.utils import setup_db

db = Database()


def test_search_by_name(setup_db):
    controller(Actions.ADD, ContactPayload(name="Joe"))
    controller(Actions.ADD, ContactPayload(name="Bill"))

    result = controller(
        Actions.SEARCH, SearchPayload(entity=EntitiesType.CONTACTS, query="jo")
    )
    assert len(result.value) == 1
    assert result.value[0] == Contact(id="Joe")


def test_search_by_phone(setup_db):
    controller(
        Actions.ADD, ContactPayload(name="Joe", phones={"1111111111", "3333333333"})
    )
    controller(Actions.ADD, ContactPayload(name="Bill", phones={"2222222222"}))

    result = controller(
        Actions.SEARCH, SearchPayload(entity=EntitiesType.CONTACTS, query="1111")
    )
    assert len(result.value) == 1
    assert result.value[0] == Contact(id="Joe", phones={"1111111111", "3333333333"})


def test_search_by_birthday(setup_db):
    controller(Actions.ADD, ContactPayload(name="Joe", birthday="10.10.1999"))
    controller(Actions.ADD, ContactPayload(name="Bill", birthday="20.02.1995"))

    result = controller(
        Actions.SEARCH, SearchPayload(entity=EntitiesType.CONTACTS, query="1995")
    )
    assert len(result.value) == 1
    assert result.value[0] == Contact(id="Bill", birthday=date(1995, 2, 20))


def test_search_by_email(setup_db):
    controller(Actions.ADD, ContactPayload(name="Joe", email="email@email.com"))
    controller(Actions.ADD, ContactPayload(name="Bill", email="test@ukr.net"))
    result = controller(
        Actions.SEARCH, SearchPayload(entity=EntitiesType.CONTACTS, query="test@")
    )
    assert len(result.value) == 1
    assert result.value[0] == Contact(id="Bill", email="test@ukr.net")


def test_search_notes(setup_db):
    id1 = controller(Actions.ADD_NOTE, NotePayload(value="test")).value.id
    controller(Actions.ADD_NOTE, NotePayload(value="note"))

    result = controller(
        Actions.SEARCH, SearchPayload(entity=EntitiesType.NOTES, query="test")
    )
    assert len(result.value) == 1
    assert result.value[0] == db.select(entity=EntitiesType.NOTES, key=id1)


# TODO - uncomment after we add tags
def test_search_by_tags(setup_db):
    id1 = controller(
        Actions.ADD_NOTE, NotePayload(value="note", tags={"tags", "test"})
    ).value.id
    controller(Actions.ADD_NOTE, NotePayload(value="note", tags={"tags"}))

    result = controller(
        Actions.SEARCH, SearchPayload(entity=EntitiesType.NOTES, query="tes")
    )
    assert len(result.value) == 1
    assert result.value[0] == db.select(entity=EntitiesType.NOTES, key=id1)
