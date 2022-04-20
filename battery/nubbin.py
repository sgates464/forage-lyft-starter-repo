# create Class Nubbin with ABC param, with last_service_date and current_date attributes and needs_service method returns true if current_date - last_service_date > 4

from abc import ABC

class Nubbin(ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > 4