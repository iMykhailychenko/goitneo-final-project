from enum import Enum
from functools import wraps
from typing import List, Optional, Union

from pydantic import BaseModel

from core.models.entities import Entity


class ResponseType(Enum):
    SUCCESS = "success"
    ERROR = "error"


class Response(BaseModel):
    message: Optional[str] = None
    value: Optional[Union[Entity, List[Entity]]] = None
    type: ResponseType = ResponseType.SUCCESS


def response(message: Optional[str] = None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return Response(value=func(*args, **kwargs), message=message)

        return inner

    return wrapper
