from functools import wraps

from core.misc.exeptions import InvalidBirthdayError, InvalidNameError, InvalidPhoneError, InvalidEmailError, DatabaseError
from core.models import Response, ResponseType


def validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        message = ""
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            message = "Invalid action." 
        except KeyError:
            message = "User do not exist."
        except IndexError:
            message = "Give me name and phone please."
        except InvalidPhoneError:
            message = "Phone number must be 10 digits long."
        except InvalidNameError:
            message = "Invalid name."
        except InvalidEmailError:
            message = "Invalid email."
        except InvalidBirthdayError:
            message = "Date of birth must be in DD.MM.YYYY format."
        except DatabaseError:
            message = "Database error. Check if path correct."
        except Exception as e:
            print(e)
            message = "Unknown error."
        return Response(value=message, type=ResponseType.ERROR)

    return inner