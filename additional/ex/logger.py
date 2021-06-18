class Logger(type):
    logs = ''

    def __new__(cls, name, bases, attrs):
        for k in attrs.keys():
            if callable(attrs[k]):
                attrs[k] = cls.decorator(cls, attrs[k])

        def __str__(self):
            return Logger.logs

        attrs['__str__'] = __str__
        return super().__new__(cls, name, bases, attrs)

    def decorator(self, method):
        def wrapper(*args, **kwargs):
            ret = method(*args, **kwargs)
            self.logs += f'{method.__name__}: {str([*args])} {str(dict(**kwargs))} -> {ret}\n'
            return ret
        return wrapper


class A(metaclass=Logger):
    def b(self):
        return 123

    def func(self, a, b):
        return a + b


def main():
    a = A()
    a.b()
    a.func(3, 5)
    print(a)


if __name__ == '__main__':
    main()

