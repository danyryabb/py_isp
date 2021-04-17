import pickle
from my_parser import MyParser


class PickleParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            pickle.dump(obj, file)

    def dumps(self, obj):
        return pickle.dumps(obj)

    def load(self, load_file_path):
        with open(load_file_path, 'r') as file:
            load_string = pickle.load(file)
        return load_string

    def loads(self, string_to_load):
        return pickle.loads(string_to_load)