import logging
import inspect
import types


class Logger:
    log = ''

    def decorator(self, method):
        def wrapper(*args, **kwargs):
            ret = method(*args, **kwargs)
            self.log += f'{method.__name__}: {str([*args])} -> {ret}\n'
            return ret
        return wrapper

    def set_decorator(self, key, value):
        bound_method = types.MethodType(value, self) #value.__get__(self, self.__class__)
        value.__get__(self, self.__class__)
        self.__dict__[key] = self.decorator(bound_method)

    def __setattr__(self, key, value):
        if inspect.isfunction(value):
            self.set_decorator(key, value)
        else:
            self.__dict__[key] = value

    def __str__(self):
        return self.log


def main():
    def f(self, a, b):
        return a + b
    l = Logger()
    l.func = f
    l.func(5, 2)
    l.func(5, 6)
    print(l)


if __name__ == '__main__':
    main()

