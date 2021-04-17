import toml
from my_parser import MyParser


class TomlParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            toml.dump(obj, file)

    def dumps(self, obj):
        return toml.dumps(obj)

    def load(self, load_file_path):
        obj = None
        with open(load_file_path, 'r') as file:
            obj = toml.load(file)
        return obj

    def loads(self, string_to_load):
        return toml.loads(string_to_load)