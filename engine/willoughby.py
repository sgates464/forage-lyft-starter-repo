# create Class Willoughby with Car and ABC params last_service_mileage and current_mileage attributes and needs_service method returns true if current_mileage - last_service_mileage > 60000

from abc import ABC


class Willoughby(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__(last_service_mileage)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000