from pathlib import Path


def total_salary(path):
    path = Path(path)
    total = 0
    count = 0

    if not path.exists():  
        raise FileNotFoundError("File not found")


    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as salaries:
                for line in salaries:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
        except Exception as e:
            return f'Error {e}'
    
    average = total // count if count > 0 else 0 
    return total, average
            
total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# # ////////////////////////////////////////////////////////

def get_cats_info(path):
    path = Path(path)
    count = 0
    cats_list = []
    
    if not path.exists():  
        raise FileNotFoundError("File not found")

    if path.exists():
        try: 
            with open(path, 'r', encoding='utf-8') as cats:
                for line in cats:
                    id, name, age = line.strip().split(',')
                    cat = {'id': id, 'name': name, 'age': age }
                    cats_list.append(cat)
            return cats_list
        except Exception as e:
            return f'Error {e}'

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)


# /////////////////////////////////////////////////////////////

from colorama import Fore, init
import sys
from pathlib import Path
init(autoreset=True)
directory_path = Path(sys.argv[1])


def print_directory_structure(directory: Path, level: int = 0):
    
    if not directory.exists():
        print(Fore.RED + f"{directory} - no such dir")
        return
    if not directory.is_dir():
        print(Fore.RED + f"{directory} - no such dir")
        return

    for item in directory.iterdir():
        if item.is_dir():
            print("  " * level + Fore.BLUE + f" {item.name}")
            
            print_directory_structure(item, level + 1)
        elif item.is_file():
            print("  " * level + Fore.GREEN + f" {item.name}")


print_directory_structure(directory_path)

# /////////////////////////////////////////////
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2: 
        return 'Not enough info'
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_phone(args, contacts):
    if len(args) < 2: 
        return 'Not enough info'
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
    return 'Contact phone number was changed'

def show_user_phone(args, contacts):
    if not args:  
        return "No name provided."
    name = args[0]  
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == 'phone':
            print(show_user_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

