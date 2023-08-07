class Name_Error(Exception):
    pass


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
            raise Name_Error("Name must be not less then 3 symbols")
        self.__value = value
