from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        mileage_threshold = self.last_service_mileage + 100000
        current_date = datetime.today().date()

        return current_date > service_threshold_date or self.current_mileage > mileage_threshold
