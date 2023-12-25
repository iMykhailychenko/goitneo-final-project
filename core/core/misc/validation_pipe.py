from functools import wraps

from core.misc.exeptions import ValidationError
from core.misc.messages import ValidationMessages
from core.models.response import Response, ResponseType


def validation_pipe(func):
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
        except ValidationError as e:
            error_message = str(e)
        except Exception as e:
            error_message = str(e) or ValidationMessages.UNKNOWN_ERROR.value
        return Response(message=error_message, type=ResponseType.ERROR)

    return inner
