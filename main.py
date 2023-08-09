import re
from record import Record
from email_class import Email
from address_class import Address
from name import Name, Name_Error
from phone import Phone
from birthday import Birthday
from address_book import AdressBook
from rich import print
from rich.table import Table
from exceptions import PhoneMustBeNumber, BirthdayException, EmailException, Name_Error
from sort_folder import sort

I = 1

address_book = AdressBook()

def sort_folder_command(args):
    return sort()

def address_book_commands():
    table_address_book = Table(
        title="\nALL COMMANDS FOR ADDRESS BOOK:\nImportant!!! All entered data must be devided by gap! Phone number must have 10 or 12 digits!\n * - optional paramiters")
    table_address_book.add_column("COMMAND", justify="left")
    table_address_book.add_column("NAME", justify="left")
    table_address_book.add_column("PHONE NUMBER", justify="left")
    table_address_book.add_column("EMAIL", justify="left")
    table_address_book.add_column("BIRTHDAY", justify="left")
    table_address_book.add_column("ADDRESS", justify="left")
    table_address_book.add_column("DESCRIPTION", justify="left")
    table_address_book.add_row(
        "hello / hi", "-", "-", "-", "-", "-", "Greeting")
    table_address_book.add_row("add / add record", "Any name", "Phone number *",
                               "Email *", "YYYY/MM/DD *", "-", "Add new contact")
    table_address_book.add_row("add phone / append / ap", "Existing name",
                               "Additional phone number", "-", "-", "-", "Add phone numbere")
    table_address_book.add_row("change phone / cph", "Existing name",
                               "Old phone number + new phone number", "-", "-", "-", "Change phone numbere")
    table_address_book.add_row("delete phone / del phone / dph", 'Existing name',
                               'Phone nunber to delete *', "-", "-", "-", "Delete phone number")
    table_address_book.add_row(
        "add birthday / ab", 'Existing name', "-", "-", "YYYY-MM-DD", "-", "Add birthday")
    # table.add_row('days to birthday', 'Existing name', '-', '-', 'Sow days to birthday')
    # table.add_row('phone', 'Existing name', '-', '-', 'Getting phone number')
    table_address_book.add_row('show all / show all + N', '-', '-', '-',
                               '-', 'Getting Address Book/ N - quantity of records on the page')
    table_address_book.add_row(
        'search + sample', '-', '-', '-', '-', 'searching <<< sumple >>> in address book')
    table_address_book.add_row(
        'good bye / close / exit', '-', '-', '-', '-', 'Exit')
    table_address_book.add_row(
        'help', '-', '-', '-', '-', 'Printing table of commands')
    return table_address_book


def note_book_commands():
    table_note_book = Table(title='\nALL COMMANDS FOR NOTE BOOK:')
    table_note_book.add_column('COMMAND', justify='left')
    table_note_book.add_column('NUNMBER', justify='left')
    table_note_book.add_column('DATA', justify='letf')
    table_note_book.add_column('TAGS', justify='letf')
    table_note_book.add_column('NOTE', justify='left')
    table_note_book.add_column('DESCRIPTION', justify='left')
    table_note_book.add_row('add note', '-', '-', 'Tags', 'Note')

    return table_note_book


def exit_command(args):
    address_book.save_data()
    return '\nGood bye! Have a nice day!\n'


def help_command(args):
    print(address_book_commands())
    return note_book_commands()


def show_all_command(args):

    if len(address_book.data) == 0:
        return '\nAddress Book is empty!'

    n = 10
    k = 1

    if len(args[1]) > 0:

        try:
            n = int(args[1][0])
        except ValueError:
            print(
                f'\nEnterd number <<< {args[0]} >>> of pages does not represent a valid integer!\nDefault number of records N = {n} is used')

    for block in address_book.iterator(n):

        table = Table(title=f"\nADDRESS BOOK page {k}")
        table.add_column("Name", justify="left")
        table.add_column("Phone number", justify="left")
        table.add_column("Email", justify="left")
        table.add_column("Birthday", justify="left")
        table.add_column("Address", justify="left")
        for item in block:
            table.add_row(str(item[0]), str(item[1]), str(
                item[2]), str(item[3]), str(item[4]))
        print(table)
        k += 1

        if len(block) == n:
            input("\nTo see next page press any key:\n>>>")

    return "End of address book."


def search_command(args):

    sample_name = args[0]
    if args[1] != []:
        sample_data = args[1][0]
    else:
        sample_data = ""

    sample = sample_name + sample_data

    if sample == '':
        return "\nMissing sample for search!"

    found_records_list = address_book.search_sample(sample)

    if len(found_records_list) > 0:

        table = Table(
            title=f"\nALL FOUND RECORDS ACCORDING TO SAMPLE <<< {sample} >>>")
        table.add_column("Name", justify='left')
        table.add_column("Phone number", justify="left")
        table.add_column("Email", justify="left")
        table.add_column("Birthday", justify="left")
        table.add_column("Address", justify="left")

        for item in found_records_list:
            table.add_row(item["name"], item["phones"],
                          item["emails"], item['birthday'], item["address"])
        return table
    else:
        return f"\nThere is now any record according to sample <<< {sample} >>>"


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Invalid command. Please try again."
        except ValueError:
            return "Error: Invalid input format. Please try again."
        except IndexError:
            return "Error: Contact not found. Please try again."
        except PhoneMustBeNumber:
            return "Phone must have 10 or 12 digits!"
        except BirthdayException:
            return "Format birthday must be YYYY/MM/DD"
        except EmailException:
            return "incorrect email"
        except Name_Error:
            return ("Enter name at least 3 symbols")
        except TypeError:
            return "Format birthday must be YYYY/MM/DD"
    return wrapper


@input_error
def add_record(args: tuple[str]) -> str:
    name = Name(args[0])
    birthday = phone = email = address = None
    for i in args[1]:
        try:
            phone = Phone(i)
            continue
        except Exception:
            pass

        try:
            email = Email(i)
            continue
        except Exception:
            pass

        try:
            birthday = Birthday(i)
            continue
        except Exception:
            pass

    if args[2]:
        address = Address(args[2])

    rec: Record = address_book.get(str(name))
    if rec:
        return f'Record with name {str(name)} is already in address book'
    return address_book.add_record(Record(name, birthday, phone, email, address))


@input_error
def delete_record_command(args):
    try:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"

        record = address_book[name]
        address_book.delete_record(record)

        return f"\nContact {name} has been deleted successfully!"

    except:
        raise ValueError


@input_error
def add_phone_command(args):

    if len(args) == 2 and len(args[1]) == 1:
        name = args[0]
        record = address_book[name]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        phone = Phone(args[1][0])
        record.add_phone(phone)
        return f"A number {phone.value} has been added to a contact {name}"

    else:
        raise ValueError


@input_error
def change_phone_command(args):

    if len(args) == 2 and len(args[1]) == 2:
        name = args[0]
        old_phone, new_phone = args[1]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        o_phone = Phone(old_phone)
        n_phone = Phone(new_phone)
        record = address_book[name]
        record.change_phone(o_phone, n_phone)
        return f"The phone number {old_phone} for contact {name} has been changed to {new_phone}."
    else:
        raise ValueError


@input_error
def add_birthday_command(args):
    if len(args) == 2 and len(args[1]) == 1:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        birthday = Birthday(args[1][0])
        record = address_book[name]
        if record.birthday:
            return f"Contact with name {name} already has a date of birth"
        record.add_birthday(birthday)
        return f"Birthday to contact {name} has been added"
    else:
        raise ValueError


@input_error
def days_to_birthday_command(args):
    day = int(args[1][0])
    list_bd = ''
    for key, value in address_book.items():
        rec = address_book.get(str(key))
        result = rec.check_cont_birthday(day)
        if result:
            list_bd += f'Contact {key}: birthday through {result} days \n'
    return list_bd.strip()


@input_error
def delete_phone_command(args):
    if len(args) == 2 and len(args[1]) == 1:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        phone = Phone(args[1][0])
        record = address_book[name]
        record.delete_phone(phone)
        return f"For contact {name} phone {phone.value} has been deleted"

    else:
        raise ValueError


@input_error
def add_email_command(args):
    if len(args) == 2 and len(args[1]) == 1:
        name = args[0]
        record = address_book[name]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        email = Email(args[1][0])
        record.add_email(email)
        return f"Email for contact {name} has been added"
    else:
        raise ValueError


@input_error
def change_email_command(args):
    if len(args) == 2 and len(args[1]) == 2:
        name = args[0]
        old_email, new_email = args[1]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        o_email = Email(old_email)
        n_email = Email(new_email)
        record = address_book[name]
        record.change_email(o_email, n_email)
        return f"The email {old_email} for contact {name} has been changed to {new_email}."
    else:
        raise ValueError


@input_error
def delete_email_command(args):
    if len(args) == 2 and len(args[1]) == 1:
        name = args[0]
        if name not in address_book.data:
            return f"You dont have contact with name {name}"
        email = Email(args[1][0])
        record = address_book[name]
        record.delete_email(email)
        return f"For contact {name} email {email.value} has been deleted"

    else:
        raise ValueError


def no_command(args) -> str:
    return 'Unknown command'


def hello_command(args) -> str:
    return 'How can I help you?'


@input_error
def add_address(args):
    name = Name(args[0])
    rec: Record = address_book.get(str(name))
    if not rec:
        return f'No record with name {name}'
    return rec.add_address(Address(args[2]))


@input_error
def delete_address_command(args):
    name = Name(args[0])
    rec: Record = address_book.get(str(name))
    if not rec:
        return f'No record with name {name}'
    return rec.delete_address()


COMMANDS = {
    add_record: ("add record",),
    add_address: ("add address", "change address"),
    change_phone_command: ("change phone",),
    add_phone_command: ("add phone",),
    exit_command: ("good bye", "close", "exit",),
    help_command: ("help",),
    delete_phone_command: ("delete phone",),
    add_birthday_command: ("add birthday",),
    show_all_command: ("show all",),
    search_command: ("search",),
    hello_command: ("hello", 'hi',),
    add_email_command: ("add email",),
    change_email_command: ("change email",),
    delete_email_command: ("delete email",),
    delete_record_command: ("delete record", "remove"),
    delete_address_command: ("delete address", "remove address"),
    days_to_birthday_command: ("days to birthday", "dtb",),
    sort_folder_command: ("sort",)
}

def get_user_name(user_info: str) -> tuple:

    regex_name = r'[a-zA-ZА-Яа-я]+'
    name = ''
    user_address = ''
    address_separator = ':'
    if address_separator in user_info:
        data = user_info.split(address_separator)
        user_info_list = data[0].strip().split()
        user_address = data[1].strip()
    else:
        user_info_list = user_info.strip().split()

    if user_info:
        while user_info_list:
            word = user_info_list[0]
            match_name = re.match(regex_name, word)
            if match_name and len(match_name.group()) == len(word):
                name = name + word + ' '
                user_info_list.remove(word)
            else:
                break

    return name.strip(), user_info_list, user_address


def parser(user_input: str):
    user_info = ''
    user_input_lower = user_input.lower()
    for command, kwds in COMMANDS.items():
        for kwd in kwds:
            if user_input_lower.startswith(kwd):
                user_info = user_input[len(kwd):].strip()
                return command, user_info

    command = no_command
    return command, user_info


def main():

    global I
    if I == 1:
        address_book.load_data()
        print(address_book_commands())
        print(note_book_commands())
        I += 1

    while True:
        user_input = (input(f'\nEnter command, please!\n\n>>>')).strip()

        command, user_info = parser(user_input)

        user_data = get_user_name(user_info)

        result = command(user_data)
        print(result)

        if command == exit_command:
            break


if __name__ == "__main__":
    main()
