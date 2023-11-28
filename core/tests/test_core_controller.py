from app import controller


class TestCoreController:
    def test_core_controller(self):
        assert controller("") == "Invalid command."
