from enum import Enum

from core.models import EntitiesType

GO_BACK = "<-  Go back\n"
CLOSE = "⛔️  Close\n"


class BaseActions(Enum):
    CONTACTS = "👥  Manage contacts\n"
    NOTES = "🗒️   Manage notes\n"
    BIRTHDAYS = "🎉  Upcoming birthdays\n"
    SEARCH = "🔎  Search\n"
    THANKS = "❓  Thanks\n"


class ContactActions(Enum):
    ADD = "➕  Create new contact\n"
    ALL = "👀  View all contacts\n"


class SingleContactActions(Enum):
    DELETE = "⛔️  Delete contact\n"
    CHANGE_NAME = "👥  Change name\n"
    CHANGE_EMAIL = "📧  Change email\n"
    CHANGE_ADDRES = "🏠  Change addres\n"
    CHANGE_BIRTHDAY = "📆  Change birthday\n"
    ADD_PHONE = "📱  Add phone number\n"
    DELETE_PHONE = "📲  Delete phone number\n"


class NoteActions(Enum):
    ADD = "➕  Create new note\n"
    ALL = "👀  View all notes\n"


class SingleNoteActions(Enum):
    UPDATE = "📝  Update note\n"
    DELETE = "⛔️  Delete note\n"
    ADD_TAG = "🏷️  Add tag\n"
    DELETE_TAG = "🏷️  Delete tag\n"


class SearchActions(Enum):
    CONTACTS = "🔎  Search Contacts\n"
    NOTES = "🔎  Search Notes\n"


base = [
    BaseActions.CONTACTS.value,
    BaseActions.NOTES.value,
    BaseActions.BIRTHDAYS.value,
    BaseActions.SEARCH.value,
    BaseActions.THANKS.value,
    CLOSE,
]

contacts = [
    GO_BACK,
    ContactActions.ADD.value,
    ContactActions.ALL.value,
    SearchActions.CONTACTS.value,
]

single_contact = [
    GO_BACK,
    SingleContactActions.DELETE.value,
    SingleContactActions.CHANGE_NAME.value,
    SingleContactActions.CHANGE_EMAIL.value,
    SingleContactActions.CHANGE_ADDRES.value,
    SingleContactActions.ADD_PHONE.value,
    SingleContactActions.DELETE_PHONE.value,
]

notes = [
    GO_BACK,
    NoteActions.ADD.value,
    NoteActions.ALL.value,
    SearchActions.NOTES.value,
]

single_note = [
    GO_BACK,
    SingleNoteActions.DELETE.value,
    SingleNoteActions.UPDATE.value,
    SingleNoteActions.ADD_TAG.value,
    SingleNoteActions.DELETE_TAG.value,
]

search_entities = [
    GO_BACK,
    SearchActions.CONTACTS.value,
    SearchActions.NOTES.value,
]
