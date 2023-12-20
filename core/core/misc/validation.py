from functools import wraps

from core.misc.constants import ValidationMessages
from core.misc.exeptions import (
    InvalidBirthdayError,
    InvalidEmailError,
    InvalidNameError,
    InvalidPhoneError,
    InvalidPhoneLengthError,
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
        except EOFError:
            return ValidationMessages.EOF_ERROR
        except Exception:
            error_message = ValidationMessages.UNKNOWN_ERROR
        return Response(message=error_message, type=ResponseType.ERROR)

    return inner
