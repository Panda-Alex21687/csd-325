# Make_population_city_functions.py

def city_country(city, country, population=None):
    """Return formatted city_country string with optional population."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"

# Calls (Still ok)
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 14000000))
print(city_country("paris", "france", 2148000))