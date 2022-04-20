# create class spindler with ABC params, current_date and last_service_date attributes and needs_service method returns true if current_date - last_service_date > 2

from abc import ABC

class spindler(ABC):
    def __init__(self, current_date, last_service_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 2