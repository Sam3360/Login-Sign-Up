import bcrypt

users_database = {}

def sign_up():
    print("\n--- Sign Up ---")
    while True:
        username = input("Choose a username: ").strip()
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        if username in users_database:
            print("That username is already taken. Please choose another.")
        else:
            break

    while True:
        password = input("Choose a password: ").strip()
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        break

    email = input("Enter your email address (optional): ").strip()

    users_database[username] = {
        'password': hashed_password,
        'email': email
    }
    print(f"\nAccount for '{username}' created successfully!")
    print("-----------------\n")

def login():
    print("\n--- Log In ---")
    username_attempt = input("Enter your username: ").strip()
    password_attempt = input("Enter your password: ").strip()

    user_data = users_database.get(username_attempt)

    if user_data and bcrypt.checkpw(password_attempt.encode('utf-8'), user_data['password']):
        print(f"\nWelcome back, {username_attempt}!")
        print("You are now logged in.")
        print("-----------------\n")
        return username_attempt
    else:
        print("\nInvalid username or password. Please try again.")
        print("-----------------\n")
        return None

def show_main_menu():
    print("--- Main Menu ---")
    print("1. Sign Up")
    print("2. Log In")
    print("0. Exit")
    print("-----------------")

def main():
    logged_in_user = None

    while True:
        if logged_in_user:
            print(f"Currently logged in as: {logged_in_user}")
            print("1. Log Out")
            print("0. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                print(f"Logging out {logged_in_user}...")
                logged_in_user = None
            elif choice == '0':
                print("Exiting application. All user data will be lost.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            show_main_menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                sign_up()
            elif choice == '2':
                logged_in_user = login()
            elif choice == '0':
                print("Exiting application. All user data will be lost.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
