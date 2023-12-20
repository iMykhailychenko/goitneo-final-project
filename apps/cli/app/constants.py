from enum import Enum

GO_BACK = "<-  Go back\n"
CLOSE = "⛔️  Close\n"


class BaseActions(Enum):
    CONTACTS = "👥  Manage contacts\n"
    BIRTHDAYS = "🎉  Upcoming birthdays\n"
    ALL = "👀  View all contacts\n"
    SEARCH = "🔎  Search\n"


class ContactActions(Enum):
    ADD = "➕  Create new contact\n"
    DELETE = "➖  Delete contact\n"
    UPDATE = "👥  Update contact\n"


class UpdateContactActions(Enum):
    pass


base = [
    BaseActions.CONTACTS.value,
    BaseActions.BIRTHDAYS.value,
    BaseActions.ALL.value,
    BaseActions.SEARCH.value,
    CLOSE,
]

contacts = [
    ContactActions.ADD.value,
    ContactActions.DELETE.value,
    ContactActions.UPDATE.value,
    GO_BACK,
    CLOSE,
]
