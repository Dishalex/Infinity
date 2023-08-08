from name import Name
from phone import Phone
from birthday import Birthday
from email_class import Email




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
        self.phones = [p for p in self.phones if p.value != phone.value]

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                phone.value = new_phone.value
                break

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def add_email(self, email: Email):
        self.emails.append(email)

    def change_email(self, old_email: Email, new_email: Email):
        for email in self.emails:
            if email.value == old_email.value:
                email.value = new_email.value

    def delete_email(self, email: Email):
        self.emails = [e for e in self.emails if e.value != email.value]

    def __str__(self):
        output = ""
        phones = [phone.value for phone in self.phones]
        phones = ", ".join(phones) if phones else "N/A"
        emails = [email.value for email in self.emails]
        emails = ", ".join(emails) if emails else "N/A"
        birthday = self.birthday.value if self.birthday else "N/A"
        output += f"{self.name.value}: Phones:{phones}, E-mails: {emails}, Birthday: {str(birthday)}\n"
        return output
