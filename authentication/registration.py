import sqlite3
import re
import validators
import bcrypt
from utilities.utils import register_args
from utilities.exceptions import *


class Signup:
    def __init__(self) -> None:
        register_args()
        self.conn = sqlite3.connect("todos.db")
        self.cursor = self.conn.cursor()
        self.database()
        self.start_registration()
        

    def start_registration(self):
        username = self.username()
        email = self.email()
        password = self.password()

        self.confirm_registration(username, email, password)
        
        

    def username(self):
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
            # raise InvalidUsernameError


    def email(self):
        while True:
            email = input("Email (optional): ")
            if validators.email(email):
                return email
            elif email == "":
                pass
            else:
                print("Invalid email address. Emails must follow the standard format, such as:")
                print("- example@example.com")
                print("- your.name@example.org")
                print("- contact123@domain.net")
                continue
            


    def password(self):
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
        # Logic for the registration process
        self.cursor.execute(
            """INSERT INTO users (username, email, password) VALUES (?, ?, ?)""",(username, email, password)
        )
        self.conn.commit()


    def database(self):
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
            task_name TEXT UNIQUE NOT NULL,
            status TEXT DEFAULT 'pending',
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
            )"""
        )
        