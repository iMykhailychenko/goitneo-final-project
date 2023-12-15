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


class Constants(Enum):
   #Command messages
    BIRTHDAY_ADDED = "Birthday for contact added."
    CONTACT_ADDED = "Contact added."
    CONTACT_CHANGED = "Contact changed."
    CONTACT_DELETED = "Contact deleted."
    CONTACT_NOT_FOUND = "Contact not found."
    CONTACTS_REMOVED = "Contacts were removed from AddressBook."
    ENTER_COMMAND = "Enter a command: "
    HELP_QUESTION = "How can I help you?"
    HELP_TEXT = """
    These are common commands used in various situations:
    start commands
        hello       Starting command
    set commands 
        add         Adds a new contact with a phone number. Note: takes name and phone number as parameters
        add-        Adds a birthday for existing contact. Note: takes name and birthday in format DD.MM.YYYY 
        birthday    as parameters         
        change      Changes phone number for the concrete contact. Note: takes name and phone number as parameters
        delete      Deletes phone number for the concrete contact. Note: takes name as parameter
        remove      Removes the phone number from the concrete contact. Note: takes name and phone number as parameters
        remove-     Removes all contacts from the AddressBook
        contacts 
               
    get commands
        all         Gets list of all created contacts with phone numbers
        birthdays   Gets birthdays that will happen in the next week
        help        In case you need help with detailed commands names and descriptions
        read        Read the AddressBook that was stored from the latest session
        phone       Gets phone number of the concrete contact. Note: takes a name as a parameter
        show-       Gets birthday of the concrete contact. Note: takes a name as a parameter
        birthday
    
    end commands
        close       Ends the interaction and saves the contacts to the file
        exit        Ends the interaction and saves the contacts to the file
    """
    GOOD_BYE_MESSAGE = "Good bye!"
    PHONE_NUMBER_REMOVED = "Phone number removed."
    PHONE_NUMBER_FOUND = "Phone number found."
    
    #Error messages
    ADDRESS_BOOK_EMPTY = "There is no contacts in the AddressBook to save."
    BIRTHDAY_NOT_EXIST = "There is no birthday for this contact in the AddressBook."
    CONTACT_NOT_EXIST = "Contact do not exist."    
    EOF_ERROR = "End-of-Line Error."
    DATABASE_FILE_NOT_FOUND = "Database error. Check if path correct."
    INVALID_COMMAND = "Invalid command."
    INVALID_BIRTHDAY = "Invalid birthday format. It should have the follovinf format: 'DD.MM.YYYY'."
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
   