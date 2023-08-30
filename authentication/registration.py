import sqlite3
import re
import validators
import bcrypt
from utilities.utils import register_args
from utilities.exceptions import *


class Signup:
    """
    The `Signup` class provides user registration functionality for the Todo List Application.
    It allows users to create a new account by providing a unique username, email (optional), and password.
    The class handles input validation, password hashing, and database insertion.
    """

    def __init__(self) -> None:
        """
        Initializes the Signup instance.
        Prompts the user for account details using `register_args()` function.
        Establishes a connection to the 'todos.db' SQLite database.
        Initializes the database tables using the `database()` method.
        """

        register_args()
        self.conn = sqlite3.connect("todos.db")
        self.cursor = self.conn.cursor()
        self.database()
        self.start_registration()
        


    def start_registration(self):
        """
        Initiates the registration process by gathering username, email, and password from the user.
        Confirms the registration with the user and proceeds to registration if confirmed.
        """
         
        username = self.username()
        email = self.email()
        password = self.password()

        self.confirm_registration(username, email, password)
        
        

    def username(self):
        """
        Validates and returns the provided username.
        Ensures the username adheres to specific naming rules and is unique in the database.
        """

        while True:
            user = input("Username: ").lower().strip()
            if valid_user := re.match("^[A-Za-z][A-Za-z_0-9]{4,14}$", user, flags=re.IGNORECASE):
                self.cursor.execute("SELECT username FROM users where username = ?", (user, ))
                username = self.cursor.fetchall()
                if username:
                    print("username already exists.")
                    raise UserExistsError
                else:
                    return valid_user.group()
            else:
                print("Invalid username. Usernames must start with a letter and can only contain letters, digits, or underscores.")
                print("Username length should be between 6 and 15 characters.")
                print("Examples of valid usernames:")
                print("- username123")
                print("- user001")
                print("- user_name_12")
                continue


    def email(self):
        """
        Validates and returns the provided email (optional).
        Ensures the email follows the standard email format.
        """

        while True:
            email = input("Email (optional): ")
            if validators.email(email):
                return email
            elif email == "":
                email = None
                break
            else:
                print("Invalid email address. Emails must follow the standard format, such as:")
                print("- example@example.com")
                print("- your.name@example.org")
                print("- contact123@domain.net")
                continue
            


    def password(self):
        """
        Validates and returns the provided password.
        Ensures the password meets complexity requirements and hashes it using bcrypt.
        """

        while True:
            password = input("Password: ")
            if password := re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$_])[A-Za-z0-9@#$_]{8,}$", password):
                encoded = password.group().encode("utf-8")
                hashed_password = bcrypt.hashpw(encoded, bcrypt.gensalt())
                return hashed_password
            else:
                raise InvalidPassError
                


    def confirm_registration(self, username, email, password):
        confirmation = input("Confirm registration (yes/no): ")
        if confirmation.lower() == "yes":
            self.register(username, email, password)
            print("Registration successful!")
        else:
            print("Registration canceled.")


    def register(self, username, email, password):
        """
        Asks the user for confirmation to proceed with the registration.
        If confirmed, calls the `register` method to insert the user data into the database.
        """

        # Logic for the registration process
        self.cursor.execute(
            """INSERT INTO users (username, email, password) VALUES (?, ?, ?)""",(username, email, password)
        )
        self.conn.commit()


    def database(self):
        """
        Creates and initializes the 'users' and 'tasks' tables in the SQLite database.
        """
         
        self.cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NULL,
            password TEXT NOT NULL 
            )""")
        
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )"""
        )
        