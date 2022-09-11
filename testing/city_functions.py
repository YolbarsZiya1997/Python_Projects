def get_city_country(city: str, country: str, population='') -> str:
    """Get the city and country name in a beautiful format"""
    if population:
        formatted_names = f"{city} {country} -{population}"
    else:
        formatted_names = f"{city} {country}"
    return formatted_names.title()


print(get_city_country('santiago', 'chile'))