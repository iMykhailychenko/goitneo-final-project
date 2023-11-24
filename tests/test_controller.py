from app.controller import controller


class TestController:
    def test_controller(self):
        assert controller() is None
