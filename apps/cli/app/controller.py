from rich.console import Console

from app.constants import CLOSE, GO_BACK, BaseActions, ContactActions
from app.exeptions import ExitException
from app.services import (
    base_action,
    contacts_actions,
    create_new_contact,
    get_all_contacts,
    get_birthdays_by_duration,
)

console = Console()
current_action = None


actions_map = {
    None: base_action,
    BaseActions.CONTACTS.value: contacts_actions,
    BaseActions.BIRTHDAYS.value: get_birthdays_by_duration,
    BaseActions.SEARCH.value: lambda *_: None,
    BaseActions.ALL.value: get_all_contacts,
    ContactActions.ADD.value: create_new_contact,
    ContactActions.DELETE.value: lambda *_: None,
    ContactActions.UPDATE.value: lambda *_: None,
}


class Controller:
    __current_action = None

    def __call__(self):
        if self.__current_action == CLOSE:
            self.__current_action = None
            raise ExitException()
        elif self.__current_action == GO_BACK:
            self.__current_action = None

        self.__current_action = actions_map[self.__current_action]()
