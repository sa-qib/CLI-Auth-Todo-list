
from utilities import login_args
import sqlite3
import exceptions
import bcrypt


class Login:
    def __init__(self):
        self.user = login_args()
        self.conn = sqlite3.connect("todos.db") 
        self.cursor = self.conn.cursor()


    # validate username from database
    def username(self):
        username = self.user.username
        user = self.cursor.execute(
            """SELECT username FROM users WHERE username = ?""",(username, )
        )
        user_exist = user.fetchone()
        if user_exist is not None:
            try:
                self.password(username)
            except 
        else:
            exceptions.UserPasswordNotFoundError

    def password(self, username):
        password = self.user.password
        password_encoded = password.encode('utf-8')
        passwd = self.cursor.execute(
            """SELECT password FROM users WHERE username = ?""",(username, )
        )
        password_fecth = passwd.fetchone()[0]
        if bcrypt.checkpw(password_encoded, password_fecth):
            print(password)
        else:
            print("password Not match")

        





# creating an instance of the login class
login = Login()
login.password('saqib')