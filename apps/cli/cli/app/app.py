from typing import Any

from rich.console import Console

from cli.app.constants import (
    CLOSE,
    GO_BACK,
    BaseActions,
    ContactActions,
    SingleContactActions,
)
from cli.app.exeptions import ExitException
from cli.app.services import (
    base_action,
    contacts_actions,
    create_new_contact,
    delete_contact,
    get_all_contacts,
    get_birthdays_by_duration,
    search,
    update_contact,
)

console = Console()


actions_map = {
    None: base_action,
    BaseActions.CONTACTS.value: contacts_actions,
    BaseActions.BIRTHDAYS.value: get_birthdays_by_duration,
    BaseActions.SEARCH.value: search,
    ContactActions.ALL.value: get_all_contacts,
    ContactActions.ADD.value: create_new_contact,
    SingleContactActions.DELETE.value: delete_contact,
    SingleContactActions.UPDATE.value: update_contact,
}


class App:
    __payload: Any = None
    __current_action: str = None

    def __call__(self):
        if self.__current_action == CLOSE:
            self.__current_action = None
            raise ExitException()
        elif self.__current_action == GO_BACK:
            self.__current_action = None
            self.__payload = None

        result = actions_map[self.__current_action](self.__payload)
        if result:
            self.__current_action = result[0]
            self.__payload = result[1]
        else:
            self.__current_action = None
            self.__payload = None
