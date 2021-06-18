
def sort_args(func):
    def wrapper(*args, **kwargs):
        arguments = sorted([*args, *kwargs.values()])
        print(f"Sorted args and kwargs: {arguments}")
        return func(*arguments)
    return wrapper


@sort_args
def f(a, b=1, c=2):
    print(f"a: {a}, b: {b}, c: {c}, ")


def main():
   f(4, 3, b=12)


if __name__ == '__main__':
    main()