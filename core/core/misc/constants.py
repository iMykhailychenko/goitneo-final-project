from enum import Enum


class Actions(Enum):
    SEARCH = "search"

    ADD = "add_contact"
    GET = "get_contact"
    DELETE = "delete_contact"
    UPDATE = "update_contact"
    ALL = "all_contacts"

    ADD_ADDRESS = "add_address"
    DELETE_ADDRESS = "delete_address"
    UPDATE_ADDRESS = "update_address"

    ADD_PHONE = "add_phone"
    UPDATE_PHONE = "update_phone"
    DELETE_PHONE = "delete_phone"

    ADD_BIRTHDAY = "add_birthday"
    GET_BIRTHDAY = "get_birthday"
    DELETE_BIRTHDAY = "delete_birthday"
    UPDATE_BIRTHDAY = "update_birthday"
    BIRTHDAYS = "all_birthdays"

    ALL_NOTES = "all_notes"
    ADD_NOTE = "add_note"
    DELETE_NOTE = "delete_note"
    UPDATE_NOTE = "update_note"

    ADD_TAG = "add_tag"
    DELETE_TAG = "delete_tag"
    UPDATE_TAG = "update_tag"
