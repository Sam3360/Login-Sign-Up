Simple Console Authentication System
This is a basic, console-based Python application that provides a fundamental user sign-up and login experience. It incorporates password hashing using the bcrypt library to demonstrate a crucial step in securing user credentials.

This project is intended for educational purposes only to illustrate core authentication concepts.

IMPORTANT: SECURITY AND DATA WARNINGS!

⚠️ NO DATA PERSISTENCE:

All user accounts created are stored only in memory (RAM). This means that all user data will be permanently lost every time the application is closed. This system does not save any data to a file or database.


⚠️ NOT SECURE FOR REAL-WORLD USE:

While this application uses bcrypt for password hashing (a strong security practice), it is NOT designed or secure enough for any real-world application, production environment, or for handling sensitive user data. Key limitations include:

Lack of Persistence: Data loss on exit.

No Rate Limiting/Account Lockout: An attacker can attempt unlimited logins, making brute-force attacks on weak passwords possible.

No Password Complexity Checks: Users can choose simple, easily guessable passwords.

Passwords Visible During Input: Passwords are echoed to the console as you type them.

No Other Security Measures: Lacks comprehensive security features like Two-Factor Authentication (2FA), secure session management, proper error logging, or protection against common web vulnerabilities (if it were a web app).

Local-Only: Designed for a single user on a single machine; no network security considerations.

DO NOT use this code for any application that requires real security or handles any sensitive information.

Features
User Sign-Up: Allows new users to create an account by choosing a unique username and password.

User Login: Enables existing users to authenticate with their credentials.

Password Hashing: Utilizes the bcrypt library to securely hash and store passwords, preventing them from being stored in plain text.

In-Memory Storage: All user data (usernames, hashed passwords, and optional emails) are stored in your computer's memory.

Requirements
Python 3.x

bcrypt library

Installation
Install Python: If you don't have Python installed, download it from python.org.

Install bcrypt: Open your terminal or command prompt (not the Python interactive interpreter >>>) and run:

pip install bcrypt

How to Run the Application
Save the Code: Copy the entire Python code into a file named auth_login_system.py.

Open Your Terminal/Command Prompt: Navigate to the directory where you saved auth_login_system.py using the cd command.

Example (Windows): cd C:\Users\YourUser\Documents\my_projects

Example (macOS/Linux): cd ~/Documents/my_projects

Run the Script: Execute the Python script using the command:

python auth_login_system.py

How to Use
When you run the script, you will see a main menu:

--- Main Menu ---
1. Sign Up
2. Log In
0. Exit
-----------------
Enter your choice:

Sign Up:

Choose option 1.

Enter a unique username and a password.

Set an optional email address.

Your account will be created (in memory).

Log In:

Choose option 2.

Enter your registered username and password.

If successful, you will be logged in. If not, you'll receive an "Invalid username or password" message.

Log Out:

Once logged in, the menu will change to offer a Log Out option.

Choose option 1 to log out, returning to the main menu.

Exit:

Choose option 0 to exit the application. Remember, all data will be lost upon exit!

Possible Future Enhancements (for advanced learning)
Data Persistence: Implement saving and loading user data to/from a file (e.g., JSON, CSV, or using sqlite3 for a simple database) so accounts are not lost when the application closes.

Stronger Password Requirements: Add checks for minimum length, uppercase/lowercase letters, numbers, and special characters.

Hide Password Input: Use the getpass module so passwords are not visible as they are typed.

Login Rate Limiting: Implement a system to temporarily lock out users after a certain number of failed login attempts to prevent brute-force attacks.

Password Confirmation: Ask the user to re-enter their password during sign-up to prevent typos.

Command-Line Arguments: Allow running the script with arguments (e.g., to create an admin user).

Graphical User Interface (GUI): Convert the console interface to a desktop application using libraries like Tkinter, PyQt, or Kivy.
