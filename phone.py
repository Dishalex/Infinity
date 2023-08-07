import re
from exceptions import PhoneMustBeNumber
from sanytize import sanitize_phone_number


class Phone:
    def __init__(self, value):
        self.value = value
        self._value = value
    
    @property
    def value(self):
         return self._value
    
    #original:
    
    # @value.setter
    # def value(self, value):
    #     if not re.match(r'^\d{11}$', value):
    #         raise PhoneMustBeNumber
    #     self._value = value

    @value.setter
    def value(self, value):
        sanytized_ph = sanitize_phone_number(value)
        if sanytized_ph == None:
            print ('25',f'\nPhone number {value} is hot correct!\nPhone must have 10 or 12 digites!\n')
            raise PhoneMustBeNumber      
        self._value = sanytized_ph
        
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)