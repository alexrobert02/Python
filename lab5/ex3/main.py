#   Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific
# types of vehicles like Car, Motorcycle, and Truck. Add methods to calculate mileage or towing capacity based on the
# vehicle type.


from Car import Car
from Motorcycle import Motorcycle
from Truck import Truck


def main():
    car = Car("Golf", "5", 2009, 4)
    motorcycle = Motorcycle("Suzuki", "GSX-8S", 2023, 2)
    truck = Truck("Ford", "F-150", 2023, 10000)

    print("Car information:")
    car.display_info()
    print("\nMotorcycle information:")
    motorcycle.display_info()
    print("\nTruck information:")
    truck.display_info()

    car.calculate_mileage(300, 15)
    motorcycle.calculate_mileage(150, 5)

    print("\nCar mileage:", car.mileage, "kilometers per liter")
    print("Motorcycle mileage:", motorcycle.mileage, "kilometers per liter")

    payload_weight = 2000
    adjusted_towing_capacity = truck.calculate_towing_capacity(payload_weight)
    print(f"Adjusted towing capacity: {adjusted_towing_capacity}kg")


if __name__ == "__main__":
    main()
