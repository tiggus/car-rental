import threading
from .CarAvailabilityManager import CarAvailabilityManager
from .CarFilter import CarFilter
from .BookingManager import BookingManager

class CarRentalCompany:
    def __init__(self):
        self.cars = []
        self.car_availability_manager = CarAvailabilityManager()
        self.booking_manager = BookingManager()
        self.booking_manager.set_car_availability_manager(self.car_availability_manager)
        self.car_filter = CarFilter(self.car_availability_manager, self.booking_manager)
        self.lock = threading.Lock()

    def add_car(self, car, from_date, to_date):
        self.car_availability_manager.add_car(car, from_date, to_date)

    def matching_cars(self, criteria):
        return self.car_filter.matching_cars(criteria)

    def rent_car(self, renter, date, criteria):
        matching_cars = self.matching_cars(criteria)
        if matching_cars:
            car = matching_cars[0]
            if self.car_availability_manager.is_car_available(car.registration_number):
                with self.lock:
                    self.booking_manager.rent_car(renter, date, car)

    def return_car(self, renter, date):
        with self.lock:
            self.booking_manager.return_car(renter, date)

    def get_bookings(self):
        return self.booking_manager.get_bookings()