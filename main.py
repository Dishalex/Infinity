import re
import os


# команди помічника
class Handler():
    def handle_hello(self):
        pass

    def handle_show_all(self):
        pass

    def handle_show_phones(self):
        pass

    def handle_show_bday(self):
        pass

    def handle_d2b(self):
        pass

    def handle_add(self):
        pass

    def handle_change(self):
        pass

    def handle_delete(self):
        pass

    def handle_search(self):
        pass

    def handle_exit(self):
        exit()


# словник команд та їх скорочених назв
COMMANDS = {
    Handler.handle_hello: ('hello', 'hi'),
    Handler.handle_show_all: ('sa', 'show all'),
    Handler.handle_show_phones: ('sp', 'show phones' 'phones'),
    Handler.handle_show_bday: ('sb', 'show bday', 'birthday'),
    Handler.handle_d2b: ('d2b', 'sd2b', 'show days to birthday'),
    Handler.handle_add: ('a', 'add'),
    Handler.handle_change: ('c', 'e', 'change', 'edit'),
    Handler.handle_delete: ('d', 'del', 'delete'),
    Handler.handle_search: ('s', 'sn', 'sp', 'search', 'search name', 'search phone'),
    Handler.handle_exit: ('q', 'quit', 'close', 'exit')
}


# функція очищення екрану
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# парсер команд
def parse_input(input_string: str):

    # ініціалізація змінних для зберігання результатів парсингу
    parsed_command = None
    parsed_name = None
    parsed_birthday = None
    parsed_phones = []

    # пошук команд помічника у рядку, введеному користувачем
    words = input_string.strip().split()
    for word in words:
        for command, aliases in COMMANDS.items():
            if word.lower() in map(str.lower, aliases):
                parsed_command = command
                words.remove(word)
                break

    # класифікація аргументів
    for word in words:
        # пошук name
        if re.match(r'^[a-zA-Z]+$', word):
            parsed_name = word
        # пошук birthday
        elif re.match(r'^\d{4}/\d{2}/\d{2}$', word):
            parsed_birthday = word
        # пошук phones
        elif re.match(r'^\d{11}$', word):
            parsed_phones.append(word)

    # повернення відсортованих аргументів
    return parsed_command, parsed_name, parsed_birthday, parsed_phones


def main():
    try:
        # безкінечний цикл для вводу данних:
        while True:
            user_input = input("[i] CTRL+C to exit\n>>> ")
            parsed_command, parsed_name, parsed_birthday, parsed_phones = parse_input(
                user_input)

            clear_screen()
            # якщо команда допустима парсер її аналізує і виводить результат на екран
            if parsed_command:
                print(
                    f"[i] <Debug> cmd: {parsed_command.__name__} name: {parsed_name}, bday: {parsed_birthday}, phones: {parsed_phones}")
            # в іншому разі, буде запропоновано повторно ввести команду
            else:
                print('[-] Try again')
    except:
        KeyError
    finally:
        print('\n[+] Arrivederci :)')


if __name__ == "__main__":
    main()
