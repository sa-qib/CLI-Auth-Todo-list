# custom exceptions for username

class UserExistsError(Exception):
    pass

class InvalidUsernameError(Exception):
    pass

class InvalidPassError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class IncorrectPassword(Exception):
    pass
