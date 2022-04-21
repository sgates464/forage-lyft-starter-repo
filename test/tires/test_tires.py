#Create unit tests for the tires module

import unittest
from tires.tireset import Tireset

class TestTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_service_status = True
        tire_set = Tireset(tire_service_status)
        self.assertTrue(tire_set.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_service_status = False
        tire_set = Tireset(tire_service_status)
        self.assertFalse(tire_set.needs_service())