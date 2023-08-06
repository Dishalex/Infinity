from record import Record
from collections import UserDict
import pickle

class AdressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        #AdressBook.write_data_to_file(self.data)
        self.save_data()
        return f"\nContact <<< {record} >>> added successfully!"


    # def write_data_to_file(self):
    #     file_name = "adress_book.bin"
    #     with open(file_name, "wb") as f:
    #         pickle.dump(self, f)
    #     return f"Data save to file - {file_name}"

    # def load_data_from_file(self):
    #     file_name = "adress_book.bin"
    #     with open(file_name, "rb") as f:
    #         self.data = pickle.load(f)
    #     return f"Data load from file - {file_name}"
    
    def load_data(self):
        try:
            with open('address_book.bin', "rb") as file:
                self.data = pickle.load(file)

        except FileNotFoundError:
            print ('\nAddress book is empty!')
    
    def save_data(self):
  
        with open('address_book.bin', "wb") as file:
            pickle.dump(self.data, file)

    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        self.save_data()
        return f"\nContact <<< {record} >>> added successfully!"
    
    def search_sample(self, sample: str):
        found_records_list = []
        for name, rec in self.data.items():

            if rec.phones != None and rec.phones != []:
                phones = ' '.join(str(p) for p in rec.phones)
            else:
                phones = 'None'
            
            if rec.birthday != None:
                birthday  = str(rec.birthday.value)
            else:
                birthday = 'None'

            user_data_str = f"{name} {phones} {birthday}"
 
            if sample.lower() in user_data_str.lower():
                user_data_dict = {}
                user_data_dict['name'] = name
                user_data_dict['phones'] = phones
                user_data_dict['birthday'] = birthday
                found_records_list.append(user_data_dict)
            else:
                continue
        return found_records_list
    
    def iterator(self, n):

        count = 0
        data_list = []
        for name, record in self.data.items():
            user_data = []
            user_name = name
            if record.birthday != None:
                user_birthday = record.birthday.value
            else:
                user_birthday = 'None'

            phones_str = 'None'
            user_phones_list = []
            user_phones= record.phones

            if record.phones == None or record.phones == [] :
                phones_str = 'None'
            else:
                for phone in user_phones:
                    user_phones_list.append(phone.value)
                phones_str = ' ,'.join(user_phones_list).strip()                
                
            user_data = [user_name, phones_str, user_birthday]
            data_list.append(user_data)
            count += 1
            if count >= n:

                yield data_list
                count = 0
                data_list = []

        if data_list:
            yield data_list

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())