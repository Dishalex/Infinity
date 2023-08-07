from exceptions import EmailException
import re


class Email:
    def __init__(self, value):
        self.value = value
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        try:
            self._value = re.match(r"([A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]+\.[A-Za-z]{2,})|([A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]{2,})",
                value)
        except:
            raise EmailException
