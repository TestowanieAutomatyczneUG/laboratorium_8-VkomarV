import unittest
import json

from src.planety import planets_time

class Test_planety(unittest.TestCase):
    def test_from_file(self):
        file = open("./planety.json")
        data = json.load(file)
        file.close()
        for [input, output] in data:
            self.assertEqual(planets_time(input[0], input[1]), output)



