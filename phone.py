import re
from exceptions import PhoneMustBeNumber
from sanytize import sanitize_phone_number


class Phone:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    # original:

    # @value.setter
    # def value(self, value):
    #     if not re.match(r'^\d{11}$', value):
    #         raise PhoneMustBeNumber
    #     self._value = value

    @value.setter
    def value(self, value):
        sanytized_ph = sanitize_phone_number(value)
        if sanytized_ph == None:
            raise PhoneMustBeNumber
        self.__value = sanytized_ph

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    phone = Phone("+3805512-12-123")
    print(phone.value)
