import unittest

from weather_app.cities import CITIES
from weather_app.predictor import average_temperature, predict_temperature, rain_message
from weather_app.validation import valid_city


class ProjectTests(unittest.TestCase):

    def test_ten_cities_exist(self):
        self.assertEqual(len(CITIES), 10)

    def test_city_validation(self):
        self.assertTrue(valid_city("Mumbai", CITIES))
        self.assertFalse(valid_city("London", CITIES))

    def test_average_temperature(self):
        self.assertEqual(average_temperature([20, 30, 40]), 30)

    def test_prediction(self):
        self.assertEqual(predict_temperature([20, 30, 40]), 30)

    def test_rain_message(self):
        self.assertEqual(rain_message([0, 0, 0]), "No significant rain recently.")


if __name__ == "__main__":
    unittest.main()
