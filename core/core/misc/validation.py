from functools import wraps

from core.misc.exeptions import InvalidBirthdayError, InvalidNameError, InvalidPhoneError, DatabaseError


def validation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command."
        except KeyError:
            return "User do not exist."
        except IndexError:
            return "Give me name and phone please."
        except InvalidPhoneError:
            return "Phone number must be 10 digits long."
        except InvalidNameError:
            return "Invalid name."
        except InvalidBirthdayError:
            return "Date of birth must be in DD.MM.YYYY format."
        except DatabaseError:
            return "Database error. Check if path correct."
        except Exception as e:
            return "Unknown error."

    return inner