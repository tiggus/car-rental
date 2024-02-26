import unittest
from datetime import date
from main.rental.Car import Car
from main.rental.Criteria import Criteria
from main.rental.Renter import Renter
from main.rental.CarRentalCompany import CarRentalCompany

# Create car rental facade
car_rental = CarRentalCompany()

# Create cars and add them to the car rental system
car1 = Car("Toyota", "Camry", "ABC123", "Economy", 50)
car2 = Car("Honda", "Civic", "XYZ789", "Economy", 55)
car3 = Car("Ford", "Mustang", "DEF456", "Luxury", 100)

car_rental.add_car(car1, None, None)  # Add car1 without date restrictions
car_rental.add_car(car2, None, None)  # Add car2 without date restrictions
car_rental.add_car(car3, None, None)  # Add car3 without date restrictions

# Create a renter
renter = Renter("Doe", "John", "DL12345", "1990-01-15")

# Define criteria
criteria = Criteria()
criteria.cost_criteria(60)  # Set maximum cost criteria

#Test renting a car
#print("Renting a car:")
#car_rental.rent_car(renter, "2023-09-15", criteria)

print("story1:")
criteria.cost_criteria(999)
matching_cars = car_rental.matching_cars(criteria)
for car in matching_cars:
    print(f"\t{car.make} {car.model}")

class CarRentalTest(unittest.TestCase):

    CAR1 = Car("VW", "Golf", "XX11 1UR", "B2", 90)
    CAR2 = Car("VW", "Passat", "XX12 2UR", "C1", 110)
    CAR3 = Car("VW", "Polo", "XX13 3UR", "A1", 65)
    CAR4 = Car("VW", "Polo", "XX14 4UR", "A1", 70)

    RENTER1 = Renter("Hydrogen", "Joe", "HYDRO010190JX8NM", date(1990, 1, 1))
    RENTER2 = Renter("Calcium", "Sam", "CALCI010203SX8NM", date(2003, 2, 1))
    RENTER3 = Renter("Neon", "Maisy", "NEONN010398MX8NM", date(1998, 3, 1))
    RENTER4 = Renter("Carbon", "Greta", "CARBO010497GX8NM", date(1997, 4, 1))

    def test_list_cars_available_to_rent_gives_more_than_one_car(self):
        car_rental_company = CarRentalCompany()
        car_rental_company.add_car(self.CAR1)
        car_rental_company.add_car(self.CAR2)
        car_rental_company.add_car(self.CAR3)
        car_rental_company.add_car(self.CAR4)

        criteria = Criteria()
        cars_available = car_rental_company.matching_cars(criteria)

        self.assertGreater(len(cars_available), 1)
    #test_list_cars_available_to_rent_gives_more_than_one_car()
