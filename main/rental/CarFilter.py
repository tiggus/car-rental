class CarFilter:
    def __init__(self, car_availability_manager, booking_manager):
        self.car_availability_manager = car_availability_manager
        self.booking_manager = booking_manager

    def matching_cars(self, criteria):
        matching_cars = []
        if criteria.get_cost_criteria() is not None:
            matching_cars = [
                car_availability['car']
                for car_registration_number, car_availability in self.car_availability_manager.car_availability.items()
                if car_availability['available'] and car_availability['car'].cost_per_day <= criteria.get_cost_criteria()
            ]

        if criteria.get_from_date_criteria() and criteria.get_to_date_criteria():
            filtered_cars = matching_cars.copy()
            for car_registration_number, car_availability in self.car_availability_manager.car_availability.items():
                car = car_availability['car']
                overlapping_bookings = [
                    booking for booking in self.booking_manager.get_bookings()
                    if booking.car == car and
                    booking.date >= criteria.get_from_date_criteria() and
                    booking.date <= criteria.get_to_date_criteria()
                ]
                if overlapping_bookings:
                    filtered_cars.remove(car)
            return filtered_cars
        else:
            return matching_cars
