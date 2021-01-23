def print_city_country(city, country, population=None):
    if population:
        city_country_population = city + ', ' + country + ' - population=' + population
        return city_country_population
    else:
        city_country = city + ', ' + country
        return city_country
