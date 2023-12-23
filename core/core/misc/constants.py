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


class InfoMessages(Enum):
    ADDRESS_ADDED = "Address for contact added."
    ADDRESS_UPDATTED = "Address for contact updated."
    ADDRESS_DELETED = "Address for contact deleted."
    BIRTHDAY_ADDED = "Birthday for contact added."
    BIRTHDAY_DELETED = "Birthday for contact deleted."
    BIRTHDAY_UPDATTED = "Birthday for contact updated."
    NOTE_ADDED = "Note for contact added."
    NOTE_UPDATED = "Note for contact updated."
    PHONE_NUMBER_ADDED = "Phone number for contact added."
    PHONE_NUMBER_DELETED = "Phone number for contact deleted."
    PHONE_NUMBER_UPDATED = '"Phone number for contact updated.'
    NOTE_DELETED = "Note for contact deleted."
    TAG_ADDED = "Tag for contact added."
    TAG_DELETED = "Tag for contact deleted."
    TAG_UPDATED = "Tag for contact updated."


class ValidationMessages(Enum):
    CONTACT_NOT_EXIST = "Contact does not exist."
    INVALID_COMMAND = "Invalid command."
    INVALID_BIRTHDAY = "Date of birth must be in DD.MM.YYYY format."
    INVALID_EMAIL = "Invalid email."
    INVALID_INPUT = "Invalid command. Try again."
    INVALID_NAME = "Invalid name for the Contact."
    INVALID_PARAMETERS = "Give me name and phone please."
    PHONE_NUMBER_LENGTH = "Phone number must be 10 digits long."
    PHONE_NUMBER_VALUE = "Phone number must have only digits and '+' or '-' symbols."
    UNKNOWN_ERROR = "Unknown error."
