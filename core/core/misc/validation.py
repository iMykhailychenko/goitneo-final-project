from functools import wraps

from core.misc.exeptions import (InvalidBirthdayError, InvalidNameError, InvalidPhoneError, InvalidPhoneLengthError,
                                InvalidEmailError, DatabaseError)
from core.misc.constants import Constants
from core.models import Response, ResponseType


def validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        error_message = ""
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
            error_message = Constants.INVALID_INPUT
        except KeyError:
            error_message = Constants.CONTACT_NOT_EXIST
        except IndexError:
            error_message = Constants.INVALID_PARAMETERS
        except InvalidPhoneLengthError:
            error_message = Constants.PHONE_NUMBER_LENGTH
        except InvalidPhoneError:
            return Constants.PHONE_NUMBER_VALUE
        except InvalidNameError:
            error_message = Constants.INVALID_NAME
        except InvalidEmailError:
            error_message = Constants.INVALID_EMAIL
        except InvalidBirthdayError:
            error_message = Constants.INVALID_BIRTHDAY
        except DatabaseError:
            error_message = Constants.DATABASE_FILE_NOT_FOUND
        except EOFError:
            return Constants.EOF_ERROR
        except Exception as e:
            print(e)
            error_message = Constants.UNKNOWN_ERROR
        return Response(message=error_message, type=ResponseType.ERROR)

    return inner