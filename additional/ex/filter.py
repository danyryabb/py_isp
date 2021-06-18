class FilterIterator:
    def __init__(self, iterator):
        self.num = 0
        self._objects = []
        for obj in iterator:
            self._objects.append(obj)

    def __iter__(self):
        return iter(self._objects)

    def filter(self, filter):
        buf = [obj for obj in self._objects if filter(obj)]
        return FilterIterator(buf)


def main():
    f = FilterIterator([1, 5, -1])
    print(list(f))
    print(list(f.filter(lambda x: x > 0)))
    print(list(f))


if __name__ == '__main__':
    main()