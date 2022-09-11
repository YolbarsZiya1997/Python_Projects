import unittest
from city_functions import get_city_country


class TestCityNames(unittest.TestCase):
    """Testing for the format"""

    def test_city_country(self):
        """Is the output correct"""
        formatted_name = get_city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')

    def test_city_country_population(self):
        formatted_name = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_name, 'Santiago Chile -5000000')


if __name__ == '__main__':
    unittest.main()