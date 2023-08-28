import sqlite3
import bcrypt
from utilities.utils import login_args
from utilities.exceptions import *
from todo.todos import TodoList



class Login:
    def __init__(self):
        self.user = login_args()
        self.conn = sqlite3.connect("todos.db") 
        self.cursor = self.conn.cursor()
        self.userName = self.user.username
        self.username()

    def __str__(self) -> str:
        return self.userName

    # validate username from database
    def username(self):
        username = self.user.username
        try:
            self.cursor.execute(
                """SELECT username FROM users WHERE username = ?""",(username, )
            )
        except sqlite3.OperationalError:
            print("No user name Found!")
        user_exist = self.cursor.fetchone()
        
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
            pass
        else:
            raise IncorrectPassword
        

login = Login()
