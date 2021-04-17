import serializers
from my_parser import Car
from my_parser import Animal
from my_parser import division
from my_parser import add_one


if __name__ == '__main__':
    car = Car("LADA", "2106")
#    obj = add_one
#    obj = Car
#    obj = Animal
#    obj = summary()

    obj = car
    serializer = serializers.Serializer
    while True:
        print("1 - JSON \n"
              "2 - TOML\n"
              "3 - YAML\n"
              "4 - PICKLE\n"
              "5 - quit")
        user_input = int(input())
        if user_input == 1:
            serializer.serialize(obj=obj, format="JSON")
        elif user_input == 2:
            serializer.serialize(obj=obj, format="TOML")
        elif user_input == 3:
            serializer.serialize(obj=obj, format="YAML")
        elif user_input == 4:
            serializer.serialize(obj=obj, format="PICKLE")
        else:
            exit(0)