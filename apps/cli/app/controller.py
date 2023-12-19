from rich.console import Console
from app.services import contacts_actions, base_action, create_new_contact, get_all_contacts
from app.constants import BaseActions, CLOSE, ContactActions, GO_BACK
from app.exeptions import ExitException

console = Console()
current_action = None


actions_map = {
    None: base_action,
    BaseActions.CONTACTS.value: contacts_actions,
    BaseActions.BIRTHDAYS.value: lambda *_: None,
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

