class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        print(312)
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


def main():
    class b(metaclass=Singleton):
        a = 1

        def __new__(cls, *args, **kwargs):
            print(123)
            return super().__new__(cls, *args, **kwargs)

    a = b()
    c = b()
    print(a)
    print(c)


if __name__ == '__main__':
    main()


