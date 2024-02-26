import threading
from .Booking import Booking

class BookingManager:
    def __init__(self):
        self.bookings = []  # List to store booking instances
        self.lock = threading.Lock()

    def rent_car(self, renter, date, car):
        with self.lock:
            booking = Booking(renter, date, car)
            self.bookings.append(booking)

    def return_car(self, renter, date):
        booking = None
        for b in self.bookings:
            if b.renter == renter and b.date == date:
                booking = b
                break

        if booking:
            with self.lock:
                self.bookings.remove(booking)

    def set_car_availability_manager(self, car_availability_manager):
        self.car_availability_manager = car_availability_manager

    def get_bookings(self):
        return self.bookings