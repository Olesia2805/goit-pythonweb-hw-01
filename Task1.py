from abc import ABC, abstractmethod
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self) -> Vehicle:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, country: str):
        super().__init__(make, model)
        self.country = country

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.country}): Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, country: str):
        super().__init__(make, model)
        self.country = country

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.country}): Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


# Використання
us_factory = USVehicleFactory()
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

eu_factory = EUVehicleFactory()
vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
vehicle3.start_engine()

vehicle4 = eu_factory.create_motorcycle("Ducati", "Monster")
vehicle4.start_engine()
