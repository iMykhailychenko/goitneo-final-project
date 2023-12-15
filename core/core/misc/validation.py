from functools import wraps

from core.misc import (InvalidBirthdayError, InvalidNameError, InvalidPhoneError, InvalidPhoneLengthError,
                                InvalidEmailError, DatabaseError, ValidationMessages)
from core.models import Response, ResponseType


def validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        error_message = ""
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
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
        except DatabaseError:
            error_message = ValidationMessages.DATABASE_FILE_NOT_FOUND
        except EOFError:
            return ValidationMessages.EOF_ERROR
        except Exception as e:
            print(e)
            error_message = ValidationMessages.UNKNOWN_ERROR
        return Response(message=error_message, type=ResponseType.ERROR)

    return inner