import sys
from tabulate import tabulate
from utilities import validate_input, exceptions
from utilities.display import Display
from .todos import TodoList


todoapp = TodoList()



def main_menu():
    """
    Main function to run the Todo app.

    This function displays the main menu and handles user choices.
    """

    while True:
        view()
        print(tabulate(Display.menu_table))
        try:
            choice = int(validate_input.get_input("Choose: "))
        except ValueError:
            Display.flash_msg("Choice should be a number between 1 and 4")
            Display.clear_screen()
            continue
        match choice:
            case 1:
                add()
        #     case 2:
        #         remove()
        #     case 3:
        #         edit()
            case 4:
                Display.clear_screen()
                sys.exit(Display.flash_msg("\n\tGood Bye.\n"))
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

    tasks_table = []
    header = ["ID", "Task", "Status"]
    colalign =["center"] * len(header)
    try:
        for id, task in enumerate(todoapp.view(), start=1):
            if task["status"] == "pending":
                task["status"] = Display.color("red", task["status"])
            if task["status"] == "Complete":
                task["status"] = Display.color("green", task["status"])

            tasks_table.append([id, task['task'], task['status']])

    except exceptions.EmptyValueError:
        print(Display.color("red", "\n\tNo task available\n"))
    
    else:
        print(tabulate(tasks_table, headers=header, colalign=colalign, tablefmt="grid"))
        


def add():
    ...
