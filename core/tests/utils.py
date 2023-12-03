from core import Database


def get_mock_db(mocker):
    db = Database()
    return mocker.patch.object(db, "set_data")
