from core import Actions, ContactPayload, Database, PhonePayload, controller
from core.misc import InfoMessages
from tests.utils import setup_db, setup_test_user

db = Database().connect()
phone_value = "1234567890"
old_phone_value = "123-456-89"


def test_add_phone_number(setup_test_user):
    result = controller(Actions.ADD_PHONE, PhonePayload(name="Joe", phone=phone_value))
    assert result.message == InfoMessages.PHONE_NUMBER_ADDED.value
    assert phone_value in result.value.phones
    assert phone_value in db["Joe"].phones


def test_delete_phone_number(setup_test_user):
    # controller(Actions.DELETE_PHONE, ContactPayload(name="Joe", phones={phone_value}))

    # result = controller(Actions.DELETE_ADDRESS, ContactPayload(name="Joe"))
    # assert result.message == InfoMessages.ADDRESS_DELETED.value
    # assert phone_value not in result.value.phones
    # assert len(db["Joe"].phones) == 0
    pass


def test_update_address(setup_db):
    result = controller(Actions.ADD_PHONE, PhonePayload(name="Joe", phone=phone_value))
    assert result.message == InfoMessages.PHONE_NUMBER_ADDED.value
    assert phone_value in result.value.phones
    assert phone_value in db["Joe"].phones

    result = controller(
        Actions.UPDATE_PHONE,
        PhonePayload(name="Joe", phone=phone_value, old_phone=old_phone_value),
    )
    assert result.message == InfoMessages.PHONE_NUMBER_UPDATED.value
    assert phone_value in result.value.phones
    assert old_phone_value not in result.value.phones
    assert phone_value in db["Joe"].phones
    assert old_phone_value not in db["Joe"].phones
