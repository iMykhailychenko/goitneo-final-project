from enum import Enum
from functools import wraps
from typing import Any, Optional

from pydantic import BaseModel


class ResponseType(Enum):
    SUCCESS = "success"
    ERROR = "error"


class Response(BaseModel):
    message: Optional[str] = None
    value: Optional[Any] = None
    type: ResponseType = ResponseType.SUCCESS


def response(message: Optional[str] = None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return Response(value=func(*args, **kwargs), message=message)

        return inner

    return wrapper
