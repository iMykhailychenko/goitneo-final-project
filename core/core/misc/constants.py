from enum import Enum


class Actions(Enum):
    EXIT = "exit"
    CLOSE = "close"
    SEARCH = "search"
    
    ADD = "add_contact"
    DELETE = "delete_contact"
    ALL = "all_contacts"
    
    ADD_ADDRESS = 'add_address'
    DELETE_ADDRESS = 'delete_address'
    UPDATE_ADDRESS = 'update_address'
    
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
    
    ADD_TAG = 'add_tag'
    DELETE_TAG = 'delete_tag'
    UPDATE_TAG = 'update_tag'


class CommandMessages(Enum):
    ENTER_COMMAND = "Enter a command: "
    HELP_QUESTION = "How can I help you?"
    GOOD_BYE_MESSAGE = "Good bye!"
    
    
class InfoMessages(Enum):    
    ADDRESS_ADDED = 'Address for contact added.'
    BIRTHDAY_ADDED = "Birthday for contact added."
    BIRTHDAY_DELETED = 'Birthday for contact deleted.'
    BIRTHDAY_UPDATTED = 'Birthday for contact updated.'
    CONTACT_CREATED = "Contact created."
    CONTACT_CHANGED = "Contact changed."
    CONTACT_DELETED = "Contact deleted."
    CONTACT_NOT_FOUND = "Contact not found."
    CONTACTS_REMOVED = "Contacts were removed from AddressBook."
    NOTE_ADDED = "Note for contact added."
    PHONE_NUMBER_REMOVED = "Phone number removed."
    PHONE_NUMBER_FOUND = "Phone number found."
    PHONE_NUMBER_ADDED = 'Phone number added.'
    
    
class ValidationMessages(Enum):
    ADDRESS_BOOK_EMPTY = "There is no contacts in the AddressBook to save."
    BIRTHDAY_NOT_EXIST = "There is no birthday for this contact in the AddressBook."
    CONTACT_NOT_EXIST = "Contact do not exist."    
    EOF_ERROR = "End-of-Line Error."
    DATABASE_FILE_NOT_FOUND = "Database error. Check if path correct."
    INVALID_COMMAND = "Invalid command."
    INVALID_BIRTHDAY = "Date of birth must be in DD.MM.YYYY format."
    INVALID_EMAIL = "Invalid email."
    INVALID_INPUT = "Invalid command. Try again."
    INVALID_NAME = "Invalid name for the Contact."
    INVALID_PARAMETERS = "Give me name and phone please."
    NO_CONTACTS_ADDED = """Contacts have not been added yet. To add a contact, please enter the following command: 
    'add contactName phone', where contactName is the name of contact, and phone is a contact phone number."""
    PHONE_NUMBER_LENGTH = "Phone number must be 10 digits long."
    PHONE_NUMBER_NOT_EXIST = "There is no phone number for this contact in the AddressBook."
    PHONE_NUMBER_VALUE = "Phone number must have only digits and '+' or '-' symbols."
    UNKNOWN_ERROR = "Unknown error."   
