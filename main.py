import sqlite3
import sys
import argparse
# from authentication.registration import Signup
# from authentication.auth import Login



def main():
    if sys.argv[1] == "--signup":
        from authentication.registration import Signup
        Signup()
    elif sys.argv[1] == "-u" and sys.argv[3]:
        from authentication.auth import Login
        Login()

        



if __name__ == "__main__":
    main()

    