import re
from record import Record
from name import Name
from phone import Phone
from birthday import Birthday
from adressbook import AdressBook
adressbook = AdressBook()

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
    
    print(args)

    
    adressbook.add_record(record)
    print(adressbook.data)

COMMANDS = {
    add_record: ('add', 'append'),
    # phone_command: ('phone',),
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


def main():


    while True:

        user_input = (input(f'\nEnter command, please!\n\n>>>')).strip()

        command, user_info = parser(user_input)

        user_data = get_user_name(user_info)

        result = command(user_data)
        print(result)

        


if __name__ == "__main__":
    main()
