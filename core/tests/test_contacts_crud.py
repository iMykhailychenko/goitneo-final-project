from datetime import datetime

from core import Actions, controller
from core.database import Database
from core.models import Contact, ContactPayload, EntitiesType
from tests.utils import setup_db, setup_test_user

db = Database()


def test_add_name(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe"),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(id="Joe")


def test_add_phone(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", phones={"1234567890"}),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe", phones={"1234567890"}
    )


def test_add_email(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", email="email@example.com"),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe", email="email@example.com"
    )


def test_add_birthday(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", birthday="20.11.1990"),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe", birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date()
    )


def test_add_all(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(
            name="Joe",
            phones={"1234567890"},
            email="email@example.com",
            birthday="20.11.1990",
        ),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe",
        phones={"1234567890"},
        email="email@example.com",
        birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date(),
    )


def test_duplicates(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe"),
    )

    result = controller(
        Actions.ADD,
        ContactPayload(name="Joe", phones={"1234567890"}),
    )

    records = db.select(entity=EntitiesType.CONTACTS, key="*")
    assert len(records) == 1
    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe", phones={"1234567890"}
    )


def test_update_contact(setup_db):
    result = controller(
        Actions.ADD,
        ContactPayload(
            name="Joe",
            phones={"1234567890"},
            email="email@example.com",
            birthday="20.11.1990",
        ),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe",
        phones={"1234567890"},
        email="email@example.com",
        birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date(),
    )

    controller(
        Actions.UPDATE,
        ContactPayload(
            name="Joe",
            phones={"2345678901", "1234567890"},
            email="joe@example.com",
        ),
    )

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == Contact(
        id="Joe",
        phones={"2345678901", "1234567890"},
        email="joe@example.com",
        birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date(),
    )


def test_all_contacts(setup_db):
    controller(Actions.ADD, ContactPayload(name="Joe", phones={"1234567890"}))
    controller(Actions.ADD, ContactPayload(name="Jane", phones={"0987654321"}))
    final = controller(Actions.ALL).value
    assert len(final) == 2


def test_delete_contact(setup_db):
    result = controller(Actions.ADD, ContactPayload(name="Joe", phones={"1234567890"}))
    controller(Actions.DELETE, ContactPayload(name=result.value.id))

    assert db.select(entity=EntitiesType.CONTACTS, key="Joe") == None


def test_change_name(setup_test_user):
    result = controller(Actions.ALL)

    assert len(result.value) == 1
    assert result.value[0] == Contact(id="Joe")

    controller(Actions.UPDATE, ContactPayload(name="Joe", new_name="Jane"))
    result = controller(Actions.ALL)

    assert len(result.value) == 1
    assert result.value[0] == Contact(id="Jane")
