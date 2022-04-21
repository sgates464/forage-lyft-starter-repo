# Creat unit test for Sternman Engine. Case: Engine needs service if warning_light_on is True. Case: Engine does not need service if warning_light_on is False.

import unittest
from engine.sternman import Sternman

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True
        car = Sternman(warning_light_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False
        car = Sternman(warning_light_on)
        self.assertFalse(car.needs_service())