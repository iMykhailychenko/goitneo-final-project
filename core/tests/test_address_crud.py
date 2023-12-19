from core import Actions, ContactPayload, Database, controller
from core.misc import InfoMessages
from tests.utils import setup_db, setup_test_user

db = Database().connect()
address_value = "Main Street 15"
new_address_value = "HauptStrasse 22"


def test_add_address(setup_test_user):
    result = controller(
        Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value)
    )
    assert result.message == InfoMessages.ADDRESS_ADDED.value
    assert result.value.address == address_value
    assert db["Joe"].address == address_value


def test_delete_address(setup_test_user):
    controller(Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value))

    result = controller(Actions.DELETE_ADDRESS, ContactPayload(name="Joe"))
    assert result.message == InfoMessages.ADDRESS_DELETED.value
    assert len(result.value.address) == 0
    assert len(db["Joe"].address) == 0


def test_update_address(setup_db):
    result = controller(
        Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value)
    )
    assert result.message == InfoMessages.ADDRESS_ADDED.value
    assert result.value.address == address_value
    assert db["Joe"].address == address_value

    result = controller(
        Actions.UPDATE_ADDRESS, ContactPayload(name="Joe", address=new_address_value)
    )
    assert result.message == InfoMessages.ADDRESS_UPDATTED.value
    assert result.value.address == new_address_value
    assert db["Joe"].address == new_address_value
