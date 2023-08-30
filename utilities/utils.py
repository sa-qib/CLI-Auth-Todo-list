import argparse


def login_args():
    """
    Parse command-line arguments for user login.

    This function uses the argparse module to parse command-line arguments
    for the user login process. It expects the username and password to be provided
    as arguments.

    Returns:
        argparse.Namespace: A namespace containing the parsed arguments.
    """

    login_parser = argparse.ArgumentParser(add_help=False)
    login_parser.add_argument("-u", "--username", required=True, nargs="?")
    login_parser.add_argument("-p", "--password", required=True)
    args = login_parser.parse_args()
    return args



def register_args():
    """
    Parse command-line arguments for user registration.

    This function uses the argparse module to parse command-line arguments
    for the user registration process. It expects the "--signup" flag to be provided,
    indicating the initiation of the signup process.

    Returns:
        argparse.Namespace: A namespace containing the parsed arguments.
    """
    
    parser = argparse.ArgumentParser(allow_abbrev=False, add_help=False)
    parser.add_argument("--signup",action='store_true', help="Initiate user signup process", required=True)
    register_args = parser.parse_args()
    return register_args




