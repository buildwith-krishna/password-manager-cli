# For a safe password
import secrets
# To use characters for passwords
import string

def password_generator(length): # added length parameters
    chars = string.ascii_letters + string.digits + string.punctuation # creates list of characters
    password = "".join(secrets.choice(chars) for i in range(length)) # uses list to generate password
    return password

def main():
    while True:
        print("\n<<-Password_Manager->>")
        print("1. Password generator")
        print("2. Exit\n")

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
            print("Goodbye!")
            break
            
        else:
            print("Invalid input! enter 1 or 2")


if __name__ == "__main__":
    main()
