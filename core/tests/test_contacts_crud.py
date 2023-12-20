from datetime import datetime

from core import Actions, controller
from core.database import Database, Entities
from core.misc import InfoMessages
from core.models import Contact, ContactPayload
from tests.utils import setup_db

db = Database()


def test_add_name(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe"),
    )

    assert result.message == InfoMessages.CONTACT_CREATED.value
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(id="Joe")


def test_add_phone(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", phones={"1234567890"}),
    )

    assert result.message == InfoMessages.CONTACT_CREATED.value
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe", phones={"1234567890"}
    )


def test_add_email(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", email="email@example.com"),
    )

    assert result.message == InfoMessages.CONTACT_CREATED.value
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe", email="email@example.com"
    )


def test_add_birthday(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", birthday="20.11.1990"),
    )

    assert result.message == InfoMessages.CONTACT_CREATED.value
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe", birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date()
    )


def test_add_tags(setup_db):
    tags = {"Hello", "World"}
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", tags=tags),
    )

    assert result.message == InfoMessages.CONTACT_CREATED.value
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe", tags=tags
    )


def test_add_note(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", note="Hello World"),
    )

    assert result.message == InfoMessages.CONTACT_CREATED.value
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe", note="Hello World"
    )


def test_add_all(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(
            command=Actions.ADD,
            name="Joe",
            phones={"1234567890"},
            email="email@example.com",
            birthday="20.11.1990",
            note="Hello World",
        ),
    )
    assert result.message == InfoMessages.CONTACT_CREATED.value

    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe",
        phones={"1234567890"},
        email="email@example.com",
        birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date(),
        note="Hello World",
    )


def test_duplicates(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe"),
    )
    assert result.message == InfoMessages.CONTACT_CREATED.value

    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", phones={"1234567890"}),
    )
    assert result.message == InfoMessages.CONTACT_CREATED.value

    records = db.select(entity=Entities.CONTACTS, key="*")
    assert len(records) == 1
    assert db.select(entity=Entities.CONTACTS, key="Joe") == Contact(
        id="Joe", phones={"1234567890"}
    )
