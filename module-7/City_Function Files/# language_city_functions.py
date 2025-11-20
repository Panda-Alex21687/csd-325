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