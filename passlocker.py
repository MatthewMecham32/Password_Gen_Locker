import hashlib
import getpass
#from passgen import auto_generate_password

password_manager = {}

def create_account(username,password):
    if username != "" and password != "":
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_manager[username] = hashed_password
        print("Account created successfully!")
    else:
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        password_manager[username] = hashed_password
        print("Account created successfully!")
        main()

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(f"Usernames and passwords: {password_manager}")
    if username in password_manager and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main(): 
    while True:
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        username = ""
        password = ""
        if choice == '1':
            create_account(username,password)
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()