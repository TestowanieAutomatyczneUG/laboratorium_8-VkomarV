from parameterized import parameterized, parameterized_class
import unittest


class Planets:
    def planets_time(planet, time):
        planets = {"Ziemia": 1, "Merkury": 0.2408467, "Wenus": 0.61519726, "Mars": 1.8808158, "Jowisz": 11.862615,
                   "Saturn": 29.447498, "Uran": 84.016846, "Neptun": 164.79132}

        if type(time) != int or type(planet) != str:
            raise Exception("Błąd typu")
        elif time < 0:
            raise Exception("Czas nie może być ujemny")

        elif planet in planets:
            return round(time / 60 / 60 / 24 / 365.25 / planets[planet], 2)
        else:
            return "Nie znaleziono"


class TestPlanets(unittest.TestCase):
    def setUp(self):
        self.temp = Planets

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
