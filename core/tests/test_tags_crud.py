from core import Actions, Database, TagPayload, controller
from tests.utils import setup_test_user

db = Database().connect()


def test_add_tags(setup_test_user):
    # controller(Actions.ADD_TAG, TagPayload(name="Joe", tag="test"))
    # assert db["Joe"].tags == {"test"}
    pass


def test_delete_tags(setup_test_user):
    # controller(Actions.ADD_TAG, TagPayload(name="Joe", tag="test"))
    # controller(Actions.ADD_TAG, TagPayload(name="Joe", tag="test2"))
    # assert db["Joe"].tags == {"test", "test2"}

    # controller(Actions.DELETE_TAG, TagPayload(name="Joe"))
    # assert db["Joe"].tags == {"test"}
    pass


def test_update_tags(setup_test_user):
    # controller(Actions.ADD_TAG, TagPayload(name="Joe", tag="test"))
    # controller(Actions.UPDATE_TAG, TagPayload(name="Joe", tag="test2"))
    # assert db["Joe"].tags == {"test2"}
    pass
