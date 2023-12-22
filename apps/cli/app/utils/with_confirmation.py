from functools import wraps


def with_confirmation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        input("\n\nPress Enter to continue...")
        return result

    return inner
