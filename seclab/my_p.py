from abc import abstractmethod
from types import FunctionType
import dill
import inspect
from data import Car


def is_primitive(obj):
    return type(obj) in [int, float, str, bool, type(None), list, tuple]


def function_to_dictionary(func):
    struct = {'__type__': 'function'}
    args = []
    if str(func).__contains__('lambda'):
        lambda_string = str(dill.source.getsource(func)[dill.source.getsource(func).find("lambda"):])
        struct['code'] = lambda_string
        return struct
    elif func.__name__.startswith('__'):
        struct['name'] = func.__name__
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
    struct = {'__type__': 'object', '__class__': obj.__class__.__name__}
    for attr in dir(obj):
        if not attr.startswith('__'):
            attr_value = getattr(obj, attr)
            if callable(attr_value):
                if len(attr_value.__code__.co_varnames) > 1:
                    struct[attr] = function_to_dictionary(attr_value)
            elif "<class '__main__." in str(attr_value.__class__):
                struct[attr] = object_to_dictionary(attr_value)
            else:
                struct[attr] = attr_value
    return struct


def class_to_dictionary(cl):
    if cl.__class__.__name__ == "type":
        struct = {'__type__': 'class', '__class__': cl.__name__}
        for attr in dir(cl):
            if attr == "__init__":
                attr_value = getattr(cl, attr)
                struct[attr] = function_to_dictionary(attr_value)
            if not attr.startswith('__'):
                attr_value = getattr(cl, attr)
                if "<class 'type'>" in str(attr_value.__class__):
                    struct[attr] = class_to_dictionary(attr_value)
                elif "<class '__main__." in str(attr_value.__class__):
                    struct[attr] = object_to_dictionary(attr_value)
                elif callable(attr_value):
                    if len(inspect.getfullargspec(attr_value).args) > 1:
                        struct[attr] = function_to_dictionary(attr_value)
                    else:
                        struct[attr] = attr_value
        return struct


def convert_to_function(json_str):
    json_str['code'] = json_str['code'].strip()
    foo_code = compile(json_str['code'], 'string', "exec")
    if json_str.get('name'):
        foo_name = FunctionType(foo_code.co_consts[0], globals(), json_str['name'])
        return foo_name
    else:
        foo_lambda = FunctionType(foo_code.co_consts[0], globals(), 'lambda')
        return foo_lambda


def convert_to_object(json_str):
    class_name = globals()[json_str['__class__']]
    init_args = inspect.getfullargspec(class_name).args
    args = {}
    for arg in init_args:
        if arg in json_str:
            args[arg] = json_str[arg]
    obj = class_name(**args)
    for attr in obj.__dir__():
        if isinstance(getattr(obj, attr), dict) and not attr.startswith('__'):
            object_attr = convert_to_object(getattr(obj, attr))
            setattr(obj, attr, object_attr)
        elif not attr.startswith('__') and attr not in args:
            object_attr = getattr(obj, attr)
            if not callable(object_attr):
                setattr(obj, attr, json_str[attr])
    return obj


def convert_to_class(json_str):
    vars = {}
    argsN = []

    def attr_init(self, *args):
        if len(args) > len(argsN):
            raise Exception("To much arguments!")
        ind = 0
        for argument in args:
            setattr(self, argsN[ind], argument)
            ind += 1

    for attr in json_str:
        if attr == '__init__':
            for arg in json_str[attr]['args']:
                if arg != 'self':
                    argsN.append(arg)
            vars[attr] = attr_init
        elif not isinstance(json_str[attr], dict) and not attr.startswith('__'):
            vars[attr] = json_str[attr]
        elif isinstance(json_str[attr], dict) and not attr.startswith('__'):
            if json_str[attr]['__type__'] == 'function':
                vars[attr] = convert_to_function(json_str[attr])
    return type("method", (object,), vars)


def pack(obj):
    if isinstance(obj, FunctionType):
        obj_dict = function_to_dictionary(obj)
        return obj_dict
    elif is_primitive(obj):
        return obj
    elif isinstance(obj, type):
        obj_dict = class_to_dictionary(obj)
        return obj_dict
    elif isinstance(obj, object):
        obj_dict = object_to_dictionary(obj)
        return obj_dict


def unpack(load_dict):
    if "code" in load_dict.keys():
        return convert_to_function(load_dict)
    elif "object" in load_dict.values():
        return convert_to_object(load_dict)
    elif "class" in load_dict.values():
        return convert_to_class(load_dict)
    else:
        return load_dict


class MyParser:
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
