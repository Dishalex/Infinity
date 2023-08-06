import re
from exceptions import PhoneMustBeNumber
class Phone:
    def __init__(self, value):
        self.value = value
        self._value = value
    
    @property
    def value(self):
         return self._value
    
    @value.setter
    def value(self, value):
        if not re.match(r'^\d{11}$', value):
            raise PhoneMustBeNumber
        self._value = value

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)