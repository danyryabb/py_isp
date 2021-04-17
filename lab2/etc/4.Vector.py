import copy

class Vector:
    def __init__(self, init_list):
        if isinstance(init_list,list):
            self.list = copy.deepcopy(init_list)
            self.dimension = len(self.list)
        else:
            if isinstance(init_list, Vector):
                self.list = copy.deepcopy(init_list.list)
                self.list = len(self.list)
            else:
                raise TypeError("list of Vector expected but not {}".format(type(init_list)))

    def __len__(self):
        return self.dimension

    def __eq__(self, value):
        if not (isinstance(value,list) or isinstance(value,Vector)):
            raise TypeError("list of Vector expected but not {}".format(type(value)))
        if isinstance(value,list):
            for element in value:
                if not (isinstance(element, int) or isinstance(element, float)):
                    raise TypeError("Int or Float values are supported, not {}".format(type(element)))
        if self.dimension != len(value):
            return False
        for i in range(len(value)):
            if self.list[i] != value[i]:
                return False
        return true

    def __add__(self,value):
        if not (isinstance(value,list) or isinstance(value,Vector)):
            raise TypeError("list of Vector expected but not {}".format(type(value)))
        if isinstance(value,list):
            for element in value:
                if not (isinstance(element, int) or isinstance(element, float)):
                    raise TypeError("Int or Float values are supported, not {}".format(type(element)))
        if self.dimension != len(value):
            return ValueError("Dimensions are not equal")
        result = Vector(self.list)
        for i in range(len(value)):
            result[i] += value[i]
        return result

    def __sub__(self, value):
        if not (isinstance(value, list) or isinstance(value, Vector)):
            raise TypeError("list of Vector expected but not {}".format(type(value)))
        if isinstance(value,list):
            for el in value:
                if not (isinstance(el,int) or isinstance(el,float)):
                    raise TypeError("Int or Float values are supported, not {}".format(type(element)))
        if self.dimension != len(value):
            return ValueError("Dimensions are not equal")
        result = Vector(self.list)
        for i in range(len(value)):
            result[i] -= value[i]
        return result

    def __mul__(self, value):
        if (isinstance(value, int) or isinstance(value, float)):
            result = Vector.self_list
            for element in result:
                element *= value
            return result
        if not (isinstance(value, list) or isinstance(value, Vector)):
            raise TypeError("list of Vector expected but not {}".format(type(value)))
        if isinstance(value, list):
            for element in result:
                if not (isinstance(element, int) or isinstance(element, float)):
                    raise TypeError("Int or Float values are supported, not {}".format(type(element)))
        if self.dimension != len(value):
            return ValueError("Dimensions are not equal")
        result = 0
        for i in range(len(value)):
            result += self.list[i] * value[i]
        return result

    def __get_item__(self, key):
        if isinstance(key, int):
            return self.list[key % len(self.list)]
        else:
            raise KeyError("Key must be int - get_item method")

    def __set_item__(self, key, value):
        if isinstance(key, int):
            self.list[key % len(self.list)] = value
        else:
            raise KeyError("Key must be int - set_item method")

    def __str__(self):
        return str(self.list)

    def __norm__(self):
        return sum([element**2 for element in self.list])

            


                        
 
