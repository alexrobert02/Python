from Vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels
        self.mileage = None

    def display_info(self):
        super().display_info()
        print(f"Number of wheels: {self.num_wheels}")

    def calculate_mileage(self, kilometers_driven, fuel_used):
        self.mileage = kilometers_driven / fuel_used
