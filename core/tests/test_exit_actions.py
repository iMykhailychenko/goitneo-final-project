from core import Actions, controller


def test_close_and_exit_actions():
    assert controller(Actions.CLOSE) is None
    assert controller(Actions.EXIT) is None
