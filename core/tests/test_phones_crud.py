from core import Actions, controller
from core.database import Database, Entities
from core.misc import InfoMessages
from core.models import PhonePayload
from tests.utils import setup_db, setup_test_user

db = Database()
phone_value = "1234567890"
old_phone_value = "123-456-89"


def test_add_phone_number(setup_test_user):
    result = controller(Actions.ADD_PHONE, PhonePayload(name="Joe", phone=phone_value))
    assert result.message == InfoMessages.PHONE_NUMBER_ADDED.value
    assert phone_value in result.value.phones
    assert phone_value in db.select(entity=Entities.CONTACTS, key="Joe").phones


def test_delete_phone_number(setup_test_user):
    controller(Actions.ADD_PHONE, PhonePayload(name="Joe", phone=phone_value))

    result = controller(
        Actions.DELETE_PHONE, PhonePayload(name="Joe", phone=phone_value)
    )
    assert result.message == InfoMessages.PHONE_NUMBER_DELETED.value
    assert phone_value not in result.value.phones
    assert len(db.select(entity=Entities.CONTACTS, key="Joe").phones) == 0


def test_update_phone_number(setup_test_user):
    result = controller(Actions.ADD_PHONE, PhonePayload(name="Joe", phone=phone_value))
    assert result.message == InfoMessages.PHONE_NUMBER_ADDED.value
    assert phone_value in result.value.phones
    assert phone_value in db.select(entity=Entities.CONTACTS, key="Joe").phones

    result = controller(
        Actions.UPDATE_PHONE,
        PhonePayload(name="Joe", phone=phone_value, old_phone=old_phone_value),
    )
    assert result.message == InfoMessages.PHONE_NUMBER_UPDATED.value
    assert phone_value in result.value.phones
    assert old_phone_value not in result.value.phones

    record = db.select(entity=Entities.CONTACTS, key="Joe")
    assert phone_value in record.phones
    assert old_phone_value not in record.phones
