import sqlite3
import bcrypt
from .utlis import login_args
from .exceptions import *


class Login:
    def __init__(self):
        self.user = login_args()
        self.conn = sqlite3.connect("todos.db") 
        self.cursor = self.conn.cursor()
        self.userName = self.user.username

    def __str__(self) -> str:
        return self.userName

    # validate username from database
    def username(self):
        username = self.user.username
        user = self.cursor.execute(
            """SELECT username FROM users WHERE username = ?""",(username, )
        )
        user_exist = user.fetchone()
        
        if user_exist is None:
            raise UserNotFoundError
        else:
            self.password(username)

    # Valitate password from database
    def password(self, username):
        password = self.user.password

        passwd = self.cursor.execute(
            """SELECT password FROM users WHERE username = ?""",(username, )
        )
        password_fetch = passwd.fetchone()
        
        if password_fetch is None:
            raise UserNotFoundError
        elif bcrypt.checkpw(password.encode('utf-8'), password_fetch[0]):
            print(password)
        else:
            raise IncorrectPassword