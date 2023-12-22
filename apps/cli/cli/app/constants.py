from enum import Enum

from core.models import EntitiesType

GO_BACK = "<-  Go back\n"
CLOSE = "⛔️  Close\n"


class BaseActions(Enum):
    CONTACTS = "👥  Manage contacts\n"
    BIRTHDAYS = "🎉  Upcoming birthdays\n"
    SEARCH = "🔎  Search\n"


class ContactActions(Enum):
    ADD = "➕  Create new contact\n"
    ALL = "👀  View all contacts\n"


class SingleContactActions(Enum):
    DELETE = "➖  Delete contact\n"
    UPDATE = "👥  Update contact\n"
    PHONE = "📱  Update phone number\n"


class UpdateContactActions(Enum):
    pass


base = [
    BaseActions.CONTACTS.value,
    BaseActions.BIRTHDAYS.value,
    BaseActions.SEARCH.value,
    CLOSE,
]

contacts = [
    GO_BACK,
    ContactActions.ADD.value,
    ContactActions.ALL.value,
    CLOSE,
]

single_contact = [
    GO_BACK,
    SingleContactActions.DELETE.value,
    SingleContactActions.UPDATE.value,
    SingleContactActions.PHONE.value,
    CLOSE,
]


entities_map = {
    "👥  Search Contacts\n": EntitiesType.CONTACTS,
    "🗒️   Search Notes\n": EntitiesType.NOTES,
}

search_entities = [
    GO_BACK,
    *entities_map.keys(),
    CLOSE,
]
