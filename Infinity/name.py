from Infinity.exceptions import Name_Error


class Name:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) < 3:
            raise Name_Error
        self.__value = value
