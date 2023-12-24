from functools import wraps

from core.misc.constants import ValidationMessages
from core.misc.exeptions import (
    InvalidBirthdayError,
    InvalidEmailError,
    InvalidNameError,
    InvalidPhoneError,
    InvalidPhoneLengthError,
    ValidationErrors,
)
from core.models import Response, ResponseType


def validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        error_message = ""
        try:
            return func(*args, **kwargs)
        except ValueError:
            error_message = ValidationMessages.INVALID_INPUT
        except KeyError:
            error_message = ValidationMessages.CONTACT_NOT_EXIST
        except IndexError:
            error_message = ValidationMessages.INVALID_PARAMETERS
        except InvalidPhoneLengthError:
            error_message = ValidationMessages.PHONE_NUMBER_LENGTH
        except InvalidPhoneError:
            return ValidationMessages.PHONE_NUMBER_VALUE
        except InvalidNameError:
            error_message = ValidationMessages.INVALID_NAME
        except InvalidEmailError:
            error_message = ValidationMessages.INVALID_EMAIL
        except InvalidBirthdayError:
            error_message = ValidationMessages.INVALID_BIRTHDAY
        except ValidationErrors as validation_errors:
            individual_errors = validation_errors.errors
            error_messages = []

            for error in individual_errors:
                if type(error) == InvalidNameError:
                    error_messages.append(ValidationMessages.INVALID_NAME.value)
                elif type(error) == InvalidEmailError:
                    error_messages.append(ValidationMessages.INVALID_EMAIL.value)
                elif type(error) == InvalidPhoneError:
                    error_messages.append(ValidationMessages.PHONE_NUMBER_VALUE.value)
                elif type(error) == InvalidBirthdayError:
                    error_messages.append(ValidationMessages.INVALID_BIRTHDAY.value)
            error_message = "\n".join(error_messages)

        except Exception:
            error_message = ValidationMessages.UNKNOWN_ERROR
        return Response(message=error_message, type=ResponseType.ERROR)

    return inner
