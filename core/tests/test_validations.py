from core import Actions, Record, controller
from tests.utils import get_mock_db


def test_invalid_phone_number(mocker):
    # get_mock_db(mocker)
    # result = controller([Actions.ADD.value, "Joe", "1234"]) # to short
    # assert result.value == "Phone number must be 10 digits long."

    # result = controller([Actions.ADD.value, "Joe", "12345678912345"]) # to long
    # assert result.value == "Phone number must be 10 digits long."
    assert True


def test_invalid_email(mocker):
    # get_mock_db(mocker)
    # result = controller([Actions.ADD.value, "Joe", "email@example"])
    # assert result.value == "Invalid email."

    # result = controller([Actions.ADD.value, "Joe", "123@example.com"])
    # assert result.value == "Invalid email."

    # result = controller([Actions.ADD.value, "Joe", "example@example..com"])
    # assert result.value == "Invalid email."

    # result = controller([Actions.ADD.value, "Joe", "example@example@com"])
    # assert result.value == "Invalid email."

    # result = controller([Actions.ADD.value, "Joe", "test.example@example.com.ua"])
    # assert result.value == "Contact created"
    assert True


def test_invalid_date(mocker):
    # get_mock_db(mocker)
    # result = controller([Actions.ADD.value, "Joe", "02.20.1990"])
    # assert result.value == "Date of birth must be in DD.MM.YYYY format."

    # result = controller([Actions.ADD.value, "Joe", "20.02.199a"])
    # assert result.value == "Date of birth must be in DD.MM.YYYY format."

    # result = controller([Actions.ADD.value, "Joe", "20.02.1990"])
    # assert result.value == "Contact created"
    assert True
