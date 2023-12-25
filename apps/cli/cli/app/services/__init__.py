from cli.app.services.base import base_action
from cli.app.services.birthday import change_birthday, get_birthdays_by_duration
from cli.app.services.contacts import (
    change_addresa,
    change_email,
    change_name,
    contacts_actions,
    create_new_contact,
    delete_contact,
    get_all_contacts,
)
from cli.app.services.notes import (
    add_note,
    delete_note,
    get_all_notes,
    notes_actions,
    update_note,
)
from cli.app.services.phone import add_phone, delete_phone, update_phone
from cli.app.services.search import search, search_contacts, search_notes
from cli.app.services.tags import add_tag, delete_tag
from cli.app.services.thanks import thanks
