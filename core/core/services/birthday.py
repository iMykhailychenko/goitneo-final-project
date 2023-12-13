from typing import Any
from core.models import response, Record


@response()
def get_birthdays_this_week(_: Any):
    return [Record(name="Ttt-1"), Record(name="Ttt-2")]