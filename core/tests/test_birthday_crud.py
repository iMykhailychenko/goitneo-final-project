from datetime import date

from core import Actions, BirthdayPayload, ContactPayload, Database, controller
from tests.utils import setup_db, setup_test_user

db = Database().connect()
mock_today = date(2023, 6, 6)  # Tuesday, not a leap year


def get_date_str(value: date) -> str:
    return value.strftime("%d.%m.%Y")


def test_add_and_get_birthday(setup_test_user):
    # assert db["Joe"].birthday is None

    # controller(
    #     Actions.ADD_BIRTHDAY,
    #     BirthdayPayload(name="Joe", birthday=get_date_str(mock_today)),
    # )
    # assert db["Joe"].birthday == mock_today

    # result = controller(
    #     Actions.GET_BIRTHDAY,
    #     BirthdayPayload(name="Joe"),
    # )
    # assert result.value == mock_today
    pass


def test_delete_birthday(setup_test_user):
    # controller(
    #     Actions.ADD_BIRTHDAY,
    #     BirthdayPayload(name="Joe", birthday=get_date_str(mock_today)),
    # )

    # controller(
    #     Actions.DELETE_BIRTHDAY,
    #     BirthdayPayload(name="Joe"),
    # )

    # result = controller(
    #     Actions.GET_BIRTHDAY,
    #     BirthdayPayload(name="Joe"),
    # )
    # assert result.value is None
    # assert db["Joe"].birthday is None
    pass


def test_update_birthday(setup_db):
    # controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday=get_date_str(mock_today)),
    # )
    # assert db["Joe"].birthday == mock_today

    # controller(
    #     Actions.DELETE_BIRTHDAY,
    #     BirthdayPayload(name="Joe"),
    # )

    # result = controller(
    #     Actions.GET_BIRTHDAY,
    #     BirthdayPayload(name="Joe"),
    # )
    # assert result.value is None
    # assert db["Joe"].birthday is None
    pass


def test_get_birthdays_this_week(mocker, setup_db):
    # fixed_date = date(2023, 6, 7)
    # mocker.patch('core.services.birthday.date', mocker.Mock(today=lambda: fixed_date))

    # # Current week - should be shown
    # controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="07.06.2023"),
    # )
    # # Date in past - should be hidden
    # controller(
    #     Actions.ADD,
    #     ContactPayload(name="Bob", birthday="01.01.2023"),
    # )
    # # Date in future - should be hidden
    # controller(
    #     Actions.ADD,
    #     ContactPayload(name="Bill", birthday="12.06.2023"),
    # )

    # result = controller(Actions.BIRTHDAYS)

    # assert len(result) == 1
    # assert result[0].birthday == date(2023, 6, 7)
    pass


def test_get_birthdays_with_leap_year(mocker, setup_db):
    # fixed_date = date(2023, 6, 7)
    # mocker.patch('core.services.birthday.date', mocker.Mock(today=lambda: fixed_date))

    # # Leap year
    # controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="07.06.1992"),
    # )
    # # Not leap year
    # controller(
    #     Actions.ADD,
    #     ContactPayload(name="Bob", birthday="08.06.2001"),
    # )

    # result = controller(Actions.BIRTHDAYS)

    # assert len(result) == 2
    # assert result[0].birthday == date(1992, 6, 7)
    # assert result[1].birthday == date(2001, 6, 8)
    pass
