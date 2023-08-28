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
    pass



# custom excetion classes for todolist

class DulpicateTaskError(Exception):
    pass