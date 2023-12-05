from enum import Enum
from typing import List
from pydantic import BaseModel


class ResponseType(Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class Response(BaseModel):
    value: str = ""
    options: List[str] = []
    type: ResponseType = ResponseType.SUCCESS