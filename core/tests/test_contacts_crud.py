from datetime import datetime

from core import Actions, ContactPayload, Database, Record, controller
from tests.utils import setup_db

db = Database().connect()


def test_add_name(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe"),
    )

    assert result.message == "Contact created."
    assert db["Joe"] == Record(name="Joe")


def test_add_phone(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", phones={"1234567890"}),
    )

    assert result.message == "Contact created."
    assert db["Joe"] == Record(name="Joe", phones={"1234567890"})


def test_add_email(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", email="email@example.com"),
    )

    assert result.message == "Contact created."
    assert db["Joe"] == Record(name="Joe", email="email@example.com")


def test_add_birthday(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", birthday="20.11.1990"),
    )

    assert result.message == "Contact created."
    assert db["Joe"] == Record(
        name="Joe", birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date()
    )


def test_add_tags(setup_db):
    tags = {"Hello", "World"}
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", tags=tags),
    )

    assert result.message == "Contact created."
    assert db["Joe"] == Record(name="Joe", tags=tags)


def test_add_notes(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", notes="Hello World"),
    )

    assert result.message == "Contact created."
    assert db["Joe"] == Record(name="Joe", notes="Hello World")


def test_add_all(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(
            command=Actions.ADD,
            name="Joe",
            phones={"1234567890"},
            email="email@example.com",
            birthday="20.11.1990",
            notes="Hello World",
        ),
    )
    assert result.message == "Contact created."

    assert db["Joe"] == Record(
        name="Joe",
        phones={"1234567890"},
        email="email@example.com",
        birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date(),
        notes="Hello World",
    )


def test_duplicates(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe"),
    )
    assert result.message == "Contact created."

    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", phones={"1234567890"}),
    )
    assert result.message == "Contact created."

    records = db.all()
    assert len(records.values()) == 1
    assert db["Joe"] == Record(name="Joe", phones={"1234567890"})