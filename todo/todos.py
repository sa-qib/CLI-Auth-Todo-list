import sqlite3
from utilities.exceptions import *
from authentication.auth import Login
from utilities.validate_input import get_input

class TodoList(Login):
    def __init__(self) -> None:
        super().__init__()
        self.conn = sqlite3.connect('todos.db')
        self.cursor = self.conn.cursor()
        self.user_name = self.userName
        self.user_id = self.cursor.execute('SELECT id FROM users WHERE username = ?', (self.user_name,)).fetchone()[0]


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
            """SELECT task_name, status, user_id FROM tasks WHERE user_id = ? """, (self.user_id,)
        )
        tasks = self.cursor.fetchall()
        for task in sorted(tasks):
            task, status, user_id = task
            task_list.append({"task":task, "status":status, "user_id":user_id})
        return task_list


    def add(self):
        """
        Add a new task to the list.

        Raises:
            ValueError: If the task already exists.
        """

        tasks = self.view() 
        task = get_input("Add Task: ")
        if task not in tasks:
            self.cursor.execute(
                """INSERT INTO tasks (user_id, task_name) VALUES (?, ?)""", (self.user_id, task,)
            )
            self.conn.commit()
        else:
            raise ValueAlreadyExistError

    def remove(self):
        tasks = self.view()
        task_id = int(get_input("remove task by ID: "))
        
        for id, task in enumerate(sorted(tasks, key=lambda t: t["task"]), start=1):
            try:
                if task_id == id:
                    # print(task)
                    self.cursor.execute(
                        """DELETE FROM tasks WHERE task_name = ?""", (task["task"],)
                    )
                    self.conn.commit()
                else:
                    raise IndexError
            except IndexError:
                Display.flash_msg(f"ID with {task_id} not found.")



    def edit(self):
        ...
    
    def delete(self):
        ...
    
