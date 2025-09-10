"""
I am trying to learn the concepts of:
    [x] dunder methods
    [x] cls methods
    [x] self methods
    [x] walrus operators
    [x] how to avoid reference counting and also circular imports
    [x] Decorator pattern with classes
    [x] Instance and class methods

Most of these are OOP concepts which I would be also using a more
OOP centered language like C++, C# of Java
"""

from typing import Callable


class Test1: ...


class Test2: ...


class Deorator:

    def __init__(self, func: Callable, *args, **kwargs):
        self.func = func
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self):

        result, __memoized = self.__memoize(self.__args, self.__kwargs)

        def wrapper_function():
            self.func(result)

        return wrapper_function()

    def __memoize(self, *args, **kwargs):
        match (self.__args, self.__kwargs):
            case self.__args:
                return self.__args, False
            case self.__kwargs:
                return self.__kwargs, False

        return None, True


"""
Using the with key word for auto closing open sessions
and file readers/db sessions for better later access
"""
