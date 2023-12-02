from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


class ResponseType(Enum):
    SUCCESS = 'success'
    ERROR = 'error'


class Response(BaseModel):
    type: ResponseType = ResponseType.SUCCESS
    value: str = ""
    options: Optional[List[str]] = []