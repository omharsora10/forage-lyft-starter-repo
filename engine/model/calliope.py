from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date + timedelta(days=730)
        if service_threshold_date <= datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
