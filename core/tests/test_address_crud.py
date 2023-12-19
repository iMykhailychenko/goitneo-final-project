from core import Actions, ContactPayload, Database, controller
from tests.utils import setup_db, setup_test_user

db = Database().connect()
address_value = "Main Street 15"
new_address_value = "HauptStrasse 22"


def test_add_address(setup_test_user):
    assert db["Joe"].birthday is None

    controller(Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value))
    assert db["Joe"].address == address_value


def test_delete_address(setup_test_user):
    # controller(Actions.ADD_ADDRESS, ContactPayload(name="Joe", address=address_value))

    # result = controller(Actions.DELETE_ADDRESS, ContactPayload(name="Joe"))
    # assert result.value.address is None
    # assert db["Joe"].address is None
    pass


def test_update_address(setup_db):
    # controller(Actions.ADD, ContactPayload(name="Joe", address=address_value))
    # assert db["Joe"].address == address_value

    # controller(
    #     Actions.UPDATE_BIRTHDAY, ContactPayload(name="Joe", address=new_address_value)
    # )
    # assert db["Joe"].address == new_address_value
    pass
