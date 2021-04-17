import unittest
from my_parser import MyParser

def division(num1, num2):
  result = num1 / num2
  return result


add_one = lambda x: x + 1


class Car(object):
  brand = "Peugeot"
  model = "406"

  def __init__(self, brand, model):
    self.brand = brand
    self.model = model


class Animal(object):
  def __init__(self, name, birth_year, daily_calories):
    self.name = name
    self.birth_year = birth_year
    self.daily_calories = daily_calories


class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.my_par = MyParser()

  def test_json_dump_func(self):
    self.assertEqual(self.my_par.dump("./unittests.json", self.my_par.function_to_dictionary(add_one)), )

  def test_json_dump_lambda(self):
    self.assertEqual(self.calculator.add(4,7), 11)

  def test_json_dump_obj(self):
    self.assertEqual(self.calculator.add(4,7), 11)

  def test_json_dump_class(self):
    self.assertEqual(self.calculator.add(4,7), 11)

  def test_pickle(self):
    self.assertEqual(self.calculator.subtract(10,5), 5)

  def test_yaml(self):
    self.assertEqual(self.calculator.multiply(3,7), 21)

  def test_toml(self):
    self.assertEqual(self.calculator.divide(10,2), 5)


if __name__ == "__main__":
  unittest.main()