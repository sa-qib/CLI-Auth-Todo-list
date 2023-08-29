from utilities.display import Display

# custom exceptions
# custom exception classes for signup

class UserExistsError(Exception):
    pass

class InvalidUsernameError(Exception):
    pass

class InvalidPassError(Exception):
    pass


# custom exception classes for login
class UserNotFoundError(Exception):
    pass

class IncorrectPassword(Exception):
    def __init__(self, message="Incorrect password.") -> None:
        self.message = message
        Display.flash_msg(self.message)  # Using Display.flash_msg to display the message
        super().__init__(self.message)



# custom excetion classes for todolist

class DulpicateTaskError(Exception):
    pass

class EmptyValueError(Exception):
    pass

class IncorrectIntError(Exception):
    pass