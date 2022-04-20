from tires.tires import Tires

class TireSet(Tires):
    def __init__(self, tire_service_status):
        self.tire_service_status = tire_service_status

    def needs_service(self):
        if self.tire_service_status:
            return True
        else:
            return False