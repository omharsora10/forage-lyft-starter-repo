from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def is_service_due(self) -> bool:
        """
        Determines if the engine should be serviced based on the last service mileage and the current mileage.

        Returns:
            True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage > 60000
