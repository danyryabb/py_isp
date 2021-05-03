
a = 5

def division(num1):
    result = num1 / a
    return result


add_one = lambda x: x + 1



class Car(object):
    brand = "Peugeot"
    model = "406"

    def greetings(self):
        print(self.brand, self.model)

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model