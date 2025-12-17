# city_functions.py

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"


# Call the function at least three times
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
print(city_country("memphis", "united states"))

# population_city_functions.py

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    return f"{city.title()}, {country.title()} - population {population}"


# Calls
print(city_country("santiago", "chile", 5000000))
print(city_country("tokyo", "japan", 14000000))
print(city_country("memphis", "united states", 633000))

# test_cities.py
import unittest
from city_functions import city_country # pyright: ignore[reportMissingImports]


class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == '__main__':
    unittest.main()

    # Make_population_city_functions.py

def city_country(city, country, population=None):
    """Return formatted city_country string with optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"

# Calls (Still ok)
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 14000000))
print(city_country("memphis", "united states"))

# language_city_functions.py

def city_country(city, country, language, population=None):
    """Return city, country, population, and language."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    return f"{city.title()}, {country.title()}, {language.title()}"

# Calls
print(city_country("santiago", "chile", 5000000, "spanish"))
print(city_country("tokyo", "japan", 14000000, "japanese"))
print(city_country("memphis", "united states", None, "english"))

# Optional_Language_city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted string for city info."""
    base = f"({city.title()}, {country.title()}"

    if population and language:
        return f"{base} - population {population}, {language.title()}"
    elif population:
        return f"{base} - population {population}"
    elif language:
        return f"{base}, {language.title()}"
    else:
        return base
    
    
    # Required calls
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 14000000))
    print(city_country("paris", "france", 2148000, "french"))