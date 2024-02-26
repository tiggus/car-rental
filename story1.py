import threading
from datetime import date
from main.rental.Renter import Renter
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.CarRentalCompany import CarRentalCompany

class CarRentalCompany:
    def __init__(self):
        self.available_cars = [
            Car("Toyota", "RAV4", "NHK 337P", "B2", 90),
            Car("BMW", "X3", "NHK 338P", "C1", 90),
            Car("BMW", "X5", "NHK 339P", "A1", 90),
            Car("Ford", "Fiesta", "NHK 340P", "A1", 90)
        ]
        self.lock = threading.Lock()

    def find_matching_cars(self, criteria):
        matching_cars = []
        with self.lock:
            for car in self.available_cars:
                if criteria(car):
                    matching_cars.append(car)
        return matching_cars

# main part !
def main():
    rental_company = CarRentalCompany()
    querycar = input("make of car? :")
    def criteria(car):
        return car.make == querycar and car.available

    matching_cars = rental_company.find_matching_cars(criteria)
    for car in matching_cars:
        print(f"{car.make} {car.model}")

if __name__ == "__main__":
    main()