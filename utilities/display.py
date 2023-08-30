from time import sleep
import os

class Display:
    main_menu = (["1. Add Task, 4. Logout"],)
    menu_table = (["1. Add, 2. Remove, 3.Edit, 4. Logout"],)
    edit_menu = (["0. Menu, 1. Mark, 2. logout"],)

    @classmethod
    def flash_msg(cls, msg):
        """
        Display a message for a short duration and then clear it.

        Args:
            msg (str): The message to be displayed briefly.
        """
            
        print(cls.color("red", msg), end='', flush=True)
        sleep(1)
        print('\r', ' ' * len(msg), '\r', end='', flush=True)


    @classmethod
    def clear_screen(cls):
        """
        Clear the terminal screen.

        This method clears the terminal screen based on the operating system.
        """

        os.system("cls" if os.name == "nt" else "clear")



    @classmethod
    def color(cls, clr, prompt):

        """
        Add color to the prompt using the ASNI escape sequences.

        Args:
            clr (str): The color to apply [red, green, yellow, blue, magenta, cyan, white].
            prompt (str): The prompt message to which color should be applied.
        """

        if prompt == "Task removed successfully.":
            return f"\u001b[32m {prompt} \u001b[0m"

        match clr:
            case "red":
                return f"\u001b[31m {prompt} \u001b[0m"
            case "green":
                return f"\u001b[32m {prompt} \u001b[0m"
            case "yellow":
                return f"\u001b[33m {prompt} \u001b[0m"
            case "blue":
                return f"\u001b[34m {prompt} \u001b[0m"
            case "megenta":
                return f"\u001b[35m {prompt} \u001b[0m"
            case "cyan":
                return f"\u001b[36m {prompt} \u001b[0m"
            case "white":
                return f"\u001b[37m {prompt} \u001b[0m"
            

    @classmethod
    def help(self):
        """
        Display help information for the application usage.

        This method provides a brief overview of the application's command-line usage.
        It explains how to sign up, log in, and view help.
        """
        
        print("Usage: main.py <command>")
        print("\nCommands:")
        print("  --signup    Create a new user account.")
        print("  -u USERNAME -p PASSWORD Log in with an existing account.")
        print("  --help      Show this help message.")