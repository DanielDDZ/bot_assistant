def input_error(func):
    def inner(user_string):
        try:
            result = func(user_string)
            return result
        except KeyError:
            print('Enter user name:')
        except ValueError:
            print('Enter correct type:')
        except IndexError:
            print('Give me name and phone please:')

    return inner


@input_error
def add_new_contact(new_contact):
    contacts[new_contact[0]] = new_contact[1]
    return f'A new contact has been added. Name: "{new_contact[0]}" Number: "{new_contact[1]}"'


@input_error
def change_contact(contact):
    contacts[contact[0]] = contact[1]
    return f'The contact has been changed. Name: "{contact[0]}" New number: "{contact[1]}"'


@input_error
def get_contact_number(name_contact):
    return f'Name: {name_contact[0]} Number: {contacts[name_contact[0]]}'


@input_error
def quit_func(quit_command):
    return f'Good bye!'


@input_error
def hello_func(hello_command):
    return f"Hello! How can I help you?"


@input_error
def show_all_func(show_all_command):
    return f'All contacts: \n{contacts}'


def main():

    commands = {
        'add': add_new_contact,
        'change': change_contact,
        'phone': get_contact_number,
        'hello': hello_func,
        'show all': show_all_func,
        'good bye': quit_func,
        'close': quit_func,
        'exit': quit_func,
    }

    print('Bot-assistant here...')

    while True:

        user_input = input().lower()
        if user_input == '.':
            break

        if user_input.split()[0] in commands:
            test_none = commands[user_input.split()[0]](user_input.split()[1:])

            if test_none is not None:
                print(commands[user_input.split()[0]](user_input.split()[1:]))

                if commands[user_input.split()[0]](user_input.split()[1:]) == "Good bye!":
                    break

        elif user_input in commands:
            print(commands[user_input](user_input))

        else:
            print(
                f"Sorry, i don't know, what is '{user_input}', please, try again:")


if __name__ == "__main__":
    contacts = {}
    main()
