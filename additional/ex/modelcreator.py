class StringField:
    def __init__(self, value = ''):
        self.value = str(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if type(value) is str:
            self.value = value
        else:
            raise ValueError()


class ModelCreator(type):
    def __new__(cls, name, bases, dct):
        attr_to_set = []
        for k, v in dct.items():
            if isinstance(v, StringField):
                attr_to_set.append(k)

        def __new__(cls, *args, **kwargs):
            inst = object.__new__(cls)
            for k, v in kwargs.items():
                if k in attr_to_set:
                    setattr(inst, k, v)
            return inst

        dct['__new__'] = __new__
        return super().__new__(cls, name, bases, dct)


def main():
    class b(metaclass=ModelCreator):
        a = StringField()

    a = b(a='fd')
    a.__dict__['a'] = 'gdf'
    print(a.__dict__)
    print(a.a)
    a.a = 'gdf'
    print(a.a)


if __name__ == '__main__':
    main()

