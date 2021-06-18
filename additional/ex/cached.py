def cached(func):
    d = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in d:
            return d[key]
        ret = func(*args, **kwargs)
        d[key] = ret
        return ret
    return wrapper

@cached
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(fibonacci(40))


if __name__ == '__main__':
    main()
