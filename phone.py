import re

class Phone:
    def __init__(self, value):
        self.value = value
    #     self._value = value
    
    # @property
    # def value(self):
    #     return self._value
    
    # @value.setter
    # def value(self, value):
    #     if not re.match(r'^\d{11}$', value):
    #         raise ValueError
    #     self._value = value