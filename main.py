import sys
from todo.views import main_menu
from utilities.exceptions import *

def main():
    if sys.argv[1] == "--signup":
        from authentication.registration import Signup
        Signup()
    elif sys.argv[1] == "-u" and sys.argv[3]:
        main_menu()
    else:
        print("Signup --signup")



if __name__ == "__main__":
    main()


