#Create Unit Test for Willoughby Engine. Case: Engine needs service if mileage difference > 60001. Case: Engine does not need service if mileage difference < 60000.

import unittest
from engine.willoughby import Willoughby

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        car = Willoughby(current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        car = Willoughby(current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())