# language_city_functions.py

def city_country(city, country, language, population=None):
    """Return city, country, population, and language."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    return f"{city.title()}, {country.title()}, {language.title()}"

# Calls
print(city_country("santiago", "chile", "spanish", 5000000))
print(city_country("tokyo", "japan", "japanese", 14000000))
print(city_country("paris", "france", "french", 2148000))