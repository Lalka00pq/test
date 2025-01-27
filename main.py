from typing import Callable


def my_decorator(func: Callable) -> Callable:
    def wrapper():
        a = func()

        a = a[:4]
        print(a)
    return wrapper

@my_decorator
def say_hello():
    return 'Hello World'

say_hello()
