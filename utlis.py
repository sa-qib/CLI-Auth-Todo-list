import argparse


def login_args():
    login_parser = argparse.ArgumentParser()
    login_parser.add_argument("-u", "--username", required=True, nargs="?")
    login_parser.add_argument("-p", "--password", required=True)
    args = login_parser.parse_args()
    return args



def register_args():
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--signup",action='store_true', help="Initiate user signup process", required=True)
    register_args = parser.parse_args()
    return register_args

