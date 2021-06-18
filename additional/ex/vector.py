class Vector(object):
    def __init__(self, array: []):
        self.array = self._array_to_vector(array)

    def _array_to_vector(self, array: []):
        for i in range(len(array)):
            if isinstance(array[i], type([])):
                array[i] = Vector(self._array_to_vector(array[i]))
        return array

    def __add__(self, other):
        v = Vector([a + b for a, b in zip(self.array, other)])
        return v

    def __sub__(self, other):
        v = Vector([a - b for a, b in zip(self.array, other)])
        return v

    def __setitem__(self, key, value):
        self.array[key] = value

    def __getitem__(self, key):
        return self.array[key]

    def __iter__(self):
        yield from self.array

    def __repr__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

    def __hash__(self):
        return hash(str(self.array))

    def __eq__(self, other):
        return hash(str(self.array)) == other.__hash__()


def main():
    v = Vector([[1, 1, 1], [2, 2, 2]])
    k = v + Vector([[1, 1, 1], [1, 1, 1]])*2
    print(k * Vector([[1, 1, 1], [2, 2, 2]]))
    print(len(v[0]))
    print(v == Vector([[1, 1, 1], [2, 2, 2]]))


if __name__ == '__main__':
    main()

