# population_city_functions.py

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    return f"{city.title()}, {country.title()} - population {population}"


# Calls
print(city_country("santiago", "chile", 5000000))
print(city_country("tokyo", "japan", 14000000))
print(city_country("memphis", "united states", 630000))