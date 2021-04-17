import yaml
from my_parser import MyParser


class YamlParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            yaml.dump(obj, file)

    def dumps(self, obj):
        return yaml.dump(obj)

    def load(self, load_file_path):
        obj = None
        with open(load_file_path, 'r') as file:
            obj = yaml.load(file, Loader=yaml.FullLoader)
        return obj

    def loads(self, string_to_load):
        return yaml.unsafe_load(string_to_load)
