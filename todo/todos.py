import sqlite3
from utilities.exceptions import *

class TodoList:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('todos.db')
        self.cursor = self.conn.cursor()
        self.user_id = self.cursor("SELECT id FROM users")


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id


    def task(self):
        description = input("Add Task: ").strip().title()
        while not description:
            raise EmptyValueError
        return description





    def view(self):
        task_list = []
        self.cursor.execute(
            """SELECT * FROM tasks"""
        )
        tasks = self.cursor.fetchall()
        for task in tasks:
            id, task, status, user_id = task
            self.user_id = user_id
            task_list.append({"task":task, "status":status, "user_id":user_id})
        return task_list


    def add(self, user_id, task):
        """
        Add a new task to the list.

        Raises:
            ValueError: If the task already exists.
        """
        tasks = self.view()
        while True:   
            task = self.get_input()
            if task not in tasks:
                self.cursor.execute(
                    """INSERT INTO tasks (user_id, task_name) VALUES (?, ?)""", (self.user_id, task)
                )
            else:
                raise DulpicateTaskError

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
    
