from datetime import date

from core import (
    Actions,
    AllBirthdaysPayload,
    BirthdayPayload,
    ContactPayload,
    Database,
    controller,
)
from tests.utils import setup_db, setup_test_user

db = Database().connect()
mock_today = date(2023, 6, 6)  # Tuesday, not a leap year
mock_new_day = date.today()


def get_date_str(value: date) -> str:
    return value.strftime("%d.%m.%Y")


def test_add_birthday(setup_test_user):
    assert db["Joe"].birthday is None

    controller(
        Actions.ADD_BIRTHDAY,
        BirthdayPayload(name="Joe", birthday=get_date_str(mock_today)),
    )
    assert db["Joe"].birthday == mock_today


def test_delete_birthday(setup_test_user):
    controller(
        Actions.ADD_BIRTHDAY,
        BirthdayPayload(name="Joe", birthday=get_date_str(mock_today)),
    )

    result = controller(
        Actions.DELETE_BIRTHDAY,
        BirthdayPayload(name="Joe"),
    )
    assert result.value is None
    assert db["Joe"].birthday is None


def test_update_birthday(setup_db):
    controller(
        Actions.ADD,
        ContactPayload(name="Joe", birthday=get_date_str(mock_today)),
    )
    assert db["Joe"].birthday == mock_today

    controller(
        Actions.UPDATE_BIRTHDAY,
        BirthdayPayload(name="Joe", birthday=get_date_str(mock_new_day)),
    )
    assert db["Joe"].birthday == mock_new_day


def test_get_birthdays_by_duration(mocker, setup_db):
    fixed_date = date(2023, 6, 7)
    mocker.patch("core.services.birthday.date", mocker.Mock(today=lambda: fixed_date))

    # Date in duratin days - should be shown
    controller(
        Actions.ADD,
        ContactPayload(name="Bill", birthday="17.06.2023"),
    )
    # Current week - should be shown
    controller(
        Actions.ADD,
        ContactPayload(name="John", birthday="07.06.2023"),
    )
    # Date in 11 days - should be hidden
    controller(
        Actions.ADD,
        ContactPayload(name="Joe", birthday="18.06.2023"),
    )
    # Date in past - should be hidden
    controller(
        Actions.ADD,
        ContactPayload(name="Bob", birthday="01.01.2023"),
    )

    result = controller(Actions.BIRTHDAYS, AllBirthdaysPayload(day_amount="10"))

    assert len(result.value) == 2
    assert result.value[0].birthday == date(2023, 6, 7)
    assert result.value[1].birthday == date(2023, 6, 17)


def test_get_birthdays_with_leap_year(mocker, setup_db):
    fixed_date = date(2023, 6, 7)
    mocker.patch("core.services.birthday.date", mocker.Mock(today=lambda: fixed_date))

    # Leap year
    controller(
        Actions.ADD,
        ContactPayload(name="Joe", birthday="07.06.1992"),
    )
    # Not leap year
    controller(
        Actions.ADD,
        ContactPayload(name="Bob", birthday="08.06.2001"),
    )

    result = controller(Actions.BIRTHDAYS, AllBirthdaysPayload())

    assert len(result.value) == 2
    assert result.value[0].birthday == date(1992, 6, 7)
    assert result.value[1].birthday == date(2001, 6, 8)
