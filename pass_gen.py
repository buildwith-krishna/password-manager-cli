#Contains the passwords 
FILE_NAME = "passwords.json"
# for storage use case
import json
# For a safe password
import secrets
# To use characters for passwords
import string

def password_generator(length): # added length parameters
    chars = string.ascii_letters + string.digits + string.punctuation # creates list of characters
    password = "".join(secrets.choice(chars) for i in range(length)) # uses list to generate password
    return password


def add_password():

    service = input("Enter service: ").strip()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if service == "" or username == "" or password == "":
        print("Entry cannot be empty!")
        return

    try:
        with open(FILE_NAME, "r") as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}

    passwords[service] = {
        "Username" : username,
        "Password": password,
        "Category" : "Personal"
    }

    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)

    print("<<-Password_Saved_Successfully->>")

def show_passwords():
    key = input("Enter master key: ").strip()
    if key == "8989@key":
        with open(FILE_NAME, "r") as file:
            passwords = json.load(file)

        for service, details in passwords.items():
            print(f"\nService: {service}")
            print(f" Username: {details['Username']}")
            print(f" Password: {details['Password']}")
            print(f" Category: {details['Category']}")
            print("\n")
    else:
        print("Invalid master Key! cannot give you access!.")

            
def main():
    while True:
        print("\n<<-Password_Manager->>")
        print("1. Password generator")
        print("2. Add a password")
        print("3. View all passwords")
        print("4. Exit\n")

        user = input("Enter task: ").strip()

        # To get password based on inputs
        if user == "1":
            try:
                length = int(input("Enter password length: ").strip()) 
                if length <= 0:
                    print("Length cannot be negative or zero!")
                    continue
                password = password_generator(length) # added length parameters
                print(f"\nGenerated Password: {password}")
            except ValueError:
                print("Please enter a valid number.")

        elif user == "2":
            add_password()
            print("\n")

        elif user == "3":
            show_passwords()

        elif user == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid input! enter 1 or 4")


if __name__ == "__main__":
    main()

