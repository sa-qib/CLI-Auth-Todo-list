import sqlite3
from authentication.exceptions import *

class TodoList:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('todos.db')
        self.cursor = self.conn.cursor()

    def view(self):
        self.cursor.execute(
            """SELECT * FROM tasks"""
        )
        tasks = self.cursor.fetchall()
        return tasks


    def add(self, user_id, task):
        tasks = self.view()
        # if task not in tasks:
        self.cursor.execute(
            """INSERT INTO tasks (user_id, task_name) VALUES (?, ?)""", (user_id, task)
        )
        # else:
        #     raise DulpicateTaskError

    def remove(self, user_id, task):

        # self.cursor.execute(
        #     """DELETE 
        #     """
        # )
        ...

    def edit(self):
        ...
    
    def delete(self):
        ...
    
