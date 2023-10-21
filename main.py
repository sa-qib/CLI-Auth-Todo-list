import sys
from utilities.exceptions import *
from utilities.display import Display

def main():
    """
    Entry point of the application.

    This script acts as the main entry point of the application.
    It parses command line arguments and initiates the appropriate functionality.

    Usage:
    - For user signup: main.py --signup
    - For user login: main.py -u USERNAME -p PASSWORD
    """
    try:
        if sys.argv[1] == "--signup":
            from authentication.registration import Signup
            Signup()
        elif sys.argv[1] == "-u" and sys.argv[3]:
            from todo import todoapp
            todoapp.main_menu()
        else:
            print("Usage: Signup --signup or Login -u USERNAME -p PASSWORD")
    except UserExistsError:
        Display.flash_msg("User Already Exists!")
    except KeyboardInterrupt:
        Display.clear_screen()
        Display.flash_msg("Good Bye!")

    except IndexError:
        Display.help()

if __name__ == "__main__":
    main()
