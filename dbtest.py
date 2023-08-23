import sqlite3
import bcrypt

conn = sqlite3.connect('todos.db')
cursor = conn.cursor()


# user = input("username: ")

# cursor.execute("INSERT INTO users (username) VALUES (?)", (user,))
# conn.commit()

# cursor.execute("""CREATE TABLE users_temp AS
#                SELECT id, username, email, password FROM users
#                """)



# cursor.execute(
#     """CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE NOT NULL,
#     email TEXT UNIQUE NULL,
#     password TEXT NOT NULL 
#     )"""
# )

# username = "saqib"
# email = "sdf"
# password = "Password2@"
# cursor.execute("DELETE FROM users WHERE id = ?", (1,))
# conn.commit()

# cursor.execute(
#     """INSERT INTO (username, email, password) VALUES (?, ?, ?)""", (username, email, password)
# )



# username = input("username: ")
# user = cursor.execute("SELECT password FROM users WHERE username = ?", (username, ))
# pass_exist = user.fetchone()

# if pass_exist is not None:
#     print(pass_exist[0])


# cursor.execute("DELETE FROM users WHERE username = 'saqib'")
# conn.commit()

# username = input("username: ")
# email = input("email (optional): ")
# password = input("password: ")
# encoded = password.encode("utf-8")

# password_hash = bcrypt.hashpw(encoded, bcrypt.gensalt())


# cursor.execute(
#     """INSERT INTO users (username, email, password) VALUES (?, ?, ?)""", (username, email, password_hash)
# )
# conn.commit()


# passwd = cursor.execute(
#     """SELECT password FROM users WHERE username = ?""", (username, )
# )

# password_fetch = passwd.fetchone()[0]

# if bcrypt.checkpw(encoded, password_fetch):
#     print(password)
# else:
#     print("No match")









