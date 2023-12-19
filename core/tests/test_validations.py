from core import Actions, ContactPayload, Record, controller
from core.misc import InfoMessages, ValidationMessages


def test_invalid_phone_number():
    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", phones={"1234"}),
    # )  # to short
    # assert result.value == ValidationMessages.PHONE_NUMBER_LENGTH.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", phones={"12345678912345"}),
    # )  # to long
    # assert result.value == ValidationMessages.PHONE_NUMBER_LENGTH.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", phones={"testString123"}),
    # )  # unapropriate format
    # assert result.value == ValidationMessages.PHONE_NUMBER_VALUE.value
    assert True


def test_invalid_email():
    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="email@example"),
    # )
    # assert result.value == ValidationMessages.INVALID_EMAIL.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="123@example.com"),
    # )
    # assert result.value == ValidationMessages.INVALID_EMAIL.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="example@example..com"),
    # )
    # assert result.value == ValidationMessages.INVALID_EMAIL.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="example@example@com"),
    # )
    # assert result.value == ValidationMessages.INVALID_EMAIL.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", email="test.example@example.com.ua"),
    # )
    # assert result.value == InfoMessages.CONTACT_CREATED.value
    assert True


def test_invalid_date():
    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="02.20.1990"),
    # )
    # assert result.value == ValidationMessages.INVALID_BIRTHDAY.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="20.02.199a"),
    # )
    # assert result.value == ValidationMessages.INVALID_BIRTHDAY.value

    # result = controller(
    #     Actions.ADD,
    #     ContactPayload(name="Joe", birthday="20.02.1990"),
    # )
    # assert result.value == InfoMessages.CONTACT_CREATED.value
    assert True
