from name import Name
from phone import Phone
from birthday import Birthday
from email import Email








class Record:
    def __init__(self, name: Name, birthday: Birthday = None, phone: Phone = None, email: Email = None):
        self.name = name
        self.birthday = birthday
        self.phones = []
        self.emails = []

        if phone:
            self.phones.append(phone)

        if email:
            self.emails.append(email)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p != phone]

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def add_email(self, email: Email):
        self.emails.append(email)

    def change_email(self, old_email, new_email):
        for email in self.emails:
            if email.value == old_email:
                email.value = new_email

    def delete_email(self, email: Email):
        self.emails = [e for e in self.emails if e != email]

    def __str__(self):
        output = ""
        phones = [
            phone.value for phone in self.phones]
        phones = ", ".join(phones) if phones else "N/A"
        birthday = self.birthday.value if self.birthday else "N/A"
        output += f"{self.name.value}: Phones:{phones}, Birthday: {birthday}\n"
        return output