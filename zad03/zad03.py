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
