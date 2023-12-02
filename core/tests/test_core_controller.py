from core import Actions, Database, controller
from pathlib import Path

DB_FOLDER_PATH = Path("./tmp")


class TestCoreController:
    def test_add_contact(self):
        db = Database()
        db.connect(DB_FOLDER_PATH)

        # Add new contact by name.
        controller([Actions.ADD.value, "Joe"])
        data = db.get_data()

        # Add new contact with phone
        controller([Actions.ADD.value, "Joe2", "1234567890"])

        # Add new contact with email
        controller([Actions.ADD.value, "Joe2", "example@example.com"])

        # Add new contact with email
        controller([Actions.ADD.value, "Joe2", "example@example.com"])

        assert True