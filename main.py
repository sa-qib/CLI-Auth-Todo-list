import sys
from todo import todoapp
from utilities.exceptions import *

def main():
    if sys.argv[2] == "--signup":
        from authentication.registration import Signup
        Signup()
    elif sys.argv[1] == "-u" and sys.argv[3]:
        todoapp.main_menu()
    else:
        print("Signup --signup")



if __name__ == "__main__":
    main()


