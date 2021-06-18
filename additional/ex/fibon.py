def fib(n):
    yield from [1, 1]
    a = 1
    b = 1
    for _ in range(n-2):
        a, b = a + b, a
        yield a

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print(list(fib(7)))
    print(fibonacci(7))


if __name__ == '__main__':
    main()

