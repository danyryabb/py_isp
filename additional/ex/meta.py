import json

class Meta(type):
    def __new__(cls, name, bases, dit):
        file_dit = json.load(open('class_attr.txt', 'r'))
        attr = {**dit, **file_dit}
        return super().__new__(cls, name, bases, attr)


def main():
    json.dump({'a': 4}, open('class_attr.txt', 'w'))

    class abc(metaclass=Meta):
        pass

    print(abc.a)


if __name__ == '__main__':
    main()