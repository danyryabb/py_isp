import inspect


def cached(func):
    d = {}
    arg = inspect.getargs(func.__code__).args

    def wrapper(*args, **kwargs):
        _args = []
        count = 0
        for a in arg:
            if a in kwargs:
                _args.append(kwargs[a])
            else:
                _args.append(args[count])
                count += 1

        _args = tuple(_args)
        print(_args)
        if _args in d:
            print('cached')
            return d[_args]
        ret = func(*args, **kwargs)
        d[_args] = ret
        return ret

    return wrapper


@cached
def f(a, b, c):
    return a+b+c


@cached
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    f(2, 3, 4)
    f(2, 3, c=4)
    f(b=3, a=2, c=4)


if __name__ == '__main__':
    main()
