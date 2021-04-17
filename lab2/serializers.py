import json_parser
import pickle_parser
import toml_parser
import yaml_parser


class Serializer:
    @staticmethod
    def serialize(obj, format):
        expr_type = make_choice(fst_prm="dump", sec_prm="dumps", th_prm="load", fth_prm="loads")
        serializer = get_serializer(format)

        if expr_type == "dump":
            file_path = get_file_path()
            obj_type = make_choice(fst_prm="func", sec_prm="simple object", th_prm="hard object", fth_prm="class")
            if obj_type == "func":
                serializer.dump(serializer, file_path, serializer.function_to_dictionary(serializer, obj))
            elif obj_type == "simple object" or obj_type == "hard object":
                serializer.dump(serializer, file_path, serializer.object_to_dictionary(serializer, obj))
            elif obj_type == "class":
                serializer.dump(serializer, file_path, serializer.class_to_dictionary(serializer, obj))
        elif expr_type == "dumps":
            obj_type = make_choice(fst_prm="func", sec_prm="simple object", th_prm="hard object", fth_prm="class")
            if obj_type == "func":
                loaded_string = serializer.dumps(serializer, serializer.function_to_dictionary(serializer, obj))
                print(loaded_string)
            elif obj_type == "simple object" or obj_type == "hard object":
                loaded_string = serializer.dumps(serializer, serializer.object_to_dictionary(serializer, obj))
                print(loaded_string)
            elif obj_type == "class":
                loaded_string = serializer.dumps(serializer, serializer.class_to_dictionary(serializer, obj))
                print(loaded_string)
        elif expr_type == "load":
            file_path = get_file_path()
            obj_type = make_choice(fst_prm="func", sec_prm="simple object", th_prm="hard object", fth_prm="class")
            if obj_type == "func":
                loaded_obj = serializer.to_function(serializer, serializer.load(serializer, file_path))
                print(loaded_obj)
            elif obj_type == "simple object" or obj_type == "hard object":
                loaded_obj = serializer.to_object(serializer, serializer.load(serializer, file_path))
                print(loaded_obj)
            elif obj_type == "class":
                loaded_obj = serializer.to_class(serializer, serializer.load(serializer, file_path))
                print(loaded_obj)
        elif expr_type == "loads":
            obj_type = make_choice(fst_prm="func", sec_prm="simple object", th_prm="hard object", fth_prm="class")
            if obj_type == "func":
                loaded_obj = serializer.to_function(serializer, serializer.loads(serializer, obj))
                print(loaded_obj)
            elif obj_type == "simple object" or obj_type == "hard object":
                loaded_obj = serializer.to_object(serializer, serializer.loads(serializer, obj))
                print(loaded_obj)
            elif obj_type == "class":
                loaded_obj = serializer.to_class(serializer, serializer.loads(serializer, obj))
                print(loaded_obj)


def get_serializer(format):
    if format == 'JSON':
        return json_parser.JsonParser
    elif format == 'PICKLE':
        return pickle_parser.PickleParser
    elif format == 'TOML':
        return toml_parser.TomlParser
    elif format == 'YAML':
        return yaml_parser.YamlParser
    else:
        raise ValueError(format)


def get_file_path():
    print("input file path: ")
    user_input = str(input())
    return user_input


def make_choice(fst_prm, sec_prm, th_prm, fth_prm):
    print(f"1 - {fst_prm}\n"
          f"2 - {sec_prm}\n"
          f"3 - {th_prm}\n"
          f"4 - {fth_prm}\n"
          "5 - quit")
    user_input = int(input())
    if user_input == 1:
        return fst_prm
    elif user_input == 2:
        return sec_prm
    elif user_input == 3:
        return th_prm
    elif user_input == 4:
        return fth_prm
    else:
        exit(0)