from typing import Any

from rich.console import Console

from cli.app.constants import (
    CLOSE,
    GO_BACK,
    BaseActions,
    ContactActions,
    NoteActions,
    SearchActions,
    SingleContactActions,
    SingleNoteActions,
)
from cli.app.exeptions import ExitException
from cli.app.services import (
    add_note,
    add_phone,
    add_tag,
    base_action,
    change_addresa,
    change_birthday,
    change_email,
    change_name,
    contacts_actions,
    create_new_contact,
    delete_contact,
    delete_note,
    delete_phone,
    delete_tag,
    get_all_contacts,
    get_all_notes,
    get_birthdays_by_duration,
    notes_actions,
    search,
    search_contacts,
    search_notes,
    thanks,
    update_note,
)

console = Console()


actions_map = {
    None: base_action,
    BaseActions.CONTACTS.value: contacts_actions,
    BaseActions.BIRTHDAYS.value: get_birthdays_by_duration,
    BaseActions.NOTES.value: notes_actions,
    BaseActions.SEARCH.value: search,
    BaseActions.THANKS.value: thanks,
    SearchActions.CONTACTS.value: search_contacts,
    SearchActions.NOTES.value: search_notes,
    ContactActions.ALL.value: get_all_contacts,
    ContactActions.ADD.value: create_new_contact,
    SingleContactActions.DELETE.value: delete_contact,
    SingleContactActions.CHANGE_NAME.value: change_name,
    SingleContactActions.CHANGE_EMAIL.value: change_email,
    SingleContactActions.CHANGE_BIRTHDAY.value: change_birthday,
    SingleContactActions.CHANGE_ADDRES.value: change_addresa,
    SingleContactActions.ADD_PHONE.value: add_phone,
    SingleContactActions.DELETE_PHONE.value: delete_phone,
    NoteActions.ADD.value: add_note,
    NoteActions.ALL.value: get_all_notes,
    SingleNoteActions.DELETE.value: delete_note,
    SingleNoteActions.UPDATE.value: update_note,
    SingleNoteActions.ADD_TAG.value: add_tag,
    SingleNoteActions.DELETE_TAG.value: delete_tag,
}


class App:
    __payload: Any = None
    __current_action: str = None

    def __reset(self):
        self.__current_action = None
        self.__payload = None

    def __call__(self):
        if self.__current_action == CLOSE:
            raise ExitException()
        elif self.__current_action == GO_BACK:
            self.__reset()

        if result := actions_map[self.__current_action](self.__payload):
            self.__current_action = result[0]
            self.__payload = result[1]
        else:
            self.__reset()
