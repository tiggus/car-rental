import threading

class CarAvailabilityManager:
    def __init__(self):
        self.car_availability = {}  # Dictionary to track car availability by registration number
        self.lock = threading.Lock()

    def add_car(self, car, from_date, to_date):
        with self.lock:
            self.car_availability[car.registration_number] = {
                'car': car,
                'available': True
            }

    def is_car_available(self, car_registration_number):
        return self.car_availability.get(car_registration_number, {}).get('available', False)
