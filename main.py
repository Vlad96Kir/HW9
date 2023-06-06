def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found"
        except ValueError:
            return "Invalid input. Please enter the name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter the name and phone number separated by a space."
    return inner


contacts = {}


@input_error
def add_contact(*args):
    if len(args) < 2:
        raise ValueError("Invalid input. Please enter the name and phone number separated by a space.")
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added successfully"


@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"Phone number for contact {name} changed to {phone}"


@input_error
def get_phone(name):
    return f"The phone number for contact {name} is {contacts[name]}"


def show_all_contacts():
    if len(contacts) == 0:
        return "No contacts found"
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result


def execute_command(command):
    command_parts = command.split(" ")
    command_parts[0] = command_parts[0].lower()  # Convert command to lowercase
    if command_parts[0] == "hello":
        return "How can I help you?"
    elif command_parts[0] == "add":
        return add_contact(*command_parts[1:])
    elif command_parts[0] == "change":
        return change_contact(*command_parts[1:])
    elif command_parts[0] == "phone":
        return get_phone(command_parts[1])
    elif command_parts[0] == "show" and command_parts[1] == "all":
        return show_all_contacts()
    elif command_parts[0] in ["good", "bye", "close", "exit"]:
        return "Good bye!"
    else:
        return "Invalid command. Please try again."


def main():
    print("How can I help you?")

    while True:
        command = input("> ")

        result = execute_command(command)
        print(result)

        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
