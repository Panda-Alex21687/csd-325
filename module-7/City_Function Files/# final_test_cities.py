# final_test_cities.py
import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

if __name__ == "__main__":
    unittest.main()
