import re
import datetime
class Birthday:
    def __init__(self, value):
        self.value = value
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        try:
            self._value = datetime.strptime(value, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Format birthday must be YYYY/mm/dd")
