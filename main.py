import re
from record import Record
from name import Name
from phone import Phone
from birthday import Birthday
from adressbook import AdressBook
from rich import print
from rich.table import Table

I = 1

def address_book_commands():
    table_address_book = Table(title='\nALL COMMANDS FOR ADDRESS BOOK:\nImportant!!! All entered data must be devided by gap! Phone number must have 10 or 12 digits!\n * - optional paramiters')
    table_address_book.add_column('COMMAND', justify='left')
    table_address_book.add_column('NAME', justify='left')
    table_address_book.add_column('PHONE NUMBER', justify='letf')
    table_address_book.add_column('E-MAIL', justify='left')
    table_address_book.add_column('BIRTHDAY', justify='left')
    table_address_book.add_column('DESCRIPTION', justify='left')
    table_address_book.add_row('hello', '-', '-', '-', '-', 'Greeting')
    table_address_book.add_row('add', 'Any name ', 'Phone number *', 'E-mail', 'Birthday', 'Add new contact')
    #table.add_row('append', 'Existing name', 'Additional phone number *', '-', 'Append phone number') 
    #table.add_row('delete', 'Existing name', 'Phone to delete *', '-', 'Delete phone number')
    #table.add_row('birthday', 'Existing name', '-', 'YYYY-MM-DD', 'Add birthday')
    #table.add_row('days to birthday', 'Existing name', '-', '-', 'Sow days to birthday')
    #table.add_row('phone', 'Existing name', '-', '-', 'Getting phone number')
    #table.add_row('show all / show all + N', '-', '-', '-', 'Getting Address Book/ N - quantity of records on the page')
    #table.add_row('search + sample', '-', '-', '-', 'searching <<< sumple >>> in address book')
    table_address_book.add_row('good bye / close / exit', '-', '-', '-', '-', 'Exit')
    table_address_book.add_row('help', '-', '-', '-', '-', 'Printing table of commands')
    return table_address_book


def note_book_commands():
    table_note_book = Table(title='\nALL COMMANDS FOR NOTE BOOK:')
    table_note_book.add_column('COMMAND', justify='left')
    table_note_book.add_column('NUNMBER', justify='left')
    table_note_book.add_column('DATA', justify='letf')
    table_note_book.add_column('TAGS', justify='letf')
    table_note_book.add_column('NOTE', justify='left')
    table_note_book.add_column('DESCRIPTION', justify='left')
    table_note_book.add_row('add nout', '-', '-', 'Tags', 'Note')

    return table_note_book


def exit_command(*args):
    #address_book.save_data()
    return '\nGood bye! Have a nice day!\n'


def help_command(*args):
    print (address_book_commands())
    return note_book_commands()


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
    return wrapper


adressbook = AdressBook()

@input_error
def add_record(args):
    if args[0]:
        name = Name(args[0])
        record = Record(name)
    if args[1]:
        birthday = Birthday(args[1][0])
        record = Record(name, birthday)
    if len(args[1]) > 1:
        birthday = Birthday(args[1][0])
        phone = Phone(args[1][1])
        record = Record(name, birthday, phone)
    
    adressbook.add_record(record)
    for rec in adressbook.data.values():
        print(rec)


@input_error
def add_p(args):
    name = args[0]
    
    record = adressbook[name]
    if name in adressbook.data:
        phone = Phone(args[1][0])
        record.add_phone(phone)
    return f"A number {phone.value} has been added to a contact {name}"


@input_error
def change_p(args):
    name = args[0]
    old_phone, new_phone = args[1]

    if name not in adressbook.data:
        return f"You dont have contact with name {name}"
    
    record = adressbook[name]
    
    record.change_phone(old_phone, new_phone)
    for rec in adressbook.data.values():
        print(rec)
    return f"The phone number {old_phone} for contact {name} has been changed to {new_phone}."
    
COMMANDS = {
    add_record: ('add', 'append'),
    change_p: ("change phone", ),
    add_p: ("p",),
    exit_command: ('good bye', 'close', 'exit'),
    help_command: ('help',),

    # phone_comman: ('phone',),
    # delete_phone_command: ('delete',),
    # exit_command: ('good bye', 'close', 'exit'),
    # show_all_command: ('show all',),
    # help_command: ('help',),
    # hello_command: ('hello',),
    # birthday_command: ('birthday',),
    # days_to_birthday_command: ('days to birthday',),
    # search_command: ('search',)
}


def get_user_name(user_info: str) -> tuple:

    regex_name = r'[a-zA-ZА-Яа-я]+'
    user_input_split = user_info.strip().split()
    name_list = []

    for i in user_input_split:
        match_name = re.match(regex_name, i)
        if match_name:
            if len(match_name.group()) == len(i):
                name_list.append(i.capitalize())
                user_info = user_info[match_name.span()[1]:].strip()
                user_data = user_info
            else:
                print(f'\nName <<< {i} >>> is not correct! Try again!')
                user_data = ('', '')
                return user_data
        else:
            break

    user_data = user_data.split()
    if len(name_list) >= 1:
        name = ' '.join(name_list)
    else:
        name = ''
        user_data = []

    return name, user_data


def parser(user_input: str):
    user_input_lower = user_input.lower()
    for command, kwds in COMMANDS.items():
        for kwd in kwds:
            if user_input_lower.startswith(kwd):
                user_info = user_input[len(kwd):].strip()
                return command, user_info

    print('\nUnknown command! Try againe!')
    command = None
    user_info = None
    return command, user_info

@input_error
def main():

    global I
    if I == 1:
        #address_book.load_data()
        print (address_book_commands())
        print (note_book_commands())
        I += 1


    # originale code:
    # while True:

    #     user_input = (input(f'\nEnter command, please!\n\n>>>')).strip()

    #     command, user_info = parser(user_input)

    #     user_data = get_user_name(user_info)

    #     result = command(user_data)
    #     print(result)

    # corrected code for commands without arguments:


    while True:

        user_input = (input(f'\nEnter command, please!\n\n>>>')).strip()

        command, user_info = parser(user_input)
        
        if user_info == "":
            result = command()
        else:
            user_data = get_user_name(user_info)
            result = command(user_data)
            
        print(result)
        if command == exit_command:
            break


if __name__ == "__main__":
    main()
