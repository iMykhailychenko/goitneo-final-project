from pytest import fixture

from core import Actions, ContactPayload, Database, controller

db = Database()


@fixture
def setup_db():
    print("\nCleaning database...")
    db.drop()


@fixture
def setup_test_user():
    print("\nCleaning database...")
    db.drop()

    print("\nCreating mock user...")
    controller(Actions.ADD, ContactPayload(name="Joe"))
