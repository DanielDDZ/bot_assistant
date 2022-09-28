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


def main():

    commands = {
        'add': add_new_contact,
        'change': change_contact,
        'phone': get_contact_number
    }

    while True:

        user_input = input().lower()

        if user_input == '.':
            break
        elif user_input == 'hello':
            print('How can I help you?')
        elif user_input == 'show all':
            print(contacts)
        elif user_input in ('good bye', 'close', 'exit'):
            print('Good bye!')
            break
        elif user_input.split()[0] in commands:
            test_none = commands[user_input.split()[0]](user_input.split()[1:])
            if test_none is not None:
                print(commands[user_input.split()[0]](user_input.split()[1:]))
        else:
            print(f"I don't know, what is '{user_input}', please, try again:")


if __name__ == "__main__":
    contacts = {}
    main()
