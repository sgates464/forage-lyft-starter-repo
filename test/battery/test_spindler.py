# create unit tests for spindler battery. Case: battery needs service if date difference > 2 years. Case: battery does not need service if date difference < 2 years.

import unittest
from datetime import date
from battery.spindler import Spindler

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date(2022, 1, 2)
        last_service_date = date(2018, 1, 1)
        car = Spindler(current_date, last_service_date)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date(2022, 1, 1)
        last_service_date = date(2018, 1, 1)
        car = Spindler(current_date, last_service_date)
        self.assertFalse(car.needs_service())