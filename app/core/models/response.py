from enum import Enum
from pydantic import BaseModel


class ResponseType(Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class Response(BaseModel):
    type: ResponseType
    value: str