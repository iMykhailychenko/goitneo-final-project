from datetime import datetime

from pytest import fixture

from core import Actions, Database, Input, Record, controller

db = Database().connect()


# Define a fixture to run code before each test
@fixture
def setup_before_each_test():
    print("\nCleaning database...")
    db.drop()
    yield


def test_add_name(setup_before_each_test):
    input = Input(command=Actions.ADD, name="Joe")
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(name="Joe")


def test_add_phone(setup_before_each_test):
    input = Input(command=Actions.ADD, name="Joe", phones={"1234567890"})
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(name="Joe", phones={"1234567890"})


def test_add_email(setup_before_each_test):
    input = Input(command=Actions.ADD, name="Joe", email="email@example.com")
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(name="Joe", email="email@example.com")


def test_add_birthday(setup_before_each_test):
    input = Input(command=Actions.ADD, name="Joe", birthday="20.11.1990")
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(
        name="Joe", birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date()
    )


def test_add_tags(setup_before_each_test):
    tags = {"Hello", "World"}
    input = Input(command=Actions.ADD, name="Joe", tags=tags)
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(name="Joe", tags=tags)


def test_add_notes(setup_before_each_test):
    input = Input(command=Actions.ADD, name="Joe", notes="Hello World")
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(name="Joe", notes="Hello World")


def test_add_all(setup_before_each_test):
    input = Input(
        command=Actions.ADD,
        name="Joe",
        phones={"1234567890"},
        email="email@example.com",
        birthday="20.11.1990",
        notes="Hello World",
    )
    result = controller(input)
    assert result.value == "Contact created."

    (record,) = db.get()
    assert record == Record(
        name="Joe",
        phones={"1234567890"},
        email="email@example.com",
        birthday=datetime.strptime("20.11.1990", "%d.%m.%Y").date(),
        notes="Hello World",
    )
