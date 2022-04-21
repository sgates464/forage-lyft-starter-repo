# Create unit test for capulet engine

import unittest
from engine.capulet import Capulet

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        car = Capulet(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        car = Capulet(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())