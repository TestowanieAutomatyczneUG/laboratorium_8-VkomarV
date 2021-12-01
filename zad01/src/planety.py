def planets_time(time, planet):
    planets = {"Ziemia": 1, "Merkury": 0.2408467, "Wenus": 0.61519726, "Mars": 1.8808158, "Jowisz": 11.862615,
               "Saturn": 29.447498, "Uran": 84.016846, "Neptun": 164.79132}

    if planet in planets:
        try:
            time = int(time)
            return round(time / 60 / 60 / 24 / 365.25 / planets[planet], 2)

        except Exception as e:
            return "Error"
    else:
        return "Error"


