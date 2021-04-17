from my_parser import MyParser


class JsonParser(MyParser):
    def dump(self, save_file_path, obj):
        with open(save_file_path, 'w') as file:
            for key, val in obj.items():
                file.write('{}:{}\n'.format(key, val))

    def dumps(self, obj):
        strings = []
        for key, item in obj.items():
            strings.append("{}:{}".format(key.capitalize(), item))
        result = "; ".join(strings)
        return result

    def load(self, load_file_path):
        load_dict = {}
        with open(load_file_path, 'r') as file:
            for i in file.readlines():
                key, val = i.strip().split(':')
                load_dict[key] = val
        return load_dict

    def loads(self, load_string):
        return load_string
