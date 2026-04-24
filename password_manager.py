from cryptography.fernet import Fernet
import base64, hashlib


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


def add_password(f):

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
        "Password" : f.encrypt(password.encode()).decode(),
        "Category" : "Personal"
    }

    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)

    print("<<-Password_Saved_Successfully->>")

def show_passwords(f):
    with open(FILE_NAME, "r") as file:
        passwords = json.load(file)

    for service, details in passwords.items():
        print(f"\nService: {service}")
        print(f" Username: {details['Username']}")
        decrypted = f.decrypt(details['Password'].encode()).decode()
        print(f" Password: {decrypted}")
        print(f" Category: {details['Category']}")
        print("\n")


def del_password(f): 
    show_passwords(f)
    with open(FILE_NAME, "r") as file:
        passwords = json.load(file)

    service = input("Enter service to delete: ").strip()

    if service in passwords:
        choice = input("Are you sure, to continue (y/n) ").strip().lower()
        if choice != "n":
            del passwords[service]

            with open(FILE_NAME, "w") as file:
                json.dump(passwords, file, indent=4)
                
            print("<<-Password has been deleted->>")
        else:
            return
    elif service == "":
        print("service cannot be empty!")

    else:
        print("this service does not exists!")


def update_password(f):
    show_passwords(f)
    with open(FILE_NAME, "r") as file:
        passwords = json.load(file)

    service = input("Enter service: ").strip()
    if service == "":
        print("Srvice cannot be empty!")
        return

    if service in passwords:
        username = input("Enter new username: ").strip()
        password = input("Enter new password: ").strip()
    
        if username != "" and password != "":
            passwords[service] = {
                "Username" : username,
                "Password": f.encrypt(password.encode()).decode(),
                "Category" : "Personal"
            }

            with open(FILE_NAME, "w") as file:
                json.dump(passwords, file, indent=4)

            print("<<-Password has been updated->>\n")

        else:
            print("Entry cannot be empty!")
            return
    else:
        print("This service does not exist!")
        return


def search_password(f):
    with open(FILE_NAME, "r") as file:
        passwords = json.load(file)

    service = input("Enter service: ").strip()

    if service != "":
        if service in passwords:
            details = passwords[service]
            print(f"\nService: {service}")
            print(f" Username: {details['Username']}")
            decrypted = f.decrypt(details['Password'].encode()).decode()
            print(f" Password: {decrypted}")
            print(f" Category: {details['Category']}")
        else:
            print("Service does not exist!")
    else:
        print("Service can't be empty!")


def get_key(master_key):
    key = hashlib.sha256(master_key.encode()).digest()
    key = base64.urlsafe_b64encode(key)
    return Fernet(key)


def main():
    master_key = input("Enter master key: ").strip()
    if master_key != "8989@master_key":
        print("Incorrect Key! Two attempts left.")
        
        master_key = input("Enter master key: ").strip()
        if master_key != "8989@master_key":
            print("Incorrect Key! Only 1 attempt left.")

            master_key = input("Enter master key: ").strip()
            if master_key != "8989@master_key":
                print("Incorrect Key! Cannot proceed further.")
                return
                
    if master_key == "8989@master_key":
        f = get_key(master_key)
        while True:
            print("\n## Password_Manager ##")
            print("1. Password generator")
            print("2. Add a password")
            print("3. View all passwords")
            print("4. Delete a password")
            print("5. Update a password")
            print("6. Search a password")
            print("7. Exit\n")

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
                add_password(f)
                print("\n")

            elif user == "3":
                show_passwords(f)
                print("\n")

            elif user == "4":
                del_password(f)
                print("\n")

            elif user == "5":
                update_password(f)

            elif user == "6":
                search_password(f)
            
            elif user == "7":
                print("Goodbye!\n")
                break
            
            else:
                print("Invalid input! enter 1 to 7")

    else:
        print("Invalid master key! Access denied!")
        return
        
if __name__ == "__main__":
    main()

