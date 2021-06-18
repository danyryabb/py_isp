class Dictionary:
    def __init__(self, value=None):
        self.d = {}
        self.value = value

    def __getitem__(self, item):
        if item not in self.d:
            self.d[item] = Dictionary()
        return self.d[item]

    def __setitem__(self, key, value):
        self.d[key] = Dictionary(value)
        self.value = None

    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        return str(self.d)

    def __copy__(self):
        return self.d.copy


def main():
    d = Dictionary()
    d['a']['b'] = 1
    print(d)
    d['a']['b']['m'] = 5
    d['a']['k'] = 55
    d['m'] = d
    print(d)
    d['a']['b'] = d['a']['b']['m']
    print(d['a']['b']['m'])
    print(d)


if __name__ == '__main__':
    main()
