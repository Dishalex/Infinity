from record import Record
from collections import UserDict
class AdressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
