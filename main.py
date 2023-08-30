import sys

from utilities.exceptions import *

def main():
    try:
        if sys.argv[1] == "--signup":
            from authentication.registration import Signup
            Signup()
        elif sys.argv[1] == "-u" and sys.argv[3]:
            from todo import todoapp
            todoapp.main_menu()
        else:
            print("Signup --signup")
    except IndexError:
        print("hello")



if __name__ == "__main__":
    main()


