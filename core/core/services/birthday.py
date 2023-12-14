from typing import Any
from datetime import date
from core.models import response, Record


@response()
def get_birthdays_this_week(_: Any):
    birthday = date.today()
    return [Record(name="Ttt-1", birthday=birthday)]