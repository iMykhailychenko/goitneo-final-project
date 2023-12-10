from enum import Enum


class Actions(Enum):
    HELLO = "hello"
    HELP = "help"
    EXIT = "exit"
    CLOSE = "close"
    SEARCH = "search"
    
    ADD = "add_contact"
    DELETE = "delete_contact"
    ALL = "all_contacts"
    
    ADD_PHONE = "add_phone"
    UPDATE_PHONE = "update_phone"
    DELETE_PHONE = "delete_phone"
    
    ADD_BIRTHDAY = "add_birthday"
    GET_BIRTHDAY = "get_birthday"
    DELETE_BIRTHDAY = "delete_birthday"
    UPDATE_BIRTHDAY = "update_birthday"
    BIRTHDAYS = "all_birthdays"
    
    ADD_NOTE = 'add_note'
    DELETE_NOTE = 'delete_note'
    UPDATE_NOTE = 'update_note'
