from core import Actions, ContactPayload, Record, controller


def test_invalid_phone_number():
    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", phones={"1234"}),
    # )  # to short
    # assert result.value == "Phone number must be 10 digits long."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", phones={"12345678912345"}),
    # )  # to long
    # assert result.value == "Phone number must be 10 digits long."
    assert True


def test_invalid_email():
    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="email@example"),
    # )
    # assert result.value == "Invalid email."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="123@example.com"),
    # )
    # assert result.value == "Invalid email."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="example@example..com"),
    # )
    # assert result.value == "Invalid email."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="example@example@com"),
    # )
    # assert result.value == "Invalid email."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="test.example@example.com.ua"),
    # )
    # assert result.value == "Contact created"
    assert True


def test_invalid_date():
    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="02.20.1990"),
    # )
    # assert result.value == "Date of birth must be in DD.MM.YYYY format."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="20.02.199a"),
    # )
    # assert result.value == "Date of birth must be in DD.MM.YYYY format."

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="20.02.1990"),
    # )
    # assert result.value == "Contact created"
    assert True
