class InvalidNameError(Exception):
    pass


class InvalidPhoneError(Exception):
    pass


class InvalidPhoneLengthError(Exception):
    pass


class InvalidBirthdayError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


class ValidationErrors(Exception):
    def __init__(self, errors):
        self.errors = errors
