import unittest
import zad03
from parameterized import parameterized, parameterized_class


class TestPlanets(unittest.TestCase):
    def setUp(self):
        self.temp = zad03.Planets

    @parameterized.expand([
        ("Ziemia", 50000000, 1.58),
        ("Neptun", 440000000, 0.08),
        ("Jowisz", 9812038123123, 26210.47)
    ])
    def test_parametrized(self, planet, time, output):
        self.assertEqual(self.temp.planets_time(planet, time), output)

    @parameterized.expand([
        ("", ""),
        (100, 100),
        (100, ""),
        ("Jowisz", []),
        ("Ziemia", 11.11),
        (None, 1111),
        ("Neptun", None),
        ([], [])
    ])
    def test_parameterized_exeptions(self, planet, time):
        self.assertRaises(Exception, self.temp.planets_time, planet, time)
