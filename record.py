from name import Name
from phone import Phone
from birthday import Birthday
from email_class import Email
from datetime import datetime
from address_class import Address


class Record:
    def __init__(self, name: Name, birthday: Birthday = None, phone: Phone = None, email: Email = None, address: Address = None):
        self.name = name
        self.birthday = birthday
        self.phones = []
        self.emails = []
        self.address = address

        if phone:
            self.phones.append(phone)

        if email:
            self.emails.append(email)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p.value != phone.value]

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                phone.value = new_phone.value
                break

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def check_cont_birthday(self, days):
        if self.birthday:
            birth = self.birthday.value
            current_date = datetime.now()
            next_birth = datetime(current_date.year, birth.month, birth.day)
            if next_birth < current_date:
                next_birth = datetime(current_date.year + 1,
                                      birth.month, birth.day)
            day_for_birth = next_birth - current_date
            if (int(day_for_birth.days)+1) < days:
                return day_for_birth.days + 1
        return None

    def add_email(self, email: Email):
        self.emails.append(email)

    def change_email(self, old_email: Email, new_email: Email):
        for email in self.emails:
            if email.value == old_email.value:
                email.value = new_email.value

    def delete_email(self, email: Email):
        self.emails = [e for e in self.emails if e.value != email.value]

    def add_address(self, address: Address):
        self.address = address

    def change_address(self, old_address: Address, new_address: Address):
        if address.value == old_address.value:
            address.value = new_address.value

    def delete_address(self):
        if self.address:
            self.address = ''
