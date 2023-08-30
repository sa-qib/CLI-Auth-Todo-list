import sys
import sqlite3
from tabulate import tabulate
from utilities import validate_input, exceptions
from utilities.display import Display
from .todos import TodoList


todo_app = TodoList()



def main_menu():
    """
    Main function to run the Todo app.

    This function displays the main menu and handles user choices.
    """

    while True:
        view()
        try:
            todo_app.view()
            print(tabulate(Display.menu_table))
        except exceptions.EmptyValueError:
            print(tabulate(Display.main_menu))
        try:
            choice = int(validate_input.get_input("Choice: "))
        except ValueError:
            Display.flash_msg("Choice should be a number between 1 and 4")
            Display.clear_screen()
            continue
        match choice:
            case 1:
                add()
            case 2:
                remove()
            case 3:
                edit()
            case 4:
                logout()
                
            case _:
                Display.flash_msg("Choice should be a number between 1 and 4")
                Display.clear_screen()
                continue



def view():
    """
    View tasks in a grid table format.

    This function displays the tasks in a tabulated grid.
    """
     
    Display.clear_screen()
    print(Display.color("cyan", tabulate([["\t|      TODO-LIST      |\t"]], tablefmt="grid")))
    print("note: CTRL + C to exit")

    tasks_table = []
    header = ["ID", "Task", "Status"]
    colalign =["center"] * len(header)

    try:
        for task in todo_app.view():
            if task["status"] == "pending":
                task["status"] = Display.color("red", task["status"])
            if task["status"] == "complete":
                task["status"] = Display.color("green", task["status"])

            tasks_table.append([task["ID"], task['task'], task['status']])

    except exceptions.EmptyValueError:
        print(Display.color("red", "\n  No task available\n"))
    else:
        print(tabulate(tasks_table, headers=header, colalign=colalign, tablefmt="grid"))
        


def add():
    view()
    Display.clear_screen()
    print("note: CTRL + C to exit")
    while True:
        try:
            todo_app.add()
            continue
        except exceptions.ValueAlreadyExistError:
            Display.flash_msg("Task Already Exist")
        except KeyboardInterrupt:
            main_menu()
        except exceptions.EmptyValueError:
            Display.flash_msg("task cannot be empty!")
        



def remove():
    while True:
        view()
        try:
            todo_app.remove()
            
        except (KeyboardInterrupt, exceptions.EmptyValueError):
            view()
            break
        except IndexError as e:
            Display.flash_msg(str(e))
        except ValueError:
            Display.flash_msg("Value cannot be empty")


        

def edit():
    
    while True:
        view()
        try:
            todo_app.edit()
            continue
        except IndexError as e:
            Display.flash_msg(str(e))
            continue
        except KeyboardInterrupt:
            view()
            break

    

    


def logout():
    Display.clear_screen()
    sys.exit(Display.flash_msg("\n\tGood Bye.\n"))