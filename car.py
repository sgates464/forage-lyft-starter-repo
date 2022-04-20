


from abc import ABC, abstractmethod


#create Car class with engine, battery, and tire attributes and needs_service method
class Car(ABC):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires
    
    @abstractmethod
    def needs_service(self):
        pass
