from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    '''according to the speficif country, return pygal's country code'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if cannot find the country, return None
    return None
