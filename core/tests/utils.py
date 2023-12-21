from pathlib import Path

from pytest import fixture

from core import Actions, controller
from core.database import Database
from core.models import ContactPayload

DB_PATH = Path(__file__).parent / "tmp"
db = Database().connect(DB_PATH)


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
