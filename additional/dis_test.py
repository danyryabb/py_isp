import dis
import dill
import inspect

class Car:
    brand = "Peugeot"
    model = "406"

    def func(self, brand, model):
        pass

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



def function_to_dictionary(func):
    struct = {'__type__': 'function'}
    args = []
    if str(func).__contains__('lambda'):
        lambda_string = str(dill.source.getsource(func)[dill.source.getsource(func).find("lambda"):])
        struct['code'] = lambda_string
        return struct
    elif func.__name__.startswith('__'):
        struct['name'] = func.__name__
#        args = inspect.getfullargspec(func).args
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


def object_to_dictionary(obj):
    if "<class '__main__." in str(obj.__class__):
        struct = {'__type__': 'object', '__class__': obj.__class__.__name__}
        for attr in obj.__dir__():
            if not attr.startswith('__'):
                attr_value = getattr(obj, attr)
                print(attr_value)
                if callable(attr_value):
                    #print(inspect.getfullargspec(attr_value).args)
                    print('=====')
                    print(len(attr_value.__code__.co_varnames))
                    print(len(inspect.getfullargspec(attr_value).args))
                    if len(inspect.getfullargspec(attr_value).args) > 1:
                         struct[attr] = function_to_dictionary(attr_value)
                elif "<class '__main__." in str(attr_value.__class__):
                    struct[attr] = object_to_dictionary(attr_value)
                else:
                    struct[attr] = attr_value
        return struct
    raise Exception("Only object")

print('=========')
#print(function_to_dictionary(__func__))
car = Car("bmw", "e60")
print(object_to_dictionary(car))
