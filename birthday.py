from exceptions import BirthdayException
from datetime import datetime, date


class Birthday:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            self._value = datetime.strptime(value, "%Y/%m/%d")
        except:
            raise BirthdayException

    def __str__(self) -> str:
        if self._value:
            return self._value.strftime("%d-%m-%Y")

    def __repr__(self) -> str:
        return str(self)
