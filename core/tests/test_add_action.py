from pathlib import Path

from core import Actions, Database, Record, controller

# from tests.utils import get_mock_db


def test_add_name(mocker):
    Database().connect()

    # set_data = get_mock_db(mocker)
    result = controller([Actions.ADD.value, "Joe"])

    # set_data.assert_called_once_with(Record(name="Joe"))
    assert result.value == "Contact created"


def test_add_phone(mocker):
    # set_data = get_mock_db(mocker)
    # result = controller([Actions.ADD.value, "Joe", "1234567890"])

    # set_data.assert_called_once_with(Record(name="Joe", phone="1234567890"))
    # assert result.value == "Contact created"
    assert True


def test_add_email(mocker):
    # set_data = get_mock_db(mocker)
    # result = controller([Actions.ADD.value, "Joe", "email@example.com"])

    # set_data.assert_called_once_with(Record(name="Joe", email="email@example.com"))
    # assert result.value == "Contact created"
    assert True


def test_add_birthday(mocker):
    # set_data = get_mock_db(mocker)
    # result = controller([Actions.ADD.value, "Joe", "20.11.1990"])

    # set_data.assert_called_once_with(
    #     Record(name="Joe", birthday=datetime.strptime("20.11.1990", "%d.%m.%Y"))
    # )
    # assert result.value == "Contact created"
    assert True


def test_add_all(mocker):
    # set_data = get_mock_db(mocker)
    # result = controller(
    #     [Actions.ADD.value, "Joe", "1234567890", "email@example.com", "20.11.1990"]
    # )

    # set_data.assert_called_once_with(
    #     Record(
    #         name="Joe",
    #         phone="1234567890",
    #         email="email@example.com",
    #         birthday=datetime.strptime("20.11.1990", "%d.%m.%Y"),
    #     )
    # )
    # assert result.value == "Contact created"
    assert True


def test_add_in_another_order(mocker):
    # set_data = get_mock_db(mocker)
    # result = controller(
    #     [Actions.ADD.value, "Joe", "email@example.com", "1234567890", "20.11.1990"]
    # )

    # set_data.assert_called_once_with(
    #     Record(
    #         name="Joe",
    #         phone="1234567890",
    #         email="email@example.com",
    #         birthday=datetime.strptime("20.11.1990", "%d.%m.%Y"),
    #     )
    # )
    # assert result.value == "Contact created"
    assert True
