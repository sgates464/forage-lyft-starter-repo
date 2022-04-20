# create class Sternman with Car and ABC params, warning_light_on: boolean attribute, needs_service method, returns true if warning_light_on is true
from abc import ABC


class Sternman(ABC):
    def __init__(self, warning_light_on):
        super().__init__(warning_light_on)
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return self.warning_light_on