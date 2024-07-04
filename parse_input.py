def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2: 
        return "Try again. Add name and phone as parameters"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: {}):
    if len(args) < 2: 
        return "Try again. Add name and phone as parameters"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"change {name} {phone}"
    else:
        return f"contact {name} not found" 

def show_phone(args, contacts):
    if len(args) < 1: 
        return "Try again. Add name as parameter"
    name = args[0]
    if name in contacts:
        return f"{contacts[name]} {name}"
    else:
        return f"contact with name {name} not found"

def show_all(contacts): 
    for key in contacts:
        print(f"{key} {contacts[key]}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        print("type exit or close to exit")

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))           
        elif command == "all":
            show_all(contacts)               
        else:
            print("Invalid command.")

if __name__ == "__main__":
    
    main()
