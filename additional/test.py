import json


my_dict = {'__type__': 'class\n',
           '__class__': "<class 'Data.Animal'>\n",
           '__init__': "{'__type__': 'function', 'name': '__init__', 'args': ['self', 'name', 'birth_year', 'daily_calories']}"}

argsN = []
print(type(my_dict['__init__']))
for attr in my_dict:
    if attr == '__init__':
        str_to_conv = my_dict[attr]
        json_acceptable_string = str_to_conv.replace("'", "\"")
        d = json.loads(json_acceptable_string)
        for arg in d['args']:
            if arg != 'self':
                argsN.append(arg)

print(argsN)
print(type(my_dict['__init__']))
