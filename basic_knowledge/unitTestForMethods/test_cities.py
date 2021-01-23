import unittest
from city_functions import print_city_country


class CityTestCase(unittest.TestCase):
    '''test city_function'''

    def test_city_contry(self):
        '''can it print in the right format as City, Country?'''
        formmatted_res = print_city_country(
            'Santiago', 'Chile')
        self.assertEqual(formmatted_res, 'Santiago, Chile')

    def test_city_contry_populatin(self):
        '''can it print in the right format as City, Country - population=xxx'''
        formmatted_res = print_city_country(
            'Santiago', 'Chile', '5000000')
        self.assertEqual(
            formmatted_res, 'Santiago, Chile - population=5000000')


unittest.main()
