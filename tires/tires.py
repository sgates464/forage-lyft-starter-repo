# create class Tires with ABC param, with tire_service_status: boolean attribute, needs_service method, returns true if tire_service_status

from abc import ABC

class Tires(ABC):
    def __init__(self, tire_service_status):
        super().__init__(tire_service_status)
        self.tire_service_status = tire_service_status

    def needs_service(self):
        return self.tire_service_status