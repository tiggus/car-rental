import threading

class Car:
    def __init__(self, make, model, year, available=True):
        self.make = make
        self.model = model
        self.year = year
        self.available = available

class CarRentalCompany:
    def __init__(self):
        self.available_cars = [
            Car("Toyota", "RAV4", 2020),
            Car("BMW", "X3", 2019),
            Car("BMW", "X5", 2019),
            Car("Ford", "Fiesta", 2021)
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

    def criteria(car):
        return car.make == "Ford" and car.available

    matching_cars = rental_company.find_matching_cars(criteria)
    for car in matching_cars:
        print(f"{car.make} {car.model} {car.year}")

if __name__ == "__main__":
    main()