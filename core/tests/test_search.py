from datetime import datetime

from core import Actions, SearchPayload, Database, Record, controller
from tests.utils import setup_test_user

db = Database().connect()


def test_search_by_name(setup_test_user):
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="jo")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Joe")
    pass
