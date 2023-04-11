import unittest
from datetime import date

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach


class CarTest(unittest.TestCase):
    def setUp(self):
        self.today = date.today()
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.last_service_mileage = 0

    def test_calliope_battery_service_due(self):
        current_mileage = 0
        car = Calliope(self.last_service_date, current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_battery_service_not_due(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        current_mileage = 0
        car = Calliope(last_service_date, current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_calliope_engine_service_due(self):
        current_mileage = 30001
        car = Calliope(self.today, current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_calliope_engine_service_not_due(self):
        current_mileage = 30000
        car = Calliope(self.today, current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_glissade_battery_service_due(self):
        current_mileage = 0
        car = Glissade(self.last_service_date, current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_battery_service_not_due(self):
        last_service_date = self.today.replace(year=self.today.year - 1)
        current_mileage = 0
        car = Glissade(last_service_date, current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_glissade_engine_service_due(self):
        current_mileage = 60001
        car = Glissade(self.today, current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_engine_service_not_due(self):
        current_mileage = 60000
        car = Glissade(self.today, current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_palindrome_battery_service_due(self):
        last_service_date = self.today.replace(year=self.today.year - 5)
        car = Palindrome(last_service_date, True)
        self.assertTrue(car.needs_service())

    def test_palindrome_battery_service_not_due(self):
        last_service_date = self.today.replace(year=self.today.year - 3)
        car = Palindrome(last_service_date, False)
        self.assertFalse(car.needs_service())

    def test_palindrome_engine_service_due(self):
        car = Palindrome(self.today, True)
        self.assertTrue(car.needs_service())

    def test_palindrome_engine_service_not_due(self):
        car = Palindrome(self.today, False)
        self.assertFalse(car.needs_service())

    def test_rorschach_battery_service_due(self):
        current_mileage = 0
        car = Rorschach(self.last_service_date, current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_rorschach_battery_service_not_due(self):
        last_service_date = self.today.replace(year
