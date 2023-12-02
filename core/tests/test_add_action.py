from core import Actions, Database, Record, Response, controller


def test_add_name(mocker):
    db = Database()
    set_data = mocker.patch.object(db, "set_data")

    # Add new contact by name.
    result = controller([Actions.ADD.value, "Joe"])
    set_data.assert_called_once_with(Record(name="Joe"))

    assert result.value == "Contact created"