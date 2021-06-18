class ran():
    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop = args
            step = 1
        elif len(args) == 3:
            start, stop, step = args
        else:
            raise TypeError()

        if step == 0:
            raise ValueError()
        elif step < 0:
            stop = min(stop, start)
        else:
            stop = max(stop, start)

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self._count = self.start - self.step
        return self

    def __next__(self):
        self._count += self.step
        if self.step < 0:
            if self._count <= self.stop:
                raise StopIteration()
        else:
            if self._count >= self.stop:
                raise StopIteration()
        return self._count


def main():
    print(list(ran(4, -10, -3)))
    print(list(ran(-4, -18, -2)))
    print(list(ran(-4, 5, 3)))


if __name__ == '__main__':
    main()
