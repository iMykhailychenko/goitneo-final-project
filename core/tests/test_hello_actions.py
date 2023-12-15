from core import Actions, controller


def test_hello_action():
    assert controller(Actions.HELLO).message == "How can I help you?"
