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