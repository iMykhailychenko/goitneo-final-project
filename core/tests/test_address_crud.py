from core import Actions, controller
from core.database import Database, Entities
from core.misc import InfoMessages
from core.models import ContactPayload
from tests.utils import setup_db, setup_test_user

db = Database()
address_value = "Main Street 15"
new_address_value = "HauptStrasse 22"


def test_add_address(setup_test_user):
    result = controller(
        Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value)
    )
    assert result.message == InfoMessages.ADDRESS_ADDED.value
    assert result.value.address == address_value
    assert db.select(entity=Entities.CONTACTS, key="Joe").address == address_value


def test_delete_address(setup_test_user):
    controller(Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value))

    result = controller(Actions.DELETE_ADDRESS, ContactPayload(name="Joe"))
    assert result.message == InfoMessages.ADDRESS_DELETED.value
    assert len(result.value.address) == 0
    assert len(db.select(entity=Entities.CONTACTS, key="Joe").address) == 0


def test_update_address(setup_test_user):
    result = controller(
        Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value)
    )
    assert result.message == InfoMessages.ADDRESS_ADDED.value
    assert result.value.address == address_value
    assert db.select(entity=Entities.CONTACTS, key="Joe").address == address_value

    result = controller(
        Actions.UPDATE_ADDRESS, ContactPayload(name="Joe", address=new_address_value)
    )
    assert result.message == InfoMessages.ADDRESS_UPDATTED.value
    assert result.value.address == new_address_value
    assert db.select(entity=Entities.CONTACTS, key="Joe").address == new_address_value
