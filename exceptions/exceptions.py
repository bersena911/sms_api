class MainException(Exception):
    pass


class NotAuthorized(MainException):
    status_code = 401
    message = 'Incorrect credentials'
