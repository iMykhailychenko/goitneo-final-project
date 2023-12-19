from datetime import date

from core import Actions, Database, Record, SearchPayload, controller
from tests.utils import setup_db

db = Database().connect()


def test_search_by_name(setup_db):
    # db["Joe"] = Record(name="Joe")
    # db["Bill"] = Record(name="Bill")
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="jo")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Joe")
    pass


def test_search_by_phone(setup_db):
    # db["Joe"] = Record(name="Joe", phones={"1111111111"})
    # db["Bill"] = Record(name="Bill", phones={"2222222222"})
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="1111")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Joe", phones={"1111111111"})
    pass


def test_search_by_birthday(setup_db):
    # db["Joe"] = Record(name="Joe", birthday=date(1999, 10, 10))
    # db["Bill"] = Record(name="Bill", birthday=date(1995, 2, 20))
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="20.02.1995")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Bill", birthday=date(1995, 2, 20))
    pass


def test_search_by_email(setup_db):
    # db["Joe"] = Record(name="Joe", email="email@email.com")
    # db["Bill"] = Record(name="Bill", email="test@ukr.net")
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="test@")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Bill", email="test@ukr.net")
    pass


def test_search_by_tags(setup_db):
    # db["Joe"] = Record(name="Joe", tags={"tags", "test"})
    # db["Bill"] = Record(name="Bill", tags={"tags"})
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="test")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Joe", tags={"test"})
    pass


def test_search_by_note(setup_db):
    # db["Joe"] = Record(name="Joe", note="test")
    # db["Bill"] = Record(name="Bill", note="note")
    # result = controller(
    #     Actions.SEARCH,
    #     SearchPayload(value="test")
    # )
    # assert len(result.value) == 1
    # assert result.value[0] == Record(name="Joe", note="test")
    pass
