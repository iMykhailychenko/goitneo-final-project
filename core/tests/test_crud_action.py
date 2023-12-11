from datetime import datetime

from pytest import fixture

from core import Actions, Database, Input, Record, controller

db = Database().connect()


# Define a fixture to run code before each test
@fixture
def setup_before_each_test():
    print("\nCleaning database...")
    db.drop()
    yield


def test_delete_action(setup_before_each_test):
    pass
