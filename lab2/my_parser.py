from abc import abstractmethod
import dill
import inspect
from types import FunctionType


def division(num1, num2):
    result = num1 / num2
    return result


add_one = lambda x: x + 1


class Car(object):
    brand = "Peugeot"
    model = "406"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Animal(object):
    def __init__(self, name, birth_year, daily_calories):
        self.name = name
        self.birth_year = birth_year
        self.daily_calories = daily_calories


class MyParser:
    def function_to_dictionary(self, func):
        struct = {'__type__': 'function'}
        args = []
        if str(func).__contains__('lambda'):
            lambda_string = str(dill.source.getsource(func)[dill.source.getsource(func).find("lambda"):])
            struct['code'] = lambda_string
            return struct
        elif func.__name__.startswith('__'):
            struct['name'] = func.__name__
            # args = inspect.getfullargspec(func).args
            for arg in func.__code__.co_varnames:
                args.append(arg)
            struct['args'] = args
        else:
            struct['name'] = func.__name__
            for arg in func.__code__.co_varnames:
                if arg == "class_name":
                    break
                args.append(arg)
            struct['args'] = args
            string = str(dill.source.getsource(func))
            string = string[string.find("def"):]
            struct['code'] = string
        return struct

    def object_to_dictionary(self, obj):
        if "<class '__main__." in str(obj.__class__):
            struct = {'__type__': 'object', '__class__': obj.__class__.__name__}
            for attr in obj.__dir__():
                if not attr.startswith('__'):
                    attr_value = getattr(obj, attr)
                    if callable(attr_value):
                        # len(inspect.getfullargspec(attr_value).args)
                        if len(attr_value.__code__.co_varnames) > 1:
                            struct[attr] = self.function_to_dictionary(self, attr_value)
                    elif "<class '__main__." in str(attr_value.__class__):
                        struct[attr] = self.object_to_dictionary(attr_value)
                    else:
                        struct[attr] = attr_value
            return struct
        raise Exception("Only object")

    def class_to_dictionary(self, cl):
        if cl.__class__.__name__ == "type":
            struct = {'__type__': 'class', '__class__': cl}
            for attr in dir(cl):
                if attr == "__init__":
                    attr_value = getattr(cl, attr)
                    struct[attr] = self.function_to_dictionary(self, attr_value)
                if not attr.startswith('__'):
                    attr_value = getattr(cl, attr)
                    if "<class 'type'>" in str(attr_value.__class__):
                        struct[attr] = self.class_to_dictionary(attr_value)
                    elif "<class '__main__." in str(attr_value.__class__):
                        struct[attr] = self.object_to_dictionary(attr_value)
                    elif callable(attr_value):
                        # len(inspect.getfullargspec(attr_value).args)
                        if len(attr_value.__code__.co_varnames) > 1:
                            struct[attr] = self.function_to_dictionary(attr_value)
                    else:
                        struct[attr] = attr_value
        return struct

    def to_function(self, json):
        json['code'] = json['code'].strip()
        foo_code = compile(json['code'], 'string', "exec")
        if json.get('name'):
            foo_name = FunctionType(foo_code.co_consts[0], globals(), json['name'])
            return foo_name
        else:
            foo_lambda = FunctionType(foo_code.co_consts[0], globals(), 'lambda')
            return foo_lambda

    def to_object(self, json):
        class_name = globals()[json['__class__']]
        init_args = inspect.getfullargspec(class_name).args
        args = {}
        for arg in init_args:
            if arg in json:
                args[arg] = json[arg]
        obj = class_name(**args)
        for attr in obj.__dir__():
            if isinstance(getattr(obj, attr), dict) and not attr.startswith('__'):
                object_attr = self.to_object(getattr(obj, attr))
                setattr(obj, attr, object_attr)
            elif not attr.startswith('__') and attr not in args:
                object_attr = getattr(obj, attr)
                if not callable(object_attr):
                    setattr(obj, attr, json[attr])
        return obj

    def to_class(self, json):
        vars = {}
        argsN = []
        for attr in json:
            if attr == '__init__':
                for arg in json[attr]['args']:
                    if arg != 'self':
                        argsN.append(arg)

                def this_init(self, *args):
                    if len(args) > len(argsN):
                        print("ERROR")
                        raise Exception("To much arguments")
                    k = 0
                    for arg in args:
                        setattr(self, argsN[k], arg)
                        k += 1

                vars[attr] = this_init
            elif not isinstance(json[attr], dict) and not attr.startswith('__'):
                vars[attr] = json[attr]
            elif isinstance(json[attr], dict) and not attr.startswith('__'):
                if json[attr]['__type__'] == 'function':
                    vars[attr] = self.to_function(json[attr])
        return type("method", (object,), vars)

    @abstractmethod
    def dump(self, file_path, obj):
        pass

    @abstractmethod
    def dumps(self, obj):
        pass

    @abstractmethod
    def load(self, file_path):
        pass

    @abstractmethod
    def loads(self, string):
        pass