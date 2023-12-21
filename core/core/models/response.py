from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel
from functools import wraps

from core.models.record import Record


class ResponseType(Enum):
    SUCCESS = "success"
    ERROR = "error"


class Response(BaseModel):
    message: Optional[str] = None
    value: Union[List[Record], Record, None] = None
    type: ResponseType = ResponseType.SUCCESS


def response(message: Optional[str] = None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return Response(value=result, message=message)

        return inner

    return wrapper
