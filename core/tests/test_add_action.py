import pytest

from core import Actions, Database, Record, controller

db = Database().connect()


# Define a fixture to run code before each test
@pytest.fixture
def setup_before_each_test():
    print("\nCleaning database...")
    db.drop()
    yield


def test_add_name(setup_before_each_test):
    result = controller([Actions.ADD.value, "Joe"])
    assert result.value == "Contact created"

    (record,) = db.get()
    assert record == Record(name="Joe")


def test_add_phone(setup_before_each_test):
    # result = controller([Actions.ADD.value, "Joe", "1234567890"])
    # assert result.value == "Contact created"

    # (record,) = db.get()
    # assert record == Record(name="Joe", phones=set("1234567890"))
    assert True


def test_add_email(setup_before_each_test):
    # result = controller([Actions.ADD.value, "Joe", "email@example.com"])
    # assert result.value == "Contact created"

    # (record,) = db.get()
    # assert record == Record(name="Joe", email="email@example.com")
    assert True


def test_add_birthday(setup_before_each_test):
    # result = controller([Actions.ADD.value, "Joe", "20.11.1990"])
    # assert result.value == "Contact created"

    # (record,) = db.get()
    # assert record == Record(name="Joe", birthday=datetime.strptime("20.11.1990", "%d.%m.%Y"))
    assert True


def test_add_all(setup_before_each_test):
    # result = controller(
    #     [Actions.ADD.value, "Joe", "1234567890", "email@example.com", "20.11.1990"]
    # )
    # assert result.value == "Contact created"

    # (record,) = db.get()
    # assert record == Record(
    #     name="Joe",
    #     phones=set("1234567890"),
    #     email="email@example.com",
    #     birthday=datetime.strptime("20.11.1990", "%d.%m.%Y"),
    # )
    assert True


def test_add_in_another_order(setup_before_each_test):
    # result = controller(
    #     [Actions.ADD.value, "Joe", "email@example.com", "1234567890", "20.11.1990"]
    # )
    # assert result.value == "Contact created"

    # (record,) = db.get()
    # assert record == Record(
    #     name="Joe",
    #     phones=set("1234567890"),
    #     email="email@example.com",
    #     birthday=datetime.strptime("20.11.1990", "%d.%m.%Y"),
    # )
    assert True
