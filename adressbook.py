from record import Record
from collections import UserDict
import pickle

class AdressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        AdressBook.write_data_to_file(self.data)


    def write_data_to_file(self):
        file_name = "adress_book.bin"
        with open(file_name, "wb") as f:
            pickle.dump(self, f)
        return f"Data save to file - {file_name}"

    def load_data_from_file(self):
        file_name = "adress_book.bin"
        with open(file_name, "rb") as f:
            self.data = pickle.load(f)
        return f"Data load from file - {file_name}"