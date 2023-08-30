import sqlite3
import bcrypt
from utilities.utils import login_args
from utilities.exceptions import *
from utilities.display import Display


class Login:
    """
    The `Login` class provides user authentication functionality for the Todo List Application.
    It allows users to log in using their credentials and validates the provided username
    and password against the stored user data in the SQLite database.
    """
    
    def __init__(self):
        """
        Initializes the Login instance.
        Prompts the user for a username and password using `login_args()` function.
        Establishes a connection to the 'todos.db' SQLite database.
        """
         
        self.user = login_args()
        self.conn = sqlite3.connect("todos.db") 
        self.cursor = self.conn.cursor()
        self.userName = self.user.username
        self.username()



    def __str__(self) -> str:
        """
        Returns the username of the authenticated user.
        Provides a string representation of the instance.
        """

        return self.userName


    
    def username(self):
        """
        Validates the provided username against the database.
        If the username is not found, raises a `UserNotFoundError`.
        If the username is valid, proceeds to validate the password using the `password` method.
        """

        username = self.user.username
        try:
            self.cursor.execute(
                """SELECT username FROM users WHERE username = ?""",(username, )
            )
        except sqlite3.OperationalError:
            print("No user name Found!")
        user_exist = self.cursor.fetchone()
        
        if user_exist is None:
            raise UserNotFoundError("Incorrect username or password.")
        else:
            self.password(username)



    
    def password(self, username):
        """
        Compares the provided password with the hashed password stored in the database using bcrypt.
        If the password is incorrect, raises an `IncorrectPassword` exception.
        """
        
        password = self.user.password

        passwd = self.cursor.execute(
            """SELECT password FROM users WHERE username = ?""",(username, )
        )
        password_fetch = passwd.fetchone()
        
        if password_fetch is None:
            raise UserNotFoundError("Incorrect username or password.")
        elif bcrypt.checkpw(password.encode('utf-8'), password_fetch[0]):
            pass
        else:
            raise IncorrectPassword
        


