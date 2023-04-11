from abc import ABC, abstractmethod


class CarPart(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(CarPart, Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()


class Engine(CarPart, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class CapuletEngine(Engine):
    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000


class Battery(CarPart, ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass


class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 365


class NubbinBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date - self.last_service_date).days > 365
