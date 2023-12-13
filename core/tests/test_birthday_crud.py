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


def test_get_birthdays_this_week(setup_db):
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
    pass


# @patch("app.services.datetime")
# def test_birthdays_this_week(self, mock_date):
#     """Returns records with birthdays in upcoming week"""

#     mock_date.today.return_value.date.return_value = self.mock_date

#     record1, record2 = get_records()
#     record1.add_birthday("07.06.2023")  # Should be shown
#     record2.add_birthday("01.01.2023")  # Should be hidden

#     contacts = AddressBook()
#     contacts.add_contact(record1)
#     contacts.add_contact(record2)

#     result = controller("birthdays", contacts)
#     self.assertEqual(
#         result,
#         "Wednesday: Contact name: Ivan, phones: 1234567890, birthday: 07.06.2023",
#     )

# @patch("app.services.datetime")
# def test_birthdays_in_leap_year(self, mock_date):
#     """Handles leap years properly"""

#     mock_date.today.return_value.date.return_value = self.mock_date

#     record1, record2 = get_records()
#     record1.add_birthday("07.06.1992")  # Leap year
#     record2.add_birthday("08.06.2001")  # Not leap year

#     contacts = AddressBook()
#     contacts.add_contact(record1)
#     contacts.add_contact(record2)

#     result = controller("birthdays", contacts)
#     self.assertEqual(
#         result,
#         "Wednesday: Contact name: Ivan, phones: 1234567890, birthday: 07.06.1992\n"
#         "Thursday: Contact name: Taras, phones: 0987654321, birthday: 08.06.2001",
#     )

# @patch("app.services.datetime")
# def test_multiple_birthdays(self, mock_date):
#     """Returns records with birthdays in upcoming week"""

#     mock_date.today.return_value.date.return_value = self.mock_date

#     record1, record2 = get_records()
#     record1.add_birthday("07.06.2023")
#     record2.add_birthday("07.06.2023")

#     contacts = AddressBook()
#     contacts.add_contact(record1)
#     contacts.add_contact(record2)

#     result = controller("birthdays", contacts)
#     self.assertEqual(
#         result,
#         "Wednesday: Contact name: Ivan, phones: 1234567890, birthday: 07.06.2023; "
#         "Contact name: Taras, phones: 0987654321, birthday: 07.06.2023",
#     )

#     record2.add_birthday("08.06.2023")
#     result = controller("birthdays", contacts)
#     self.assertEqual(
#         result,
#         "Wednesday: Contact name: Ivan, phones: 1234567890, birthday: 07.06.2023"
#         "\nThursday: Contact name: Taras, phones: 0987654321, birthday: 08.06.2023",
#     )
