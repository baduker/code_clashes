SECONDS_IN_EARTH_YEAR = 31557600

ORBITAL_PERIODS = {
    'Earth': 1,
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132,
}

def space_age(seconds_alive, planet):
    annual_seconds = SECONDS_IN_EARTH_YEAR * ORBITAL_PERIODS[planet]
    return round(seconds_alive / annual_seconds, 2)