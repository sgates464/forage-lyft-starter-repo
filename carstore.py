from battery.nubbin import Nubbin
from battery.spindler import Spindler
from car import Car
from engine.capulet import Capulet
from engine.sternman import Sternman
from engine.willoughby import Willoughby
from tires.tireset import TireSet

class CarStore:
    @staticmethod
    def add_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_service_status):
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Spindler(last_service_date, current_date)
        tires = TireSet(tire_service_status)
        return Car(engine, battery, tires)

    @staticmethod
    def add_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_service_status):
        engine = Willoughby(current_mileage, last_service_mileage)
        battery = Spindler(last_service_date, current_date)
        tires = TireSet(tire_service_status)
        return Car(engine, battery, tires)

    @staticmethod
    def add_palindrome(current_date, last_service_date, warning_light_on, tire_service_status):
        engine = Sternman(warning_light_on)
        battery = Spindler(last_service_date, current_date)
        tires = TireSet(tire_service_status)
        return Car(engine, battery, tires)

    @staticmethod
    def add_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_service_status):
        engine = Willoughby(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        tires = TireSet(tire_service_status)
        return Car(engine, battery, tires)

    @staticmethod
    def add_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_service_status):
        engine = Capulet(last_service_mileage, current_mileage)
        battery = Nubbin(last_service_date, current_date)
        tires = TireSet(tire_service_status)
        return Car(engine, battery, tires)