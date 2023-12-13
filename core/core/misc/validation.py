from functools import wraps

from core.misc.exeptions import InvalidBirthdayError, InvalidNameError, InvalidPhoneError, InvalidEmailError, DatabaseError
from core.models import Response, ResponseType


def validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        error_message = ""
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(e)
            error_message = "Invalid action." 
        except KeyError:
            error_message = "User do not exist."
        except IndexError:
            error_message = "Give me name and phone please."
        except InvalidPhoneError:
            error_message = "Phone number must be 10 digits long."
        except InvalidNameError:
            error_message = "Invalid name."
        except InvalidEmailError:
            error_message = "Invalid email."
        except InvalidBirthdayError:
            error_message = "Date of birth must be in DD.MM.YYYY format."
        except DatabaseError:
            error_message = "Database error. Check if path correct."
        except Exception as e:
            print(e)
            error_message = "Unknown error."
        return Response(message=error_message, type=ResponseType.ERROR)

    return inner